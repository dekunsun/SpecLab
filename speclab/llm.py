"""Anthropic backend for the XRD qualification runs. One request per item; every exchange
and the usage are written to results/xrd/<run>/raw/<item>.json. Silence (API failure after one
retry, or no parsable JSON) is recorded as no response and scored as coverage."""
from __future__ import annotations
import json, re, time
from pathlib import Path
import numpy as np
from . import prompts, xrd

MODEL = "claude-opus-5-5"
PRICE = {"claude-opus-5-5": (4.0, 20.0), "claude-sonnet-5-5": (2.0, 10.0)}   # $/MTok in, out (reference table 2026-10)

TOOL = {"name": "simulate_pattern", "description": "Return the simulated clean powder pattern (no strain, no noise) of one candidate id on the item's 10-80 degree, 0.05 degree grid, as intensities normalised to 100.",
        "input_schema": {"type": "object", "properties": {"candidate_id": {"type": "string"}}, "required": ["candidate_id"], "additionalProperties": False}, "strict": True}


def parse(text: str):
    m = re.findall(r"\{[^{}]*\"present\"[^{}]*\}", text, flags=re.S)
    if not m:
        return None
    try:
        d = json.loads(m[-1])
    except json.JSONDecodeError:
        return None
    p = d.get("present")
    return d if isinstance(p, list) and 1 <= len(p) <= 2 and all(isinstance(x, str) for x in p) else None


def _simulate(item, cid):
    from pymatgen.core import Structure
    c = next((c for c in item["candidates"] if c["id"] == cid), None)
    if c is None:
        return {"error": "unknown candidate id"}
    x, y = xrd.peaks(Structure.from_str(c["cif"], fmt="cif"))
    p = xrd.profile(x, y, fwhm=0.2); p = p / max(p.max(), 1e-9) * 100
    return {"candidate_id": cid, "intensity": np.round(p, 2).tolist()}


def count_tokens(client, item, arm="A"):
    kw = dict(model=MODEL, system=prompts.SYSTEM_XRD_TOOL if arm == "B" else prompts.SYSTEM_XRD,
              messages=[{"role": "user", "content": prompts.user_xrd(item)}])
    if arm == "B":
        kw["tools"] = [TOOL]
    return client.messages.count_tokens(**kw).input_tokens


def run_item(client, item, arm, effort, out_dir: Path, max_tool_calls=12):
    """Returns (present_ids or None, record). Retries the API once on failure."""
    payload = xrd.prompt_payload(item) | {"id": item["id"]}
    system = prompts.SYSTEM_XRD_TOOL if arm == "B" else prompts.SYSTEM_XRD
    messages = [{"role": "user", "content": prompts.user_xrd(payload)}]
    rec = {"id": item["id"], "arm": arm, "model": MODEL, "effort": effort, "exchanges": [], "usage": {"input": 0, "output": 0}, "tool_calls": 0, "error": None}
    kw = dict(model=MODEL, max_tokens=16000, system=system, output_config={"effort": effort}, messages=messages)
    if arm == "B":
        kw["tools"] = [TOOL]
    text, t0 = "", time.time()
    for _ in range(max_tool_calls + 1):
        resp = None
        for attempt in range(2):
            try:
                resp = client.messages.create(**kw); break
            except Exception as e:   # recorded, retried once, then silence
                rec["error"] = f"{type(e).__name__}: {str(e)[:200]}"; time.sleep(5)
        if resp is None:
            break
        rec["usage"]["input"] += resp.usage.input_tokens; rec["usage"]["output"] += resp.usage.output_tokens
        rec["exchanges"].append({"stop_reason": resp.stop_reason, "content": [b.model_dump() for b in resp.content]})
        text = "".join(b.text for b in resp.content if b.type == "text")
        if resp.stop_reason != "tool_use":
            break
        messages.append({"role": "assistant", "content": resp.content})
        results = []
        for b in resp.content:
            if b.type == "tool_use":
                rec["tool_calls"] += 1
                results.append({"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(_simulate(item, b.input.get("candidate_id", "")))})
        messages.append({"role": "user", "content": results})
    rec["seconds"] = round(time.time() - t0, 1); rec["final_text"] = text
    d = parse(text); rec["parsed"] = d
    pin, pout = PRICE[MODEL]; rec["cost_usd"] = round(rec["usage"]["input"] / 1e6 * pin + rec["usage"]["output"] / 1e6 * pout, 4)
    (out_dir / "raw").mkdir(parents=True, exist_ok=True)
    (out_dir / "raw" / f"{item['id']}.json").write_text(json.dumps(rec, indent=1, default=str))
    return (d["present"] if d else None), rec


TOOL_RESIDUAL = {"name": "fit_and_residual",
                 "description": "Fit the observed pattern as a non-negative combination of the simulated patterns of the given candidate ids (each candidate at its best isotropic strain in [-2 %, +2 %]) and return the fitted weights, the R-factor, and the residual pattern (observed minus fit) on the same 10-80 degree grid, normalised so the observed maximum is 100. Use the residual to look for a second phase after accounting for the first.",
                 "input_schema": {"type": "object", "properties": {"candidate_ids": {"type": "array", "items": {"type": "string"}}},
                                  "required": ["candidate_ids"], "additionalProperties": False}, "strict": True}


def fit_and_residual(item, cids):
    """NNLS fit of the observed pattern on the named candidates with a per-candidate strain scan."""
    import numpy as np
    from pymatgen.core import Structure
    from scipy.optimize import nnls
    obs = np.array(item["intensity"], dtype=float)
    cids = list(cids)[:3]   # the API schema cannot carry maxItems; the limit lives here and in the description
    if not cids:
        return {"error": "candidate_ids is empty"}
    cols, used, strains = [], [], []
    for cid in cids:
        c = next((c for c in item["candidates"] if c["id"] == cid), None)
        if c is None:
            return {"error": f"unknown candidate id {cid}"}
        s = Structure.from_str(c["cif"], fmt="cif")
        best, best_corr, best_st = None, -1.0, 0.0
        for st in np.linspace(-0.02, 0.02, 9):
            x, y = xrd.peaks(s, float(st)); p = xrd.profile(x, y, fwhm=0.25); p = p / max(p.max(), 1e-9) * 100
            corr = float(np.dot(p, obs) / (np.linalg.norm(p) * np.linalg.norm(obs) + 1e-9))
            if corr > best_corr:
                best, best_corr, best_st = p, corr, float(st)
        cols.append(best); used.append(cid); strains.append(round(best_st * 100, 2))
    A = np.array(cols).T
    w, _ = nnls(A, obs)
    fit = A @ w
    resid = obs - fit
    r_factor = float(np.sum(np.abs(resid)) / max(np.sum(obs), 1e-9))
    wn = (w / w.sum()).tolist() if w.sum() > 0 else [0.0] * len(w)
    return {"candidate_ids": used, "weights_normalised": [round(v, 3) for v in wn], "strain_pct": strains, "r_factor": round(r_factor, 4),
            "residual": np.round(resid, 2).tolist(), "residual_max": round(float(resid.max()), 2)}
