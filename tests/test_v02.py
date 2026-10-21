import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speclab import spec as specmod, jarvis, hull

ROOT = Path(__file__).resolve().parent.parent


def test_spec_v02_tolerances_declared():
    sp = specmod.load()
    m = sp["material_proxies"]
    assert m["band_gap"]["mbj_threshold_eV"] == pytest.approx(5.0 * 0.85, abs=0.01)
    assert m["dielectric_constant"]["dfpt_pass_min"] == pytest.approx(25 * 0.84, abs=0.01)


@pytest.mark.skipif(not jarvis.SLIM.exists(), reason="JARVIS slim file not downloaded")
def test_hull_puts_rocksalt_mgo_on_hull_and_jarvis_ehull_is_not_used():
    entries = jarvis.load()
    byid = {x["jid"]: x for x in entries}
    mgo = byid["JVASP-116"]; hfo2 = byid["JVASP-9147"]
    assert hull.e_above_hull(entries, mgo) < 0.05    # JARVIS holds a lower-energy MgO entry (JVASP-115229); rocksalt sits 30 meV above it in their data
    assert hull.e_above_hull(entries, hfo2) < 0.001         # ground state must be on the hull
    assert float(hfo2["ehull"]) > 1.0                       # the field we refused to use
