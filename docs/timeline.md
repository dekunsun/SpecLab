# Timeline (append-only, UTC)

Note 2026-10-21 06:45 UTC: clock times in the entries below this note and in the registration
headers up to this point were estimated while working and run up to 80 minutes fast; `date -u`
read 06:44 when the v0.2 retrospective finished. Order is correct. From here on times come from the clock.

- 2026-10-21 06:24 Repository renamed to SpecLab; proposal doc carried over from the csp repo.
- 2026-10-21 06:27 Network policy found to allow GitHub and PyPI only; figshare, Materials Project API, Zenodo, Hugging Face blocked. Data source set to MP-20 (GitHub-hosted).
- 2026-10-21 06:40 Clausius-Mossotti estimator checked on 13 anchors; divergence cut-off and score cap fixed; registration written.
- 2026-10-21 06:50 Funnel v0.1 and retrospective run; 3 of 6 predictions held; deviations logged.
- 2026-10-21 07:00 XRD items generated (120 public, 60 held-out local); baselines run; 4 of 5 predictions held.
- 2026-10-21 07:15 Strain-refined classic baseline registered and run; 1 of 3 predictions held.
- 2026-10-21 07:20 Network policy widened to full by the author; JARVIS dft_3d, Petousis dielectric set and MACE weights now reachable. Funnel v0.2 planned.
- 2026-10-21 ~07:50 UTC JARVIS ehull field found unusable; hull recomputed from formation energies; v0.2 registration amended (tolerances on DFPT k and TBmBJ gap) before the valid run.
- 2026-10-21 ~08:05 UTC Funnel v0.2 valid run (29 grade A); CM validated against JARVIS DFPT (recall 0.45 at the screen: CM demoted to a flag); Petousis validation underpowered; MACE cross-check registered and started.
- 2026-10-21 06:48 UTC MACE cross-check done, all 35 pass. Model file untracked (a 76 MB blob remains in one earlier commit; rewriting history is the author's call). No model API keys in this environment: the frontier-model XRD runs wait for the author.
- 2026-10-21 07:05-07:20 UTC Substrate ZSL stage (both predictions held); soft-mode check on divergent entries (all three held); v0.3 rule applied to all grade A: 9 demoted, 20 remain.
- 2026-10-21 (after v0.3) Opus 5.5 XRD registration written (P38-P47), prompts frozen, runner and backend written; no model call made (no key).
- 2026-10-21 20:25 UTC Arm A (Opus 5.5, reading only, batch) on the public set: T1 94.6 %, T2 89.2 %, T3 33.3 % exact; 19 silences, all max_tokens stops; USD 14.50.
