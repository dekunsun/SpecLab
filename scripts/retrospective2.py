"""Check the v0.2 registration (P19-P24, as amended) against results/funnel/v0.2_jarvis.json."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import jarvis, spec as specmod, hull as hullmod

res = json.loads(Path("results/funnel/v0.2_jarvis.json").read_text())
sp = specmod.load(); m = sp["material_proxies"]
entries = jarvis.load(); byid = {x["jid"]: x for x in entries}
surv = {s["jid"]: s for s in res["survivors"]}
A = [s for s in res["survivors"] if s["grade"] == "A"]

def stage_of(x):
    if not specmod.composition_ok(sp, x["elements"])[0]: return "composition"
    eah = hullmod.e_above_hull(entries, x)
    if eah is None or eah > m["energy_above_hull_eV_per_atom_max"]: return f"stability ({eah:.3f})" if eah is not None else "stability (no hull)"
    if x["gap_mbj"] is not None:
        if x["gap_mbj"] < m["band_gap"]["mbj_threshold_eV"]: return f"band_gap (mbj {x['gap_mbj']:.2f})"
    elif (x["gap_opt"] or 0) < m["band_gap"]["pbe_threshold_eV"]: return f"band_gap (optb88 {x['gap_opt']})"
    k = x["eps_dfpt_total"]
    if k is not None and k < m["dielectric_constant"]["dfpt_pass_min"]: return f"dielectric (dfpt {k:.1f})"
    return "survived"

controls = {"JVASP-9147": ("HfO2 monoclinic", "positive"), "JVASP-52653": ("HfO2 Pca21", "positive"), "JVASP-113": ("ZrO2 monoclinic", "positive (amended: expect band_gap)"),
            "JVASP-5": ("TiO2 rutile", "negative: band_gap"), "JVASP-8082": ("SrTiO3", "negative: band_gap"),
            "JVASP-32": ("Al2O3 corundum", "negative: dielectric"), "JVASP-116": ("MgO rocksalt", "negative: dielectric")}
# quartz SiO2: find by formula and spg 154
for x in entries:
    if x["formula"] == "SiO2" and str(x["spg_number"]) == "154":
        controls[x["jid"]] = ("SiO2 quartz", "negative: dielectric"); break
rows = []
for jid, (name, role) in controls.items():
    x = byid[jid]; st = stage_of(x); s = surv.get(jid)
    rows.append((jid, name, role, st, s["grade"] if s else "", s["rank"] if s else ""))
stab = res["counts"]["stability"]
mbj_share = sum(1 for x in entries if x["gap_mbj"] is not None and specmod.composition_ok(sp, x["elements"])[0] and (hullmod.e_above_hull(entries, x) or 9) <= 0.05) / stab
classes = lambda f: any(t in f for t in ("Hf", "Ta", "Nb", "Zr")) or any(f.endswith(t) for t in ("AlO3", "ScO3"))
named = sum(1 for s in A if classes(s["formula"]))
icsd = sum(1 for s in A if s["icsd"])
verdict = {"P19_stable_oxides_4000_12000": 4000 <= stab <= 12000,
           "P20_mbj_share_20_40pct": 0.20 <= mbj_share <= 0.40,
           "P21_gradeA_10_80": 10 <= len(A) <= 80,
           "P22_controls_as_amended": all((r[3] == "survived") == (r[2] == "positive") for r in rows if "amended" not in r[2]) and rows[2][3].startswith("band_gap"),
           "P23_icsd_share_ge_60pct": icsd / len(A) >= 0.6,
           "P24_named_classes_ge_half": named / len(A) >= 0.5}
divergent = [s for s in A if s["k_dfpt"] > 100]
out = ["# Retrospective controls, funnel v0.2 (JARVIS-DFT)", "",
       f"Stable oxides: {stab}. Share with TBmBJ gap: {mbj_share:.1%}. Grade A: {len(A)}; with ICSD id: {icsd} ({icsd/len(A):.0%}); in the named classes: {named} ({named/len(A):.0%}).",
       f"Grade A with DFPT k > 100 (soft-mode divergence, not registered, flagged after the run): {len(divergent)}: " + ", ".join(f"{s['formula']} {s['k_dfpt']:.0f}" for s in divergent), "",
       "| jid | material | role | outcome | grade | rank |", "|---|---|---|---|---|---:|"]
out += [f"| {a} | {b} | {c} | {d} | {e} | {f} |" for a, b, c, d, e, f in rows]
out += ["", "| prediction | held |", "|---|---|"] + [f"| {k} | {'yes' if v else 'NO'} |" for k, v in verdict.items()]
Path("results/funnel/retrospective_v0.2.md").write_text("\n".join(out) + "\n")
Path("results/funnel/retrospective_v0.2.json").write_text(json.dumps({"rows": rows, "verdict": verdict, "mbj_share": mbj_share, "gradeA": len(A), "icsd": icsd, "named": named}, indent=1))
print("\n".join(out))
