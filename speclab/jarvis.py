"""JARVIS-DFT 3D loader (slim JSON written by scripts/fetch_jarvis.py from jarvis-tools' figshare copy).

Fields used: optb88vdw_bandgap (all), mbj_bandgap (TBmBJ, ~21k), epsx/y/z (OptB88 electronic
dielectric, ~60k), mepsx/y/z (mBJ electronic, ~20k), dfpt_piezo_max_dielectric (DFPT total,
~4.7k; electronic + ionic), ehull, icsd, spg_number, atoms."""
from __future__ import annotations
import json, os
from functools import lru_cache
from pathlib import Path

RAW = Path(os.environ.get("SPECLAB_DATA", Path(__file__).resolve().parent.parent / "data" / "raw"))
SLIM = RAW / "jarvis_dft_3d_slim.json"
KEYS = ["jid", "formula", "optb88vdw_bandgap", "mbj_bandgap", "hse_gap", "epsx", "epsy", "epsz", "mepsx", "mepsy",
        "mepsz", "dfpt_piezo_max_dielectric", "dfpt_piezo_max_dielectric_electronic", "dfpt_piezo_max_dielectric_ionic",
        "ehull", "formation_energy_peratom", "icsd", "spg_number", "nat", "typ", "atoms"]


def fetch() -> None:
    from jarvis.db.figshare import data
    RAW.mkdir(parents=True, exist_ok=True)
    d = data("dft_3d")
    json.dump([{k: x.get(k) for k in KEYS} for x in d], open(SLIM, "w"))


def _num(v):
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return f if f == f and f >= 0 else None


@lru_cache(maxsize=None)
def load() -> list[dict]:
    if not SLIM.exists():
        fetch()
    out = []
    for x in json.load(open(SLIM)):
        x["elements"] = tuple(sorted(set(x["atoms"]["elements"])))
        x["gap_opt"] = _num(x["optb88vdw_bandgap"]); x["gap_mbj"] = _num(x["mbj_bandgap"])
        e = [_num(x[k]) for k in ("epsx", "epsy", "epsz")]
        x["eps_el_opt"] = sum(e) / 3 if all(v is not None for v in e) else None
        m = [_num(x[k]) for k in ("mepsx", "mepsy", "mepsz")]
        x["eps_el_mbj"] = sum(m) / 3 if all(v is not None for v in m) else None
        x["eps_dfpt_total"] = _num(x["dfpt_piezo_max_dielectric"])
        x["ehull_f"] = _num(x["ehull"])
        x["has_icsd"] = bool(x.get("icsd")) and x.get("icsd") not in ("na", "", None)
        out.append(x)
    return out


def structure(x: dict):
    from jarvis.core.atoms import Atoms
    return Atoms.from_dict(x["atoms"]).pymatgen_converter()
