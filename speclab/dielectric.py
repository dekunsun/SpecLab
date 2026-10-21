"""Clausius-Mossotti estimate of the static dielectric constant of an oxide from Shannon ion
polarizabilities (R. D. Shannon, J. Appl. Phys. 73, 348 (1993)).

    eps = (3 V + 8 pi a) / (3 V - 4 pi a)

with V the volume per formula unit (A^3) and a the sum of ion polarizabilities (A^3).

This is a rule-based baseline, not a prediction model. It is known to fail where the
denominator approaches zero (soft, ferroelectric or strongly anharmonic lattices) and it
ignores structure beyond the molar volume. Its role in the funnel is a cheap first screen
with a stated margin; the DFPT stage is the authority.

PROVENANCE OF THE TABLE. The values below were transcribed from memory of Shannon's Table 1
and have NOT yet been checked against the paper, which is unreachable under this project's
network policy. They are marked verified: False until that check is done. Hf4+ is not in the
transcribed set and is set equal to Zr4+ (lanthanide contraction gives the two ions nearly
identical radii); that choice is flagged separately. Anchor tests in tests/test_dielectric.py
check the estimator against experimental values for MgO, SiO2, Al2O3 and ZrO2.
"""
from __future__ import annotations
import math

VERIFIED = False

POLARIZABILITY = {  # A^3, keyed by (element, oxidation state)
    ("O", -2): 2.01,
    ("Li", 1): 1.20, ("Na", 1): 1.80, ("K", 1): 3.83, ("Rb", 1): 5.29, ("Cs", 1): 7.43, ("Ag", 1): 2.40,
    ("Mg", 2): 1.32, ("Ca", 2): 3.16, ("Sr", 2): 4.24, ("Ba", 2): 6.40, ("Zn", 2): 2.04,
    ("Mn", 2): 2.64, ("Fe", 2): 2.23, ("Co", 2): 1.65, ("Ni", 2): 1.23, ("Cu", 2): 2.11,
    ("B", 3): 0.05, ("Al", 3): 0.79, ("Ga", 3): 1.50, ("In", 3): 2.62, ("Sc", 3): 2.81,
    ("Y", 3): 3.81, ("La", 3): 6.07, ("Ce", 3): 6.15, ("Pr", 3): 5.32, ("Nd", 3): 5.01,
    ("Sm", 3): 4.74, ("Eu", 3): 4.53, ("Gd", 3): 4.37, ("Tb", 3): 4.25, ("Dy", 3): 4.07,
    ("Ho", 3): 3.97, ("Er", 3): 3.81, ("Tm", 3): 3.82, ("Yb", 3): 3.58, ("Lu", 3): 3.64,
    ("Bi", 3): 6.12, ("Cr", 3): 1.45, ("Fe", 3): 2.29,
    ("Si", 4): 0.87, ("Ge", 4): 1.63, ("Sn", 4): 2.83, ("Ti", 4): 2.93, ("Zr", 4): 3.25,
    ("Ce", 4): 3.94, ("Th", 4): 4.70,
    ("V", 5): 2.92, ("Nb", 5): 3.97, ("Ta", 5): 4.73,
    ("Mo", 6): 3.28, ("W", 6): 3.20,
}
POLARIZABILITY[("Hf", 4)] = POLARIZABILITY[("Zr", 4)]   # flagged assumption, see module docstring
ASSUMED = {("Hf", 4)}


def oxidation_states(structure) -> dict | None:
    """Guess integer oxidation states for a structure; None if no charge-balanced guess."""
    comp = structure.composition
    guesses = comp.oxi_state_guesses(max_sites=-1)
    if not guesses:
        return None
    return {el: int(round(v)) for el, v in guesses[0].items()}


def estimate(structure) -> dict:
    """Return {'k': float|None, 'reason': str, 'x': 4 pi a / 3V, 'missing': [...]}"""
    oxi = oxidation_states(structure)
    if oxi is None:
        return {"k": None, "reason": "no_oxidation_state_guess", "x": None, "missing": []}
    comp = structure.composition
    n_fu, red = comp.get_reduced_composition_and_factor()[1], comp.reduced_composition
    alpha, missing = 0.0, []
    for el, amt in red.items():
        key = (str(el), oxi[str(el)])
        if key not in POLARIZABILITY:
            missing.append(f"{key[0]}{key[1]:+d}")
            continue
        alpha += POLARIZABILITY[key] * amt
    if missing:
        return {"k": None, "reason": "no_polarizability:" + ",".join(missing), "x": None, "missing": missing}
    v_fu = structure.volume / n_fu
    x = 4 * math.pi * alpha / (3 * v_fu)
    if x >= 0.98:
        return {"k": None, "reason": "cm_divergent", "x": x, "missing": []}
    k = (1 + 2 * x) / (1 - x)
    return {"k": k, "reason": "ok", "x": x, "missing": []}
