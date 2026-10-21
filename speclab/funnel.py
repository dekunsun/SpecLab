"""The candidate funnel: ordered hard-constraint stages, each recording what it removed and why.

Stages in this version:
  0 all entries
  1 composition   must contain O, no blacklisted element
  2 stability     energy above hull <= spec
  3 band gap      PBE gap >= calibrated threshold
  4 dielectric    Clausius-Mossotti estimate >= screen_min (None -> removed as 'unscorable')
  5 rank          survivors ordered by a Pareto-aware score

Not run (declared in the spec): band offset, reaction with Si, precursors, crystallisation
temperature, novelty. The ranking is a tie-breaker for the deliverable list, not a verdict.
"""
from __future__ import annotations
from collections import Counter
from . import spec as specmod, dielectric
from .data import Entry, structure

STAGES = ["all", "composition", "stability", "band_gap", "dielectric"]


def run(entries: list[Entry], spec: dict, progress=None) -> dict:
    counts = Counter(all=len(entries))
    removed = {s: Counter() for s in STAGES[1:]}
    survivors = []
    for i, e in enumerate(entries):
        if progress and i % 2000 == 0:
            progress(i)
        ok, why = specmod.composition_ok(spec, e.elements)
        if not ok:
            removed["composition"][why.split(":")[0]] += 1
            continue
        counts["composition"] += 1
        if not specmod.stability_ok(spec, e.e_above_hull):
            removed["stability"]["above_hull"] += 1
            continue
        counts["stability"] += 1
        if not specmod.gap_ok(spec, e.band_gap):
            removed["band_gap"]["pbe_gap_below_threshold"] += 1
            continue
        counts["band_gap"] += 1
        est = dielectric.estimate(structure(e))
        if not specmod.dielectric_ok(spec, est["k"]):
            removed["dielectric"][est["reason"] if est["k"] is None else "k_below_screen"] += 1
            continue
        counts["dielectric"] += 1
        survivors.append({"material_id": e.material_id, "formula": e.formula, "spacegroup": e.spacegroup,
                          "band_gap_pbe": e.band_gap, "e_above_hull": e.e_above_hull,
                          "k_cm": round(est["k"], 2), "cm_x": round(est["x"], 4), "split": e.split,
                          "assumed_polarizability": any((el, 4) in dielectric.ASSUMED for el in e.elements)})
    for s in survivors:
        s["score"] = score(s, spec)
    survivors.sort(key=lambda s: -s["score"])
    for r, s in enumerate(survivors, 1):
        s["rank"] = r
    return {"counts": dict(counts), "removed": {k: dict(v) for k, v in removed.items()}, "survivors": survivors}


def score(s: dict, spec: dict) -> float:
    """Tie-breaker: distance above each proxy threshold, equally weighted, hull penalised.
    Not a figure of merit for the physics; stated as such in the registration."""
    m = spec["material_proxies"]
    g = (s["band_gap_pbe"] - m["band_gap"]["pbe_threshold_eV"]) / m["band_gap"]["pbe_threshold_eV"]
    k = min(s["k_cm"], 60) / m["dielectric_constant"]["target_min"]
    h = s["e_above_hull"] / m["energy_above_hull_eV_per_atom_max"]
    return round(g + k - 0.5 * h, 4)
