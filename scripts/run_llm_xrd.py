"""Run Claude on the XRD items under the registered protocol.

  --arm A|B          A: pattern + CIFs only. B: plus the simulate_pattern tool.
  --set public|heldout
  --run N            run index (held-out gate needs three)
  --effort high      declared in the registration
  --dry-run          count tokens for one item, estimate the set's cost, make no model call
  --budget 40        hard stop in USD for this invocation
  Credential: SPECLAB_ANTHROPIC_KEY (ANTHROPIC_API_KEY as fallback; the cloud environment does not pass that name through)
"""
import argparse, json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import xrd, llm
import anthropic

ap = argparse.ArgumentParser()
ap.add_argument("--arm", default="A"); ap.add_argument("--set", default="public"); ap.add_argument("--run", type=int, default=1)
ap.add_argument("--effort", default="high"); ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--budget", type=float, default=40.0)
a = ap.parse_args()
items_path = Path("items/xrd_public.json") if a.set == "public" else Path("data/heldout/xrd_heldout.json")
ans_path = Path("items/xrd_public_answers.json") if a.set == "public" else Path("data/heldout/xrd_heldout_answers.json")
items = json.loads(items_path.read_text()); answers = json.loads(ans_path.read_text())
# The cloud environment does not pass a variable named ANTHROPIC_API_KEY into sessions (the
# platform reserves it), so the key is read from SPECLAB_ANTHROPIC_KEY first.
import os
_key = os.environ.get("SPECLAB_ANTHROPIC_KEY") or os.environ.get("ANTHROPIC_API_KEY")
if not _key:
    sys.exit("no key: set SPECLAB_ANTHROPIC_KEY in the environment")
client = anthropic.Anthropic(api_key=_key)
if a.dry_run:
    n = llm.count_tokens(client, xrd.prompt_payload(items[0]) | {"id": items[0]["id"]}, a.arm)
    pin, pout = llm.PRICE[llm.MODEL]
    est = len(items) * (n / 1e6 * pin + 3000 / 1e6 * pout) * (3 if a.arm == "B" else 1)
    print(json.dumps({"input_tokens_item0": n, "items": len(items), "assumed_output_tokens": 3000, "arm_multiplier": 3 if a.arm == "B" else 1, "estimated_usd": round(est, 2)}))
    sys.exit(0)
run_name = f"{llm.MODEL}_arm{a.arm}_{a.set}_run{a.run}"
out = Path("results/xrd") / run_name; out.mkdir(parents=True, exist_ok=True)
responses, spent, t0 = {}, 0.0, time.time()
for i, it in enumerate(items):
    if (out / "raw" / f"{it['id']}.json").exists():       # resume
        rec = json.loads((out / "raw" / f"{it['id']}.json").read_text()); spent += rec["cost_usd"]
        if rec["parsed"]: responses[it["id"]] = rec["parsed"]["present"]
        continue
    present, rec = llm.run_item(client, it, a.arm, a.effort, out)
    spent += rec["cost_usd"]
    if present: responses[it["id"]] = present
    print(f"{i+1}/{len(items)} {it['id']} {it['tier']} -> {present} ${spent:.2f}", file=sys.stderr)
    if spent > a.budget:
        print(f"budget {a.budget} exceeded; stopping", file=sys.stderr); break
(out / "responses.json").write_text(json.dumps(responses, indent=1))
score = xrd.score(answers, responses)
summary = {"run": run_name, "effort": a.effort, "items": len(items), "answered": len(responses), "cost_usd": round(spent, 2), "seconds": round(time.time() - t0), "score": score}
(out / "summary.json").write_text(json.dumps(summary, indent=1)); print(json.dumps(summary, indent=1))
