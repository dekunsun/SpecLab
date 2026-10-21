"""Run the funnel over MP-20 and write results/funnel/<spec>.json and .md."""
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import data, spec as specmod, funnel, dielectric

name = sys.argv[1] if len(sys.argv) > 1 else "high_k_gate_dielectric"
sp = specmod.load(name)
data.download()
entries = data.load()
t = time.time()
res = funnel.run(entries, sp, progress=lambda i: print(f"  {i}/{len(entries)}", file=sys.stderr))
res["meta"] = {"spec": name, "spec_version": sp["version"], "n_entries": len(entries),
               "seconds": round(time.time() - t, 1), "polarizability_table_verified": dielectric.VERIFIED,
               "dataset": "MP-20 (txie-93/cdvae, GitHub), <=20 atoms per cell, PBE gaps"}
out = Path("results/funnel"); out.mkdir(parents=True, exist_ok=True)
(out / f"{name}.json").write_text(json.dumps(res, indent=1))
lines = [f"# Funnel: {name} v{sp['version']}", "", f"Dataset: {res['meta']['dataset']}; {len(entries)} entries; {res['meta']['seconds']} s.", "",
         "| stage | survivors | removed (reason: n) |", "|---|---:|---|"]
prev = res["counts"]["all"]
for s in funnel.STAGES:
    n = res["counts"].get(s, 0)
    rem = ", ".join(f"{k}: {v}" for k, v in sorted(res["removed"].get(s, {}).items(), key=lambda kv: -kv[1])) if s != "all" else ""
    lines.append(f"| {s} | {n} | {rem} |")
lines += ["", f"Survivors: {len(res['survivors'])}. Top 30 by tie-breaker score:", "",
          "| rank | id | formula | sg | Eg PBE | hull | k_CM | score |", "|---:|---|---|---:|---:|---:|---:|---:|"]
for s in res["survivors"][:30]:
    lines.append(f"| {s['rank']} | {s['material_id']} | {s['formula']} | {s['spacegroup']} | {s['band_gap_pbe']:.2f} | {s['e_above_hull']:.3f} | {s['k_cm']:.1f} | {s['score']:.3f} |")
(out / f"{name}.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines[:12]))
