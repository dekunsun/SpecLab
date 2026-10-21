# SpecLab

From a customer's property spec to a deliverable material candidate set.

SpecLab is the design stage of a self-driving-lab loop. Its siblings cover the other stages:
[LiveLab 1.0](https://github.com/dekunsun/livelab) (monitoring a running experiment),
[LiveLab 2.0](https://github.com/dekunsun/livelab2) (diagnosing when an anomaly began) and
[ai4s.fyi](https://github.com/dekunsun/ai4s) (the evidence record of the field). The shared
thesis: in an AI-for-Science product the system owns the guarantees, the model explains, and
every step has an eval and an evidence grade.

**Status (2026-10-21): v0.1, one deterministic run of the funnel and one run of the XRD baselines,
both registered before running. No model has been run yet. No material has been made.**

## What it does

A hypothetical customer (an ALD / sputter tool vendor or a logic/memory fab) asks for a
next-generation high-k gate dielectric or ferroelectric memory oxide. SpecLab turns that into a
two-layer reference product profile (`specs/high_k_gate_dielectric.yaml`): device-level targets
in the customer's language (EOT, leakage, polarisation, endurance, retention) and material-level
proxies the computational funnel can screen (band gap, dielectric constant, hull distance,
composition), with the margin and the mapping stated per field.

The funnel (`speclab/funnel.py`) then applies the proxies as ordered hard constraints to 45,229
Materials Project structures (MP-20, the only structure set reachable under this environment's
network policy) and records what every stage removed and why.

| stage | survivors | removed (reason: n) |
|---|---:|---|
| all | 45,229 | |
| composition | 7,259 | no oxygen: 33,707; blacklisted element: 4,263 |
| stability | 5,489 | above hull by > 50 meV/atom: 1,770 |
| band gap | 777 | PBE gap < 3.4 eV: 4,712 |
| dielectric | 184 | Clausius-Mossotti k < 15: 526; ion not in table: 64; no oxidation state: 2; estimator divergent: 1 |

Full table and Top-30: [results/funnel/high_k_gate_dielectric.md](results/funnel/high_k_gate_dielectric.md).
The Top-20 is rare-earth tantalates (RETaO4) and the LaAlO3 family, with LaScO3, LiTaO3 and
rare-earth aluminates close behind: all classes the high-k literature has already proposed,
which is the point of a retrospective check, not a discovery.

## The retrospective test (registered before the run)

Does a spec written in proxies recover what the industry uses and reject what it rejected, for
the stated reason? [docs/registration.md](docs/registration.md) holds the predictions;
[results/funnel/retrospective.md](results/funnel/retrospective.md) the outcome.

| control | outcome |
|---|---|
| HfO2 (monoclinic and ferroelectric Pca21), ZrO2, La2O3, LaAlO3, LaLuO3 | all six survive (ranks 5 to 150 of 184) |
| TiO2, SrTiO3, Ta2O5 | removed at band gap, as the textbook says |
| Al2O3, SiO2, MgO, HfSiO4 | removed at dielectric, as the textbook says |

Three of six registered predictions held. The three that failed are logged with their
direction: the funnel is tighter than predicted (184 survivors, not 200-800), the tie-breaker
score is less distorted by the estimator's divergence than I feared, and the ion table's gaps
are smaller than I feared (8.6 % unscorable, not 10-40 %). No threshold was changed afterwards.

## The XRD phase-identification eval

Characterisation quality control is the bottleneck of an automated lab, and the interface
between this project and the diagnosis stage. `items/xrd_public.json` holds 120 closed-set
items (nine candidate structures with CIFs, one or two present) in three tiers; rules frozen in
[docs/question_rules.md](docs/question_rules.md). Baselines were registered and run before any
model:

| agent | T1 single clean | T2 single, strained | T3 two-phase |
|---|---:|---:|---:|
| random | 5 % | 10 % | 2.5 % |
| classic NNLS matcher | 100 % | 37.5 % | 15 % (Jaccard 0.40) |
| classic NNLS with strain refinement | 100 % | 65 % | 50 % (Jaccard 0.73) |
| oracle | 100 % | 100 % | 100 % |

Four of five predictions held for the plain matcher; for the refined one, one of three (it gained less on T2 than predicted). Any model result is to be read against the refined row. The
simulation's limits (no K-alpha2, no texture beyond a per-peak factor, no amorphous hump) are
stated in the rules: a good score here is necessary, not sufficient.

## What is deliberately not claimed

- The dielectric screen is a Clausius-Mossotti estimate from Shannon polarizabilities, with a
  table transcribed from memory and marked `VERIFIED = False` until checked against the paper.
  Its anchors (MgO 8.8 vs 9.8, SiO2 4.1 vs 4.5, Al2O3 9.1 vs 9-10, HfSiO4 11.2 vs 11) are
  recorded; its known divergence on perovskites (LaAlO3 119 vs 24) is cut off and flagged.
- Band offset to Si, reaction with Si, precursor availability, crystallisation temperature and
  novelty are declared in the spec as not screened in this version.
- MP-20 has no cell larger than 20 atoms and uses the 2021 hull; see [docs/data.md](docs/data.md).

## Run it

```bash
python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt scipy
./.venv/bin/python scripts/run_funnel.py        # downloads MP-20 from GitHub on first run
./.venv/bin/python scripts/retrospective.py
./.venv/bin/python scripts/make_xrd_items.py <private-seed>
./.venv/bin/python scripts/xrd_baseline.py
./.venv/bin/python -m pytest -q
```

## Layout

- `specs/` the reference product profile (YAML, two layers)
- `speclab/` data loader, spec evaluation, Clausius-Mossotti estimator, funnel, XRD items and scoring
- `scripts/` run the funnel, the retrospective controls, item generation, baselines
- `items/` the public XRD set and its answers; the held-out set stays local (sha256 recorded)
- `results/` every run's output, kept
- `docs/` [proposal](docs/speclab-proposal.md), [registration and deviation log](docs/registration.md),
  [question rules](docs/question_rules.md), [data](docs/data.md), [timeline](docs/timeline.md)
- `tests/` spec rules, estimator anchors, funnel stage accounting, item leakage, scorer

## Next

1. Register and run frontier models (Claude, Gemini, GPT) and one open-weight model on the XRD set.
2. Funnel v0.2 on JARVIS-DFT (TBmBJ gaps, DFPT dielectric) now that the network policy allows it; validate the Clausius-Mossotti table against the Petousis DFPT set.
3. MACE-MP-0 relaxation of the Top-30 as a cross-check on the hull stage.
4. Funnel v0.2: verify the polarizability table; add the Si band-offset and reaction stages.

Code and documents: MIT. Data: MP-20 (CDVAE, Xie et al.) from the Materials Project, CC BY 4.0.
