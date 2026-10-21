# SpecLab

From a customer's property spec to a deliverable material candidate set.

SpecLab is the design stage of a self-driving-lab loop. Its siblings cover the other stages:
[LiveLab 1.0](https://github.com/dekunsun/livelab) (monitoring a running experiment),
[LiveLab 2.0](https://github.com/dekunsun/livelab2) (diagnosing when an anomaly began) and
[ai4s.fyi](https://github.com/dekunsun/ai4s) (the evidence record of the field). The shared
thesis: in an AI-for-Science product the system owns the guarantees, the model explains, and
every step has an eval and an evidence grade.

**Status (2026-10-21): v0.3. Three funnel versions, two validations, a potential cross-check, a
phonon check, a substrate stage and one eval set with baselines, all registered before running.
No language model has been run yet. No material has been made. 37 registered predictions:
21 held, 12 failed, 4 could not be read. Every failure is logged with its direction in
[docs/registration.md](docs/registration.md).**

**Deliverable:** [results/funnel/v0.3_gradeA.md](results/funnel/v0.3_gradeA.md), 20 oxides with a
TBmBJ gap, a DFPT dielectric constant, a stable phonon spectrum in MACE-MP-0 and a substrate
lattice-match column, each with its evidence stated.

## What it does

A hypothetical customer (an ALD / sputter tool vendor or a logic/memory fab) asks for a
next-generation high-k gate dielectric or ferroelectric memory oxide. SpecLab turns that into a
two-layer reference product profile (`specs/high_k_gate_dielectric.yaml`): device-level targets
in the customer's language (EOT, leakage, polarisation, endurance, retention) and material-level
proxies the computational funnel can screen (band gap, dielectric constant, hull distance,
composition), with the margin and the mapping stated per field.

The funnel applies the proxies as ordered hard constraints to a structure database, records what
every stage removed and why, and grades each survivor by the evidence behind it.

## Funnel v0.2 on JARVIS-DFT, with evidence grades

93,902 entries. A candidate is removed only on DFT-level evidence; a proxy grades it, it does not
reject it (the band-gap proxy is the one exception, because no gap at all is worse).

| stage | survivors | removed (reason: n) |
|---|---:|---|
| all | 93,902 | |
| composition | 13,825 | no oxygen: 68,708; blacklisted element: 11,369 |
| stability | 7,061 | above hull by > 50 meV/atom: 6,764 (hull recomputed from JARVIS formation energies) |
| band gap | 1,189 | below threshold on the OptB88 proxy: 4,994; on TBmBJ: 878 |
| dielectric | 1,059 | DFPT total below 21: 130 |

Grades: **A 29** (TBmBJ gap and DFPT dielectric, both verified at DFT level), B 325 (one verified),
C 705 (proxies only). The deliverable is the grade-A list,
[results/funnel/v0.2_jarvis.md](results/funnel/v0.2_jarvis.md): hafnates (SrHfO3, BaHfO3,
Sr2HfO4, Ba2HfO4), three HfO2 polymorphs including the ferroelectric Pca21 phase, tantalates
(LuTaO4, TaGaO4), rare-earth sesquioxides and NaREO2 / LiREO2 layered oxides. Five of the 29 carry
DFPT values above 100 (SrHfO3, LuTaO4, tetragonal HfO2, Na2Hf2O5): soft-mode divergences, flagged
for a phonon check rather than removed, because the rule was not registered before the run.

Registered controls ([results/funnel/retrospective_v0.2.md](results/funnel/retrospective_v0.2.md)):
monoclinic HfO2 survives at grade B (JARVIS has no DFPT value for it), Pca21 HfO2 at grade A;
rutile TiO2 and SrTiO3 leave at band gap; corundum Al2O3, rocksalt MgO and quartz SiO2 leave at
dielectric on DFPT values. Monoclinic ZrO2 leaves at band gap by 0.04 eV: its TBmBJ gap in JARVIS
is 4.21 eV against 5.8 eV experimental. That removal was declared before the run and is kept as
the cost of a threshold rule with no per-material uncertainty.

## What the validations changed

- **Clausius-Mossotti is not a screen.** v0.1 screened dielectric constant with a
  Clausius-Mossotti estimate from Shannon polarizabilities. Checked against 765 JARVIS oxides
  with DFPT values ([results/dielectric/cm_vs_dfpt.md](results/dielectric/cm_vs_dfpt.md)):
  Spearman 0.70, MARD 47 %, but recall of k >= 25 at the k_CM >= 15 screen only 0.45, and the
  misses are not soft lattices (86 % have x < 0.8). The registered rule (set the threshold for
  recall 0.9) gives k_CM >= 7, which keeps two thirds of everything. So v0.2 keeps the estimate
  as a flag and removes nothing on it. A second check on the Petousis set was underpowered
  (one oxide with k >= 25) and is recorded as such.
- **The JARVIS `ehull` field is unusable** in the 2025 release (monoclinic HfO2 reads 1.78 eV/atom
  above hull). `speclab/hull.py` recomputes the hull from JARVIS formation energies with
  pymatgen phase diagrams per chemical system; HfO2 lands at 0.000, ZrO2 at 0.003.
- **Thresholds need the method's error.** DFPT vs experiment MARD is 16 % (Petousis), TBmBJ about
  15 %: the v0.2 pass thresholds are 21 (not 25) and 4.25 eV (not 5.0), declared before the run.

## Funnel v0.1 on MP-20 (kept as run)

The first run used MP-20 (45,229 structures, GitHub-hosted, the only set reachable under the
initial network policy) with PBE gaps and the Clausius-Mossotti screen. 184 survivors; all six
positive controls survived and all seven negatives left at the textbook stage;
[results/funnel/high_k_gate_dielectric.md](results/funnel/high_k_gate_dielectric.md) and
[results/funnel/retrospective.md](results/funnel/retrospective.md). The Top-20 was rare-earth
tantalates and the LaAlO3 family, the classes the literature already names.

## v0.3: the soft-mode rule

Five grade-A entries carried DFPT values above 100. Hypothesis, registered before the run: those
are polar soft modes at a symmetric minimum, which DFPT's ionic term turns into 1/omega^2.
Finite-displacement phonons (phonopy, forces from MACE-MP-0b3, 4x4x4 mesh) found an imaginary
mode in all five (SrHfO3 at -4.9 THz, the known octahedral-tilt instability of the cubic phase)
and in none of three controls, so the rule was applied to the whole list: 9 of 29 are demoted,
four of them with ordinary-looking DFPT values between 28 and 73 (Sr2HfO4, SiBi2O5, LiSiBiO4,
TaGaO4). The registered ceiling for that second group was 2; it is logged as a failure.
[results/phonon/softmodes_all.md](results/phonon/softmodes_all.md).

## Substrate lattice match

Zur-McGill coincident-site matching of each grade-A film on Si(001), Si(111), TiN(001) and Pt(111)
below 2 % strain. At 400 A^2 every candidate matches something, as registered; the column is
informative only where the area is small (one candidate below 100 A^2 on Si(001)).
[results/substrate/zsl.md](results/substrate/zsl.md). Polycrystalline ALD films do not need a
match; the column is a plausibility note for epitaxial routes.

## MACE-MP-0 cross-check

The 29 grade-A structures and the six v0.1 positives relaxed with mace-mp-0b3-medium (CPU):
all 35 within 3 % volume (max 2.5 %) and 30 meV/atom (max 3.0). The potential agrees with both
DFT sources on every geometry; it cannot see the soft modes behind the divergent DFPT values.
[results/mace/relax.md](results/mace/relax.md).

## The XRD phase-identification eval

Characterisation quality control is the bottleneck of an automated lab, and the interface
between this project and the diagnosis stage. `items/xrd_public.json` holds 120 closed-set items
(nine candidate structures with CIFs, one or two present) in three tiers; rules frozen in
[docs/question_rules.md](docs/question_rules.md). Baselines registered and run before any model:

| agent | T1 single clean | T2 single, strained | T3 two-phase |
|---|---:|---:|---:|
| random | 5 % | 10 % | 2.5 % |
| classic NNLS matcher | 100 % | 37.5 % | 15 % (Jaccard 0.40) |
| classic NNLS with strain refinement | 100 % | 65 % | 50 % (Jaccard 0.73) |
| oracle | 100 % | 100 % | 100 % |

Any model result is to be read against the refined row. A held-out set of 60 items exists
locally; its sha256 is in `items/README.md`.

## What is deliberately not claimed

- No material was made; no band offset to Si, reaction with Si, precursor or growth-window
  stage has run; all are declared in the spec as not screened.
- The grade-A list is bounded by TBmBJ coverage (10.6 % of stable oxides), not by physics.
- The Shannon table is transcribed from memory and marked unverified; its empirical check is above.
- The XRD simulation lacks K-alpha2, texture beyond a per-peak factor and amorphous humps.

## Run it

```bash
python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt
./.venv/bin/python scripts/run_funnel.py          # v0.1, MP-20 (downloads from GitHub)
./.venv/bin/python scripts/retrospective.py
./.venv/bin/python scripts/run_funnel2.py         # v0.2, JARVIS (downloads via jarvis-tools)
./.venv/bin/python scripts/retrospective2.py
./.venv/bin/python scripts/validate_cm.py
./.venv/bin/python scripts/make_xrd_items.py <private-seed>
./.venv/bin/python scripts/xrd_baseline.py
./.venv/bin/python scripts/mace_check.py          # needs torch + mace-torch and the model file in data/models/
./.venv/bin/python -m pytest -q
```

## Layout

- `specs/` the reference product profile (YAML, two layers, versioned)
- `speclab/` loaders (MP-20, JARVIS), spec rules, hull, Clausius-Mossotti estimator, funnels v0.1 and v0.2, XRD items and scoring
- `scripts/` every run, one script each
- `items/` the public XRD set and answers; the held-out set stays local
- `results/` every run's output, kept, including the invalid first v0.2 run
- `docs/` [PRD](docs/prd.md) ([中文](docs/prd.zh.md)), [proposal](docs/speclab-proposal.md), [registration and deviation log](docs/registration.md),
  [question rules](docs/question_rules.md), [data](docs/data.md), [timeline](docs/timeline.md)
- `tests/` spec rules, estimator anchors, funnel stage accounting, hull, item leakage, scorer

## Next

1. Register and run frontier models (Claude, Gemini, GPT) and one open-weight model on the XRD set (needs API keys).
2. The Si band-offset and reaction-with-Si stages; precursor availability from the literature.
3. Verify the Shannon table against the paper, or retire the estimator.
4. Run the phonon check on the grade-B list, whose DFPT values (where present) carry the same risk.

Code and documents: MIT. Data: MP-20 (CDVAE, Xie et al.) from the Materials Project, CC BY 4.0;
JARVIS-DFT (NIST), CC BY 4.0; Petousis 2017 via matminer.
