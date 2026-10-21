"""XRD phase-identification items: simulated Cu K-alpha powder patterns from MP-20 structures.

An item is a closed-set identification task: one observed pattern, nine candidate structures
(CIF included, so any agent can simulate them), and the question "which candidate phase or
phases are present". Three tiers:

  T1  single phase, light noise, no distortion
  T2  single phase, isotropic strain of up to +-1.5 %, per-peak intensity distortion
      (a crude stand-in for preferred orientation), heavier noise and background
  T3  two phases (minor fraction 0.10-0.35), T2-level distortion on both

The answer is the set of candidate ids present. Scoring is exact set match and Jaccard.
The truth is constructed, so it is correct by construction; what is NOT guaranteed is that
the simulated difficulty matches a real diffractometer. That is stated in docs/question_rules.md.
"""
from __future__ import annotations
import hashlib, json, random
import numpy as np
from pymatgen.analysis.diffraction.xrd import XRDCalculator

GRID = np.round(np.arange(10.0, 80.0, 0.05), 2)
CALC = XRDCalculator(wavelength="CuKa")


def peaks(structure, strain: float = 0.0):
    s = structure.copy()
    if strain:
        s.scale_lattice(s.volume * (1 + strain) ** 3)
    p = CALC.get_pattern(s, two_theta_range=(10, 80))
    return np.array(p.x), np.array(p.y)


def profile(x, y, fwhm=0.15, distort=None, rng=None):
    """Sum of Gaussians on GRID; distort = sigma of lognormal per-peak intensity factor."""
    out = np.zeros_like(GRID)
    if distort and rng is not None:
        y = y * rng.lognormal(0.0, distort, size=len(y))
    sig = fwhm / 2.3548
    for xi, yi in zip(x, y):
        out += yi * np.exp(-0.5 * ((GRID - xi) / sig) ** 2)
    return out


def observe(clean, rng, noise=0.02, background=0.05, counts=2000.0):
    """Background + Poisson noise, normalised to max 100."""
    bg = background * 100 * (1 - (GRID - 10) / 70) ** 2
    sig = clean / max(clean.max(), 1e-9) * 100 + bg
    obs = rng.poisson(sig / 100 * counts) / counts * 100
    obs = obs + rng.normal(0, noise * 100, size=len(obs))
    obs = np.clip(obs, 0, None)
    return obs / obs.max() * 100


def make_item(idx, tier, pool, rng, structure_of):
    """pool: list of entries; structure_of: entry -> Structure."""
    n_cand = 9
    cands = rng.sample(pool, n_cand)
    if tier == "T3":
        present = cands[:2]
        frac = rng.uniform(0.10, 0.35)
        weights = [1 - frac, frac]
    else:
        present = cands[:1]; weights = [1.0]
    nprng = np.random.default_rng(rng.getrandbits(32))
    clean = np.zeros_like(GRID)
    for e, w in zip(present, weights):
        strain = 0.0 if tier == "T1" else nprng.uniform(-0.015, 0.015)
        distort = None if tier == "T1" else 0.35
        x, y = peaks(structure_of(e), strain)
        clean += w * profile(x, y, fwhm=0.15 if tier == "T1" else 0.25, distort=distort, rng=nprng)
    obs = observe(clean, nprng, noise=0.01 if tier == "T1" else 0.03, background=0.03 if tier == "T1" else 0.08,
                  counts=5000.0 if tier == "T1" else 1500.0)
    order = list(range(n_cand)); rng.shuffle(order)
    cand_out = [{"id": cands[i].material_id, "formula": cands[i].formula, "spacegroup": cands[i].spacegroup, "cif": cands[i].cif} for i in order]
    item = {"id": f"xrd-{idx:03d}", "tier": tier, "two_theta": GRID.tolist(), "intensity": np.round(obs, 2).tolist(),
            "candidates": cand_out, "question": "Which candidate phase or phases are present (one or two)? Answer with candidate ids."}
    answer = {"id": item["id"], "present": [e.material_id for e in present], "weights": weights}
    return item, answer


def prompt_payload(item: dict) -> dict:
    """What an agent is allowed to see. Must contain no answer field; tested in tests/."""
    return {k: v for k, v in item.items() if k in ("id", "tier", "two_theta", "intensity", "candidates", "question")}


def sha256(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()


# ---- scoring ---------------------------------------------------------------------------------
def score(answers: dict, responses: dict) -> dict:
    """answers/responses: id -> list of ids. Returns per-tier exact and jaccard, plus coverage."""
    per = {}
    for aid, truth in answers.items():
        t = set(truth["present"]); tier = truth["tier"]
        r = responses.get(aid)
        d = per.setdefault(tier, {"n": 0, "answered": 0, "exact": 0, "jaccard": 0.0})
        d["n"] += 1
        if r is None:
            continue   # silence is not an answer: counted as coverage, not as wrong
        r = set(r); d["answered"] += 1
        d["exact"] += int(r == t)
        d["jaccard"] += len(r & t) / len(r | t) if (r | t) else 1.0
    for d in per.values():
        d["exact_rate"] = round(d["exact"] / d["answered"], 3) if d["answered"] else None
        d["jaccard_mean"] = round(d["jaccard"] / d["answered"], 3) if d["answered"] else None
        d["coverage"] = round(d["answered"] / d["n"], 3)
    return per


# ---- agents ----------------------------------------------------------------------------------
def agent_random(item, rng):
    k = rng.choice([1, 2])
    return [c["id"] for c in rng.sample(item["candidates"], k)]


def agent_oracle(item, answers):
    return list(answers[item["id"]]["present"])


def agent_classic(item, two_phase_threshold=0.12):
    """Non-negative least squares of the observed pattern on the candidates' simulated clean
    profiles (no strain, no distortion). Phases with normalised weight >= threshold are reported.
    This is the rule-based baseline every learned or LLM agent has to beat."""
    from pymatgen.core import Structure
    from scipy.optimize import nnls
    obs = np.array(item["intensity"])
    A = []
    for c in item["candidates"]:
        x, y = peaks(Structure.from_str(c["cif"], fmt="cif"))
        p = profile(x, y, fwhm=0.2)
        A.append(p / max(p.max(), 1e-9) * 100)
    A = np.array(A).T
    w, _ = nnls(A, obs)
    if w.sum() <= 0:
        return [item["candidates"][0]["id"]]
    wn = w / w.sum()
    order = np.argsort(-wn)
    out = [item["candidates"][order[0]]["id"]]
    if wn[order[1]] >= two_phase_threshold:
        out.append(item["candidates"][order[1]]["id"])
    return out
