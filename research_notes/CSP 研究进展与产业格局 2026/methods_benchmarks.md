# CSP methods and benchmarks, state of the art 2025-2026 (inorganic + molecular)

Notes compiled 2026-10-22. Sources marked "preprint" are arXiv or ChemRxiv and not peer-reviewed. "Vendor" marks a company's own claim. Matbench Discovery numbers were parsed directly from the official GitHub repo (janosh/matbench-discovery, last commit 2026-10-19), because the live site could not be fetched from this environment. Citation counts come from Semantic Scholar (queried 2026-10-22). Taxonomy used throughout:
- (A) Classical global search: USPEX, CALYPSO, AIRSS, XtalOpt, GA/PSO/basin or minima hopping, and molecular CSP codes (GRACE, CrystalPredictor, GLEE, Genarris, UPACK).
- (B) MLIP-accelerated search: classical search with a universal or fine-tuned MLIP as the energy model.
- (C) Generative models: diffusion, flow, autoregressive and masked models.
- (D) LLM-based approaches.

## Q1. Which benchmarks are used in 2026 and what are the leading numbers?

### Takeaway
No single benchmark measures CSP well, and each one has a different leader.
- **Matbench Discovery** (MLIP stability pre-screening) is saturated near F1 ≈ 0.93. EquiformerV3+DeNS-OAM leads on F1 (0.931, April 2026) and Prophet-OAME-MBD leads on the combined score (vendor model, Sept 2026).
- **MP-20 / MPTS-52** (composition-to-structure match rate) are led by 2026 preprints. MaskGXT reports 73.8% on MP-20 and 36.8% on MPTS-52 (one-to-one protocol).
- **CSPBench-style independent tests** find that template retrieval (TCSPv3) still beats all 12 generative models tested.
- **LeMat-GenBench** (de novo generation scored against ~5M known structures) shows strict SUN rates of only 0-1%. MatterGen leads metastable-SUN at 15.0%.
- **7th CCDC blind test** (molecular, published 2024) is still the reference molecular benchmark. No 8th blind test announcement was found.

