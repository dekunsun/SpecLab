"""Arm B (with the simulate_pattern tool) through the Message Batches API, one batch per round.

Each round submits every unfinished item's full conversation; replies that stop with tool_use get
their tool results appended and go into the next round. The message sequence per item is
identical to the synchronous runner, so results are comparable; the price is half.

  --set public|heldout  --run N  --effort high  --poll 60  --max-rounds 13
State per item lives in results/xrd/<run>/state/<item>.json; rounds in rounds.json. Safe to
re-invoke: a round whose batch was submitted but not collected is collected, never resubmitted.
"""
import argparse, json, os, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import xrd, llm, prompts
import anthropic

ap = argparse.ArgumentParser()
ap.add_argument("--set", default="public"); ap.add_argument("--run", type=int, default=1); ap.add_argument("--effort", default="high")
ap.add_argument("--poll", type=int, default=60); ap.add_argument("--max-rounds", type=int, default=13); ap.add_argument("--max-tool-calls", type=int, default=12)
a = ap.parse_args()
key = os.environ.get("SPECLAB_ANTHROPIC_KEY") or os.environ.get("ANTHROPIC_API_KEY")
if not key:
    sys.exit("no key: set SPECLAB_ANTHROPIC_KEY")
client = anthropic.Anthropic(api_key=key)
items_path = Path("items/xrd_public.json") if a.set == "public" else Path("data/heldout/xrd_heldout.json")
ans_path = Path("items/xrd_public_answers.json") if a.set == "public" else Path("data/heldout/xrd_heldout_answers.json")
items = json.loads(items_path.read_text()); answers = json.loads(ans_path.read_text()); by_id = {it["id"]: it for it in items}
run_name = f"{llm.MODEL}_armB_batch_{a.set}_run{a.run}"
out = Path("results/xrd") / run_name; (out / "state").mkdir(parents=True, exist_ok=True)
rounds_path = out / "rounds.json"
rounds = json.loads(rounds_path.read_text()) if rounds_path.exists() else []


def state_path(iid): return out / "state" / f"{iid}.json"


def load_state(it):
    p = state_path(it["id"])
    if p.exists():
        return json.loads(p.read_text())
    payload = xrd.prompt_payload(it) | {"id": it["id"]}
    return {"id": it["id"], "messages": [{"role": "user", "content": prompts.user_xrd(payload)}], "usage": {"input": 0, "output": 0},
            "tool_calls": 0, "rounds": 0, "done": False, "stop_reason": None, "final_text": "", "parsed": None, "error": None}


def save_state(s): state_path(s["id"]).write_text(json.dumps(s, indent=1, default=str))


def simulate(item, cid):
    import numpy as np
    from pymatgen.core import Structure
    c = next((c for c in item["candidates"] if c["id"] == cid), None)
    if c is None:
        return {"error": "unknown candidate id"}
    x, y = xrd.peaks(Structure.from_str(c["cif"], fmt="cif"))
    p = xrd.profile(x, y, fwhm=0.2); p = p / max(p.max(), 1e-9) * 100
    return {"candidate_id": cid, "intensity": np.round(p, 2).tolist()}


def finish(s, text):
    s["done"] = True; s["final_text"] = text; s["parsed"] = llm.parse(text)


states = {it["id"]: load_state(it) for it in items}

# submit a round when nothing is open; collect the open round; repeat until every item is done
while True:
    open_rounds = [rd for rd in rounds if not rd["collected"]]
    if not open_rounds:
        pending = [s for s in states.values() if not s["done"]]
        if not pending or len(rounds) >= a.max_rounds:
            break
        reqs = [{"custom_id": s["id"], "params": {"model": llm.MODEL, "max_tokens": 16000, "system": prompts.SYSTEM_XRD_TOOL, "output_config": {"effort": a.effort},
                                                 "tools": [llm.TOOL], "messages": s["messages"]}} for s in pending]
        batch = client.messages.batches.create(requests=reqs)
        rounds.append({"round": len(rounds) + 1, "batch_id": batch.id, "n": len(reqs), "submitted_at": time.time(), "collected": False})
        rounds_path.write_text(json.dumps(rounds, indent=1))
        print(f"round {len(rounds)}: submitted {len(reqs)} items as {batch.id}", file=sys.stderr)
        continue
    rd = open_rounds[0]
    while True:
        b = client.messages.batches.retrieve(rd["batch_id"])
        print(f"round {rd['round']} {b.processing_status} {b.request_counts}", file=sys.stderr)
        if b.processing_status == "ended":
            break
        time.sleep(a.poll)
    for res in client.messages.batches.results(rd["batch_id"]):
        s = states[res.custom_id]; s["rounds"] += 1
        if res.result.type != "succeeded":
            s["error"] = str(getattr(res.result, "error", res.result))[:500]; finish(s, ""); save_state(s); continue
        m = res.result.message
        s["usage"]["input"] += m.usage.input_tokens; s["usage"]["output"] += m.usage.output_tokens; s["stop_reason"] = m.stop_reason
        content = [c.model_dump() for c in m.content]
        text = "".join(c.text for c in m.content if c.type == "text")
        if m.stop_reason == "tool_use":
            s["messages"].append({"role": "assistant", "content": content})
            results = []
            for c in m.content:
                if c.type == "tool_use":
                    s["tool_calls"] += 1
                    results.append({"type": "tool_result", "tool_use_id": c.id, "content": json.dumps(simulate(by_id[s["id"]], c.input.get("candidate_id", "")))})
            s["messages"].append({"role": "user", "content": results})
            if s["tool_calls"] >= a.max_tool_calls:
                finish(s, text)
        else:
            s["messages"].append({"role": "assistant", "content": content}); finish(s, text)
        save_state(s)
    rd["collected"] = True; rd["collected_at"] = time.time(); rounds_path.write_text(json.dumps(rounds, indent=1))

# summary
responses = {i: s["parsed"]["present"] for i, s in states.items() if s["parsed"]}
usage_in = sum(s["usage"]["input"] for s in states.values()); usage_out = sum(s["usage"]["output"] for s in states.values())
pin, pout = llm.PRICE[llm.MODEL]
import statistics
summary = {"run": run_name, "effort": a.effort, "items": len(items), "answered": len(responses), "api_errors": sum(1 for s in states.values() if s["error"]),
           "rounds": len(rounds), "tool_calls_median": statistics.median(s["tool_calls"] for s in states.values()), "tool_calls_max": max(s["tool_calls"] for s in states.values()),
           "output_tokens_median": statistics.median(s["usage"]["output"] for s in states.values()), "max_tokens_stops": sum(1 for s in states.values() if s["stop_reason"] == "max_tokens"),
           "usage": {"input": usage_in, "output": usage_out}, "cost_usd_batch_price": round((usage_in / 1e6 * pin + usage_out / 1e6 * pout) * 0.5, 2),
           "score": xrd.score(answers, responses)}
(out / "responses.json").write_text(json.dumps(responses, indent=1))
(out / "summary.json").write_text(json.dumps(summary, indent=1)); print(json.dumps(summary, indent=1))
