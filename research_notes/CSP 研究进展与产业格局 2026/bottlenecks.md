# The real bottlenecks of crystal structure prediction (CSP) and AI materials discovery, 2025-2026: from predicted structure to material in hand

Research date: 2026-10-22. Primary sources were read directly wherever possible (arXiv full text and abstracts, the Europe PMC full text of the A-Lab correction, MIT Technology Review, the Periodic Labs blog, PubMed and Crossref metadata). When a finding comes only from a search snippet or a secondary source, it is labelled that way. Measured facts are kept apart from opinion, and opinion is attributed to whoever holds it.

---

## Q1. What do leading reviews, perspectives and critics (2025-2026) say the actual bottleneck is?

### Takeaway
Reviews, critics and practitioners agree. Generating candidate structures is no longer the bottleneck. The hard steps are (a) making the compound, which depends on synthesizability, kinetics and precursors, (b) proving what was made and that it is new, which depends on XRD/phase identification and on disorder, and (c) showing that it is useful, which depends on properties measured outside the 0 K DFT setting. Even the AI-lab founders now say this publicly. Critics add that novelty claims have been inflated by ordered approximants of known disordered phases and by element substitution into known prototypes.

### Cited Findings
**Journalism and practitioners (opinion and reported quotes)**
- MIT Technology Review (David Rotman, 15 Dec 2025, "AI materials discovery now needs to move into the real world", part of the "Hype Correction" package). The author says: "By far the most time-consuming and expensive step in materials discovery is not imagining new structures but making them in the real world." It reports that there has been no "eureka" or ChatGPT-like moment, "no discovery of new miracle materials or even slightly better ones", and that DeepMind's 2023 "millions of new materials" claim "in retrospect, clearly overpromised." — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
  - John Gregoire (Lila Sciences, chief autonomous science officer): "there's zero problems we can ever solve in the real world with simulation alone." Rafael Gómez-Bombarelli (Lila cofounder, MIT): "Structure helps us think about the problem, but it's neither necessary nor sufficient for real materials problems." — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
  - Gerbrand Ceder (A-Lab principal scientist, now CSO at Radical AI): "How it works today and how we envision it are still somewhat different. There's just a lot of tool building that needs to be done." — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
  - Physical realities named in the article: solid-state powder synthesis is "far more difficult to automate than the liquid-handling activities" used in pharma; "Even determining what you've made can be tricky"; GNoME structures were computed at 0 K, and "a number of the so-called novel materials predicted by DeepMind appeared to be well-ordered versions of disordered ones that were already known"; many properties depend on microstructure, which lies beyond atomistic scale. — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
  - Status at the time of the article: Lila's labs were "largely empty" when the reporter visited. Periodic Labs was "starting with manual synthesis guided by AI predictions; its robotic high-throughput lab will come soon." — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
  - The companion newsletter (18 Dec 2025, "Can AI really help us discover new materials?") ends: "for now, I'm calling hype." — [MIT TR newsletter](https://www.technologyreview.com/2025/12/18/1130102/ai-materials-discovery/)
- Periodic Labs (company blog, 15 Sep 2026): learning from physical environments "presents new issues: the number of agents is not elastically scalable ... each experiment can take days, and the results are often ambiguous"; and "The future we seek requires materials no one yet knows how to make." — [Periodic Labs, Building Labs that Learn](https://periodic.com/news/building-labs-that-learn)

**Peer-reviewed critiques**
- Cheetham & Seshadri, Chem. Mater. 36, 3490-3495 (8 Apr 2024), "Artificial Intelligence Driving Materials Discovery? Perspective on the Article: Scaling Deep Learning for Materials Discovery". They found "scant evidence for compounds that fulfill the trifecta of novelty, credibility, and utility." They wrote: "We would respectfully suggest that the work does not report any new materials but reports a list of proposed compounds... a compound can be called a material when it exhibits some functionality." Many entries rely on metal-ion ordering that is unlikely in real materials, and up to about 42k entries contain radioactive elements. — [DOI 10.1021/acs.chemmater.4c00643](https://doi.org/10.1021/acs.chemmater.4c00643); quotes as reproduced in [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/) and [The Stack](https://thestack.technology/scant-evidence-googles-ai-chemistry-claims-were-misleading) (secondary; I did not re-read the full text)
- Leeman, Liu, Stiles, Lee, Bhatt, Schoop, Palgrave, "Challenges in High-Throughput Inorganic Materials Prediction and Autonomous Synthesis", PRX Energy 3, 011002 (7 Mar 2024). They reviewed every A-Lab product and identified four recurring shortfalls. They concluded that no new materials were discovered, that automated Rietveld analysis of PXRD "is not yet reliable", and that about two thirds of the claimed successes were likely known compositionally disordered versions of the predicted ordered compounds. — [UCL Discovery](https://discovery-pp.ucl.ac.uk/id/eprint/10188733); [ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/65957d349138d231611ad8f7) (summary taken from search snippets)
- Juelsholt, Materials Horizons 2026, DOI 10.1039/D6MH00268D (PubMed 42007796; ChemRxiv v3 dated 23 Jan 2026; issue dated June 2026). The persistent challenge is "modelling compounds where multiple elements occupy the same crystallographic site, often leading to misclassification of known disordered phases as new ordered compounds." The paper calls for "rigorous human verification", which, it says, limits these tools' use "for rapid and large-scale prediction of new materials." — [RSC](https://pubs.rsc.org/en/content/articlehtml/2026/mh/d6mh00268d); [PubMed](https://pubmed.ncbi.nlm.nih.gov/42007796/)
- Widdowson, Kurlina, Anosova & Kurlin (arXiv:2610.13885, 9 Oct 2026). If novelty is judged by composition, by CIF text, or by "standard structure matchers based on manually chosen thresholds, one can easily generate millions of 'new' compositions or files without discovering truly novel materials." The authors propose automatically enforced "necessary conditions" before anyone claims a new material, to avoid an "embarrassment of over-prediction." — [arXiv:2610.13885](https://arxiv.org/abs/2610.13885)

**Reviews**
- Choi, Kim, Park, Choi, An & Jung, "AI for Accelerated Materials Discovery: From Generative Design to Autonomous Realization", Chem. Rev. (online 3 Aug 2026). Synthesis planning and self-driving labs (SDLs) are framed as bridging "the persistent gap between the computational design and experimental realization." Database limitations, FAIR data, knowledge graphs and data provenance are listed as critical infrastructure challenges. A search snippet, not verified against the full text, says the review calls the "design-realization gap" perhaps the most significant bottleneck and notes that characterization throughput often cannot keep pace with synthesis. — [DOI 10.1021/acs.chemrev.6c00154](https://doi.org/10.1021/acs.chemrev.6c00154)
- Lambard (NIMS), "Beyond Structure: Revolutionising Materials Discovery via AI-Driven Synthesis Protocol-Property Relationships" (arXiv:2605.00313, 1 May 2026). Structure-centric pipelines "routinely falter when their predictions meet experimental synthesis" because they neglect "kinetics, precursor availability and practical constraints." The paper argues for a "synthesis-first" paradigm. Its often-quoted statistic, "fewer than 2% of over 50,000 low-enthalpy phases identified in high-throughput surveys have been realised", is attributed to Zunger, Nature 566, 447 (2019), "Beware of plausible predictions of fantasy materials". This is a 2019 figure re-cited, not a new 2026 measurement. — [arXiv:2605.00313](https://arxiv.org/html/2605.00313v1)
- Sheng ... Buonassisi (MIT; arXiv:2608.15928, Aug 2026): "Most computationally predicted materials are never synthesized because conventional synthesis optimization is slow, expertise-dependent, and iterative." — [arXiv:2608.15928](https://arxiv.org/abs/2608.15928)
- Guinan ... Spurgeon (PNNL), "Mind the Gap: Bridging the Divide Between AI Aspirations and the Reality of Autonomous Characterization" (arXiv:2502.18604, Feb 2025). The paper treats autonomous characterization, especially electron microscopy, as a distinct gap between promise and practice. — [arXiv:2502.18604](https://arxiv.org/abs/2502.18604)
- A 2025 ScienceDirect review ("Advancing materials discovery through artificial intelligence") is reported in a search snippet as saying that CAMD validated only 1 of 6 predicted oxide phases, and that GNoME's 0 K DFT favours ordered configurations. I did not verify this against the full text. — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2352940725003981)

### Inferences
- Since about 2024, the critique has moved from "the predictions are wrong" to "the claims are wrong". Hull-stable predicted compounds are often plausible, but calling them "new materials" ignores disorder, prototype substitution and the lack of any demonstrated function. By late 2025 the companies (Lila, Periodic, Radical AI) had reorganized around the experimental loop, which concedes the critics' central point.
- Disorder is the most cited technical failure mode across the A-Lab, GNoME and MatterGen critiques. A 0 K ordered supercell of a site-disordered known phase scores as "novel" to any composition- or ordered-structure-based novelty check.

### Gaps
- I did not find 2025-2026 editorials or perspectives on this topic in Nature, Nature Materials, Nature Reviews Materials, Matter or Joule. Searches surfaced reviews in Chem. Rev., arXiv and ChemRxiv instead. Those journal sites need a direct search.
- I found no Ceder, Persson, Jain, Ong, Walsh or Aspuru-Guzik blog post or talk from 2025-2026 with quantified bottleneck statements, apart from the Ceder quotes in MIT TR. I did not verify the Acceleration Consortium reports.

---

## Q2. What fraction of AI-predicted "new materials" have actually been made and confirmed? Quantified follow-ups on GNoME, A-Lab and MatterGen, and the novelty audits

### Takeaway
The verifiable count of genuinely new, AI-predicted inorganic compounds that were made, confirmed and shown to be useful is very small, and no consolidated tally exists. The A-Lab paper was formally corrected on 19 Jan 2026: 36 confirmed out of 57 targets, with "new" redefined as new to the platform. MatterGen's flagship TaCr2O6 has been shown in peer review to be a known 1971 phase that was in its training set. The Oct 2026 invariant-based audit finds the GNoME releases geometrically dominated by known crystals.

### Cited Findings
**A-Lab Author Correction (read in full)**
- Nature 650, E1. Published online 19 Jan 2026, issue dated Feb 2026. DOI 10.1038/s41586-025-09992-y; PMC12872444. It corrects Szymanski et al., Nature 624, 86 (published 29 Nov 2023). — [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12872444/fullTextXML); [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12872444/)
  - Trigger: "concerns were raised about the unambiguous identification of the compound structures using diffraction as well as the original claims of material novelty."
  - Novelty redefined: "the original claims of material novelty were subject to misinterpretation—their intention was to indicate that the materials were new to the prediction platform, not necessarily new to science." The article text was changed in the HTML and PDF, and an annotated PDF of the changes was published.
  - Re-analysis: "we have manually re-analyzed the diffraction patterns and have confirmed that the prediction platform came to the correct conclusion in 36 of its 40 reported successes, with 4 compounds being inconclusive. This re-analysis was peer-reviewed post-publication." The success count now excludes those four XRD-inconclusive targets.
  - Data leak: "removed one compound from the discussion (Zn2Cr3FeO8) that was mistakenly included in the training data."
  - Fig. 2, the Supplementary Information and the Supplementary Data were all updated. Nature thanked "the correspondents who brought these issues to our and the authors' attention."
  - Arithmetic: original claim 41 of 58 (71%), minus Zn2Cr3FeO8, gives 40 of 57, of which 36 were confirmed and 4 inconclusive. That is 36/57 = 63%. NOTE for the report writer: the brief describes "41-of-58" as the preprint figure and "36-of-57" as the published one. The evidence shows instead that 41/58 was the originally published Nature (2023) figure and 36/57 is the post-correction (2026) figure. MIT TR (Dec 2025) still quoted "41 novel materials", before the correction. — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
- C&EN (Dec 2025, "Duplicate structures haunt crystallography databases") reported that critics had called for retraction of the GNoME and A-Lab Nature papers. — [C&EN Dec 2025](https://cen.acs.org/research-integrity/Duplicate-structures-haunt-crystallography-databases/103/web/2025/12) (paywalled; only headline and dek read)

**The Oct 2026 GNoME audit (arXiv:2610.13885, read in full text)**
- Bibliographic details: "Necessary conditions for benchmarking next-generation AI in materials discovery", by Daniel E. Widdowson, Tatiana V. Kurlina, Olga D. Anosova and Vitaliy A. Kurlin (University of Liverpool School of Computer Science and Informatics and Materials Innovation Factory; UCL Mathematics). Submitted 9 Oct 2026, 44 pages. — [arXiv:2610.13885](https://arxiv.org/abs/2610.13885)
- C&EN report: Dalmeet Singh Chawla, 15 Oct 2026, "Google DeepMind AI crystallography database includes near duplicate structures and unrealistic compounds". It reports that Google DeepMind did not comment on the novelty inquiries. — [C&EN Oct 2026](https://cen.acs.org/research-integrity/Google-DeepMind-structures-near-duplicates-questionable/104/web/2026/10) (paywalled; key insights read). Search snippets of the C&EN piece give "over 15%" internal near duplicates, "nearly 25%" duplicating the Materials Project and "just under 17%" resembling ICSD. These match the paper's numbers below exactly.
- Datasets: GNoME1 is the 29 Nov 2023 release with 384,938 entries. GNoME2 is the 21 Nov 2024 release with 554,054 entries. They share 301,413 entries; 83,525 were withdrawn and 252,641 added; the background removal rate is 21.7%. The releases are not nested: 10,201 entries withdrawn on 21 Aug 2024 were restored on 21 Nov 2024. — [arXiv:2610.13885](https://arxiv.org/abs/2610.13885)
- **Exact duplicate percentages** (all from the arXiv paper):
  - **Internal near-duplicates, GNoME2.** Redundancy rate 0.057% at τ=1e-10 Å, 0.129% at 1e-4 Å, 0.207% at 1e-3 Å and **15.178% at τ=0.01 Å**. At 0.01 Å that is 84,092 excess entries, with 108,286 entries in groups of size ≥2 and a largest group of 723. These are geometric, element-blind matches. No geochemical (chemistry-preserving) pairs exist in GNoME2 up to 0.01 Å.
  - **Internal near-duplicates, GNoME1.** Redundancy rate 0.437% at 1e-10 Å and 12.438% at 0.01 Å (geometric; 47,878 excess; largest group 352). Geochemical: 0.306% to 1.156%.
  - **Text-identical CIFs, GNoME1.** 1 quadruple, 43 triples and 1,089 pairs, totalling 2,311 entries, even though the Nature paper stated that pymatgen StructureMatcher deduplication had been applied. Identical geometry with element labels ignored covers 3,248 entries (0.84%). After rounding coordinates to 0.1 Å, 44,238 entries (11.49%) fall in near-duplicate groups. The GNoME2 equivalents are 591 (0.11%) and 60,012 (10.83%).
  - **Against Materials Project** (snapshot up to Mar 2021, the GNoME input date; EMD on PDA[100]). Within 0.02 Å: **GNoME2 24.1%**, GNoME1 21.3%. Within 0.05 Å: 78.4% and 74.8%.
  - **Against ICSD.** Within 0.02 Å: **GNoME2 16.3%**, GNoME1 15.2%. Within 0.05 Å: 73.1% and 69.7%. With pymatgen StructureMatcher RMSD within 0.05 Å: ICSD 66.1% and MP 74.3% for GNoME2. The authors: "over 60% of predictions in GNoMEs 1&2 are geometrically close to known crystals in the ICSD and MP up to 0.05Å". The median GNoME2 entry is 0.034 Å from some ICSD structure, which they attribute to GNoME "tak[ing] existing crystals and relabel[ling] chemical elements with similar ones".
  - **Matches with chemistry preserved are rare.** Only 5.3% of GNoME2 entries share an element set with any ICSD entry, and 0.9% share a composition. Matches on geometry and chemistry together within 0.05 Å: 824 ICSD + 1 MP = 0.15% of GNoME2. For GNoME1: 1,315 ICSD + 155 MP = 0.37%.
  - **Ordered vs disordered known crystals.** Of 559 GNoME1 entries matching a known ORDERED crystal, 92.7% were withdrawn in GNoME2. Of 853 matching a known DISORDERED ICSD crystal, only 40.4% were withdrawn (background 21.7%). GNoME2 still holds 774 entries matching disordered known crystals, against 879 in GNoME1, a 12% drop compared with 89% for ordered matches. The authors infer that DeepMind's filter removed known ordered crystals but "was unable to identify entries matching a disordered ICSD crystal". This is direct quantitative evidence of the ordered-approximant problem.
  - **Radioactive elements.** 80,235 GNoME1 entries (20.8%) and 108,020 GNoME2 entries (19.5%) contain at least one radioactive element (counting Bi, Th and U, which Cheetham and Seshadri's count of about 42k omitted).
- The same group's earlier preprint (arXiv:2406.12894, June 2024) found thousands of GNoME CIF pairs with volumes identical to eight decimal places. Per C&EN, it also found 1,224 exact duplicate pairs (plus triplets and a quadruplet) and argued that more than 10% may be near duplicates. — [arXiv:2406.12894](https://arxiv.org/pdf/2406.12894); [C&EN Dec 2025](https://cen.acs.org/research-integrity/Duplicate-structures-haunt-crystallography-databases/103/web/2025/12) (the counts come via search snippet; the 2026 paper gives 1,089 pairs + 43 triples + 1 quadruple for text-identical CIFs)

**The GNoME "736" and later counts**
- DeepMind's 2023 claim was that 736 GNoME structures had been independently realized experimentally (matched to ICSD), along with 380k "stable" structures out of 2.2M. — [DeepMind blog](https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/); [Nature 2023](https://www.nature.com/articles/s41586-023-06735-9)
- Per MIT TR (Dec 2025), DeepMind says it "has been working with scientists in labs around the world to synthesize AI-identified compounds and has achieved some success". No number was given. — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
- Xin ... Ma (arXiv:2505.09161, May 2025) flagged 92,310 of 554,054 GNoME candidates (about 17%) as highly synthesizable by their ML model. This is a prediction, not a synthesis count. — [arXiv:2505.09161](https://arxiv.org/abs/2505.09161)
- Prein et al. (arXiv:2511.01790, Nov 2025) screened unsynthesized Materials Project, GNoME and Alexandria entries with a synthesizability score and attempted 16 targets. **7 of 16 (44%)** were synthesized; the experimental process took 3 days. They also found "omissions in lists of known synthesized structures", meaning some "unsynthesized" entries are in fact known. — [arXiv:2511.01790](https://arxiv.org/abs/2511.01790)
- Nguyen ... Ratcliff (NIST; arXiv:2606.30967, Jun 2026) embedded 167,500 ICSD entries in a structural-similarity space. Experimentally, 82.9% of new formulas enter existing structural communities, and the rate of new-community formation fell from 40.2% in the 1930s to 2.6% in the 2010s. All computed sets depart from experimental basins, ranked held-out ICSD > MatterGen > {GNoME ≈ MP-theoretical} > JARVIS > Alexandria. — [arXiv:2606.30967](https://arxiv.org/abs/2606.30967)
- Vepa (arXiv:2606.23725, Jun 2026; single-author preprint, low weight) found that an exact-composition check of 500 random GNoME entries against COD matched 0 of 500. The author cautions that this "measure[s] our coverage as much as GNoME's novelty". — [arXiv:2606.23725](https://arxiv.org/abs/2606.23725) (the 0/500 figure comes via search snippet)

**MatterGen TaCr2O6**
- Microsoft and Zeni et al. predicted ordered TaCr2O6, synthesized it as disordered Ta1/3Cr2/3O2, and reported a bulk modulus of 169 GPa against a 200 GPa target. — [Microsoft Research blog](https://www.microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai/)
- Juelsholt (Materials Horizons 2026) concludes that the product "is not a novel compound but is identical to the previously reported Ta1/2Cr1/2O2, first described in 1971 and included in MatterGen's training dataset." — [PubMed 42007796](https://pubmed.ncbi.nlm.nih.gov/42007796/); [RSC](https://pubs.rsc.org/en/content/articlehtml/2026/mh/d6mh00268d)
- I found no Microsoft rebuttal or correction.

### Inferences
- The 15-25% figures from the Oct 2026 audit use thresholds of 0.01-0.02 Å on element-blind geometric invariants. They measure prototype reuse (element substitution into known structure types), not literal rediscovery. Literal chemistry-preserving rediscovery is 0.15-0.37%. The report should present both numbers: GNoME is largely "known structure types with new element labels", while literal duplicates of known compounds are few and were mostly curated out between releases. The exception is the ordered approximants of disordered phases, which the curation missed.
- The GNoME ICSD comparison uses a pre-March-2021 snapshot, so it cannot count compounds synthesized afterwards. No one has published a definitive "fraction made" for GNoME.
- Across GNoME/A-Lab, MatterGen and the Prein pipeline, the realistic hit rate for "targeted, synthesized, XRD-confirmed" sits between 44% and 63% for curated targets. "Novel to science and functional" is a much smaller, unquantified subset.

### Gaps
- Exact text of C&EN's Oct 2026 article behind the paywall, beyond the key insights, and any DeepMind statement.
- No 2025-2026 consolidated tally of GNoME-predicted compounds that were synthesized after March 2021.
- Whether Nature or Microsoft has responded to the MatterGen critique: not found.

---

## Q3. What is the state of synthesizability prediction (CSLLM, Materealize, PU-learning, text-mined recipes, data leakage)?

### Takeaway
Synthesizability classifiers report very high benchmark accuracies, such as CSLLM's 98.6%. Prospective experimental hit rates are far lower, around 44% in the best documented 2025 test (7 of 16). Precursor and condition prediction remains weak: Top-1 precursor accuracy is about 54% for off-the-shelf LLMs, and temperature MAEs are about 70-130 °C. The authors of arXiv:2506.12557 themselves warn that LLM benchmark scores may be inflated by pretraining leakage of test-set recipes.

### Cited Findings
- **Hull stability is not synthesizability.**
  - The MatterGen paper concedes that many off-hull materials are routinely synthesized and many on-hull ones are not. Tolerable metastability depends on chemistry: 0.1-1 eV/atom for nitrides and carbides against meV for intermetallics. — [arXiv:2312.03687](https://arxiv.org/pdf/2312.03687)
  - An earlier Materials Project analysis found 90% of synthesized metastable materials within 67 meV/atom of the hull. — cited in [Carr & Bartel, J. Mater. Chem. C 2025](https://bartel.cems.umn.edu/sites/bartel.cems.umn.edu/files/2025-08/carr.bartel_2025-journalofmaterialschemistryc.pdf) (secondary)
  - Experimentally confirmed phases can sit up to 5+ eV/atom above the hull. — [arXiv:2510.19251](https://arxiv.org/pdf/2510.19251) (search snippet)
  - Energy-driven CSP "struggle[s] to identify experimentally realizable metastable materials synthesized through kinetically controlled pathways." — [arXiv:2505.09161](https://arxiv.org/abs/2505.09161)
- **CSLLM** (Song, Lu et al., Nat. Commun. 2025). The Synthesizability LLM reaches 98.6% test accuracy on a 140,120-structure dataset, compared with 74.1% for an E_hull ≥ 0.1 eV/atom rule and 82.2% for a phonon lowest-frequency ≥ -0.1 THz rule. Separate LLMs predict method and precursors. — [Nat. Commun.](https://www.nature.com/articles/s41467-025-61778-y) (search summary). Caveat: these are retrospective classification metrics on balanced (PU-style) datasets, not prospective synthesis.
- **arXiv:2506.12557.** Prein, Pan, Jehkul, Weinmann, Olivetti & Rupp, "Language Models Enable Data-Augmented Synthesis Planning for Inorganic Materials", 14 Jun 2025. — [arXiv:2506.12557](https://arxiv.org/abs/2506.12557)
  - Off-the-shelf LLMs (GPT-4.1, Gemini 2.0 Flash, Llama 4 Maverick and others) reach Top-1 precursor accuracy of up to 53.8% (GPT-4.1) and Top-5 of 66.1% on 1,000 held-out reactions. Calcination and sintering temperature MAEs are below 126 °C.
  - The best literature baseline reaches Top-5 of 73% and Top-10 of 78%, against at most about 66% and 69% for the LLMs.
  - The authors generated 28,548 synthetic LLM recipes. Combined with text-mined data, these trained SyntMTE, which reached sintering MAE 73 °C and calcination MAE 98 °C, up to 8.7% better than baselines.
  - **Data-leakage statements (verbatim from the paper):** "LM predictions alone cannot demonstrate real progress over existing workflows when there are no independent training and test sets and data leakage from earlier synthesis reports is likely"; "LMs may have benefited from data leakage during pretraining on test-set synthesis protocols"; "Since LM benchmark scores may be inflated by data leakage..." — [arXiv HTML](https://arxiv.org/html/2506.12557)
- **Synthesizability-guided pipeline** (Prein, O'Leary, Savvidou, Bourneix, Laulainen et al., arXiv:2511.01790, Nov 2025). A combined compositional and structural score, followed by predicted routes and experiments on 16 targets, gave 7 successes in 3 days. — [arXiv:2511.01790](https://arxiv.org/abs/2511.01790)
- **Materealize** (arXiv:2601.15743, Jan 2026; Seoul National University and Acceleration Consortium, led by Yousung Jung and Alán Aspuru-Guzik) is a multi-agent system that orchestrates structure generation, property prediction, synthesizability prediction (reportedly PU-CGCNN, SynCry and StructGPT explanations) and synthesis planning. It has an "instant" mode and a multi-agent debate "thinking" mode, and can diagnose and redesign unsynthesizable structures. It is a preprint, and the tool list comes from a third-party alphaXiv summary; I found no prospective experimental validation. — [arXiv:2601.15743](https://arxiv.org/pdf/2601.15743); [alphaXiv](https://www.alphaxiv.org/abs/2601.15743)
- **Structural memory prior** (NIST, arXiv:2606.30967) proposes a "historical synthesizability prior": structural proximity to experimental communities combined with reduced-formula precedent. — [arXiv:2606.30967](https://arxiv.org/abs/2606.30967)
- **Training-data contamination in practice:** A-Lab's Zn2Cr3FeO8 was "mistakenly included in the training data" (Nature correction), and MatterGen's TaCr2O6 analogue was in its training set (Juelsholt). — [A-Lab correction](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12872444/fullTextXML); [PubMed 42007796](https://pubmed.ncbi.nlm.nih.gov/42007796/)
- **Prior-art saturation:** a pre-registered Na-cathode screen found at least 70% of its targeted Na-substitution space already published. — [arXiv:2606.23725](https://arxiv.org/abs/2606.23725) (single-author preprint)

### Inferences
- Benchmarks in this area are retrospective, and labels are positive-unlabeled: "unsynthesized" often means unreported, as Prein et al. found. Benchmarks can also be contaminated, through LLM pretraining or recipes already in training sets. The defensible figure is the prospective hit rate. The only clean 2025 example is 7 of 16; A-Lab's corrected figure is 36 of 57 for curated, mostly known-chemistry targets.
- Precursor availability, atmosphere sensitivity and kinetic selectivity are rarely inputs to these models. A-Lab GPSS (2026) shows that ambient-only robotic platforms structurally excluded air-sensitive chemistries until recently.

### Gaps
- No independent prospective benchmark of CSLLM or Materealize synthesizability calls was found.
- Thin-film versus bulk synthesizability: I found no quantitative 2025-2026 comparison. Only anecdotal evidence exists, such as thin-film SDL campaigns on LiCoO2 and Rb3BiI6 films, and Lila's sputtering.
- Precursor commercial availability and cost as a model input: no source found.

---

## Q4. What is the state of automated XRD phase identification and characterization QC in self-driving labs, including benchmarks such as FrontierXRD?

### Takeaway
Phase identification from powder XRD is the weakest link in the loop that has been documented publicly. The A-Lab correction shows that 4 of 40 claimed successes were XRD-inconclusive on manual re-analysis. The best-resourced industrial effort, Periodic Labs' FrontierXRD, reports a 55.3% success rate on hard multiphase patterns. There is no ground truth; scoring relies on judges, and human experts agree with each other only 77.2% of the time.

### Cited Findings
- **A-Lab:** "concerns were raised about the unambiguous identification of the compound structures using diffraction." Manual re-analysis confirmed 36 of 40, with 4 inconclusive "from XRD alone". — [Nature correction 2026](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12872444/fullTextXML)
- **Leeman ... Palgrave (2024):** automated Rietveld analysis of PXRD is "not yet reliable". — [UCL Discovery](https://discovery-pp.ucl.ac.uk/id/eprint/10188733) (search snippet)
- **Periodic Labs FrontierXRD** (company research post, 15 Sep 2026; primary but not peer reviewed, no public dataset) — [Periodic Labs](https://periodic.com/news/nature-is-our-learning-environment)
  - The benchmark has 134 samples from Periodic's own labs "that human experts take hours to resolve". Accepted solutions contained **five phases on average**.
  - Periodic Neon, a 1T-parameter model post-trained from open-weight Kimi K2.6, scores **55.3%**, against **2.7%** for base Kimi K2.6. Periodic claims Neon beats "GPT-6 Astra" and "Claude Fable 5.1" at lower cost. Its cost basis is $2.5 per H200-hour; the final run used 1,300 H200 GPUs.
  - Scoring uses an LLM-judge ensemble (Opus 5 + GPT-5.6-Sol). Expert labels came from three PhD annotators per pattern across thousands of patterns. **Human-human agreement was 77.2%**; LLM-judge vs human 74.6%; LLM-judge vs expert consensus 84%.
  - A second eval of 198 measurements from held-out chemical systems is described as easier.
  - Periodic's harness achieved 3.8x the success rate of Claude Code with COD, Materials Project and BGMN, at similar cost, using the same model.
  - Quotes: "XRD analysis success cannot be cheaply verified based on pattern-fitting alone"; "as we scale our autonomous labs, scientists can no longer keep up with analyzing XRD results manually"; "this holistic interpretation can take several hours of expert time per pattern"; "Science is falsifiable, but not easily verifiable."
  - Secondary coverage (KuCoin, 36Kr, an Eigent marketing blog) repeats these numbers. Eigent's "$300M funding" figure is unverified here. — [KuCoin](https://www.kucoin.com/news/flash/periodic-neon-outperforms-gpt-6-astra-in-xrd-analysis-with-1300-h200-gpus); [36Kr](https://eu.36kr.com/en/p/3987162640038914)
- **Dara** (Fei, McDermott, Rom, Wang & Ceder; arXiv:2510.19667, 22 Oct 2025; the A-Lab group). Multiphase XRD interpretation "remains a manual and expertise-demanding task", and "multiple reference phases can often be fit to a single pattern". Dara runs an exhaustive tree search with BGMN Rietveld refinement and outputs multiple hypotheses for humans or further characterization to resolve. — [arXiv:2510.19667](https://arxiv.org/abs/2510.19667)
- **PhaseMatcher** (arXiv:2610.05844, Oct 2026) addresses weak-phase peaks hidden under strong ones and an unknown number of phases. It is evaluated on synthetic and controlled mixtures (PhaseMix-135K), not on real autonomous-lab output. — [arXiv:2610.05844](https://arxiv.org/abs/2610.05844)
- **XMatcher** (arXiv:2607.17162, Jul 2026): "reliable phase assignment still requires transparent, evidence-based validation, particularly for complex samples where interpretability and expert assessment remain essential". It notes that many search-match implementations are proprietary. — [arXiv:2607.17162](https://arxiv.org/abs/2607.17162)
- **A probabilistic phase-labeling and lattice-refinement approach** for autonomous research was published in npj Comput. Mater. in 2025. — [npj Comput Mater](https://www.nature.com/articles/s41524-025-01627-0) (title only; not read)
- **Disorder and XRD:** PXRD cannot easily distinguish an ordered superstructure from its site-disordered parent when superstructure reflections are weak. This is the mechanism behind the A-Lab and MatterGen novelty disputes. — [Juelsholt, Materials Horizons 2026](https://pubmed.ncbi.nlm.nih.gov/42007796/); [Leeman et al. 2024](https://discovery-pp.ucl.ac.uk/id/eprint/10188733)

### Inferences
- The FrontierXRD number implies that even a heavily RL-tuned frontier-scale model fails on about 45% of hard real-lab patterns. The 77% human-human agreement suggests a ceiling on what any judge-based benchmark can certify. "Phase-pure target confirmed" is therefore a probabilistic call, and the A-Lab correction shows what happens when it is treated as binary.
- The documented trend runs toward multi-hypothesis output with a human tie-break (Dara) and judge-calibrated agents (Periodic), not toward full autonomy. A human expert remains the QC gate.

### Gaps
- No public, independent XRD phase-ID benchmark on real autonomous-lab data was found. FrontierXRD is internal and unreleased.
- I found no quantified SDL QC metrics for other characterization modalities (SEM/EDS, electrochemistry, property measurement).

---

## Q5. Where are money and time actually spent, and what cycle times are reported?

### Takeaway
Practitioners and journalists consistently place the cost in synthesis, characterization and the long road from a first sample to a usable material, not in prediction. Reported throughput numbers are mostly press claims, such as A-Lab's 100-200 samples/day. Published 2025-2026 SDL campaigns run tens to a few hundred samples, with useful-hit rates of a few percent.

### Cited Findings
- **Industry timescales (opinion and reported):** making, testing, optimizing and manufacturing a new material typically takes "20 years or more" and "hundreds of millions of dollars". "It can take a researcher a year or more to make a crystal structure for the first time. Then there are typically years of further work to test its properties and figure out how to make the larger quantities." Corporate R&D has "been burned before", by combinatorial chemistry in the early 2000s among other things. — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
- **A-Lab throughput:** the 2023 LBNL press release claims 100-200 samples/day with 3 robotic arms and 8 furnaces. This is not a measured benchmark. The Nature paper reports a 17-day continuous campaign on 58 targets. — [LBNL 2023](https://newscenter.lbl.gov/2023/04/17/meet-the-autonomous-lab-of-the-future/); [Nature 2023](https://www.nature.com/articles/s41586-023-06734-w)
- **A-Lab GPSS** (air-free, 2026): 352 samples in one campaign. The fraction of samples with conductivity >0.05 mS/cm and high phase purity rose from 1.33% (first 75 agent proposals) to 5.33% (last 75). — [arXiv:2604.11957](https://arxiv.org/abs/2604.11957)
- **CASS NASICON** (A-Lab, Sep 2026): 18 promising compositions in 78 trials; best total ionic conductivity 0.7 mS/cm. This is element substitution in a known framework. — [arXiv:2609.29344](https://arxiv.org/abs/2609.29344)
- **Thin-film SDLs:** SynAgent ran 18 autonomous experiments on LiCoO2(001). — [arXiv:2609.18598](https://arxiv.org/abs/2609.18598). The MIT group made Rb3BiI6 films with hyperspectral screening. — [arXiv:2608.15928](https://arxiv.org/abs/2608.15928)
- **Prein et al. 2025:** 16 targets taken from prediction to characterized product in 3 days. — [arXiv:2511.01790](https://arxiv.org/abs/2511.01790)
- **Characterization labour:** complex XRD interpretation takes "several hours of expert time per pattern", and some experiments "can take days". — [Periodic Labs](https://periodic.com/news/nature-is-our-learning-environment); [Periodic Labs](https://periodic.com/news/building-labs-that-learn)
- **Validation of computed references:** an ML voltage screen failed pre-registered validation. The Materials Project PBE+U reference voltage sat about 0.54 V below experiment ("the reference, not the model, dominated the error"); held-out MAE was 0.67 V. — [arXiv:2606.23725](https://arxiv.org/abs/2606.23725) (single-author preprint; low weight)
- **Investor view:** SOSV's Susan Schofer wants evidence that startups are "finding something new" and a business model that captures the value of new materials. — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)

### Inferences
- Discovery yield (new, confirmed, useful compounds per day) is the metric that matters, and it is orders of magnitude below sample throughput. At 1-5% useful hits over hundreds of samples, characterization and QC per sample dominate cost. That explains why Periodic chose XRD analysis as its first trained capability.

### Gaps
- No source gives a cost breakdown in dollars or hours across DFT validation, synthesis and characterization for an AI discovery campaign.
- No peer-reviewed per-sample cycle time for A-Lab was found.
- No public figures were found on Lila, Periodic or Radical AI throughput, or on their discoveries.

---

## Q6. Which data and physics limitations break the pipeline (DFT errors, band gaps, DFPT soft modes, database fields, hull vintage, finite temperature, disorder, property gap)?

### Takeaway
Training data and screening targets inherit 0 K, ordered, PBE-level physics. Band gaps are systematically underestimated, hull positions shift with the functional and with database vintage, dielectric and phonon data are missing exactly for soft-mode (often ferroelectric or high-κ) materials, and disorder is not represented. Device-level metrics such as endurance, retention, fatigue and lifetime are not computable from bulk DFT. I found no 2025-2026 source quantifying that last gap.

### Cited Findings
- **Band gaps:** on the JARVIS leaderboard (54 materials versus experiment), TBmBJ gives MAE about 0.50 eV against about 1.36 eV for OptB88vdW, a GGA-type functional. PBE "systematically underestimate[s] bandgaps". — [JARVIS leaderboard](https://pages.nist.gov/jarvis_leaderboard/ES/SinglePropertyPrediction/dft_3d_bandgap); [CHIPS-TB arXiv:2511.20740](https://arxiv.org/pdf/2511.20740). An ML leaderboard for TBmBJ gaps covers 18,167 entries. — [JARVIS mbj leaderboard](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_mbj_bandgap) (secondary summary)
- **Functional and hull vintage:** in Materials Project's GGA/GGA+U/r2SCAN mixing scheme, for about 7,300 materials within 50 meV/atom of the hull, r2SCAN moved E_hull by ≤19 meV/atom in 95% of cases. Individual cases moved more, for example SbN from about 172 meV/atom (PBE) to about 260 meV/atom (r2SCAN). — [Kingsbury et al., npj Comput. Mater. 2022](https://www.nature.com/articles/s41524-022-00881-w)
  - The mixing rules apply only to specific thermo types. An MP developer (Oct 2025 forum) said the r2SCAN-only hull is considered reliable. — [matsci.org](https://matsci.org/t/energy-above-hull-calculation-from-formation-energy/65846)
  - GNoME candidates derive from March 2021 database snapshots, so its "new/stable" labels are tied to that hull vintage. — [arXiv:2610.13885](https://arxiv.org/abs/2610.13885), quoting the GNoME paper
- **DFPT, dielectric data and soft modes:**
  - The high-throughput DFPT phonon database (about 1,521 materials) does not compute thermodynamic properties when imaginary modes are present. — [Petretto et al., Sci. Data 2018](https://www.nature.com/articles/sdata201865)
  - JARVIS computes IR, piezo and dielectric properties only for structures with all-positive phonon frequencies, which excludes high-symmetry, soft-mode (often ferroelectric) phases. — [NIST JARVIS DFPT](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=928845)
  - A benchmark of 88 compounds for GGA dielectric constants found a mean absolute relative deviation of 16.2%, with the largest errors in perovskites with octahedral rotations or strong anharmonicity. — [Petousis et al., PRB 93, 115151 (2016)](https://perssongroup.lbl.gov/papers/petousis-2016-benchmarking.pdf)
  - GGA lattice overestimation softens low-frequency modes and inflates the ionic dielectric contribution. — [arXiv:2401.05848](https://arxiv.org/pdf/2401.05848)
  - These figures come from search summaries of the sources.
- **Reference-data error dominating model error:** Materials Project PBE+U voltages sit about 0.54 V below experiment for the Na cathodes tested. — [arXiv:2606.23725](https://arxiv.org/abs/2606.23725) (low-weight preprint)
- **Finite temperature and disorder:**
  - GNoME computations at 0 K favour ordered configurations, and many predicted "new" compounds are ordered versions of known disordered phases. — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
  - The quantitative evidence: GNoME's curation removed 92.7% of matches to known ordered crystals but only 40.4% of matches to known disordered ones. — [arXiv:2610.13885](https://arxiv.org/abs/2610.13885)
  - Juelsholt names disorder prediction as an "unresolved issue". — [PubMed 42007796](https://pubmed.ncbi.nlm.nih.gov/42007796/)
- **Database field and integrity errors:**
  - GNoME1 contained 2,311 text-identical CIFs. Some groups have identical coordinates to 6+ decimal places but different elements, which the authors call "physically unrealistic" because substituting atoms should perturb the geometry.
  - About 20% of entries contain radioactive elements.
  - The releases are non-nested, with entries withdrawn and later restored.
  - — [arXiv:2610.13885](https://arxiv.org/abs/2610.13885)
- **Microstructure and complex phenomena:** "many desirable properties are determined by the microstructure of the materials—at a scale much larger than the atomic world", and phenomena such as high-Tc superconductivity and industrial catalysis are "far too complex or poorly understood to be explained by atomic simulations alone". — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
- **Computable versus non-computable properties:** ML+DFT ferroelectric pipelines, including a 2026 MatterGen workflow with 12,800 generated candidates, stop at polarization, band gap, stability and switchability. — [search summary of KIST 2026](https://pubs.kist.re.kr/handle/201004/154727); [arXiv:2201.05668](https://ar5iv.labs.arxiv.org/html/2201.05668)

### Inferences
- Reliably computable at scale: formation energy and hull position (with functional-dependent uncertainty of tens of meV/atom), lattice parameters, elastic moduli, and (with hybrid/mBJ/GW) band gaps. Partially reliable: dielectric constants (around 16% error, missing for soft-mode materials), voltages (systematic errors around 0.5 V reported), and phonon stability (sensitive to numerical settings). Not computable from bulk DFT: endurance, retention, fatigue, wake-up/imprint, leakage in real films, interface and defect-controlled behaviour, microstructure-controlled transport, thin-film vs bulk phase selection. This classification is my inference from the sources above. I found no single 2025-2026 review that states it explicitly.
- "Novelty" and "stability" labels depend on a database snapshot and on the functional. Re-labelling as r2SCAN data and new ICSD entries accumulate will change any "new stable" count.

### Gaps
- No 2025-2026 source was found that explicitly quantifies the device-metric gap (endurance, retention) for AI-discovered materials.
- Coverage counts for Materials Project dielectric data and for JARVIS TBmBJ entries in 2026 were not found. The 18,167 TBmBJ figure comes from an ML leaderboard dataset, not total coverage.
- Defect and interface modelling in AI pipelines: no specific 2025-2026 quantified sources were found.
