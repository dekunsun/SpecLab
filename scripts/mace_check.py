"""Relax grade-A v0.2 survivors and v0.1 positives with MACE-MP-0; record energy and volume change."""
import json, sys, time, warnings
from pathlib import Path
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import data, jarvis
from mace.calculators import mace_mp
from ase.optimize import FIRE
from ase.filters import FrechetCellFilter
from pymatgen.io.ase import AseAtomsAdaptor

calc = mace_mp(model="data/models/mace-mp-0b3-medium.model", device="cpu", default_dtype="float64")
res = json.loads(Path("results/funnel/v0.2_jarvis.json").read_text())
A = [s for s in res["survivors"] if s["grade"] == "A"]
jby = {x["jid"]: x for x in jarvis.load()}; mby = {e.material_id: e for e in data.load()}
todo = [(s["jid"], s["formula"], jarvis.structure(jby[s["jid"]]), "v0.2 grade A", s["k_dfpt"]) for s in A]
todo += [(m, mby[m].formula, data.structure(mby[m]), "v0.1 positive", None) for m in ["mp-352", "mp-685097", "mp-2858", "mp-1968", "mp-5304", "mp-22220"]]
rows = []
for sid, formula, st, role, k in todo:
    atoms = AseAtomsAdaptor.get_atoms(st); atoms.calc = calc
    e0 = atoms.get_potential_energy() / len(atoms); v0 = atoms.get_volume(); t = time.time()
    opt = FIRE(FrechetCellFilter(atoms), logfile=None); conv = opt.run(fmax=0.05, steps=300)
    e1 = atoms.get_potential_energy() / len(atoms)
    rows.append({"id": sid, "formula": formula, "role": role, "k_dfpt": k, "n_atoms": len(atoms), "dE_meV_atom": round(1000 * (e1 - e0), 1),
                 "dV_pct": round(100 * (atoms.get_volume() / v0 - 1), 2), "converged": bool(conv), "steps": opt.get_number_of_steps(), "seconds": round(time.time() - t, 1)})
    print(rows[-1], file=sys.stderr)
Path("results/mace").mkdir(exist_ok=True)
Path("results/mace/relax.json").write_text(json.dumps(rows, indent=1))
n = len(rows); okv = sum(abs(r["dV_pct"]) < 3 for r in rows); oke = sum(abs(r["dE_meV_atom"]) < 30 for r in rows)
fails = [r for r in rows if abs(r["dV_pct"]) >= 3 or abs(r["dE_meV_atom"]) >= 30]
div_fail = sum(1 for r in fails if r["k_dfpt"] and r["k_dfpt"] > 100)
verdict = {"P25_volume_lt_3pct_ge_90pct": okv / n >= 0.9, "P26_energy_lt_30meV_ge_90pct": oke / n >= 0.9,
           "P27_failures_half_divergent": (div_fail / len(fails) >= 0.5) if fails else None}
L = ["# MACE-MP-0b3 relaxation cross-check", "", f"{n} structures; |dV| < 3 %: {okv}; |dE| < 30 meV/atom: {oke}; failures: {len(fails)}, of which DFPT-divergent: {div_fail}.", "",
     "| id | formula | role | k DFPT | dE (meV/atom) | dV (%) | conv | steps | s |", "|---|---|---|---:|---:|---:|---|---:|---:|"]
L += [f"| {r['id']} | {r['formula']} | {r['role']} | {r['k_dfpt'] if r['k_dfpt'] else ''} | {r['dE_meV_atom']} | {r['dV_pct']} | {r['converged']} | {r['steps']} | {r['seconds']} |" for r in rows]
L += ["", "| prediction | held |", "|---|---|"] + [f"| {k} | {'yes' if v else ('n/a' if v is None else 'NO')} |" for k, v in verdict.items()]
Path("results/mace/relax.md").write_text("\n".join(L) + "\n"); print("\n".join(L))
