import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import spec as specmod, dielectric, funnel
from speclab.data import Entry
from pymatgen.core import Structure, Lattice


def test_spec_loads_and_declares_unscreened():
    sp = specmod.load()
    assert sp["material_proxies"]["band_gap"]["pbe_threshold_eV"] == 3.4
    assert "band_offset_to_Si" in sp["not_screened_in_this_version"]


def test_composition_rules():
    sp = specmod.load()
    assert specmod.composition_ok(sp, ("Hf", "O"))[0]
    assert not specmod.composition_ok(sp, ("Hf", "N"))[0]
    assert specmod.composition_ok(sp, ("Pb", "Ti", "O"))[1].startswith("blacklisted")


def _mgo():
    return Structure.from_spacegroup("Fm-3m", Lattice.cubic(4.212), ["Mg", "O"], [[0, 0, 0], [0.5, 0.5, 0.5]])


def test_clausius_mossotti_anchor_mgo():
    k = dielectric.estimate(_mgo())["k"]
    assert 7.5 <= k <= 11.5, k   # experiment 9.8


def test_clausius_mossotti_reports_missing_ion():
    s = Structure(Lattice.cubic(4.0), ["Sb", "Sb", "O", "O", "O", "O", "O"],
                  [[0, 0, 0], [0.5, 0.5, 0.5], [0.25, 0.25, 0.25], [0.75, 0.75, 0.75], [0.25, 0.75, 0.25], [0.75, 0.25, 0.75], [0.5, 0, 0]])
    r = dielectric.estimate(s)
    assert r["k"] is None and r["reason"].startswith("no_")


def test_funnel_records_each_removal_stage():
    sp = specmod.load()
    cif = _mgo().to(fmt="cif")
    mk = lambda i, els, gap, hull: Entry(f"t-{i}", "X", gap, hull, -1.0, 1, tuple(els), cif, "test")
    entries = [mk(1, ["Mg", "N"], 5, 0), mk(2, ["Mg", "O"], 5, 0.2), mk(3, ["Mg", "O"], 1, 0), mk(4, ["Mg", "O"], 5, 0)]
    res = funnel.run(entries, sp)
    assert res["removed"]["composition"] == {"missing_required_element": 1}
    assert res["removed"]["stability"] == {"above_hull": 1}
    assert res["removed"]["band_gap"] == {"pbe_gap_below_threshold": 1}
    assert res["removed"]["dielectric"] == {"k_below_screen": 1}   # MgO k_CM ~ 9 < 15
    assert res["survivors"] == []
