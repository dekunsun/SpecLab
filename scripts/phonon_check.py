"""Finite-displacement phonons with MACE for the DFPT-divergent grade-A entries and controls."""
import json, sys, warnings, time
from pathlib import Path
import numpy as np
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import jarvis
from mace.calculators import mace_mp
from phonopy import Phonopy
from phonopy.structure.atoms import PhonopyAtoms
from ase import Atoms

TARGETS = {"JVASP-41602": "divergent", "JVASP-7773": "divergent", "JVASP-8061": "divergent", "JVASP-4492": "divergent", "JVASP-35894": "divergent",
           "JVASP-52653": "control", "JVASP-36951": "control", "JVASP-8020": "control"}
if "--all" in sys.argv:
    _res = json.loads(Path("results/funnel/v0.2_jarvis.json").read_text())
    TARGETS = {s["jid"]: ("divergent" if s["k_dfpt"] > 100 else "gradeA") for s in _res["survivors"] if s["grade"] == "A"}
OUT = "softmodes_all" if "--all" in sys.argv else "softmodes"
calc = mace_mp(model="data/models/mace-mp-0b3-medium.model", device="cpu", default_dtype="float64")
jby = {x["jid"]: x for x in jarvis.load()}
rows = []
for jid, role in TARGETS.items():
    s = jarvis.structure(jby[jid]); t = time.time()
    unit = PhonopyAtoms(symbols=[str(sp) for sp in s.species], cell=s.lattice.matrix, scaled_positions=s.frac_coords)
    rep = [max(1, int(np.ceil(8.0 / a))) for a in s.lattice.abc]
    ph = Phonopy(unit, supercell_matrix=np.diag(rep), primitive_matrix=None)
    ph.generate_displacements(distance=0.01)
    forces = []
    for sc in ph.supercells_with_displacements:
        at = Atoms(symbols=sc.symbols, cell=sc.cell, scaled_positions=sc.scaled_positions, pbc=True); at.calc = calc
        forces.append(at.get_forces())
    ph.forces = forces; ph.produce_force_constants()
    ph.run_mesh([4, 4, 4], with_eigenvectors=False, is_gamma_center=True)
    freqs = ph.get_mesh_dict()["frequencies"]
    fmin = float(freqs.min())
    g = ph.get_frequencies([0, 0, 0]); gmin = float(np.min(g))
    rows.append({"jid": jid, "formula": jby[jid]["formula"], "role": role, "k_dfpt": jby[jid]["eps_dfpt_total"], "n_unit": len(s), "supercell": rep,
                 "n_displacements": len(forces), "min_freq_THz_mesh": round(fmin, 3), "min_freq_THz_gamma": round(gmin, 3), "soft": fmin < -0.3, "seconds": round(time.time() - t, 1)})
    print(rows[-1], file=sys.stderr)
Path("results/phonon").mkdir(exist_ok=True)
Path(f"results/phonon/{OUT}.json").write_text(json.dumps(rows, indent=1))
div_soft = sum(r["soft"] for r in rows if r["role"] == "divergent"); ctl_soft = sum(r["soft"] for r in rows if r["role"] == "control")
if "--all" in sys.argv:
    other_soft = sum(r["soft"] for r in rows if r["role"] == "gradeA"); remaining = sum(1 for r in rows if not r["soft"])
    v = {"P36_le_2_soft_among_21_unchecked": other_soft <= 2, "P37_v03_gradeA_20_24": 20 <= remaining <= 24}
    ctl_soft = other_soft
else:
    sr = all(r["soft"] for r in rows if r["formula"] == "SrHfO3")
    v = {"P33_ge_3_of_5_divergent_soft": div_soft >= 3, "P34_le_1_of_3_controls_soft": ctl_soft <= 1, "P35_both_SrHfO3_soft": sr}
L = ["# Soft-mode check (phonopy + MACE-MP-0b3, 4x4x4 mesh)", "", f"Divergent entries soft: {div_soft}/5. Other entries soft: {ctl_soft}.", "",
     "| jid | formula | role | k DFPT | unit atoms | supercell | displacements | min f mesh (THz) | min f Gamma (THz) | soft | s |", "|---|---|---|---:|---:|---|---:|---:|---:|---|---:|"]
L += [f"| {r['jid']} | {r['formula']} | {r['role']} | {r['k_dfpt']:.0f} | {r['n_unit']} | {r['supercell']} | {r['n_displacements']} | {r['min_freq_THz_mesh']} | {r['min_freq_THz_gamma']} | {'YES' if r['soft'] else 'no'} | {r['seconds']} |" for r in rows]
L += ["", "| prediction | held |", "|---|---|"] + [f"| {k} | {'yes' if b else 'NO'} |" for k, b in v.items()]
Path(f"results/phonon/{OUT}.md").write_text("\n".join(L) + "\n"); print("\n".join(L))
