# Data

Network policy during the first hours allowed GitHub and PyPI only; the author widened it to
full at about 06:20 UTC on 2026-10-21. Both phases are recorded here.

## MP-20 (funnel v0.1, XRD items)

`https://raw.githubusercontent.com/txie-93/cdvae/main/data/mp_20/{train,val,test}.csv`
(Xie et al., CDVAE, ICLR 2022): 45,229 Materials Project entries with at most 20 atoms per cell,
PBE band gap, formation energy, energy above hull (MP 2021 hull), CIF. 11,522 contain oxygen.
Limits: no cell above 20 atoms (cubic Y2O3 is absent), PBE gaps, no dielectric data, no ICSD
flag, pre-GNoME hull.

## JARVIS-DFT 3D (funnel v0.2, Clausius-Mossotti validation)

`jarvis-tools` figshare copy, 93,902 entries (`scripts`: `speclab.jarvis.fetch`). Fields used:
OptB88vdW gap (all), TBmBJ gap (21,559), OptB88 and mBJ electronic dielectric tensors (60,354 and
19,834), DFPT total dielectric constant (4,706), formation energy, ICSD ids (20,812), structure.
Limits: the `ehull` field in this release is not usable (see registration); the hull is
recomputed from formation energies per chemical system. TBmBJ coverage among stable oxides is
10.6 %, which bounds the grade-A list. DFPT values above about 100 are soft-mode divergences.

## Petousis 2017 (MP DFPT, via matminer `dielectric_constant`)

1,056 compounds; only 130 oxides pass the composition rule and only one has k >= 25, so it could
not test the screen (recorded as an underpowered run).

## MACE-MP-0b3 medium

Weights from the ACEsuit/mace-foundations GitHub release, downloaded to `data/models/`
(not tracked). CPU, float64.

## Shannon polarizabilities

`speclab/dielectric.py` carries the table and its provenance note (`VERIFIED = False`). Its
empirical check against JARVIS DFPT is in `results/dielectric/`.
