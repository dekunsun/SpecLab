"""Load a reference product profile and evaluate its hard material-level constraints."""
from __future__ import annotations
from pathlib import Path
import yaml

SPECS = Path(__file__).resolve().parent.parent / "specs"


def load(name: str = "high_k_gate_dielectric") -> dict:
    with open(SPECS / f"{name}.yaml") as fh:
        return yaml.safe_load(fh)


def composition_ok(spec: dict, elements) -> tuple[bool, str]:
    m = spec["material_proxies"]
    els = set(elements)
    if not set(m["must_contain"]) <= els:
        return False, "missing_required_element"
    bad = els & set(m["blacklist_elements"])
    if bad:
        return False, "blacklisted:" + ",".join(sorted(bad))
    return True, "ok"


def stability_ok(spec: dict, e_above_hull: float) -> bool:
    return e_above_hull <= spec["material_proxies"]["energy_above_hull_eV_per_atom_max"]


def gap_ok(spec: dict, pbe_gap: float) -> bool:
    return pbe_gap >= spec["material_proxies"]["band_gap"]["pbe_threshold_eV"]


def dielectric_ok(spec: dict, k_est: float | None) -> bool:
    return k_est is not None and k_est >= spec["material_proxies"]["dielectric_constant"]["screen_min"]
