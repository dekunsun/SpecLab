"""Funnel v0.2: JARVIS-DFT with evidence grades. Removal needs DFT-level evidence; proxies grade,
they do not reject (except the band-gap proxy, which is kept from v0.1 because no gap at all
is worse than a calibrated PBE-level gap)."""
from __future__ import annotations
from collections import Counter
from . import spec as specmod, dielectric
from .jarvis import structure
from . import hull as hullmod

STAGES = ["all", "composition", "stability", "band_gap", "dielectric"]


def run(entries: list[dict], spec: dict) -> dict:
    m = spec["material_proxies"]
    counts = Counter(all=len(entries)); removed = {s: Counter() for s in STAGES[1:]}
    out = []
    for x in entries:
        ok, why = specmod.composition_ok(spec, x["elements"])
        if not ok:
            removed["composition"][why.split(":")[0]] += 1; continue
        counts["composition"] += 1
        eah = hullmod.e_above_hull(entries, x)
        if eah is None or eah > m["energy_above_hull_eV_per_atom_max"]:
            removed["stability"]["above_hull" if eah is not None else "no_hull"] += 1; continue
        x["ehull_f"] = eah
        counts["stability"] += 1
        if x["gap_mbj"] is not None:
            gap_ev, gap_val, gap_ok = "mbj", x["gap_mbj"], x["gap_mbj"] >= m["band_gap"]["mbj_threshold_eV"]
        else:
            gap_ev, gap_val, gap_ok = "optb88", x["gap_opt"], (x["gap_opt"] or 0) >= m["band_gap"]["pbe_threshold_eV"]
        if not gap_ok:
            removed["band_gap"][f"below_threshold_{gap_ev}"] += 1; continue
        counts["band_gap"] += 1
        k_dfpt = x["eps_dfpt_total"]; k_el = x["eps_el_mbj"] if x["eps_el_mbj"] is not None else x["eps_el_opt"]
        if k_dfpt is not None:
            if k_dfpt < m["dielectric_constant"]["dfpt_pass_min"]:
                removed["dielectric"]["dfpt_below_target"] += 1; continue
            k_ev = "dfpt"
        elif k_el is not None and k_el >= m["dielectric_constant"]["dfpt_pass_min"]:
            k_ev = "electronic_lower_bound_passes"
        else:
            k_ev = "lower_bound_only" if k_el is not None else "none"
        counts["dielectric"] += 1
        grade = "A" if (gap_ev == "mbj" and k_ev == "dfpt") else ("B" if (gap_ev == "mbj" or k_ev in ("dfpt", "electronic_lower_bound_passes")) else "C")
        rec = {"jid": x["jid"], "formula": x["formula"], "spacegroup": x["spg_number"], "nat": x["nat"], "ehull": x["ehull_f"],
               "gap": gap_val, "gap_evidence": gap_ev, "k_dfpt": k_dfpt, "k_electronic": k_el, "k_evidence": k_ev,
               "icsd": x["has_icsd"], "grade": grade}
        if grade != "A":
            est = dielectric.estimate(structure(x)); rec["k_cm_flag"] = round(est["k"], 1) if est["k"] else est["reason"]
        out.append(rec)
    out.sort(key=lambda r: ({"A": 0, "B": 1, "C": 2}[r["grade"]], -(r["k_dfpt"] or r["k_electronic"] or 0)))
    for i, r in enumerate(out, 1):
        r["rank"] = i
    return {"counts": dict(counts), "removed": {k: dict(v) for k, v in removed.items()}, "survivors": out,
            "grades": dict(Counter(r["grade"] for r in out))}