### Cited Findings
**Matbench Discovery (inorganic stability pre-screen with MLIPs; WBM test set, 257k structures)**
- The framework paper was published in Nature Machine Intelligence (June 2025). The original arXiv 2308.14920 reported universal interatomic potentials "achieving F1 scores of 0.57-0.82 and discovery acceleration factors of up to 6x" and warned that "accurate regressors can yield high false-positive rates near the decision boundary at 0 eV/atom above the convex hull." — [arXiv 2308.14920](https://arxiv.org/abs/2308.14920); [Riebesell et al., Nat. Mach. Intell. 2025 (PDF)](https://perssongroup.lbl.gov/papers/Riebesell_et_al-2025-Nature_Machine_Intelligence.pdf)
- The current leaderboard snapshot is below. F1 is on the "unique prototypes" subset, with full-test-set F1 in parentheses. Values were parsed from the per-model YAML files in [github.com/janosh/matbench-discovery/tree/main/models](https://github.com/janosh/matbench-discovery/tree/main/models); the live site is [matbench-discovery.materialsproject.org/models](https://matbench-discovery.materialsproject.org/models).

| Model (organisation) | F1 unique (full) | κ_SRME (phonons, lower is better) | RMSD (Å) | Params | Added | Paper |
|---|---|---|---|---|---|---|
| EquiformerV3+DeNS-OAM (MIT / Mirror Physics) | **0.931** (0.912) | 0.118 | 0.060 | 30.3M | 2026-04-07 | arXiv 2604.09130 (preprint) |
| TECE-OAM-RRA-1.0 | 0.929 (0.910) | 0.093 | 0.058 | 222M | 2026-07-05 | arXiv 2607.10664 (preprint) |
| EquFlashV2 | 0.929 (0.910) | 0.094 | 0.058 | 44.9M | 2026-06-11 | ICML 2025 (PMLR v267) |
| TACE-OAM-RRA-Preview | 0.928 (0.909) | 0.101 | 0.058 | 214M | 2026-06-27 | arXiv 2607.10664 |
| Prophet-OAME-MBD (Kairos Materials, **vendor**) | 0.928 (0.910) | **0.065** | 0.059 | 62.3M | 2026-09-13 | company PDF, not peer-reviewed |
| GRACE-3L-OAM-L | 0.925 (0.905) | 0.121 | 0.058 | 42.1M | 2026-07-02 | npj Comput. Mater. 2026 |
| eSEN-30M-OAM (Meta) | 0.925 (0.902) | 0.170 | 0.061 | 30.2M | 2025-03-17 | arXiv 2502.12147 |
| PET-OAM-XL | 0.924 (0.904) | 0.119 | 0.060 | 730M | 2026-01-10 | Nat. Commun. 2025 |
| MatRIS-10M-OAM | 0.921 (0.903) | 0.218 | 0.060 | 10.4M | 2025-10-29 | arXiv 2603.02002 |
| eqV2 M (Meta) | 0.917 (0.896) | 1.771 | 0.069 | 86.6M | 2024-10-18 | arXiv 2410.12771 |
| SevenNet-Omni-i12 (SNU) | 0.906 (0.887) | 0.192 | 0.062 | 54.9M | 2026-01-12 | arXiv 2510.11241 |
| Nequip-OAM-XL | 0.906 (0.885) | 0.125 | 0.063 | 32.1M | 2025-11-30 | arXiv 2504.16068 |
| ORB v3 (Orbital Materials) | 0.905 (0.887) | 0.210 | 0.075 | 25.5M | 2025-04-05 | arXiv 2504.06231 |
| MatterSim v1 5M (Microsoft) | 0.862 (0.838) | 0.575 | 0.073 | 4.5M | 2024-12-16 | arXiv 2405.04967 |
| MACE-MPA-0 | 0.852 | 0.412 | 0.073 | 9.1M | — | — |
| NequIP-GNoME (DeepMind) | 0.829 (0.810) | n/a | n/a | 16.2M | 2024-02-03 | Nature 2023 |
| SevenNet-0 / MACE-MP-0 / CHGNet / M3GNet | 0.724 / 0.669 / 0.613 / 0.569 | | | | 2022-2024 | |

- On the combined performance score (CPS), Prophet-OAME-MBD ranks #1 (CPS 0.912) and EquiformerV3+DeNS-OAM #4 (CPS 0.902). — [Matbench Discovery /models page (search snippet)](https://matbench-discovery.materialsproject.org/models)
- Kairos describes Prophet as "pretrained on OMat24 and ELEMENTA … aligned on MPtrj and sAlex", and says "structures and trajectories in ELEMENTA overlapping with the WBM test set were removed." This is a vendor self-description. — [repo readme for Prophet](https://github.com/janosh/matbench-discovery/tree/main/models/prophet)
- **UMA (Meta FAIR).** The UMA paper claims "UMA-M achieves the highest F1 score to date" on Matbench Discovery (F1 0.930 per secondary summaries). It adds that "further scaling of model sizes is unlikely to result in better performance on the MBD benchmark." UMA-M has 1.4B total and ~50M active parameters (mixture of linear experts). It was trained on ~500M structures (OMat24, OMol25, OC20, ODAC25, OMC25). UMA has no entry in the official Matbench Discovery repo as of 2026-10-19, so the number is self-reported. — [arXiv 2506.23971 (UMA, NeurIPS 2025)](https://arxiv.org/abs/2506.23971); [summary](https://www.themoonlight.io/en/review/uma-a-family-of-universal-models-for-atoms)

**MP-20 and MPTS-52 (composition-conditioned CSP; StructureMatcher match rate, MR)**
- MaskGXT (arXiv 2606.22866, June 2026, preprint) reports one-to-one MR as unfiltered / validity-filtered values:

| Model | MP-20 MR (%) | MPTS-52 MR (%) |
|---|---|---|
| MaskGXT | **73.79 / 67.06** (RMSE 0.033) | **36.75 / 33.34** (RMSE 0.100) |
| OMatG | 69.83 / 63.75 | 27.38 / 25.15 |
| MCFlow | 69.23 / 63.14 | 28.77 / 26.46 |
| Crystalite, reproduced | 69.64 / 63.46 | 27.26 / 24.98 |
| Crystalite, as self-reported (filtered) | 66.05 | 31.49 |
| FlowMM | 66.22 / 59.98 | 22.29 / 20.28 |
| DiffCSP | 57.82 / 52.51 | 15.79 / 14.29 |

  — [arXiv 2606.22866](https://arxiv.org/abs/2606.22866)
- DAO-G (Siamese foundation models) reports MP-20 74.17% and MPTS-52 42.01% under a "best of 1-shot" protocol. That protocol is not comparable to the one-to-one table above. Published in Nature Communications 2026. — [Nat. Commun.](https://www.nature.com/articles/s41467-026-72362-3); [arXiv 2503.10471](https://arxiv.org/abs/2503.10471)
- Benchmark hygiene: MP-20 and perov-5 contain many polymorphs of the same composition spread across random splits, and carbon-24 is only ~40% unique structures. Martirossyan et al. propose polymorph-grouped splits and the METRe and cRMSE metrics, which are now used (e.g. by MaskGXT, 79.06% METRe vs 70.87% for the best baseline). — [arXiv 2509.12178 "All that structure matches does not glitter" (NeurIPS 2025)](https://arxiv.org/abs/2509.12178)

**CSPBench and its successors (180 MP structures; template, de novo, ML and DFT methods)**
- CSPBench (2024) evaluated 13 algorithms. Template methods led: TCSP 57.8% and CSPML 45.6% space-group match (preprint). The journal version gives CSPML 45.0% and TCSP 41.1% StructureMatcher success. De novo ParetoCSP and AlphaCrystal-II reached only ~12-13%. — [arXiv 2407.00733](https://arxiv.org/abs/2407.00733); [Adv. Intell. Discov.](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aidi.70162)
- PNcsp+ (J. Chem. Theory Comput. 2026) self-reports top-5 accuracy of 86.1% (space group) and 85.0% (structure match), vs TCSP 2.0 at 75.0% structure match. — [JCTC](https://pubs.acs.org/jctcce/article/22/7/3761/5149869/PNcsp-A-Periodic-Number-Based-Crystal-Structure)
- The 2026 independent generative-vs-template study on T180 is summarised under Q3.

**LeMat-GenBench (de novo generation; Dec 2025; NeurIPS 2025 workshop / arXiv 2512.04562)**
- 12 models were benchmarked against LeMat-Bulk (~5M structures) with an MLIP ensemble:

| Model | Novel % | Stable % (on hull) | SUN % | Metastable % | MSUN % |
|---|---|---|---|---|---|
| MatterGen | 70.5 | 2.0 | 0.2 | 33.4 | **15.0** |
| PLaID++ | 24.2 | 12.4 | 1.0 | 60.7 | 7.6 |
| WyFormer-DFT | — | 3.7 | 0.4 | 24.8 | 7.8 |
| DiffCSP | — | 2.3 | 0.1 | 29.8 | 8.5 |
| DiffCSP++ | — | 1.0 | 0.2 | 26.4 | 5.0 |
| CrystalFormer | — | 1.4 | 0.0 | 28.8 | 3.1 |
| SymmCD | — | 1.4 | 0.1 | 18.6 | 2.4 |
| WyFormer | — | 0.5 | 0.1 | 15.7 | 1.9 |
| ADiT | — | 0.4 | 0.0 | 36.5 | 1.0 |
| LLaMat2-CIF | — | 0.7 | 0.1 | 34.7 | 2.1 |
| LLaMat3-CIF | — | — | — | — | 0.2 |
| Crystal-GFN | — | — | 0.0 | — | 0.0 |

- The authors conclude: "an increase in stability leads to a decrease in novelty and diversity on average, with no model excelling across all dimensions." The live leaderboard is on Hugging Face and reportedly has 15+ models; it was not fetched. — [arXiv 2512.04562](https://arxiv.org/abs/2512.04562); [HF leaderboard](https://lematerial-lemat-genbench.hf.space); [GitHub](https://github.com/LeMaterial/lemat-genbench)
- ANCHOR (Sept 2026, preprint) claims that under "MatterGen's evaluation pipeline" it raises the state-of-the-art MSUN from 29.2% to 41.3%, and to 47.1% after distillation into Crystalite-CSP. It also reports SUN rising from 1.1% to 22.1% when a GRPO composition policy is placed over a frozen CSP model. These numbers are not on the LeMat-GenBench protocol, and the authors caution that "its on-hull rate depends on that potential." — [arXiv 2609.33407](https://arxiv.org/abs/2609.33407)
- Orbitol (Oct 2026, preprint, built on Crystalite) reports that 13.8% of attempts on MP-20 gave S/M-S.U.N. structures that kept the requested space group, vs 10.8% for SGFM. — [arXiv 2610.30086](https://arxiv.org/abs/2610.30086)

**AtomBench (JARVIS / NIST; arXiv 2510.16165, Oct 2025)**
- Reconstruction benchmark on superconductor datasets (JARVIS Supercon-3D, Alexandria DS-A/B). "MatterGen achieves the best atomic-coordinate reconstruction, followed by AtomGPT, while CDVAE reconstructs lattices most accurately, and FlowMM is the least accurate but fastest." Conditioning on T_c "does not consistently improve fidelity." — [arXiv 2510.16165](https://arxiv.org/abs/2510.16165); [GitHub atomgptlab/atombench](https://github.com/atomgptlab/atombench)

**Molecular CSP benchmarks**
- The 7th CCDC blind test (Acta Cryst. B80, Dec 2024; details under Q2) is the community reference. ML-CSP papers now reuse its targets and the CSD:
  - UMA evaluates "lattice energies, rank, and match structures" on the 7th blind test, with lattice-energy error "≤3 kJ/mol" — [arXiv 2506.23971](https://arxiv.org/abs/2506.23971)
  - CSP-MACE-Å uses a 28-compound set collated from all seven blind tests — [arXiv 2605.28905](https://arxiv.org/abs/2605.28905)
  - CG-OMatG validates on "the CSP blind test benchmark" with COMPACK — [arXiv 2609.39773](https://arxiv.org/abs/2609.39773)
  - Clari introduces a "CSD Teaching Subset" test split — [arXiv 2606.03199](https://arxiv.org/abs/2606.03199)
- An earlier CCDC news item: [CCDC blind test news](https://www.ccdc.cam.ac.uk/discover/news/post-43-2/)

### Inferences
- Matbench Discovery is saturated: the top 9 models span F1 0.921-0.931. Differentiation has moved to κ_SRME (phonons), RMSD and CPS. F1 gains no longer translate obviously into better CSP.
- MP-20 match rates (~65-74% one-to-one) mostly measure interpolation within the Materials Project distribution. MPTS-52 (≤52 atoms, chronological split) is far harder (best ~33-37%) and is a better proxy for real CSP on larger cells.
- Protocols diverge in candidate count (1 vs 20), validity filtering and splits. Cross-paper "SOTA" claims on MP-20 are often not comparable.

### Gaps
- Could not load the live Matbench Discovery site or the LeMat-GenBench Hugging Face leaderboard. CPS ranks come from a search snippet. The current LeMat-GenBench leader (post-Dec 2025 additions, e.g. Crystalite or CrystaLLM-π) is unverified.
- No 2025-2026 announcement of an 8th CCDC blind test was found. Status unknown.
- Could not verify UMA-M's F1 = 0.930 against an official leaderboard entry.

## Q2. What did the 7th CCDC blind test conclude, who did best, what remains unsolved?

### Takeaway
The 7th CCDC blind test (run ~2020-2022, published Oct/Dec 2024 in Acta Cryst. B80) was the largest so far, with 28 groups. Two commercial groups did best:
- **Group 20, Avant-garde Materials Simulation** (Neumann; GRACE with a tailor-made force field plus DFT-D), generated correct structures for all targets.
- **Group 10, XtalPi** (XtalCSP; "AI-enhanced self-adaptive Monte Carlo"), got all except target XXIX.

Periodic DFT-D with free-energy corrections (Groups 3, 10, 20) ranked best. Still unsolved:
- over-prediction
- the definition of a "match"
- disorder
- Z'>1
- ~1-2 kJ/mol polymorph energy differences
- the value of finite-temperature corrections, which helped only sometimes
- cost

ML potentials (system-specific AIMNet2) showed promise. Since then, MLIP-only pipelines (FastCSP/UMA, CSP-MACE-Å, Lavo-NN) have been benchmarked on blind-test targets.

### Cited Findings
- **Targets (seven):** a Si/I-containing molecule, a Cu coordination complex, a near-rigid molecule, a cocrystal, a polymorphic small agrochemical (XXXI), a highly flexible polymorphic drug candidate and a polymorphic morpholine salt (XXXIII). "Many CSP methods performed well for the small but flexible agrochemical … while few groups were successful for the systems of higher complexity." Two groups "blindly predicted the existence of disorder for the first time." — [Hunnisett et al., Acta Cryst. B80, 517-547 (2024), structure generation](https://journals.iucr.org/b/issues/2024/06/00/aw5093/) ([OSTI full text](https://www.osti.gov/pages/servlets/purl/3675988))
- **Scale:** "150 researchers from 28 unique groups spanning 14 countries," plus 18 experimentalists. "Machine learning approaches becoming more prominent, and wider adoption of quantum chemical calculations earlier in the CSP workflow." — [OSTI PDF](https://www.osti.gov/pages/servlets/purl/3675988)
- **Winners:** "Group 20 generated correct structures for all target compounds, and Group 10 generated correct structures for all except target XXIX." The authors credit success to "highly reliable quantum chemical calculations, cloud computing, machine learning techniques, tailor-made force fields, careful accounting of thermal effects, and efficient conformational sampling algorithms." Accurate CSP "favour[s] commercial CSP providers or collaborations between academia and industry over purely academic researchers." — [OSTI PDF](https://www.osti.gov/pages/servlets/purl/3675988)
- **Group identities** (participants table, same paper):
  - Group 20: Neumann, Anelli, Woollam, Abraham, Dietrich, Firaha … Tkatchenko, van de Streek. "Monte Carlo parallel tempering, tailor-made force field," GRACE (Avant-garde Materials Simulation).
  - Group 10: Jin, Yang, L. Tan, Chang, Sun … Greenwell, Bellucci, Sekharan. "AI-enhanced Self-adaptive Monte Carlo method," XtalCSP (XtalPi).
  - Classical inorganic codes also took part: USPEX (Oganov, Group 22; Johnson/Otero-de-la-Roza, Group 11), AIRSS with a Δ-learning potential at finite temperature (Pickard/Cheng/Brandenburg, Group 23), and LASP SSW+NN (Z.-P. Liu, Group 25).
  - Genarris+AIMNet2 (Marom/Isayev, Group 16) took part.
  - Source: [OSTI PDF](https://www.osti.gov/pages/servlets/purl/3675988)
- Only one target was missed by every group: the Z'=2 polymorph of the drug candidate. "All of the target systems were predicted, apart from a single Z′ = 2 polymorph." — [CCDC blind test page](https://www.ccdc.cam.ac.uk/community/ccdc-for-the-community/partnerships-and-initiatives/csp-blind-test/)
- **Open problems (generation paper):**
  - "Overlap between structure sets generated by most CSP methods is still strikingly small."
  - "One prominent issue that still remains is over-prediction."
  - There is no standardized practice for deciding when two crystal structures are the same, which "likely led to lower success rates for targets XXVII, XXIX … and XXX."
  - Disorder needs "molecular dynamics or symmetry-adapted ensembles."
  - "The use of enormous computational resources … ethical considerations and a focus on … more computationally efficient algorithms should shape any future blind test."
  - Source: [OSTI PDF](https://www.osti.gov/pages/servlets/purl/3675988)
- **Ranking paper:**
  - 22 groups ranked standardized structure sets. "Periodic DFT-D methods overall agreed with experimental data within expected error margins, while one machine learned model, applying system-specific AIMnet potentials, agreed with experiment in many cases."
  - For XXXII, periodic DFT methods agreed that experimental forms lie ">4 kJ/mol" above the global minimum, "suggesting a more stable polymorph is likely not yet observed."
  - Free energies at ambient temperature improved predictions "only in some cases (XXVII and XXXI)."
  - Source: [Hunnisett et al., Acta Cryst. B80, 548-574 (2024), structure ranking (OSTI)](https://www.osti.gov/pages/servlets/purl/3675822)
- **Ranking winners and hardest case:** Groups 3 (Boese/Graz), 10 (XtalPi) and 20 (AMS) gave "results in excellent agreement with experimental data" for all targets except XXXII, and all three used free energies. Groups 2, 5, 9 and 22 were also in line with experiment within error. The hardest case was XXXI Forms A vs B (B more stable), "consistently calculated to have 1-2 kJ/mol difference." The ranking exercise's small structure lists "did not provide an incentive to use recently developed more efficient methods (such as those based on machine learning)." — [OSTI PDF (ranking)](https://www.osti.gov/pages/servlets/purl/3675822)
- **Post-blind-test industrial claims (molecular):**
  - **Schrödinger** (Zhou, Bier, Santra, Jacobson, Abel et al.; Nat. Commun. 16, 2210, published 5 March 2025). Validated on 66 molecules / 137 known polymorphs, it "reproduces all the experimentally known polymorphs." For 33 single-form Z'=1 molecules, the match was in the top 10 in all cases and in the top 2 for 26 of 33. Costs: 22.6k CPU-h (PF-998245, vs ~200k reported previously); 93k CPU-h + 200 GPU-h for blind test target XXXI. A blinded study was run on Bayer's flupyradifurone. Calculations were "limited to Z′ = 1." — [Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-57479-1)
  - **Lavo-NN** (Glick, Metcalf, Swarthout; arXiv 2507.16218, July 2025, preprint; affiliation appears industrial, not verified). On a retrospective benchmark of 49 mostly drug-like molecules, it matched "all 110 Z′=1 experimental polymorphs" at ~8.4k CPU-h per CSP on average. — [arXiv 2507.16218](https://arxiv.org/abs/2507.16218)
  - **FastCSP** (Meta FAIR + Beran et al.; arXiv 2508.02641 v2, July 2026, preprint). Genarris 3 random generation plus UMA relaxation, free energy and conformer correction, "without any system-specific fine-tuning or DFT." On 28 semi-rigid and 10 flexible molecules (74 polymorphs) it "reliably recovers all known structures, ranking them within 9 kJ/mol of the global minimum." Cost is "hours to several days on tens of … H200 GPUs." UMA is weaker for chemistries under-represented in OMC25, such as metal-organics. — [arXiv 2508.02641](https://arxiv.org/abs/2508.02641); [Meta publication page](https://ai.meta.com/research/publications/fastcsp-accelerated-molecular-crystal-structure-prediction-with-universal-model-for-atoms/)
  - **CSP-MACE-Å** (Csányi group with AstraZeneca; arXiv 2605.28905, May 2026, preprint). A MACE-POLAR intramolecular model trained on OMol25, plus intermolecular, XDM-dispersion and Δ terms trained on 50k B86bPBE-XDM calculations. On 19 AstraZeneca compounds it is "comparable to PBE-NP DFT"; on 28 compounds from the seven blind tests (including cocrystals and salts) it is "close to B86bPBE-XDM DFT." It "outperform[s] the MACE-POLAR-1 and UMA-OMC foundation models." Harmonic free-energy reranking "substantially improves" results. — [arXiv 2605.28905](https://arxiv.org/abs/2605.28905)
- **Generative molecular CSP (2025-2026, all preprints):**
  - OXtal (100M-parameter all-atom diffusion, trained on 600k CSD structures): "conformer RMSD1 < 0.5 Å and over 80% packing similarity rate." — [arXiv 2512.06987](https://arxiv.org/abs/2512.06987)
  - Clari (Aspuru-Guzik group, unit-cell flow matching): beats OXtal's solve rate at 15-30x speed, "CSP within seconds." — [arXiv 2606.03199](https://arxiv.org/abs/2606.03199)
  - Zhu & Weng conditional lattice flow plus packing search: reproduces 83 of 84 Z'≤1 systems, but with Hall setting and Z' given. — [arXiv 2610.04193](https://arxiv.org/abs/2610.04193)
  - Others: CG-OMatG with RL (Martiniani group), MolCrystalFlow, PackFlow, OrgFlow, Packora. — [arXiv 2609.39773](https://arxiv.org/abs/2609.39773)

### Inferences
- The center of gravity in molecular CSP has shifted from tailor-made force fields to general MLIPs (UMA, MACE variants, AIMNet2, Lavo-NN) followed by DFT-D or free-energy reranking. Compute is falling from ~10^5 CPU-h to ~10^4 CPU-h or GPU-days per molecule. Accuracy claims, however, are retrospective and mostly Z'=1.
- The unsolved items from the blind test remain largely untested by the new ML methods. These are Z'>1, salts and cocrystals at scale, disorder, sub-kJ/mol ranking (Form A vs B of XXXI), and finite-temperature stability. Most ML papers explicitly restrict to Z'≤1 or given symmetry.

### Gaps
- No public 8th blind test details were found.
- Could not confirm which group(s) predicted disorder blindly. The paper does not name them in the extracted text.
- Lavo-NN's affiliation was not verified (it appears to be a company).

## Q3. Inorganic CSP: how good are generative models at (a) reproducing known structures, (b) proposing genuinely novel stable structures, (c) large cells, disorder, finite temperature?

### Takeaway
(a) On standard splits, generative models reproduce ~55-74% of MP-20 structures one-to-one but only ~15-37% of MPTS-52 structures. In an independent 2026 test, template retrieval still beat all 12 generative models (TCSPv3 67.8% vs CrystalFlow 63.9% top-1). Removing prototype families from training cut accuracy by 50-78%.

(b) Novelty claims are under sustained attack:
- MatterGen's flagship synthesized compound was shown to be a known disordered phase in its own training data (Materials Horizons 2026).
- 81-92% of valid metastable generated crystals are training duplicates or simple substitutions (Negishi & Walsh 2026).
- Cheetham and Seshadri found "scant evidence" of novel, credible, useful compounds among GNoME's 384,870 "stable" entries (Chem. Mater. 2024).

(c) Disorder, large cells and finite temperature are early-stage. There are disorder-aware generators (Dis-GEN, DMFlow, EP-Flow) and MLIP/SSCHA or learned free-energy CSP for hydrides, but no standard benchmark.

### Cited Findings
**(a) Reproduction**
- Wei, Dong, Feng, Miklos, Hu (U. South Carolina; arXiv 2609.26502 v2, 17 Oct 2026, preprint). T180 is 180 MP targets screened against MP-20 training data; top-1 StructureMatcher success:
  - TCSPv3 template 67.8% (72.2% with ORB-v3 relax; top-20 90.6%)
  - CrystalFlow 63.9% (top-20 72.2%)
  - OMatG 59.4%; Uni-3DAR 58.3%; EquiCSP 56.7%
  - DiffCSP 53.9%; MatterGen 53.9%
  - cond-CDVAE 40.0%; GemsDiff 34.4%; TGDMat 27.8%; CDVAE 26.7%; SymmCD 22.2%; CrystalGRW 12.8%
  - Of 182 generative-only successes, 157 had a matching prototype in the MP-20 train/val set, 21 in the wider 731k template library, and **4 in neither**.
  - Ablation: removing a prototype family from training cut accuracy on that family by 50-78%.
  - Conclusion: generative CSP models "function largely as implicit, softer-edged prototype libraries rather than genuinely de novo predictors."
  - Discrepancy: the abstract quotes TCSP 68.3%, EquiCSP 66.4% and Uni-3DAR 62.9%, which differ from the tables. This is possibly a version difference; check before quoting.
  - Source: [arXiv 2609.26502](https://arxiv.org/abs/2609.26502)
- CrystalFormer-CSP (Cao, Ou, Wang, IOP-CAS; arXiv 2512.18251, Dec 2025, preprint). Combines a space-group-informed autoregressive generator with ORB-v3 relaxation and RL. Match on two literature sets of 40 and 50 compounds (up to 104 atoms, e.g. Ca14MnSb11) is 82.5% and 80%, rising to 95% and 86% with RL, vs 77.5% and 78% in the prior reference. Space-group top-1 accuracy is 52.7% (top-40: 98.9%). It fails when the Wyckoff sequence is longer than 20. Many "misses" relax to energies below the reference. — [arXiv 2512.18251](https://arxiv.org/abs/2512.18251)
- MP-20 / MPTS-52 numbers are in Q1. The 2026 crop of methods includes:
  - MaskGXT (masked transformer found by an AI co-scientist) and Crystalite (lightweight diffusion transformer, "best S.U.N. discovery score among evaluated baselines") — [arXiv 2604.02270](https://arxiv.org/abs/2604.02270)
  - KLDM (kinetic Langevin diffusion), "competitive" — [arXiv 2507.03602](https://arxiv.org/abs/2507.03602)
  - OMatG-IRL, the first RL for flow-based CSP, claiming order-of-magnitude sampling speedups — [arXiv 2602.00424](https://arxiv.org/abs/2602.00424)
  - NextCrystal (LLM-generated Wyckoff patterns plus diffusion; claims SOTA SUN and a new HfO2 Pnma phase 0.056 eV/atom lower) — [arXiv 2602.17176](https://arxiv.org/abs/2602.17176)
  - CrystalAR (Oct 2026) — [arXiv 2610.27762](https://arxiv.org/abs/2610.27762)

**(b) Genuine novelty and stability**
- **MatterGen (Microsoft; Nature, published 16 Jan 2025; 754 citations per Semantic Scholar).**
  - "More than twice as likely to be new and stable, and more than ten times closer to the local energy minimum" than prior models.
  - 78% of samples are within 0.1 eV/atom of the MP hull (13% below 0). 75% are within 0.1 eV/atom of the Alex-MP-ICSD hull (850,384 structures), with 3% below 0.
  - 61% are new. Uniqueness is 100% at 1k samples and 52% at 10M.
  - Novelty is checked with an "ordered-disordered structure matcher" against 117,652 disordered ICSD entries.
  - The synthesized TaCr2O6 had bulk modulus within 20% of target.
  - Source: [Zeni et al., Nature 2025](https://www.nature.com/articles/s41586-025-08628-5)
- **Materials Horizons critique** (Mikkel Juelsholt; Mater. Horiz. 2026, 13, 5672; received 12 Feb 2026, accepted 8 Apr 2026; DOI 10.1039/d6mh00268d; ChemRxiv preprint 2025):
  - The synthesized "TaCr2O6," obtained in disordered form as Ta1/3Cr2/3O2, "is not a novel compound but is identical to the previously reported Ta1/2Cr1/2O2, first described in 1971 and included in MatterGen's training dataset (ICSD 9516 / COD 9011856)."
  - Rietveld refinement of the MatterGen PXRD data with the known Ta1/2Cr1/2O2 model fits well (RBragg 1.62%) and refines to Ta0.43Cr0.57O2.
  - Conclusion: "MatterGen cannot distinguish between its training data and the compounds it predicts … human inspection of each predicted compound is needed."
  - Sources: [RSC Mater. Horiz.](https://pubs.rsc.org/mh/article/13/11/5672/1228702/Continued-challenges-in-high-throughput-materials); [ChemRxiv v3](https://chemrxiv.org/doi/full/10.26434/chemrxiv-2025-mkls8/v3)
  - No published Microsoft reply was found.
- **Negishi & Walsh (Imperial; arXiv 2606.23166, June 2026, preprint):** "81-92% of chemically valid and metastable generated crystals are either training duplicates or substitution-derived structures," with high-symmetry duplicates attributed to memorisation. — [arXiv 2606.23166](https://arxiv.org/abs/2606.23166)
- **LeMat-GenBench:** against ~5M LeMat-Bulk structures, strict SUN (on-hull, unique, novel) is ≤1% for all 12 models (MatterGen 0.2%, PLaID++ 1.0%). MatterGen leads metastable MSUN at 15.0%. — [arXiv 2512.04562](https://arxiv.org/abs/2512.04562)
- **GNoME critique (Cheetham & Seshadri, Chem. Mater. 36, 3490-3495, Apr 2024; 175 citations):**
  - They examined random subsets of GNoME's 384,870-entry "Stable Structure" database and found "scant evidence for compounds that fulfill the trifecta of novelty, credibility, and utility."
  - "We have yet to find any strikingly novel compounds."
  - Many entries are ordered versions of compounds that would be disordered in reality.
  - 18,138 entries contain Pm, Ac or Pa, and a further 23,529 contain Tc, Np or Pu.
  - The space-group distribution is anomalous. The top four are all non-centrosymmetric (~34% of entries), and Pnma and P21/c account for only 1.56% and 0.7%, vs ~8% each in the ICSD.
  - They concede that "the underlying approach is sound."
  - Source: [Cheetham & Seshadri, Chem. Mater. 2024 (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044265/)
- **GNoME original claims** (Merchant et al., Nature, Nov 2023; 1,850 citations): 2.2M structures below the previous hull, ~381k on the new hull ("order-of-magnitude expansion"), and 736 independently realized experimentally (as reported in coverage). — [Nature 2023](https://www.nature.com/articles/s41586-023-06735-9); [Cheetham & Seshadri quoting the claims](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044265/)
- A later 2026 preprint characterizes the record: Cheetham and Seshadri found almost none credible, new and useful, and a re-examination of autonomous-synthesis (A-Lab) claims found none convincingly demonstrated (Leeman et al., PRX Energy 2024). Secondary characterization only. — [arXiv 2606.23725](https://arxiv.org/abs/2606.23725)
- **uMLIP-driven classical CSP finding new compounds:**
  - An & Wang (arXiv 2602.03369, preprint) used M3GNet-driven CSP in Sr-Li-Al-O and Ba-Y-Al-O. It rediscovered known phases absent from training and found seven new thermodynamically and dynamically stable compounds. They note that PBE stability needs SCAN/RPA cross-checks, and that "the primary bottleneck has shifted to the efficiency of search algorithms." — [arXiv 2602.03369](https://arxiv.org/abs/2602.03369)
  - Chtchelkatchev et al. (arXiv 2606.30870) ran foundation-MLIP evolutionary CSP with adaptive fine-tuning and predicted Ca6FeNi stable above 100 GPa. — [arXiv 2606.30870](https://arxiv.org/abs/2606.30870)

**(c) Large cells, disorder, finite temperature**
- **Large cells:** MPTS-52 (≤52 atoms) best MR is ~33-37% vs ~67-74% on MP-20 (Q1). CrystalFormer-CSP fails beyond a Wyckoff length of 20. — [arXiv 2606.22866](https://arxiv.org/abs/2606.22866); [arXiv 2512.18251](https://arxiv.org/abs/2512.18251)
- **Disorder:**
  - Dis-GEN (July 2025) is trained on the ICSD and generates mixed occupancy and vacancies with symmetry. — [arXiv 2507.18275](https://arxiv.org/abs/2507.18275)
  - DMFlow (Feb 2026) handles substitutional and positional disorder with a COD-derived benchmark. — [arXiv 2602.04734](https://arxiv.org/abs/2602.04734)
  - EP-Flow (Oct 2026) uses an occupancy distribution matrix and claims "state-of-the-art performance on formula-conditioned disordered CSP benchmarks derived from COD and MPDS." — [arXiv 2610.01315](https://arxiv.org/abs/2610.01315)
  - A 2026 review says generative models still need better ways to represent and validate partial occupancy. — [arXiv 2605.19124](https://arxiv.org/abs/2605.19124)
- **Finite temperature and quantum nuclei:**
  - Oganov group SSCHA plus MLIP evolutionary CSP for LaH10. MatterSim-5M "enables SSCHA-based CSP without per-structure training, but fine-tuning is required for higher accuracy"; "quantum anharmonicity … is essential for the correct energy ranking." — [arXiv 2512.24849](https://arxiv.org/abs/2512.24849)
  - "Deep free energy" model (Han Wang, Lei Wang et al., Apr 2026) learns the SCHA free-energy surface, giving a 1.72×10^6-fold cost reduction vs DFT-SSCHA. It found P4/mmm LaScH8 at 200 GPa / 300 K. — [arXiv 2604.20230](https://arxiv.org/abs/2604.20230)
  - OpenCSP (pressure-resolved data, Sept 2025) reports matching or beating MACE-MPA-0, MatterSim v1 5M and GRACE-2L-OAM on high-pressure enthalpy ranking. — [arXiv 2509.10293](https://arxiv.org/abs/2509.10293)

### Inferences
- For known chemistries, template and substitution retrieval combined with a uMLIP relax is still a very strong (often the strongest) baseline. Generative models add modest, largely prototype-dependent coverage. The best-supported 2026 framing is "generative models as soft prototype libraries."
- The novelty problem is partly a disorder problem. The MatterGen and GNoME critiques both hinge on ordered predictions of phases that are disordered in reality. Disorder-aware generators exist but have no shared benchmark or experimental validation yet.
- Finite-temperature CSP is advancing fastest in hydrides and high pressure, where ML free-energy surrogates are used, not in generative models.

### Gaps
- No independent experimental-validation rate (synthesized / proposed) for generative-model proposals in 2025-2026 was found.
- Could not verify the "736 experimentally realized" GNoME number from the primary paper in this session.
- No Microsoft response to the Materials Horizons critique was found.

## Q4. How are universal MLIPs changing CSP (speed, hull accuracy, F1, failure modes)?

### Takeaway
uMLIPs are now the default energy engine for both inorganic and molecular CSP. Examples include ORB-v3 inside CrystalFormer-CSP and as the relaxer in benchmarks, UMA inside FastCSP, MatterSim in SSCHA-CSP, and M3GNet in quaternary-oxide searches. Matbench Discovery F1 rose from 0.57-0.82 (2023) to 0.93 (2026). Known failure modes persist:
- systematic PES softening (under-curvature)
- energy and hull under-prediction, with E_hull MAE above ~30 meV/atom even for the best of nine models, and above 40 meV/atom for high-symmetry-DOF structures
- degraded accuracy at high pressure and in low dimensions
- under-represented chemistries (metal-organics in OMC25)
- smoother PESs that do not guarantee correct landscapes

### Cited Findings
- F1 trajectory: M3GNet 0.569 (2022) → CHGNet 0.613 → MACE-MP-0 0.669 (2023) → NequIP-GNoME 0.829 (Feb 2024) → eqV2 M 0.917 (Oct 2024) → eSEN-30M-OAM 0.925 (Mar 2025) → EquiformerV3+DeNS-OAM 0.931 (Apr 2026). — [Matbench Discovery repo](https://github.com/janosh/matbench-discovery/tree/main/models)
- Training data is the main driver. MP-only (MPtrj) versions lag OAM (OMat24 + sAlex + MPtrj) versions of the same architecture: EquiformerV3 0.863 vs 0.931, and eSEN 0.831 vs 0.925. — [same repo](https://github.com/janosh/matbench-discovery/tree/main/models)
- Matbench Discovery's own caveat: "accurate regressors can yield high false-positive rates near the decision boundary at 0 eV/atom above the convex hull." — [arXiv 2308.14920](https://arxiv.org/abs/2308.14920)
- **Softening:** M3GNet, CHGNet and MACE-MP-0 "systematically underpredict energies and forces" (surfaces, defects, phonons, migration barriers), because training data over-represents near-equilibrium structures. A single fine-tuning data point largely corrects it. — [Deng et al., arXiv 2405.07105](https://arxiv.org/abs/2405.07105)
- **Under-prediction tied to symmetry:**
  - Over 12M calculations, 9 MLIPs, >150k MP crystals.
  - "Most frontier models consistently underpredict energy above hull … MAE for Ehull exceed ~30 meV/atom even by the best model," despite >90% of test structures being in training data.
  - "Pronounced errors (MAE for Ehull > ~40 meV/atom) in structures with high symmetry DOF," with "severe energy underprediction for a large proportion of near-hull materials."
  - Source: [Nong et al., arXiv 2507.15190 (preprint, v2 Nov 2025)](https://arxiv.org/abs/2507.15190)
- **Elemental minima-hopping benchmark** (MACE variants, MatterSim, PET-MAD): gaps in alkali and alkaline-earth metals, and "a decoupling between search efficiency and structural fidelity … smoother learned PESs do not necessarily yield more accurate energetic landscapes." — [arXiv 2512.20230](https://arxiv.org/abs/2512.20230)
- **High pressure:** "most large atomistic models are trained on near-ambient, equilibrium data, leading to degraded stress accuracy at tens to hundreds of gigapascals." — [OpenCSP arXiv 2509.10293](https://arxiv.org/abs/2509.10293)
- **Molecular crystals:**
  - UMA-S reaches lattice energies ≤3 kJ/mol on the 7th blind test and outperforms an eSEN-S-OMC baseline — [arXiv 2506.23971](https://arxiv.org/abs/2506.23971)
  - CSP-MACE-Å, a purpose-built model, beats UMA-OMC and MACE-POLAR-1 on 47 blind-test and AstraZeneca compounds — [arXiv 2605.28905](https://arxiv.org/abs/2605.28905)
  - FastCSP notes UMA weaknesses for "metal-organic compounds" under-represented in OMC25 — [arXiv 2508.02641](https://arxiv.org/abs/2508.02641)
- **Speed:** UMA-M has ~50M active of 1.4B parameters, and UMA reports single-GPU MD speeds vs eSEN and ORB-v3. FastCSP gives hours to days on tens of H200s per molecule. CSP-MACE-Å is "multiple orders of magnitude faster than DFT." The DAO generator claims ">2000x faster per iteration than DFT-based structure predictors" (self-reported). — [UMA](https://arxiv.org/abs/2506.23971); [FastCSP](https://arxiv.org/abs/2508.02641); [CSP-MACE-Å](https://arxiv.org/abs/2605.28905); [DAO](https://arxiv.org/abs/2503.10471)
- **Bottleneck shift:** "While uMLIPs substantially reduce the computational cost of CSP, the primary bottleneck has shifted to the efficiency of search algorithms in navigating complex structural spaces." — [arXiv 2602.03369](https://arxiv.org/abs/2602.03369)
- CSPBench reports that on a 23-structure subset, "ML potential-based algorithms prove highly competitive with DFT-based methods" at finding lower-energy structures. — [CSPBench, Adv. Intell. Discov.](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aidi.70162)
- **Classical codes plus ML:**
  - Hot-AIRSS with ephemeral data-derived potentials (EDDPs) handles complex boron in large cells — [Pickard, Faraday Discuss. 2025](https://pubs.rsc.org/en/content/articlehtml/2025/fd/d4fd00134f)
  - SRSS: symmetry-constrained random search with uMLIP relaxation on CPUs only — [arXiv 2604.08972](https://arxiv.org/abs/2604.08972)
  - XtalOpt v14 adds variable-composition Pareto search — [arXiv 2506.17246](https://arxiv.org/abs/2506.17246)

### Inferences
- In practice, uMLIPs now do the fast pre-screening and relaxation, and DFT (or higher-level theory for near-degenerate polymorphs) is kept for final ranking. Their errors (~20-40 meV/atom on E_hull; kJ/mol-level for molecules) are of the same order as the polymorph energy differences CSP must resolve. They are therefore not a drop-in replacement for final ranking without fine-tuning or Δ-learning, which is the route taken by CSP-MACE-Å.
- Matbench Discovery F1 measures stability classification of given (relaxed) structures, not search success. A high F1 does not by itself imply a better CSP engine.

### Gaps
- No standardized "uMLIP-as-CSP-engine" benchmark (e.g. AIRSS or USPEX ground-state recovery rate per potential) was found for bulk inorganic crystals.
- Soft-mode / imaginary-phonon failure rates in CSP outputs are not quantified in sources found. Only the indirect κ_SRME and softening evidence is available.

## Q5. Most-cited and most-discussed 2025-2026 papers and preprints, and what they claim

### Takeaway
By citations, MatterGen (Nature, Jan 2025; ~754) and UMA (NeurIPS 2025; ~306) dominate the 2025 crop, alongside 2023-2024 anchors: GNoME ~1,850, MACE-MP-0 ~861, MatterSim ~311, DiffCSP ~252. Most 2025-2026 CSP-specific works have under 50 citations. The most consequential 2026 contributions are critical evaluations (prototype dependence, substitution analysis, the MatterGen critique) and MLIP-only molecular CSP pipelines.

### Cited Findings
Semantic Scholar citation counts, queried 2026-10-22 — [Semantic Scholar API](https://api.semanticscholar.org/):

| Paper | Citations | Claim |
|---|---|---|
| Merchant et al., "Scaling deep learning for materials discovery" (GNoME), Nature Nov 2023 | 1,850 | 2.2M new structures / ~381k stable |
| Batatia et al., MACE-MP-0, 2023 / J. Chem. Phys. | 861 | foundation MLIP |
| Zeni et al., MatterGen, Nature 16 Jan 2025 | **754** | >2x SUN vs prior models; synthesized TaCr2O6 (disputed, see Q3) |
| MatterSim (Microsoft), 2024 | 311 | MLIP across elements, temperatures and pressures |
| UMA, Meta FAIR, Jun 2025 (NeurIPS 2025) | **306** | ~500M training structures; claims top Matbench Discovery F1 |
| DiffCSP, NeurIPS 2023 | 252 | |
| OMat24, 2024 | 183 | |
| Cheetham & Seshadri, Chem. Mater. Apr 2024 | 175 | GNoME critique |
| Orb-v3, Apr 2025 | 162 | |
| Matbench Discovery (arXiv record; Nat. Mach. Intell. 2025) | 114 | |
| 7th blind test, generation / ranking (Acta Cryst. B 2024) | 43 / 32 | |
| Schrödinger CSP, Nat. Commun. Mar 2025 | 34 | 66 molecules / 137 polymorphs all reproduced |
| LeMat-GenBench, Dec 2025 | 27 | |
| FastCSP, Aug 2025 | 14 | UMA-only molecular CSP recovers all 74 polymorphs within 9 kJ/mol |
| "All that structure matches does not glitter", NeurIPS 2025 | 13 | dataset and metric flaws; METRe |
| MatLLMSearch, 2025 | 12 | |
| DAO (Nat. Commun.) | 11 | |
| OXtal, Dec 2025 | 10 | |
| CSPBench | 8 | |
| CrystalFormer-CSP | 1 | |
| Nong et al. symmetry under-prediction | 1 | |

**LLM-based CSP**
- MatLLMSearch (Gan, Zhong, … Gomes, Persson, Wei Wang; Feb 2025, revised Oct 2025) uses pre-trained LLMs without fine-tuning as crossover and mutation operators in an evolutionary loop. It reports "78.38% metastable rate validated by MLIPs and 31.7% DFT-verified stability," outperforming CrystalTextLLM. — [arXiv 2502.20933](https://arxiv.org/abs/2502.20933)
- LLaMat2-CIF and LLaMat3-CIF (fine-tuned LLMs) score MSUN 2.1% and 0.2% on LeMat-GenBench, far below diffusion models. — [arXiv 2512.04562](https://arxiv.org/abs/2512.04562)
- Hybrid LLM + continuous models:
  - Lang2Str: LLM text description, then flow decoder — [arXiv 2603.03946](https://arxiv.org/abs/2603.03946)
  - NextCrystal: LLM proposes Wyckoff patterns, then diffusion — [arXiv 2602.17176](https://arxiv.org/abs/2602.17176)
  - Atomistic Language Models (Gómez-Bombarelli / Ju Li, June 2026): LLM bridged into atomistic diffusion; claims SOTA on CSP and DNG; ALM Bench — [arXiv 2606.21395](https://arxiv.org/abs/2606.21395)
  - CrystalFormer-CSP ships an LLM integration — [arXiv 2512.18251](https://arxiv.org/abs/2512.18251)
- AI co-scientist (HACO) "discovered" the MaskGXT algorithm, which tops MP-20 and MPTS-52 in its own comparison. — [arXiv 2606.22866](https://arxiv.org/abs/2606.22866)
- Chemeleon (Park, Onwuli, Walsh; Nat. Commun., 12 May 2025): text-guided diffusion via cross-modal contrastive learning. Demonstrated on Zn-Ti-O and Li-P-S-Cl; runs on a laptop in minutes. — [PMC12069578](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12069578/)

### Inferences
- LLM-only crystal generators lag diffusion and flow models on rigorous SUN metrics. LLMs are most useful as orchestrators or proposal operators (evolutionary operators, Wyckoff and composition proposal, tool use), not as coordinate generators.

### Gaps
- Citation counts for FlowMM, CrystalFlow, ADiT, Crystalite and Uni-Mat were not retrieved: IDs were not resolved in the batch query.
- Uni-Mat and an independent ADiT CSP benchmark were not specifically investigated. ADiT appears only in LeMat-GenBench (MSUN 1.0%).
- The awesome-crystal-structure-prediction GitHub list (usccolumbia) was not fetched.
