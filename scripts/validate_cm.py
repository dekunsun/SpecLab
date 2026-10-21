"""Validate the Clausius-Mossotti screen against DFPT total dielectric constants in JARVIS-DFT.
Writes results/dielectric/cm_vs_dfpt.{json,md}."""
import json, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import jarvis, dielectric, spec as specmod

sp = specmod.load()
rows = []
for x in jarvis.load():
    if x["eps_dfpt_total"] is None or "O" not in x["elements"]:
        continue
    if not specmod.composition_ok(sp, x["elements"])[0]:
        continue
    est = dielectric.estimate(jarvis.structure(x))
    rows.append({"jid": x["jid"], "formula": x["formula"], "dfpt": x["eps_dfpt_total"], "cm": est["k"], "x": est["x"], "reason": est["reason"]})
scored = [r for r in rows if r["cm"] is not None]
d = np.array([r["dfpt"] for r in scored]); c = np.array([r["cm"] for r in scored])
from scipy.stats import spearmanr
mask = d < 200   # DFPT also diverges on near-ferroelectrics; compare on the sane range
mard = float(np.mean(np.abs(c[mask] - d[mask]) / d[mask]))
rho = float(spearmanr(c[mask], d[mask]).correlation)
screen = sp["material_proxies"]["dielectric_constant"]["screen_min"]; target = sp["material_proxies"]["dielectric_constant"]["target_min"]
pos = d >= target
recall = float(np.mean(c[pos] >= screen)) if pos.any() else None
precision = float(np.mean(d[c >= screen] >= target)) if (c >= screen).any() else None
unscor = len(rows) - len(scored)
out = {"n_oxides_with_dfpt": len(rows), "n_scored": len(scored), "n_unscorable": unscor, "mard_dfpt_lt_200": mard,
       "spearman_dfpt_lt_200": rho, "n_dfpt_ge_target": int(pos.sum()), "recall_at_screen": recall, "precision_at_screen": precision,
       "screen_min": screen, "target_min": target}
Path("results/dielectric").mkdir(parents=True, exist_ok=True)
json.dump({"summary": out, "rows": rows}, open("results/dielectric/cm_vs_dfpt.json", "w"), indent=1)
md = ["# Clausius-Mossotti estimate vs DFPT total dielectric constant (JARVIS-DFT, oxides passing the composition rule)", ""]
md += [f"- {k}: {round(v, 3) if isinstance(v, float) else v}" for k, v in out.items()]
md += ["", "Worst 15 under-estimates among DFPT >= target:", "", "| jid | formula | DFPT | CM | x |", "|---|---|---:|---:|---:|"]
miss = sorted([r for r in scored if r["dfpt"] >= target and r["cm"] < screen], key=lambda r: -r["dfpt"])[:15]
md += [f"| {r['jid']} | {r['formula']} | {r['dfpt']:.1f} | {r['cm']:.1f} | {r['x']:.3f} |" for r in miss]
Path("results/dielectric/cm_vs_dfpt.md").write_text("\n".join(md) + "\n")
print("\n".join(md))
