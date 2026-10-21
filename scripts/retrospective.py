"""Score the registered controls against results/funnel/<spec>.json."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import data, spec as specmod, funnel, dielectric

name = sys.argv[1] if len(sys.argv) > 1 else "high_k_gate_dielectric"
res = json.loads(Path(f"results/funnel/{name}.json").read_text())
sp = specmod.load(name)
POS = ["mp-352", "mp-685097", "mp-2858", "mp-1968", "mp-5304", "mp-22220"]
NEG = {"mp-2657": "band_gap", "mp-5229": "band_gap", "mp-10390": "band_gap",
       "mp-1143": "dielectric", "mp-7000": "dielectric", "mp-1265": "dielectric", "mp-4609": "dielectric"}
byid = {e.material_id: e for e in data.load()}
surv = {s["material_id"]: s for s in res["survivors"]}


def stage_of(e):
    ok, _ = specmod.composition_ok(sp, e.elements)
    if not ok: return "composition"
    if not specmod.stability_ok(sp, e.e_above_hull): return "stability"
    if not specmod.gap_ok(sp, e.band_gap): return "band_gap"
    est = dielectric.estimate(data.structure(e))
    if not specmod.dielectric_ok(sp, est["k"]): return "dielectric"
    return "survived"

rows, verdict = [], {}
for mid in POS:
    s = surv.get(mid); e = byid[mid]
    rows.append((mid, e.formula, "positive", "survived" if s else stage_of(e), s["rank"] if s else None))
verdict["P2_all_positives_survive"] = all(r[3] == "survived" for r in rows)
for mid, exp in NEG.items():
    e = byid[mid]; st = stage_of(e)
    rows.append((mid, e.formula, f"negative (expect {exp})", st, surv.get(mid, {}).get("rank")))
verdict["P3_negatives_removed_at_named_stage"] = all(r[3] == NEG[r[0]] for r in rows if r[2].startswith("negative") and r[0] != "mp-4609")
verdict["P6_HfSiO4_removed_at_dielectric"] = stage_of(byid["mp-4609"]) == "dielectric"
n = len(res["survivors"]); verdict["P1_survivors_200_800"] = 200 <= n <= 800
top20 = res["survivors"][:20]
pos_in_top = [m for m in POS if surv.get(m) and surv[m]["rank"] <= 20]
div = sum(1 for s in top20 if s["cm_x"] > 0.95)
verdict["P4_tiebreaker_weakness"] = len(pos_in_top) <= 2 and div >= 10
gap_pass = res["counts"]["band_gap"]; unscor = sum(v for k, v in res["removed"]["dielectric"].items() if k.startswith("no_") or k == "cm_divergent")
frac = unscor / gap_pass if gap_pass else 0
verdict["P5_unscorable_10_40pct"] = 0.10 <= frac <= 0.40
out = ["# Retrospective controls", "", f"Survivors: {n}. Positives in Top-20: {pos_in_top}. Top-20 with x > 0.95: {div}. Unscorable after band_gap: {unscor}/{gap_pass} = {frac:.1%}.", "",
       "| id | formula | role | outcome | rank |", "|---|---|---|---|---:|"]
out += [f"| {a} | {b} | {c} | {d} | {e if e else ''} |" for a, b, c, d, e in rows]
out += ["", "| prediction | held |", "|---|---|"] + [f"| {k} | {'yes' if v else 'NO'} |" for k, v in verdict.items()]
Path("results/funnel/retrospective.md").write_text("\n".join(out) + "\n")
Path("results/funnel/retrospective.json").write_text(json.dumps({"rows": rows, "verdict": verdict, "pos_in_top20": pos_in_top, "top20_divergent": div, "unscorable_frac": frac}, indent=1))
print("\n".join(out))
