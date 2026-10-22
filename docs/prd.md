# SpecLab PRD

As of 2026-10-21 · Dekun Sun · [中文版](prd.zh.md) · See also: [proposal](speclab-proposal.md) · [registration and deviation log](registration.md) · [v0.3 deliverable](../results/funnel/v0.3_gradeA.md)

## One page

| Item | Content |
| --- | --- |
| Product | Turns an industrial customer's material property spec into a deliverable: a candidate set, an evidence grade per candidate, and a validation plan |
| Customer | Process-integration teams at semiconductor tool vendors or fabs; computational and synthesis teams at automated materials labs |
| Job to be done | "I give device-level targets; tell me which materials to try first, on what evidence, what is still unverified, and how to schedule the experiments" |
| Most dangerous failure | Delivering a computed number as a verified property: a threshold with no method error, an estimator used as a screen, a DFT value computed at an unstable structure |
| Core design | The system removes a candidate only on DFT-level evidence; proxies grade, they do not reject; every threshold carries its method's error; every candidate carries an evidence grade and a list of what is unverified; predictions are registered before every run |
| Measures | 100 % recall of known positives; known negatives removed at the textbook stage; grade-A yield and evidence coverage; cost and cycle time per candidate; an XRD quality-control gate |
| Status | v0.3: 93,902 JARVIS entries to 20 grade-A candidates; 21 of 37 registered predictions held; no language model run yet; no material made |

## Problem and users

Public accounts of AI materials discovery count new materials. Industrial customers ask something else: for my spec, which few should I try first, how far does the evidence go, and what is missing. That gap is the product.

| User | Situation | What v1 gives them |
| --- | --- | --- |
| **Process-integration engineer** (primary): selecting the next high-k gate dielectric or ferroelectric memory oxide | Literature and databases offer hundreds of "promising" compounds with no common evidence standard, and no way to tell which numbers were computed at an unstable structure | A candidate set ranked by evidence grade, each with band gap, dielectric constant, phonon stability, ICSD flag, substrate match and an explicit list of unverified items |
| **Computational scientist at an automated lab** (secondary): feeding candidates into a synthesis-characterisation loop | Needs a reproducible, auditable screen, not a one-off script | A staged funnel with removal counts and reasons per stage; registrations; a deviation log; a reusable eval set |
| **Program / operations lead**: deciding where experimental capacity goes | Throughput is limited; needs the evidence cost and next-experiment cost per candidate | Stage gates, cost per candidate, cycle-time estimates, an XRD QC gate |

## Two-layer spec: customer language and model language

| Layer | Content | Owner |
| --- | --- | --- |
| Device-level targets | EOT, gate leakage, remanent polarisation, endurance, retention, thermal budget | The customer; recorded, not computed |
| Material-level proxies | Band gap, dielectric constant, hull distance, composition rules, band offset to Si, depositability | The product; each with its mapping, tolerance and source |

The product states that proxies are not device metrics: the SiOx interfacial layer contributes 0.4 to 0.7 nm of EOT, so the material-level k target carries margin; endurance, retention and wake-up cannot be computed and are left to experiment.

## Design principles (from the v0.1 to v0.3 findings)

| Finding (registered, run) | Data | Design |
| --- | --- | --- |
| An estimator is not a screen | Clausius-Mossotti recall 0.45 on 765 oxides with DFPT values; the registered rule (threshold at recall 0.9) keeps 67 % of candidates | Removal only on DFT-level evidence; estimates are flags (FR2) |
| Database fields are not trusted by default | JARVIS `ehull` puts monoclinic HfO2 at 1.78 eV/atom above hull | Hull recomputed from formation energies; each source lists its unusable fields (FR5) |
| Thresholds carry the method's error | DFPT vs experiment MARD 16 %, TBmBJ about 15 %; ZrO2's JARVIS TBmBJ gap is 4.21 eV against 5.8 | Pass line = target × (1 − method error), declared before the run; a known material lost to it is recorded as the cost (FR3) |
| A DFT value may sit on an unstable structure | All 5 grade-A entries with DFPT k > 100 have imaginary modes; 4 more with k between 28 and 73 do too | A phonon check is a necessary condition for grade A; unstable entries are demoted with the flag "DFPT at a dynamically unstable structure" (FR4) |
| Evidence coverage bounds yield | Only 10.6 % of stable oxides carry a TBmBJ gap | Every deliverable reports coverage, not only counts (FR7) |
| Predictions first | 37 predictions: 21 held, 12 failed, 4 unreadable; every failure logged with its direction | Every threshold change and new stage is registered before it runs (FR9) |

## Functional requirements

