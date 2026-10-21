import json, sys
from pathlib import Path
import numpy as np, pandas as pd
from scipy.stats import spearmanr
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import dielectric, spec as specmod
from pymatgen.core import Structure

sp = specmod.load(); df = pd.read_pickle("data/raw/matminer_dielectric_constant.pkl")
rows = []
for _, r in df.iterrows():
    s = r["structure"] if isinstance(r["structure"], Structure) else Structure.from_dict(r["structure"])
    els = tuple(sorted({str(e) for e in s.composition.elements}))
    if "O" not in els or not specmod.composition_ok(sp, els)[0]:
        continue
    est = dielectric.estimate(s)
    rows.append({"material_id": r["material_id"], "formula": r["formula"], "dfpt": float(r["poly_total"]), "cm": est["k"], "x": est["x"], "reason": est["reason"], "pot_ferroelectric": bool(r["pot_ferroelectric"])})
sc = [x for x in rows if x["cm"] is not None]
d = np.array([x["dfpt"] for x in sc]); c = np.array([x["cm"] for x in sc]); mask = d < 200
out = {"n_oxides": len(rows), "n_scored": len(sc), "unscorable_share": round(1 - len(sc) / len(rows), 3),
       "spearman_lt_200": round(float(spearmanr(c[mask], d[mask]).correlation), 3), "mard_lt_200": round(float(np.mean(np.abs(c[mask] - d[mask]) / d[mask])), 3),
       "n_ge_25": int((d >= 25).sum()), "recall_at_15": round(float(np.mean(c[d >= 25] >= 15)), 3), "precision_at_15": round(float(np.mean(d[c >= 15] >= 25)), 3)}
Path("results/dielectric").mkdir(exist_ok=True)
json.dump({"summary": out, "rows": rows}, open("results/dielectric/cm_vs_petousis.json", "w"), indent=1)
md = ["# Clausius-Mossotti vs Petousis 2017 DFPT (MP), oxides passing the composition rule", ""] + [f"- {k}: {v}" for k, v in out.items()]
v = {"P28_spearman_0.6_0.8": 0.6 <= out["spearman_lt_200"] <= 0.8, "P29_recall_0.35_0.6": 0.35 <= out["recall_at_15"] <= 0.6, "P30_unscorable_20_40pct": 0.2 <= out["unscorable_share"] <= 0.4}
md += ["", "| prediction | held |", "|---|---|"] + [f"| {k} | {'yes' if b else 'NO'} |" for k, b in v.items()]
Path("results/dielectric/cm_vs_petousis.md").write_text("\n".join(md) + "\n"); print("\n".join(md))
