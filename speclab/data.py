"""MP-20 loader. MP-20 (Xie et al., CDVAE) is a GitHub-hosted subset of the Materials Project:
45,229 structures with at most 20 atoms per cell, with PBE band gap, formation energy and
energy above hull as of the 2021 MP release. It is the only structure dataset reachable under
this project's network policy (GitHub and PyPI only)."""
from __future__ import annotations
import csv, os, ast
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

csv.field_size_limit(10**9)
RAW = Path(os.environ.get("SPECLAB_DATA", Path(__file__).resolve().parent.parent / "data" / "raw"))
MP20_URL = "https://raw.githubusercontent.com/txie-93/cdvae/main/data/mp_20/{split}.csv"


@dataclass(frozen=True)
class Entry:
    material_id: str
    formula: str
    band_gap: float          # PBE, eV
    e_above_hull: float      # eV/atom
    formation_energy: float  # eV/atom
    spacegroup: int
    elements: tuple
    cif: str
    split: str


def _path(split: str) -> Path:
    return RAW / f"mp20_{split}.csv"


def download(splits=("train", "val", "test")) -> None:
    import urllib.request
    RAW.mkdir(parents=True, exist_ok=True)
    for s in splits:
        p = _path(s)
        if not p.exists():
            urllib.request.urlretrieve(MP20_URL.format(split=s), p)


@lru_cache(maxsize=None)
def load(splits=("train", "val", "test")) -> list[Entry]:
    out = []
    for s in splits:
        p = _path(s)
        if not p.exists():
            raise FileNotFoundError(f"{p} missing; run speclab.data.download()")
        with open(p) as fh:
            for r in csv.DictReader(fh):
                out.append(Entry(
                    material_id=r["material_id"], formula=r["pretty_formula"],
                    band_gap=float(r["band_gap"]), e_above_hull=float(r["e_above_hull"]),
                    formation_energy=float(r["formation_energy_per_atom"]),
                    spacegroup=int(r["spacegroup.number"]),
                    elements=tuple(sorted(ast.literal_eval(r["elements"]))), cif=r["cif"], split=s))
    return out


def structure(entry: Entry):
    from pymatgen.core import Structure
    return Structure.from_str(entry.cif, fmt="cif")
