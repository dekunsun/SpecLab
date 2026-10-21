# XRD phase-identification items: rules (frozen before generation)

1. **Source pool.** Oxides from MP-20 that pass the spec's composition and stability stages
   (so every candidate is a plausible oxide, not a random metal), restricted to entries with at
   most 20 atoms per cell (all of MP-20) and a spacegroup number recorded.
2. **Closed set.** Each item lists nine candidates with their CIFs. The present phase or phases
   are among them. The truth is the set of present ids.
3. **Tiers.** T1 single clean; T2 single with strain and intensity distortion; T3 two phases.
   40 public items per tier, generated with seed 20261021. A held-out set with a different seed
   is generated locally, not committed; its sha256 is recorded in `items/README.md`.
4. **Simulation.** Cu K-alpha, 10-80 degrees, 0.05 degree grid, Gaussian peaks, polynomial
   background, Poisson plus Gaussian noise. Parameters per tier are in `speclab/xrd.py`.
5. **Leakage.** The payload an agent sees (`xrd.prompt_payload`) carries no answer field; the
   candidate order is shuffled; a test asserts both. The answer is never the first candidate
   more often than chance.
6. **Scoring.** Exact set match and Jaccard, per tier. An item with no response counts as
   coverage, never as a wrong answer.
7. **Baselines run before any model.** Random, oracle (sanity), classic NNLS matcher.
8. **What the items cannot show.** Whether an agent reads a real diffractometer's output.
   The simulation lacks instrument asymmetry, sample displacement, texture beyond a per-peak
   lognormal factor, amorphous humps and K-alpha2 splitting. A model that scores well here has
   passed a necessary test, not a sufficient one.
