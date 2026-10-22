# GNoME and A-Lab (Nature 624, 2023): published work that supports, uses, critiques, or corrects them (Nov 2023 to Oct 2026)

Papers in scope: Merchant, Batzner, Schoenholz, Aykol, Cheon & Cubuk, "Scaling deep learning for materials discovery", Nature 624, 80-85, published online 29 Nov 2023, DOI 10.1038/s41586-023-06735-9 ("GNoME"). Szymanski et al., "An autonomous laboratory for the accelerated synthesis of inorganic materials", Nature 624, 86-91, published online 29 Nov 2023, DOI 10.1038/s41586-023-06734-w ("A-Lab"; Merchant and Cubuk are co-authors). Research date: 22 Oct 2026.

How each item was checked: [READ] means I read the full text, or the relevant section, at the source. [ABSTRACT/PARTIAL] means I read only the abstract, the free lead of a paywalled article, or a metadata page. [SECONDARY] means I know the item only through another source or a search snippet. Peer-review status is given for every item.

## Q1 (A). Critiques: who argued what, with which numbers and methods?

### Takeaway
The critiques form one consistent chain of argument. Most GNoME "discoveries" are element substitutions or artificially ordered versions of known structure types, and many are ordered approximants of compounds already known in disordered form. The A-Lab "new" materials were mostly misidentified or already known. The critiques progressed from qualitative expert sampling in 2024 (Cheetham & Seshadri: 10 of 10 random entries had ICSD analogues; Leeman/Schoop/Palgrave: 42 of 43 A-Lab products problematic) to database-wide statistics in 2025-2026. Those statistics are: an ML disorder classifier predicting 80-84% of GNoME compositions are prone to disorder; the Liverpool invariant audit (arXiv:2610.13885, 9 Oct 2026), which found 0.44% exact geometric duplicates and 12-15% near-duplicates at 0.01 Å inside GNoME; and the same audit finding that about 70-78% of entries are geometrically within 0.05 Å of a pre-2021 ICSD or MP structure. The audit itself says that only 0.15-0.37% are true geometry-plus-chemistry duplicates of known crystals.

### Cited Findings

