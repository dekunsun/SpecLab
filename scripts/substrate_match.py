"""ZSL coincident-site lattice matching of grade-A candidates on common substrates."""
import json, sys, warnings
from pathlib import Path
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import jarvis
from pymatgen.core import Structure, Lattice
from pymatgen.analysis.interfaces.substrate_analyzer import SubstrateAnalyzer

subs = {"Si(001)": (Structure.from_spacegroup("Fd-3m", Lattice.cubic(5.431), ["Si"], [[0, 0, 0]]), (0, 0, 1)),
        "Si(111)": (Structure.from_spacegroup("Fd-3m", Lattice.cubic(5.431), ["Si"], [[0, 0, 0]]), (1, 1, 1)),
        "TiN(001)": (Structure.from_spacegroup("Fm-3m", Lattice.cubic(4.24), ["Ti", "N"], [[0, 0, 0], [0.5, 0.5, 0.5]]), (0, 0, 1)),
        "Pt(111)": (Structure.from_spacegroup("Fm-3m", Lattice.cubic(3.924), ["Pt"], [[0, 0, 0]]), (1, 1, 1))}
res = json.loads(Path("results/funnel/v0.2_jarvis.json").read_text())
A = [s for s in res["survivors"] if s["grade"] == "A"]
jby = {x["jid"]: x for x in jarvis.load()}
sa = SubstrateAnalyzer(max_area=400)
rows = []
for s in A:
    film = jarvis.structure(jby[s["jid"]])
    row = {"jid": s["jid"], "formula": s["formula"], "k_dfpt": s["k_dfpt"]}
    for name, (sub, miller) in subs.items():
        best = None
        try:
            for m in sa.calculate(film=film, substrate=sub, substrate_millers=[miller], lowest=True):
                strain = m.von_mises_strain if m.von_mises_strain is not None else 9
                if strain < 0.02 and (best is None or m.match_area < best[0]):
                    best = (round(float(m.match_area), 1), round(100 * float(strain), 2), tuple(int(i) for i in m.film_miller))
        except Exception as e:
            best = ("err", str(e)[:40], None)
        row[name] = best
    rows.append(row); print(row, file=sys.stderr)
Path("results/substrate").mkdir(exist_ok=True)
Path("results/substrate/zsl.json").write_text(json.dumps(rows, indent=1))
ok = lambda b: b is not None and b[0] != "err"
any_match = sum(1 for r in rows if any(ok(r[n]) for n in subs))
si_small = sum(1 for r in rows if ok(r["Si(001)"]) and r["Si(001)"][0] < 100)
v = {"P31_ge_20_with_any_match": any_match >= 20, "P32_lt_10_small_area_on_Si001": si_small < 10}
L = ["# ZSL substrate match, grade-A candidates (area A^2, strain %, film Miller) with strain < 2 %", "",
     f"{len(rows)} candidates; with a match on any substrate: {any_match}; Si(001) match below 100 A^2: {si_small}.", "",
     "| jid | formula | k DFPT | " + " | ".join(subs) + " |", "|---|---|---:|" + "---|" * len(subs)]
fmt = lambda b: "none" if b is None else (f"{b[0]} / {b[1]} / {b[2]}" if b[0] != "err" else "err")
L += [f"| {r['jid']} | {r['formula']} | {r['k_dfpt']:.0f} | " + " | ".join(fmt(r[n]) for n in subs) + " |" for r in rows]
L += ["", "| prediction | held |", "|---|---|"] + [f"| {k} | {'yes' if b else 'NO'} |" for k, b in v.items()]
Path("results/substrate/zsl.md").write_text("\n".join(L) + "\n"); print("\n".join(L[:4] + L[-3:]))
