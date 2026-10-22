# Budget rules (from 2026-10-22)

Measured unit costs, Claude Opus 5.5, effort high, Batches API (half price), 16,000-token cap:

| arm | per item | basis |
| --- | ---: | --- |
| A, reading only | USD 0.12 | public run 1: 14.50 / 120 |
| B, simulate_pattern tool, round-batched | USD 0.27 | public run 1: 32.03 / 120 |
| B2, plus fit_and_residual, retired | USD 0.41 | public run 1: 49.33 / 120 |

Why the early estimates were low: 20,000 input tokens per item (numbers tokenise one per
token), 7,900 output tokens per item in arm A, and every tool round resends the whole
conversation. The dry run exposed the first; the other two were only visible after a run.

Rules for every future paid run:

1. **Pilot first.** `--pilot 5` (5 items per tier, 15 items) on any new arm, model or set. Its
   per-item cost x items x 1.2 is the estimate that goes into the registration. No full run
   without a pilot number.
2. **Hard stop in the runner.** `--budget` is checked before every round is submitted
   (tool runner) or before the single submission (arm A). The default is USD 40.
3. **One reason per dollar.** A run is submitted only when the registration names the product
   decision it informs. The held-out gate decides whether arm B is qualified (PRD FR12); a
   second model decides whether the harness result is model-specific; a tool change decides
   nothing until its harness lessons are built in.
4. **Report after every run** in this file: estimate, actual, ratio.

| run | estimate | actual | ratio |
| --- | ---: | ---: | ---: |
| arm A public | 8.5 | 14.50 | 1.7 |
| arm B public | 15-30 | 32.03 | 1.1-2.1 |
| arm B2 public | 32-51 (1.0-1.6x B) | 49.33 | inside, but the run was not worth it |

Planned, not approved:

| run | pilot needed | estimate from measured unit cost | decision it informs |
| --- | --- | ---: | --- |
| arm B, held-out, 3 runs x 60 items | no (same arm, same model) | 0.27 x 180 x 1.2 = USD 58 | FR12 qualification: is arm B the gate |
| Gemini 4 Argon, arm B, public | yes | pilot x 120 x 1.2 | whether the result is Opus-specific |
