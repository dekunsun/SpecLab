import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import jarvis, spec as specmod, funnel2

sp = specmod.load(); entries = jarvis.load(); t = time.time()
res = funnel2.run(entries, sp)
res["meta"] = {"dataset": "JARVIS-DFT 3D (jarvis-tools figshare copy)", "n_entries": len(entries), "seconds": round(time.time() - t, 1), "spec_version": sp["version"]}
out = Path("results/funnel"); out.mkdir(parents=True, exist_ok=True)
(out / "v0.2_jarvis.json").write_text(json.dumps(res, indent=1))
L = ["# Funnel v0.2: JARVIS-DFT with evidence grades", "", f"{len(entries)} entries; {res['meta']['seconds']} s.", "",
     "| stage | survivors | removed (reason: n) |", "|---|---:|---|"]
for s in funnel2.STAGES:
    rem = ", ".join(f"{k}: {v}" for k, v in sorted(res["removed"].get(s, {}).items(), key=lambda kv: -kv[1])) if s != "all" else ""
    L.append(f"| {s} | {res['counts'].get(s, 0)} | {rem} |")
L += ["", f"Grades: {res['grades']}", "", "Grade A (TBmBJ gap >= 4.25 eV and DFPT k >= 21), sorted by DFPT k:", "",
      "| rank | jid | formula | sg | Eg mBJ | hull | k DFPT | ICSD | flag |", "|---:|---|---|---:|---:|---:|---:|---|---|"]
for r in [r for r in res["survivors"] if r["grade"] == "A"]:
    L.append(f"| {r['rank']} | {r['jid']} | {r['formula']} | {r['spacegroup']} | {r['gap']:.2f} | {r['ehull']:.3f} | {r['k_dfpt']:.1f} | {'yes' if r['icsd'] else ''} | {'DFPT k > 100: soft-mode divergence, needs a phonon check' if r['k_dfpt'] > 100 else ''} |")
(out / "v0.2_jarvis.md").write_text("\n".join(L) + "\n"); print("\n".join(L))