**A1. Cheetham, A. K. & Seshadri, R.** "Artificial Intelligence Driving Materials Discovery? Perspective on the Article: Scaling Deep Learning for Materials Discovery." *Chem. Mater.* 36(8), 3490-3495. Received 4 Mar 2024; accepted 25 Mar 2024; published online 8 Apr 2024. DOI 10.1021/acs.chemmater.4c00643. Peer-reviewed perspective, open access. [READ] — [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044265/); [ACS](https://pubs.acs.org/doi/10.1021/acs.chemmater.4c00643)
- Claim: "We examine the claims of this work here, unfortunately finding scant evidence for compounds that fulfill the trifecta of novelty, credibility, and utility." Also: "we have yet to find any strikingly novel compounds in the GNoME and Stable Structure listings, although we anticipate that there must be some among the 384,870 compositions." They concede that "the computational approach delivers credible overall compositions, which gives us confidence that the underlying approach is sound."
- Method: (1) They manually inspected the first 250 of the 2,047 entries in the Materials Project "GNoME Explorer". (2) They compiled space-group statistics for all 384,870 "Stable Structure" entries and compared them with ICSD statistics (Urusov & Nadezhina). (3) They took 10 randomly selected Stable Structure entries and searched ICSD for each by elements, lattice parameters and space group.
- Numbers:
  - All 10 random entries had an identifiable ICSD structural analogue, usually with higher symmetry. Only 1 of the 10 had the same space group.
  - Actinium compounds: 27 in GNoME Explorer and about 6,754 in the Stable Structure database.
  - Radioactive elements: 18,138 compounds of Pm, Ac and Pa, plus 23,529 entries containing Tc, Np or Pu.
  - Space groups: the top four GNoME space groups are all non-centrosymmetric and together hold about 34% of entries (Pm alone is 49,037 entries, 12.7%). In ICSD, Pnma and P21/c hold about 8% each (about 16% together), and only one non-centrosymmetric group is in the ICSD top 24 (about 1% of entries). In GNoME, Pnma ranks 16th at 1.56% and P21/c holds 0.7%.
- Mechanism: 0 K DFT places chemically similar cations (lanthanides, Zr/Hf, Nb) on separate crystallographic sites because it ignores configurational entropy, and this lowers the symmetry. Examples, with the known structure each corresponds to:
  - TbSmSeO2 → La2SeO2
  - DyHo2Rh9 → PuNi3 type
  - TbHo2Tm9Co4 → Fe3C-type Ho3Co
  - Tb16HoEr3Ir12 → Tb5Ir3
  - Hf4Ir8N4NbZr11 → Zr4Ir2N
  - K3Nd(AsO4)2 → K3Nd(PO4)2
  - AcEr3(B6)4 → a LaB6 superstructure
  - TbSmF30 contains F2 molecules.

**A2. Leeman, J., Liu, Y., Stiles, J., Lee, S. B., Bhatt, P., Schoop, L. M. & Palgrave, R. G.** "Challenges in High-Throughput Inorganic Materials Prediction and Autonomous Synthesis." *PRX Energy* 3, 011002 (2024). Received 30 Jan 2024; published 7 Mar 2024. DOI 10.1103/PRXEnergy.3.011002. Peer-reviewed perspective, open access. An earlier preprint, ChemRxiv doi 10.26434/chemrxiv-2024-5p9j4, was posted about 8 Jan 2024. [READ] — [PRX Energy](https://doi.org/10.1103/PRXEnergy.3.011002); preprint DOI from [Nature News](https://www.nature.com/articles/d41586-023-03956-w)
- Claim: "We discuss all 43 synthetic products and point out four common shortfalls in the analysis. These errors unfortunately lead to the conclusion that no new materials have been discovered in that work." Of the 36 A-Lab successes plus 7 partial successes, they found "significant issues with 42 of them (the exception being CaFe2(PO4)2O)". "Two thirds of the claimed successful materials ... are likely to be known compositionally disordered versions of the predicted ordered compounds." Three products were made correctly but were already known: MnAgO2, Y3In2Ga3O12 and CaFe2(PO4)2O.
- Method: they redid Rietveld refinements of A-Lab's published PXRD patterns in GSAS-II (the software A-Lab used), with empirically fitted peak profiles, and searched ICSD for known phases, often disordered ones.
- Numbers (error types among the 36 "successes"):
  - Unmodelled peaks or incomplete reaction: 18/36.
  - Prediction changed to match the observed pattern by substituting a cation-disordered CIF: 8/36 (the count is truncated in my text extraction to "8/3…", so 8/36 is inferred).
  - The disordered version already exists in ICSD: 24/36.
  - Existing compounds reported as new: 3/36.
- Disorder argument: the predicted compounds put every element on its own site, but in reality elements share sites, which gives higher-symmetry known alloys or solid solutions. They also note that some targets were reported between 2021 and 2023, after GNoME's 2021 database snapshot.

**A3. Widdowson, D. E., Kurlina, T. V., Anosova, O. D. & Kurlin, V. A.** "Necessary conditions for benchmarking next-generation AI in materials discovery." arXiv:2610.13885 [cond-mat.mtrl-sci], v1 9 Oct 2026. University of Liverpool and UCL. Preprint, not peer-reviewed. This is the October 2026 audit that C&EN reported (see A4). [READ, full PDF] — [arXiv](https://arxiv.org/abs/2610.13885)
- Claim: invariant-based all-vs-all comparison (AMD/PDD/PDA invariants, isosets, EMD metric) "exposes the unexpected scale of duplication in the world's largest materials databases, shown here in the high-profile case of GNoME datasets". In their words, "GNoME's geometry is largely the geometry of known crystals." They propose four necessary conditions before anyone claims new materials, including a continuous "Local Novelty Distance" and bond-length sanity checks.
- Data:
  - "GNoME1" is the 29 Nov 2023 release, with 384,938 entries.
  - "GNoME2" is the 21 Nov 2024 release, with 554,054 entries. It shares 301,413 entries with GNoME1; 83,525 GNoME1 entries were removed and 252,641 were added.
  - Reference sets were ICSD and Materials Project, keeping only entries from before March 2021 (MP v2026.04.13 queried with include_gnome=False).
- Near-duplicates within GNoME:
  - Text-identical CIFs in GNoME1: 2,311 entries (one quadruple, 43 triples and 1,089 pairs). This contradicts the paper's stated pairwise pymatgen deduplication.
  - Identical geometry once element labels are ignored: 3,248 entries (0.84%).
  - With coordinates rounded to 4, 3, 2 and 1 digits in Å: 4,379 (1.14%), 4,716 (1.23%), 5,972 (1.55%) and 44,238 (11.49%).
  - GNoME2 has fewer: 591 (0.11%), 1,206 (0.22%), 1,322 (0.24%), 2,083 (0.38%) and 60,012 (10.83%).
- Invariant "geometric matches" and redundancy rate (excess entries ÷ dataset size):

  | Dataset | τ = 1e-10 Å | τ = 1e-3 Å | τ = 1e-2 Å |
  |---|---|---|---|
  | GNoME1 | 0.437% (3,248 entries in 1,567 groups) | 0.787% | 12.438% (67,488 entries in 19,610 groups; largest group 352) |
  | GNoME2 | 0.057% (591 entries in 273 groups) | 0.207% | 15.178% (108,286 entries in 24,194 groups; largest group 723) |

  "Geochemical" matches (same elements as well as geometry): GNoME1 has 2,311 entries (0.306%) at 1e-10 Å and 8,622 entries (1.156%) at 1e-2 Å. GNoME2 has none up to 0.01 Å.
- Overlap with known crystals (pre-2021 ICSD and MP, geometry only, EMD on PDA[100]). Share of GNoME entries within 0.05 Å of a known structure:

  | | vs ICSD | vs MP |
  |---|---|---|
  | GNoME1 | 69.7% | 74.8% |
  | GNoME2 | 73.1% | 78.4% |

  - Within 0.02 Å the shares are 15.2/16.3% (ICSD) and 21.3/24.1% (MP). Within 0.01 Å they are 3.3/3.0% and 5.1/5.5%.
  - With pymatgen StructureMatcher RMSD under 0.05, the shares are 62.8/66.1% (ICSD) and 71.1/74.3% (MP).
  - The median GNoME2 entry sits 0.034 Å from some ICSD structure and 0.03 Å from some MP structure.
  - The authors' headline: "over 60% of predictions in GNoMEs 1&2 are geometrically close to known crystals in the ICSD and MP up to 0.05Å."
- Authors' own caveat on chemistry: true geometry-plus-chemistry matches to known crystals are rare.
  - GNoME2: 824 entries match an ICSD crystal within 0.05 Å and 1 entry matches an MP crystal, together 0.15%.
  - GNoME1: 1,315 (ICSD) and 155 (MP), together 0.37%.
  - Only 5.3% of GNoME2 entries (29,167) share an element set with any ICSD entry, and 0.9% (5,201) share a composition.
  - Their explanation for the high geometric overlap is GNoME's approach of taking existing crystals and relabelling elements with similar ones.
- Curation forensics:
  - Between GNoME1 and GNoME2, 92.7% of GNoME1 entries that matched a known ordered ICSD crystal were withdrawn. Only 40.4% of those matching a known disordered crystal were withdrawn. The background removal rate was 21.7%.
  - 99.4% of the 155 MP matches were withdrawn.
  - 95.3% of GNoME1 entries with a geochemical duplicate were dropped.
  - The authors infer that a filter removed known ordered ICSD crystals but could not catch ordered versions of known disordered ones.
  - GNoME2 also introduced new geometric duplicates: of its 273 groups, 62 grew out of GNoME1 singletons and 32 consist entirely of new entries.
  - The release notes give no withdrawal counts. Old versions sit undocumented in gs://gdm_materials_discovery/gnome_data/legacy_versions/ (11_29_23, 12_1_23, 8_21_24).
  - The GNoME overview still says "~381,000 novel structures".
- Radioactive elements (counting Bi, Th and U as well as Ac, Np, Pa, Pm, Pu and Tc): 80,235 GNoME1 entries (20.8%) and 108,020 GNoME2 entries (19.5%).
- Unphysical examples: GNoME1 entry 83cc15ef46 (H2O11, "chaotically located molecules"); entry eed3027c1e, with a K atom that has no neighbours; an entry with density 0.18 g/cm3; and 8175bee583 (H2ORb2Se), which contains a water molecule.
- Checks of downstream "confirmations":
  - Miura et al. (JACS 2024): none of its six successfully made compositions appears in GNoME1 or GNoME2. The impure Cs2LiVCl6 corresponds to GNoME1 entry 66ae3fec06, which is a near-duplicate of ICSD 002064 (CsCuCl3, published 1974) at EMD about 0.064 Å and of mp-1206187 at about 0.043 Å.
  - Naganuma & Kitagawa (JMMM 2026): their MnFeCo4Si2, GNoME entry d8afdc992d, has a near-duplicate in ICSD (675046, deposited 2018) at EMD about 0.022 Å.

**A4. Chawla, D. S.** "Google DeepMind AI crystallography database includes near duplicate structures and unrealistic compounds." *C&EN*, 15 Oct 2026. News, paywalled after the lead. [ABSTRACT/PARTIAL: headline, subtitle, key insights and first paragraphs] — [C&EN](https://cen.acs.org/research-integrity/Google-DeepMind-structures-near-duplicates-questionable/104/web/2026/10)
- Subtitle: "After hyping previous claims, tech giant doesn't comment on inquiries about lack of novelty in database of AI-generated crystals."
- Key insight: the new paper "details a large amount of very similar entries both within a crystallographic database produced by Google DeepMind's GNoME and between GNoME's database and other repositories", following earlier evidence that GNoME's predictions "lack novelty and uniqueness."
- I could not read which percentages C&EN quoted. The verified numbers are in A3.

**A5. Chawla, D. S.** "The duplicates that haunt crystallography databases" (URL slug "Duplicate-structures-haunt-crystallography-databases"). *C&EN*, 16 Dec 2025. News feature, paywalled. [ABSTRACT/PARTIAL] — [C&EN](https://cen.acs.org/research-integrity/Duplicate-structures-haunt-crystallography-databases/103/web/2025/12)
- Deck: "Researchers call for retraction of two recent Nature studies about AI-generated crystals." Lead: "Two years on, the study—which has already attracted around 1,000 citations—faces calls for retraction. Critics say many crystals that the study authors claimed were novel were in fact duplicates."
- Widdowson et al. say this story "highlighted our research since 2021" and preceded the A-Lab correction.

**A6. Chawla, D. S.** "'Nature' robot chemist paper corrected, but some questions remain unanswered." *C&EN*, 29 Jan 2026. News, paywalled. [ABSTRACT/PARTIAL] — [C&EN](https://cen.acs.org/research-integrity/Nature-robot-chemist-paper-corrected/104/web/2026/01)
- Lead: Nature "has corrected a highly cited study about a robot designed to synthesize entirely new materials ... but critics say their concerns haven't been fully addressed."
- A search-engine summary of the body says Palgrave and Schoop were not fully satisfied, that disorder concerns were not addressed, and that Ceder did not reply to requests for comment. [SECONDARY; the snippet is internally ambiguous on whether Palgrave still wants a retraction]

**A7. Jakob, K. S., Walsh, A., Reuter, K. & Margraf, J. T.** "Learning Crystallographic Disorder: Bridging Prediction and Experiment in Materials Discovery." *Advanced Materials* 38(5), DOI 10.1002/adma.202514226. Published online 23 Oct 2025; issue dated 22 Jan 2026. Peer-reviewed. [READ via Europe PMC full text, PMC12822528] — [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12822528/)
- Claim: classifiers trained on ICSD predict substitutional disorder from composition alone with about 90% accuracy. They estimate the share of compositions prone to disorder at 39-47% for MP and 80-84% for GNoME (classification thresholds of 70% and 50%), so GNoME is "potentially being dominated by disordered systems."
- Method: RNN/LSTM composition classifiers applied to all 554,054 GNoME structures in the February 2025 GitHub release, with no further curation.
- Cross-checks against the critiques:
  - For the A-Lab compounds with known disordered phases (23 of 35), the model predicts 16 (70%) are disordered.
  - It predicts 9 of Cheetham & Seshadri's 10 random GNoME entries are disordered.
  - Stated caveat: there is a large covariate shift relative to the training data.

**A8. Yamazaki, S., Huang, Y., Petersen, M. H., Nong, W., Hippalgaonkar, K. et al.** "Navigating Order-(Dis)Order Family Trees via Group-Subgroup Transitions." arXiv:2604.21386, 23 Apr 2026. Preprint. [READ, HTML full text] — [arXiv](https://arxiv.org/abs/2604.21386)
- Claim: a predicted ordered structure is often an "ordered child of a disordered parent". Novelty checks against databases of ordered structures miss this, which leads to "a systematic overestimation of discovery rates."
- Method: automated matching of group-subgroup symmetry relations against ICSD.
- Numbers:
  - Of the 35 GNoME phases A-Lab reported as successfully made, 22 have experimentally reported disordered parents (found by the framework or by Leeman et al.). The framework alone finds 21, or 60%.
  - It also recovers parents for 3 cases where Leeman et al. had only suspected disorder, for example K2TiCr(PO4)3.
  - In a 50,000-entry sample of GNoME stable structures, the disorder-parent share is only 0.73% and the order share 0.40%. MP-20 gives 23.27% and Alex-MP-20 3.75%. The authors say this "should not be interpreted as evidence that computational structures are intrinsically less prone to disorder" and attribute it to ICSD's incomplete coverage of exotic chemistries.
  - Symmetry-agnostic generative models produce children of known disordered parents 2-4 times more often than symmetry-constrained models.

**A9. Nguyen, D., Cao, K., Chu, B., Lemoff, N., Kienzle, P. & Ratcliff II, W.** "Computed materials proposals depart from the structural memory of experimental discovery." arXiv:2606.30967, 29 Jun 2026. Submitted to npj Comput. Mater. Preprint. [READ, HTML full text] — [arXiv](https://arxiv.org/abs/2606.30967)
- Claim: they embed 167,500 ICSD entries in a structural-similarity space and find that 82.9% of new experimental formulas enter pre-existing structural communities. They then project a 5,000-CIF sample of the public GNoME release into these frozen historical maps.
- GNoME lands "in basin" at 26.6% (1990 map) and 36.4% (2010 map), statistically indistinguishable from MP-theoretical entries (28.8% and 35.8%). Held-out ICSD lands in basin at 52.0-60.6%. The ordering is held-out ICSD > MatterGen > {GNoME ≈ MP-theoretical} > JARVIS > Alexandria.
- 0.0% of the GNoME sample shares a reduced formula with any post-1980 ICSD entry. The authors say this "quantifies one aspect of the Cheetham and Seshadri critique" (high-element-count compositions such as Dy5HoAl24Os5Pd2Pt).
- Note that this cuts the other way from A3. It treats GNoME as structurally far from experimental basins and compositionally new, whereas A3 finds GNoME geometrically close to known prototypes. The two use different metrics: A3 measures local atomic geometry, A9 measures community membership in a 32-dimensional embedding.

**A10. Zhang, X., Lee, S. B., Chatterjee, S., ..., Widdowson, D. E., ..., Kurlin, V. A., Wilson, S. D., Bernevig, B. A. & Schoop, L. M. (17 authors).** "New Crystal Structures Hide in Plain Sight: A Stress Test for AI-Guided Materials Discovery." arXiv:2603.05613; v1 5 Mar 2026, v2 18 Jun 2026. Preprint. [ABSTRACT] — [arXiv](https://arxiv.org/abs/2603.05613)
- Claim: AI models "have so far produced new chemical compositions within known structural families rather than genuinely new structures."
- Evidence: the authors report GdNiSn4 and LuNiSn4, a new structure type found by exploratory synthesis. MatterGen and DiffCSP++ fail to recover it within matching tolerance under their sampling budget.
- Relevance: this paper tests generative models, not GNoME directly, but it belongs to the Schoop/Kurlin critique line.

**A11. Song, Z. & Cheng, L.** "Autonomous discovery of new structure-plausibility laws for explainable and rapid crystal diagnosis and screening." arXiv:2609.01209, 1 Sep 2026. Preprint. [ABSTRACT] — [arXiv](https://arxiv.org/abs/2609.01209)
- Claim: agent-derived "Plausibility Rules for Inorganic Structures" (PRIS) explain "why GNoME remains enriched in rare low-symmetry structures". This independently echoes the space-group finding in A1.

**A12. Kurlin group's earlier peer-reviewed work, cited in A3 but not opened here.** [SECONDARY]
- Anosova, O., Kurlin, V. & Senechal, M. "The importance of definitions in crystallography." *IUCrJ* 11, 453-463 (2024). According to A3, its Table 1 already reported the 2,311 text-identical GNoME1 CIFs and a group of 9 CIFs with the same geometry but swapped elements. This is apparently the first published duplicate count for GNoME.
- Widdowson, D. & Kurlin, V. "Geographic-style maps with a local novelty distance help navigate in the materials space." *Sci. Rep.* 15, 27588 (2025). It introduces the Local Novelty Distance (LND) and applies it to the 43 A-Lab products.
- Widdowson, D. & Kurlin, V. "Pointwise distance distributions for detecting near-duplicates in large materials databases." *SIAM J. Appl. Math.* 86, 898-918 (2026).

**A13. Press coverage of the GNoME critique, 11 Apr 2024.** News. [READ]
- Sources: [404 Media, J. Koebler, "Is Google's AI Actually Discovering 'Millions of New Materials?'"](https://www.404media.co/google-says-it-discovered-millions-of-new-materials-with-ai-human-researchers/); [The Register, T. Claburn, "Boffins deem Google DeepMind's material discoveries rather shallow"](https://www.theregister.com/2024/04/11/google_deepmind_material_study/)
- Palgrave to 404 Media: "In the DeepMind paper there are many examples of predicted materials that are clearly nonsensical ... compounds like H2O11 (which is a Deepmind prediction) do not look right ... basic quality control has not happened."
- Cheetham: "the Google paper falls way short in terms of it being a useful, practical contribution to the experimental materials scientists."
- Seshadri: "we actually think that Google has missed the mark here."

**A14. Robert Palgrave and Leslie Schoop on X/Twitter, from about 30 Nov 2023.** Social media, not peer-reviewed. [SECONDARY: search snippets; X pages not opened] — [Palgrave, 8 Jan 2024](https://twitter.com/Robert_Palgrave/status/1744383962913394758); [Schoop Lab, 8 Jan 2024](https://twitter.com/SchoopLab/status/1744391934024491181)
- Palgrave's initial thread disputed the A-Lab pyrochlore and other assignments; this prompted Ceder's response (C3).
- 8 Jan 2024: the two groups announced their joint ChemRxiv analysis. Schoop wrote: "compositional disorder in materials cannot be neglected."

### Inferences
- The central technical critique, that GNoME and A-Lab predictions are ordered approximants of disordered or known phases, has been independently reproduced by four different methods: expert crystallographic search (A1, A2), ML disorder classification (A7, 80-84% of GNoME), group-subgroup symmetry matching (A8, 60% of A-Lab GNoME targets), and continuous geometric invariants (A3). That convergence makes it the most robust finding in the literature.
- The October 2026 audit's headline numbers need careful reading:
  - "Over 60%" (actually 62.8-78.4%) is geometric closeness, at 0.05 Å, to some known crystal regardless of chemistry. It quantifies prototype reuse, not duplication of known compounds. True chemical duplicates of known crystals are 0.15-0.37%.
  - Within GNoME, exact geometric duplicates are 0.44% (GNoME1) and 0.06% (GNoME2). Near-duplicates are 12-15% only at the loose 0.01 Å tolerance.
  - A summary saying "most GNoME structures are duplicates" would therefore overstate the paper.
- A3 shows that DeepMind's silent dataset revisions removed most known-ordered matches (92.7%) but left most disordered-parent matches. This is consistent with A7 and A8: the remaining "novelty" problem is specifically disorder.
- A9 and A3 are not contradictory. They measure different things (local geometry versus embedding-space community), and both support the view that GNoME is substitution-heavy and compositionally exotic: many elements per compound, about 20% containing radioactive elements.

### Gaps
- I could not read the body of the C&EN 15 Oct 2026 article, so I cannot confirm which exact percentages C&EN printed for within-GNoME near-duplicates and for overlap with MP and ICSD. The arXiv paper's own figures are given above.
- The full text of Anosova, Kurlin & Senechal (IUCrJ 2024) and of Widdowson & Kurlin (Sci. Rep. 2025) was not opened. Their dates and numbers come from citations in arXiv:2610.13885.
- I did not open Palgrave's X threads directly. I found no separate peer-reviewed Palgrave or Schoop paper on GNoME itself (as opposed to A-Lab); the closest are A2 and A10.
- The exact type-(2) count in Leeman et al. is truncated in my extraction and reads as "8/3…".
- I did not find any formal Matters Arising or comment published in Nature against either paper.

## Q2 (B). Supporting/confirming evidence and downstream uses

### Takeaway
Direct experimental confirmation of individual GNoME predictions published since 2023 is sparse. I found one dedicated synthesis paper (MnFeCo4Si2, JMMM 2026), one DeepMind-co-authored synthesis campaign (Cs chlorides, JACS 2024), and one GNoME-derived target in a 2025 synthesizability pipeline (Nd3BTeO9). Critics have argued that at least two of these were not new. The original paper's own validation remains its 736 ICSD matches and its 91% structure agreement on 2,202 later-added MP compositions. Downstream use is extensive but almost entirely computational:
- Energy-GNoME (more than 33,000 energy candidates)
- Mg and Na battery cathode screens
- superconducting-hydride and LLM-based superconductor screens
- work-function screens
- synthesizability filters
- benchmarks for generative models
- Matbench Discovery, where GNoME's potential scores F1 0.81-0.83.

I found no evidence that GNoME's DFT training data was used to train MatterSim, Orb, MACE-OMat or UMA. That data was never released.

### Cited Findings

**B1. Original paper's validation claims (Merchant et al., Nature, 29 Nov 2023).** Peer-reviewed. [READ, Nature full text] — [Nature](https://www.nature.com/articles/s41586-023-06735-9)
- "Of the experimental structures aggregated in the ICSD, 736 match structures that were independently obtained through GNoME." Six examples appear in Fig. 1c; details are in Supplementary Note 1.
- "Of the 3,182 compositions added to the Materials Project since the snapshot, 2,202 are available in the GNoME database and 91% match on structure."
- Scale claims: 2.2 million structures "stable with respect to the Materials Project", of which "381,000 entries live on the updated convex hull as newly discovered materials", for a total of 421,000 stable crystals.
- Application screens:
  - Layered materials: about 52,000 with GNoME, versus about 1,000 stable relative to MP before.
  - "528 promising Li-ion conductors ... a 25 times increase".
  - 15 extra Li/Mn transition-metal oxide candidates.
- Interatomic potentials were tested on 623 compositions the models had never seen.
- All candidates derive from database snapshots taken in March 2021 (MP) and June 2021 (OQMD).

**B2. Google DeepMind blog, "Millions of new materials discovered with deep learning" (A. Merchant & E. D. Cubuk), 29 Nov 2023.** Company blog. [READ] — [DeepMind blog](https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/)
- "We share the discovery of 2.2 million new crystals – equivalent to nearly 800 years' worth of knowledge."
- "External researchers in labs around the world have independently created 736 of these new structures experimentally in concurrent work."
- "We will be contributing 380,000 materials that we predict to be stable to the Materials Project."
- Promises 52,000 graphene-like layered compounds and 528 Li-ion conductors.
- No correction or update note appears on the page as of 22 Oct 2026.

**B3. Miura, A., Aykol, M., Cubuk, E. D., Merchant, A., Batzner, S., Kohli, P. et al. (with Hokkaido U., Hiroshima U., JASRI/SPring-8, Kyoto U. and AIST).** "Efficient Exploratory Synthesis of Quaternary Cesium Chlorides Guided by In Silico Predictions." *J. Am. Chem. Soc.* 146, 29637ff. Published 16 Oct 2024. DOI 10.1021/jacs.4c10294. Peer-reviewed; DeepMind-co-authored. [ABSTRACT/PARTIAL via the JST press release; paper not opened] — [JST press release, 21 Oct 2024](https://www.jst.go.jp/pr/announce/20241021/index.html)
- Claim (JST, in Japanese): large-scale first-principles predictions, rapid in-situ synchrotron XRD screening, then neutron and electron diffraction led to "three new cesium chlorides".
- A DeepMind conference talk ([SEMI SMC 2024, Aykol](https://www.semi.org/sites/semi.org/files/2024-10/SMC2024_5.3_Muratahan%20Aykol_GoogleDeepMind.pdf), not opened) describes it as in-situ experiments driven by GNoME-predicted stabilities. [SECONDARY]
- Counterpoint: Widdowson et al. (A3) quote the paper as searching "the combined zero-temperature convex hull of crystals from Materials Project, OQMD, and GNoME". They report that its successfully made Cs2LiCrCl6, Cs2LiFeCl6, Cs2LiIrCl6, Cs2LiRhCl6, Cs2LiRuCl6 and Cs2NaDyCl6 are not in GNoME1 or GNoME2, and that Cs2LiVCl6 (impure) is a near-duplicate of known structures.
- Conflict: the press release says three new compounds, while A3 lists six successful compositions plus one impure one. The two may be counting different things (new versus successfully made); unresolved.

**B4. Naganuma, S. & Kitagawa, J.** "Experimental investigation of magnetic properties of MnFeCo4Si2 discovered by GNoME." arXiv:2603.22748, 24 Mar 2026; "to appear in J. Magn. Magn. Mater." (cited in A3 as JMMM 174056, 2026). Peer-reviewed journal version. [ABSTRACT] — [arXiv](https://arxiv.org/abs/2603.22748)
- Claim: "Consistent with the GNoME prediction, MnFeCo4Si2 [mp-3203253] crystallizes in a rhombohedral structure with a single-phase nature." It is a soft ferromagnet with Curie temperature 1039 K. The paper notes that MP lists 45,608 GNoME compounds as stable.
- Counterpoint: A3 reports that the GNoME entry has an ICSD near-duplicate (675046, deposited 2018) at EMD about 0.022 Å.

**B5. Prein, T., O'Leary, W., Savvidou, A. F., Bourneix, E., Laulainen, J. E. M. et al.** "A Synthesizability-Guided Pipeline for Materials Discovery." arXiv:2511.01790, 3 Nov 2025. Preprint. [READ, HTML full text] — [arXiv](https://arxiv.org/abs/2511.01790)
- Method: a compositional plus structural synthesizability score applied to about 4.4 million candidates from MP, GNoME and Alexandria, followed by experiments on 16 high-scoring targets completed in three days.
- Results:
  - The target was made in 7 of 16 cases (44%), a known or predicted polymorph in 2 (12%), and 7 failed (44%).
  - Of the 9 hits, 3 were nearly identical to structures already in MP/ICSD listed as synthesized, and 3 more had similar ICSD structures although MP labelled them theoretical.
  - Only 3 had no ICSD structure. One of these is the GNoME-derived Nd3BTeO9, made at near-full purity (P63; a = 8.761 Å, c = 5.553 Å; isostructural with Bi3BTeO9). A 2023 paper had already reported its synthesis without a CIF.
- Their PCA analysis finds GNoME concentrated in narrow regions of composition space, with mean synthesizability falling where GNoME density is highest.

**B6. De Angelis, P., Trezza, G., Barletta, G., Asinari, P. & Chiavazzo, E.** "Energy-GNoME: A Living Database of Selected Materials for Energy Applications." arXiv:2411.10125, 15 Nov 2024. *Energy and AI* (2025), DOI 10.1016/j.egyai.2025.100605. Peer-reviewed. [ABSTRACT] — [arXiv](https://arxiv.org/abs/2411.10125)
- Starting from GNoME's "over 380,000 novel stable crystals", ML and DL classifiers and regressors identify "over 33,000 materials with potential as energy materials" as thermoelectric, cathode or perovskite candidates, with predicted zT, band gap and voltage.
- A search summary says the journal version reports about 38,500 candidates. [SECONDARY]
- Computational only.

**B7. Alghamdi, N., de Angelis, P., Asinari, P. & Chiavazzo, E.** "Screening novel cathode materials from the Energy-GNoME database using MACE machine learning force field and DFT." arXiv:2511.22504; v1 27 Nov 2025, v2 9 Feb 2026. Preprint. [ABSTRACT] — [arXiv](https://arxiv.org/abs/2511.22504)
- Uses foundational MACE MLFF plus DFT+U to screen Energy-GNoME for Na-, K-, Mg- and Ca-ion cathodes. Computational.

**B8. Chen, W., Lin, Z., Zhang, X., Zhou, H. & Zhang, Y.** "AI-Driven Accelerated Discovery of Intercalation-type Cathode Materials for Magnesium Batteries." arXiv:2412.11032, 15 Dec 2024. *J. Energy Chem.* 108, 40-46 (2025), DOI 10.1016/j.jechem.2025.03.085. Peer-reviewed. [ABSTRACT] — [arXiv](https://arxiv.org/abs/2412.11032)
- A CGCNN voltage model applied to 15,308 stable Mg compounds from MP and GNoME found 160 with voltage above 3.0 V and capacity above 800 Ah/L. NequIP molecular dynamics then selected 23 with high Mg conductivity. Computational.

**B9. Akter, S., Faruque, M. O. & Momeni, M. R.** "At-Scale Discovery of High-Voltage Cathode Active Materials for Na-Ion Batteries ..." arXiv:2605.27229; v2 3 Oct 2026. Preprint. [ABSTRACT] — [arXiv](https://arxiv.org/abs/2605.27229)
- Builds the NaCAM-Atlas, with 14,843 Na cathode candidates above 3 V, from MP, AFLOW, OQMD and GNoME hosts. Computational.

**B10. Sanna, A., Cerqueira, T. F. T., Cubuk, E. D., Errea, I., Fang, Y.-W. et al.** "Search for thermodynamically stable ambient-pressure superconducting hydrides in GNoME database." arXiv:2508.19781 (v3 17 Mar 2026). *Commun. Phys.* 9, 94 (2026), DOI 10.1038/s42005-026-02552-4. Peer-reviewed; DeepMind co-author (Cubuk). [ABSTRACT] — [arXiv](https://arxiv.org/abs/2508.19781)
- An ML pre-screen followed by ab initio Eliashberg-level calculations on the thousands of GNoME hydrides found 25 cubic hydrides with Tc above 4.2 K, with a maximum of 17 K. They are "likely to be experimentally accessible". No synthesis reported.

**B11. Itani, S., Zhang, Y., Itani, R. & Zang, J.** "Large Language Models for Superconductor Discovery." arXiv:2512.10847, 11 Dec 2025. Preprint. [ABSTRACT] — [arXiv](https://arxiv.org/abs/2512.10847)
- A fine-tuned LLM Tc predictor, trained on 78,203 literature records, flagged GNoME materials with predicted Tc above 10 K. The authors call these candidates "unverified".

**B12. Meng, J., Jacobs, R., Kapadia, R. & Booske, J.** "Accelerated Discovery of Materials with Extreme Work Functions ..." arXiv:2608.11062, 11 Aug 2026. Preprint. [ABSTRACT] — [arXiv](https://arxiv.org/abs/2608.11062)
- Screened 5.5 million GNoME and Alexandria compounds and found 136 unique materials with work function below 2.0 eV and 172 above 6.0 eV. Computational.

**B13. Xin, Y., Liu, P., ..., Wang, Y. & Ma, Y.** "Bridging Theory and Experiment in Materials Discovery: Machine-Learning-Assisted Prediction of Synthesizable Structures." arXiv:2505.09161, 14 May 2025. Preprint. [ABSTRACT] — [arXiv](https://arxiv.org/abs/2505.09161)
- Of 554,054 GNoME candidates, 92,310 were filtered as likely synthesizable.
- A search snippet says the paper notes 17 GNoME structures were recently synthesized, based on ICSD comparison. [SECONDARY; not verified in the full text]

**B14. Kim, S., Jeon, G., Hwang, S., Lee, J., Jung, J., Han, S. & Kang, S.** "Are diffusion models ready for materials discovery in unexplored chemical space?" arXiv:2510.09406 (v3 2 Feb 2026). *Patterns* (2026), DOI 10.1016/j.patter.2026.101537. Peer-reviewed. [ABSTRACT] — [arXiv](https://arxiv.org/abs/2510.09406)
- Uses GNoME as a benchmark of "uncommon" chemical space, with many rare-earth compositions and unconventional stoichiometries. MatterGen and DiffCSP are "less effective" there than on oxide and nitride sets.

**B15. Liu, M. & Meng, S.** "Recent Breakthrough in AI-Driven Materials Science: Tech Giants Introduce Groundbreaking Models." arXiv:2402.05799, 8 Feb 2024. *Mater. Futures* 3, 027501 (2024), DOI 10.1088/2752-5724/ad2e0c. Peer-reviewed commentary. [ABSTRACT] — [arXiv](https://arxiv.org/abs/2402.05799)
- "A close look of Google's GNoME inorganic materials dataset ... and 11 things you would like to know." Mixed and expository.

**B16. Matbench Discovery benchmark entry "NequIP-GNoME" (model key gnome).** Added to the benchmark 3 Feb 2024 (PR #84). Benchmark leaderboard, not peer-reviewed itself; the Matbench Discovery paper is arXiv:2308.14920. [READ, model YAML] — [matbench-discovery gnome.yml](https://github.com/janosh/matbench-discovery/blob/main/models/gnome/gnome.yml); [leaderboard](https://matbench-discovery.materialsproject.org/)
- Full test set: F1 0.81, DAF 4.81, precision 0.825, recall 0.796, accuracy 0.936, MAE 0.034 eV/atom, RMSE 0.083, R² 0.786, with 1,744 missing predictions.
- Unique prototypes: F1 0.829, DAF 5.523, precision 0.844, accuracy 0.948, MAE 0.035 eV/atom.
- Model: 16.24 million parameters; training set "GNoME".
- Note in the YAML: "The model weights and training set are unpublished."
- A search snippet says current leaders are around F1 0.92-0.93 (PET-OAM-XL, eSEN-30M-OAM). [SECONDARY]
- DeepMind's 404 Media statement cited MP finding GNoME "top-of-the-line when compared to other machine learning models", which refers to this benchmark (A13).

**B17. Training of later universal MLIPs (MatterSim, Orb, MACE-OMat, UMA).** [SECONDARY: search-result summaries of reviews and tutorials; model cards not opened]
- MatterSim used about 17 million structures from MP, Alexandria and its own DFT.
- Orb v2 used MPtrj and Alexandria; Orb v3 used OMat24.
- MACE-MP-0 used MPtrj; MACE-MPA-0 used MPtrj and sAlex; MACE-OMAT-0 used OMat24.
- UMA uses OMat24 and other Meta datasets.
- I found no source saying any of these used GNoME data. Given that the GNoME training set is unreleased (B16), the premise that "GNoME data trained MatterSim/Orb/MACE-OMat/UMA" appears false; at most, GNoME's public structures could have been used. GNoME is instead an early demonstrator of scaling MLIP data, and a competitor on Matbench Discovery.

### Inferences
- The "736 independently realized" and "hundreds ... independently synthesized" figures (B1, B2, C7) are retrospective ICSD matches. They are not new syntheses prompted by GNoME. Post-2023 prospective syntheses of GNoME-specific predictions number only a handful (B3, B4, B5), and each has a published novelty objection (A3, B5's own ICSD analysis).
- Downstream literature mostly treats GNoME as a large candidate pool for further computational screening. These papers implicitly accept GNoME's 0 K stability but rarely address disorder or novelty, and almost none report synthesis.
- DeepMind's own follow-ups (B3, B10, C8) keep promoting GNoME as a discovery source rather than revisiting the novelty claims.

### Gaps
- I did not open the Miura et al. JACS full text, so I cannot reconcile the "three new cesium chlorides" (JST) with the six compositions listed by Widdowson et al.
- I did not systematically check Google Scholar "cited by" for the GNoME paper (about 1,820 citations per the Nature page). The B list is drawn from arXiv title and abstract searches for "GNoME" plus targeted searches, so many citing papers are not catalogued.
- I found no experimental confirmation of GNoME-predicted superconductors, Li-ion conductors from the 528 list, or layered materials from the 52,000 list.
- I could not verify the Supplementary Note 1 list behind the 736 matches, or whether any independent group has audited it.

## Q3 (C). Official responses, corrections, dataset updates, and whether GNoME itself was corrected

### Takeaway
- The only formal correction is the A-Lab Author Correction (Nature, 19 Jan 2026, DOI 10.1038/s41586-025-09992-y). It:
  - reframes "novel" as "new to the prediction platform, not necessarily new to science";
  - confirms 36 of 40 reported successes on manual re-analysis, with 4 inconclusive and removed;
  - drops Zn2Cr3FeO8, which had been in the training data.
- The GNoME Nature paper has no correction, editor's note or change history as of 22 Oct 2026. The claim of a "January 2026 Nature correction to GNoME" confuses it with the A-Lab correction, which GNoME's lead authors Merchant and Cubuk co-signed.
- DeepMind's public response has been "We stand by all claims" (April 2024), followed by silence to C&EN (October 2026), while the dataset was silently revised (December 2023, August 2024, November 2024).
- Materials Project has incorporated about 117,000 r2SCAN-recomputed GNoME materials as of June 2026.

### Cited Findings

**C1. Szymanski, N. J., Rendy, B., Fei, Y., Kumar, R. E., He, T., Milsted, D., McDermott, M. J., Gallant, M., Cubuk, E. D., Merchant, A., Kim, H., Jain, A., Bartel, C. J., Persson, K., Zeng, Y. & Ceder, G.** "Author Correction: An autonomous laboratory for the accelerated synthesis of inorganic materials." *Nature* 650 (8100), E1. Published 19 Jan 2026. DOI 10.1038/s41586-025-09992-y; PMID 41554984; PMCID PMC12872444. Peer-reviewed correction; the re-analysis was "peer-reviewed post-publication". [READ: full text via Europe PMC XML. The NCBI PMC page returned a reCAPTCHA; the Nature article page confirms the correction date] — [Europe PMC PMC12872444](https://europepmc.org/article/PMC/PMC12872444); [DOI](https://doi.org/10.1038/s41586-025-09992-y)
- Exactly what the correction says was changed:
  1. "Following publication of this article, concerns were raised about the unambiguous identification of the compound structures using diffraction as well as the original claims of material novelty."
  2. "We acknowledge that the original claims of material novelty were subject to misinterpretation—their intention was to indicate that the materials were new to the prediction platform, not necessarily new to science. The article text has been updated to reflect this in the HTML and PDF versions." An annotated PDF of the textual changes is in the Supplementary Information.
  3. "We have manually re-analyzed the diffraction patterns and have confirmed that the prediction platform came to the correct conclusion in 36 of its 40 reported successes, with 4 compounds being inconclusive. This re-analysis was peer-reviewed post-publication."
  4. "The total number of compounds successfully made by the platform has now been updated to exclude four target materials whose presence is inconclusive from XRD alone."
  5. "We have also removed one compound from the discussion (Zn2Cr3FeO8) that was mistakenly included in the training data."
  6. Fig. 2, the SI and the Supplementary Data were updated, with edits shown in accompanying PDFs. "Nature thanks the correspondents who brought these issues to our and the authors' attention, and the reviewers who assessed the re-analyzed PXRD data post-publication."
- Widdowson et al. (A3) describe the correction as "crossing out almost all the words 'novelty' and 'discovery'". That is a critic's description of the annotated PDF, which I did not open.

**C2. Correction status of the GNoME Nature paper.** [READ: Nature article pages fetched 22 Oct 2026] — [GNoME article](https://www.nature.com/articles/s41586-023-06735-9); [A-Lab article](https://www.nature.com/articles/s41586-023-06734-w)
- The GNoME page shows "Nature volume 624, pages 80–85 (2023)", 436k accesses, 1,820 citations and an Altmetric score of 1,228. It contains no "Correction", "Author Correction", "Editor's Note" or "Change history" text; the string "correction" occurs zero times in the page text.
- The A-Lab page shows "An Author Correction to this article was published on 19 January 2026. This article has been updated" and "Change history 19 January 2026". It also shows 310k accesses and 1,242 citations.
- Verdict: the GNoME paper has received no correction or editor's note as of 22 Oct 2026. The secondary claim of a January 2026 GNoME correction walking back novelty is a misattribution of C1.

**C3. Ceder, G.** "Regarding our recent A-Lab article." LinkedIn, 2 Dec 2023. The Ceder group's response; not peer-reviewed. [READ] — [LinkedIn](https://www.linkedin.com/pulse/regarding-our-recent-a-lab-article-gerbrand-ceder-0sz6c)
- Restates the result: "For the 58 compounds targeted in the study, the A-Lab successfully produced 41 of the materials."
- Defends the five MxSb4-xPb4O13 pyrochlores (M = Hf, Zr, Sn, Fe, In) against Palgrave's claim that they were Sb2Pb2O7. The evidence offered is new SEM/EDS maps showing the M cations retained and uniformly distributed, and XRD peak shifts that correlate with Shannon ionic radius.
- On the automated Rietveld fits: "We have no doubt that a human can perform a higher-quality refinement ... it was our objective to show what an autonomous laboratory can achieve."
- On novelty: "MnAgO2 and Mg3Ni3MnO8 are not 'new'. We agree with this assessment." They were absent from the older ICSD version the team checked against, but had been reported before. "We will certainly update the published paper."
- Framing: the A-Lab handles the early exploratory stage, and "a human in the loop is still required."
- Leeman et al. (A2) argue that this EDS and peak-shift evidence is also consistent with known disordered Pb–Sb–M pyrochlores (Cascales et al., 1985-86).

**C4. Peplow, M.** "Robot chemist sparks row with claim it created new materials." *Nature* News, 12 Dec 2023; updated 9 Jan 2024. News, paywalled. [ABSTRACT/PARTIAL] — [Nature News](https://www.nature.com/articles/d41586-023-03956-w)
- The 9 Jan 2024 update notes the Palgrave/Schoop preprint (ChemRxiv 10.26434/chemrxiv-2024-5p9j4).

**C5. Google DeepMind statements to press.**
- 11 Apr 2024, to The Register and 404 Media: "We stand by all claims made in Google DeepMind's GNoME paper. ... Our GNoME research represents orders of magnitude more candidate materials than were previously known to science, and hundreds of the materials we've predicted have already been independently synthesized by scientists around the world." [READ] — [The Register](https://www.theregister.com/2024/04/11/google_deepmind_material_study/); [404 Media](https://www.404media.co/google-says-it-discovered-millions-of-new-materials-with-ai-human-researchers/)
- 404 Media paraphrase (not a direct quote): Google said that criticisms such as known structures with different elements reflected choices made "by design".
- 15 Oct 2026, C&EN: the subtitle says DeepMind "doesn't comment on inquiries about lack of novelty". [ABSTRACT/PARTIAL] — [C&EN](https://cen.acs.org/research-integrity/Google-DeepMind-structures-near-duplicates-questionable/104/web/2026/10)
- I could not verify the reported quote "the dataset was released for community study" in any source I opened. Closest wording: the README says "Please help by exploring the structures and let us know what you think!" and the blog says "We've made GNoME's predictions available to the research community."

**C6. GNoME dataset release notes** (google-deepmind/materials_discovery, DATASET.md "Versioning" and README, read 22 Oct 2026). [READ] — [DATASET.md](https://github.com/google-deepmind/materials_discovery/blob/main/DATASET.md); [README](https://github.com/google-deepmind/materials_discovery)
- 11/29/23: "Initial dataset release".
- 12/1/23: "Re-introduce paper filters to remove un-physical energies; add 2 missing columns ('Dimensionality Cheon' and 'Is Train')".
- 8/21/24: "Adjust threshold to 1meV/atom off the hull significantly increasing the number of released crystals, update to use 'require_bound' version of MP corrections, re-relax structure where VASP did not update lattice coordinates, provide convex hull entries from recomputations of MP / OQMD / ..."
- 11/21/24: "Ensure consistency in formation energies, provide used elemental references + pseudopotential corrections used in the GNoME paper".
- There are no later entries, and no note on withdrawn entries. A3 counts 83,525 removed and 252,641 added between Nov 2023 and Nov 2024.
- The README still says "share the discovery of 381,000 novel stable materials". It adds: "As of August 2024, we have expanded the dataset to release all materials measured to be within 1 meV/atom from the convex hull ... for a total of >520,000 materials" (A3 counts 554,054).
- Caveats in the files: "as more crystals are discovered by the scientific community, the above set may not remain stable"; and for the r2SCAN set, "not all released materials remain stable according to this metric."
- Model notes: the GNoME model was trained on a 2018 MP snapshot (21 meV/atom), and a NequIP JAX implementation is provided.

**C7. Materials Project's incorporation of GNoME** (docs.materialsproject.org "Database Versions", read 22 Oct 2026). [READ] — [MP Database Versions](https://docs.materialsproject.org/changes/database-versions)
- November 2023: an initial 2,047 GNoME-originated materials in the "GNoME Explorer". Cheetham & Seshadri cite the same number.
- v2024.11.14 (live 12 Dec 2024): "The current set of 2,047 GNoME-originated materials has been deprecated in preparation for a release of about 120,000 GNoME materials."
- v2024.12.18 (live 20 Dec 2024): "Added 15,483 GNoME-originated materials calculated using r2SCAN". From this release, users must explicitly accept the BY-NC licence to access GNoME data. "A further release of an additional ~100k GNoME materials is in preparation."
- v2025.04.10 (live 18 Apr 2025): "Added 30,00 [sic, presumably 30,000] GNoME-originated materials calculated using r2SCAN".
- MatSci forum, 1 May 2025: GNoME Explorer listed 45,608 materials. Aaron Kaplan (MP): "~119,000 GNoME materials that were initially determined to be stable with the r2SCAN meta-GGA. The remaining ~73k materials will be released in an upcoming database update. These 119k materials are a subset of the 381k." — [matsci.org](https://matsci.org/t/number-of-materials-in-gnome-explorer/63304)
- v2026.04.13 (posted to S3 13 Apr 2026; live 8 Jun 2026): "Added 74,052 new GNoME materials computed at the r2SCAN level of theory. This brings the total to 117k GNoME materials. A future release will be dedicated to the final bulk release of the remaining GNoME materials."
- v2026.09.28 (live 19 Oct 2026): no new GNoME content.
- The figure of "~520k within 1 meV/atom" belongs to DeepMind's own August 2024 GitHub release, not to MP.

**C8. DeepMind-authored follow-up papers, 2024-2026.**
- Miura et al., JACS, 16 Oct 2024 (B3): Aykol, Cubuk, Merchant, Batzner and Kohli.
- Aykol, M., Merchant, A., Batzner, S., Wei, J. N. & Cubuk, E. D. "Predicting emergence of crystals from amorphous precursors with deep learning potentials." *Nat. Comput. Sci.*, published 18 Dec 2024, DOI 10.1038/s43588-024-00752-y (preprint arXiv:2310.01117, Oct 2023). Peer-reviewed. Uses universal deep-learning potentials of the GNoME/NequIP kind to predict which polymorphs nucleate first from amorphous precursors. [SECONDARY: search summary; not opened] — [PMC11860218](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11860218/)
- Sanna, Cerqueira, Cubuk et al., *Commun. Phys.* 2026 (B10): superconducting hydrides in GNoME.
- The A-Lab Author Correction (C1), co-signed by Cubuk and Merchant.
- I found no DeepMind paper that re-examines or defends GNoME's novelty claims.

### Inferences
- Arithmetic from the correction:
  - The original abstract claimed 41 of 58 targets made, and press coverage counted 43 including partial successes.
  - 40 is plausibly the 41 minus the removed Zn2Cr3FeO8.
  - After removing the 4 inconclusive targets, the platform's count would be 36. On 57 remaining targets that is about 63%, against the original 71%.
  - This is my inference; the correction does not state the new headline count or denominator.
- The correction accepts the critics' novelty point (C1 item 2). It does not concede the disorder point: it says 36 identifications were "correct", without addressing whether those are known disordered phases. That matches the critics' remaining complaint reported by C&EN (A6).
- No correction exists for GNoME. The DeepMind response pattern is: a public defence (April 2024); undocumented dataset curation that removed most known-ordered duplicates (A3); a quiet expansion to more than 520,000 entries (August 2024); then no comment (October 2026).
- Materials Project's r2SCAN gate means only about 117k of the 381k claimed materials (about 31%) had passed MP's r2SCAN-based ingestion as of June 2026. MP's notes do not say whether the rest failed r2SCAN stability or simply have not been processed.

### Gaps
- I did not open the annotated A-Lab PDF or the updated Fig. 2, so the exact revised headline count and the names of the 4 inconclusive compounds are unverified.
- I could not find or verify any DeepMind statement containing "the dataset was released for community study", or any DeepMind comment on the A-Lab correction.
- The C&EN January 2026 and October 2026 article bodies were paywalled.
- MP's notes do not say how many GNoME materials failed r2SCAN stability, as opposed to not yet being processed.
