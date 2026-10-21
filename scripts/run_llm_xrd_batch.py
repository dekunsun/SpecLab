"""Arm A (reading only) through the Message Batches API: same model, prompts, effort and
max_tokens as scripts/run_llm_xrd.py, half price, no latency need. Arm B needs the tool loop
and stays on the synchronous runner.

  --set public|heldout  --run N  --effort high
  --submit   build and submit the batch, write batch id, exit
  --collect  poll until ended, write raw/, responses.json, summary.json
"""
import argparse, json, os, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import xrd, llm, prompts
import anthropic

ap = argparse.ArgumentParser()
ap.add_argument("--set", default="public"); ap.add_argument("--run", type=int, default=1); ap.add_argument("--effort", default="high")
ap.add_argument("--submit", action="store_true"); ap.add_argument("--collect", action="store_true"); ap.add_argument("--poll", type=int, default=60)
a = ap.parse_args()
key = os.environ.get("SPECLAB_ANTHROPIC_KEY") or os.environ.get("ANTHROPIC_API_KEY")
if not key:
    sys.exit("no key: set SPECLAB_ANTHROPIC_KEY")
client = anthropic.Anthropic(api_key=key)
items_path = Path("items/xrd_public.json") if a.set == "public" else Path("data/heldout/xrd_heldout.json")
ans_path = Path("items/xrd_public_answers.json") if a.set == "public" else Path("data/heldout/xrd_heldout_answers.json")
items = json.loads(items_path.read_text()); answers = json.loads(ans_path.read_text())
run_name = f"{llm.MODEL}_armA_batch_{a.set}_run{a.run}"
out = Path("results/xrd") / run_name; out.mkdir(parents=True, exist_ok=True)
meta_path = out / "batch.json"

if a.submit:
    if meta_path.exists():
        sys.exit(f"{meta_path} exists; refusing to submit twice")
    reqs = []
    for it in items:
        payload = xrd.prompt_payload(it) | {"id": it["id"]}
        reqs.append({"custom_id": it["id"], "params": {"model": llm.MODEL, "max_tokens": 16000, "system": prompts.SYSTEM_XRD,
                                                      "output_config": {"effort": a.effort}, "messages": [{"role": "user", "content": prompts.user_xrd(payload)}]}})
    batch = client.messages.batches.create(requests=reqs)
    meta_path.write_text(json.dumps({"batch_id": batch.id, "submitted_at": time.time(), "n": len(reqs), "effort": a.effort, "model": llm.MODEL}, indent=1))
    print(json.dumps({"batch_id": batch.id, "n": len(reqs), "status": batch.processing_status}))

if a.collect:
    meta = json.loads(meta_path.read_text()); bid = meta["batch_id"]
    while True:
        b = client.messages.batches.retrieve(bid)
        print(f"{b.processing_status} {b.request_counts}", file=sys.stderr)
        if b.processing_status == "ended":
            break
        time.sleep(a.poll)
    (out / "raw").mkdir(exist_ok=True)
    responses, usage_in, usage_out, errors = {}, 0, 0, 0
    for r in client.messages.batches.results(bid):
        rec = {"id": r.custom_id, "arm": "A", "model": llm.MODEL, "effort": meta["effort"], "result_type": r.result.type}
        if r.result.type == "succeeded":
            m = r.result.message
            rec["stop_reason"] = m.stop_reason; rec["content"] = [c.model_dump() for c in m.content]
            rec["usage"] = {"input": m.usage.input_tokens, "output": m.usage.output_tokens}
            usage_in += m.usage.input_tokens; usage_out += m.usage.output_tokens
            text = "".join(c.text for c in m.content if c.type == "text"); rec["final_text"] = text
            d = llm.parse(text); rec["parsed"] = d
            if d: responses[r.custom_id] = d["present"]
        else:
            errors += 1; rec["error"] = str(getattr(r.result, "error", r.result))[:500]
        (out / "raw" / f"{r.custom_id}.json").write_text(json.dumps(rec, indent=1, default=str))
    pin, pout = llm.PRICE[llm.MODEL]
    cost = (usage_in / 1e6 * pin + usage_out / 1e6 * pout) * 0.5
    (out / "responses.json").write_text(json.dumps(responses, indent=1))
    summary = {"run": run_name, "batch_id": bid, "effort": meta["effort"], "items": len(items), "answered": len(responses), "api_errors": errors,
               "usage": {"input": usage_in, "output": usage_out}, "cost_usd_batch_price": round(cost, 2), "score": xrd.score(answers, responses)}
    (out / "summary.json").write_text(json.dumps(summary, indent=1)); print(json.dumps(summary, indent=1))