| ID | Requirement | Status |
| --- | --- | --- |
| FR1 | Two-layer spec file (YAML); each proxy carries target, tolerance, source and mapping | v0.2 |
| FR2 | Staged funnel; removal only on DFT-level evidence; proxies set the grade | v0.2 |
| FR3 | Every threshold carries its method error; changes are registered first | v0.2 |
| FR4 | Phonon stability (MLIP finite displacement) is required for grade A | v0.3 |
| FR5 | Loaders for several sources; usable and unusable fields listed per source; hull recomputable | MP-20, JARVIS, Petousis |
| FR6 | Each candidate carries values with sources, grade, ICSD flag, substrate match, unverified list | v0.3 |
| FR7 | Each deliverable reports stage counts, evidence coverage, A/B/C distribution | done |
| FR8 | Retrospective controls: known positives recovered, known negatives removed at the textbook stage | done (v0.1, v0.2) |
| FR9 | Registration and deviation log; every run kept, invalid runs included | done |
| FR10 | XRD phase-ID eval: public items, local held-out set, baselines; used as the characterisation QC gate and the model qualification test | items and baselines done; no model run |
| FR11 | Band offset to Si, reaction with Si, precursor availability, crystallisation temperature | not built; declared in the spec |
| FR12 | Model qualification: one run on the XRD held-out set within 10 points of the public result on every tier and above the refined classic baseline; two more runs only if a tier falls short (amended 2026-10-22, see registration) | pending |

## Measures and targets

| Measure | Definition | Target | v0.3 actual |
| --- | --- | --- | --- |
| Positive recall | Share of known industrial materials passing the spec | 100 %, or a registered explanation per miss | 6/6 (v0.1); ZrO2 lost to the TBmBJ error in v0.2, declared beforehand |
| Negative stage accuracy | Share of known negatives removed at the textbook stage | 100 % | 7/7 (v0.1); 6/6 (v0.2) |
| Grade-A yield | Candidates with DFT-level evidence on both key proxies and a stable phonon spectrum | 10 to 50 | 20 |
| Evidence coverage | Share of stable oxides with a TBmBJ gap / a DFPT dielectric constant | reported, no target | 10.6 % / about 1.5 % |
| Unstable-structure detection | Share of grade-A entries found phonon-unstable | reported | 9/29 |
| Compute cost | Wall time of a full run | under one hour on one CPU machine | funnel 75 s; phonons for 29 about 10 min; MACE relax for 35 about 5 min |
| XRD QC gate | Accuracy on single clean / strained single / two-phase | above the strain-refined classic baseline: 100 % / 65 % / 50 % | baselines measured |

North star: every number in the customer's candidate set can answer "how far does the evidence go".

## Model qualification (FR12)

Before any language model handles literature extraction, synthesis routes or experiment plans, it runs once on the local XRD held-out set (60 items) and must land within 10 points of its public-set result on every tier and match or beat the strain-refined classic baseline; two more runs follow only if a tier falls short; a non-answer counts as coverage, not as an error. Re-tested on every model update. LiveLab 1.0's conclusion carries over: when the evidence is insufficient, the system says "cannot verify"; the model does not decide.

## Operations model

| Item | Content |
| --- | --- |
| Stage gates | Composition, stability, band gap, dielectric, phonon, substrate, then (to build) band offset / reaction / precursor; each gate logs removals and reasons |
| Cycle time | Spec freeze to candidate dossier: under one hour on one CPU machine today |
| Experimental assumption | At a few hundred samples a day, combinatorial deposition and XRD screening of 20 grade-A candidates takes one to two days; the bottleneck is phase-ID QC, not deposition |
| Data pipeline | Every run written to results/, invalid runs included; items and answers separated; the held-out set was meant to be stored as a hash only and was committed by mistake (corrected 2026-10-22; see registration) |
| Cost | Compute near zero; model evals billed per token (proposal appendix) |

## Non-goals

- No claim of a new material; this version handles structures already in databases.
- Not a replacement for DFT or experiment; the product organises evidence, exposes gaps and sets priority.
- No device-level prediction.

## Risks and open questions

| Risk | Response |
| --- | --- |
| Shannon polarizability table unverified | Estimator already demoted to a flag; keep or retire after checking |
| Low TBmBJ coverage bounds the grade-A list by data, not physics | Next version fills gaps with an MLIP or HSE subset; coverage reported |
| Substrate match search too permissive | Reported only where the area is small; consider a tighter area cap |
| Threshold rule blind to per-material uncertainty (the ZrO2 case) | v0.4 candidate rule, to be registered |
| Model qualification not yet run | Waits on API keys; runs under the registered protocol |

## Roadmap

| Version | Content |
| --- | --- |
| v0.4 | XRD qualification of frontier and open-weight models; phonon check extended to grade B |
| v0.5 | Band offset and reaction-with-Si stages; precursor extraction from literature with its own eval |
| v1.0 | One partner lab deposits and measures one or two candidates, adding the "tested" evidence level |
