# Data

## MP-20

Source: `https://raw.githubusercontent.com/txie-93/cdvae/main/data/mp_20/{train,val,test}.csv`
(Xie et al., CDVAE, ICLR 2022). 45,229 Materials Project entries with at most 20 atoms per unit
cell, with PBE band gap, formation energy per atom, energy above hull (MP 2021 hull) and CIF.
11,522 of them contain oxygen.

Limits that matter for this project:

- **Cell size.** Cubic Y2O3 (Ia-3, 40 atoms) and other large cells are absent. Any claim about
  "the oxides in MP" is a claim about the small-cell subset.
- **PBE gaps.** Systematically low for oxides; the spec uses a calibrated threshold, not the
  target value.
- **No dielectric data.** The Materials Project DFPT set (Petousis 2017) and JARVIS are behind
  hosts this environment cannot reach. The funnel uses a Clausius-Mossotti estimate instead
  and says so.
- **No synthesizability flag.** MP-20 does not carry the ICSD / theoretical flag.
- **Hull vintage.** The hull is MP 2021, before the GNoME additions. Some entries stable here
  would be above the post-GNoME hull.

## Why not the Materials Project API, JARVIS, Alexandria, OQMD

All four need a host outside the allowed list (api.materialsproject.org, figshare, ICAMS, oqmd.org).
The code keeps the loader behind one module so these can be swapped in on a machine that reaches them.

## Shannon polarizabilities

`speclab/dielectric.py` carries the table and its provenance note. `VERIFIED = False` until the values
are checked against Shannon 1993 Table 1.
