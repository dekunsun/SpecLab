"""Run random, oracle and classic agents on the public items; write results/xrd/."""
import json, random, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import xrd

items = json.loads(Path("items/xrd_public.json").read_text())
answers = json.loads(Path("items/xrd_public_answers.json").read_text())
out = Path("results/xrd"); out.mkdir(parents=True, exist_ok=True)
rng = random.Random(1)
runs = {"random": lambda it: xrd.agent_random(it, rng), "oracle": lambda it: xrd.agent_oracle(it, answers), "classic_nnls": xrd.agent_classic, "classic_refined": xrd.agent_classic_refined}
summary = {}
for name, fn in runs.items():
    t = time.time(); resp = {}
    for it in items:
        resp[it["id"]] = fn(xrd.prompt_payload(it) | {"id": it["id"]})
    (out / f"{name}_responses.json").write_text(json.dumps(resp, indent=1))
    summary[name] = xrd.score(answers, resp) | {"seconds": round(time.time() - t, 1)}
(out / "summary.json").write_text(json.dumps(summary, indent=1))
lines = ["# XRD baselines (public set, 40 items per tier)", "", "| agent | tier | exact | jaccard | coverage |", "|---|---|---:|---:|---:|"]
for name, per in summary.items():
    for tier in ("T1", "T2", "T3"):
        d = per[tier]; lines.append(f"| {name} | {tier} | {d['exact_rate']} | {d['jaccard_mean']} | {d['coverage']} |")
(out / "summary.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
