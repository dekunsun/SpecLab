"""Energy above hull from JARVIS formation energies, per chemical system, with pymatgen.
JARVIS's own `ehull` field is not usable in the 2025 release (see docs/registration.md)."""
from __future__ import annotations
from itertools import combinations
from functools import lru_cache
from pymatgen.core import Composition
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDEntry

_INDEX = None


def _index(entries):
    global _INDEX
    if _INDEX is None:
        idx = {}
        for x in entries:
            ef = x.get("formation_energy_peratom")
            try:
                ef = float(ef)
            except (TypeError, ValueError):
                continue
            idx.setdefault(frozenset(x["elements"]), []).append((x["jid"], x["formula"], ef, x["nat"]))
        _INDEX = idx
    return _INDEX


def _subsets(elements):
    els = sorted(elements)
    for r in range(1, len(els) + 1):
        for c in combinations(els, r):
            yield frozenset(c)


@lru_cache(maxsize=None)
def _pd(chemsys: frozenset, _entries_id: int):
    idx = _INDEX
    pde = [PDEntry(Composition(el), 0.0, name=el) for el in chemsys]
    for sub in _subsets(chemsys):
        for jid, formula, ef, nat in idx.get(sub, []):
            comp = Composition(formula)
            pde.append(PDEntry(comp, ef * comp.num_atoms, name=jid))
    try:
        return PhaseDiagram(pde)
    except Exception:
        return None


def e_above_hull(entries, x) -> float | None:
    idx = _index(entries)
    chemsys = frozenset(x["elements"])
    pd = _pd(chemsys, id(entries))
    if pd is None:
        return None
    try:
        ef = float(x["formation_energy_peratom"])
    except (TypeError, ValueError):
        return None
    comp = Composition(x["formula"])
    return float(pd.get_e_above_hull(PDEntry(comp, ef * comp.num_atoms, name=x["jid"])))
