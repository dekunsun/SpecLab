# Influential academic research groups in CSP and AI-driven materials discovery (2025-2026)

Scope: academic (and quasi-academic / corporate-research) groups worldwide working on inorganic crystal structure prediction (CSP), molecular/pharmaceutical CSP, machine-learned interatomic potentials (MLIPs) used for CSP, generative crystal models, and autonomous labs. For each group: PI, institution, flagship contribution, 2025-2026 output, industry ties. Research date: 22 Oct 2026. Sources fetched via WebSearch and curl; where a claim relies on a secondary/aggregator source this is flagged.

---

## Q1. United States (and US-based industry research labs): who matters, what they built, 2025-2026 output, industry ties

### Takeaway
The US cluster is anchored by Berkeley/LBNL (Ceder's A-Lab, Persson's Materials Project, Jain's atomate2), MIT (Gómez-Bombarelli, Smidt, Olivetti), Harvard (Kozinsky's NequIP/Allegro) and corporate labs (Meta FAIR, Microsoft MatterGen, ex-Google GNoME). The defining 2025-2026 trend is the exodus of leading figures into heavily funded start-ups: Cubuk co-founded Periodic Labs ($300M seed, Sep 2025), Gómez-Bombarelli is CSO for Materials at Lila Sciences, Ceder co-founded Radical AI, Hautier moved Dartmouth→Rice, and Ong is moving UCSD→NUS (Singapore).

### Cited Findings

**Gerbrand Ceder (UC Berkeley / LBNL) — A-Lab autonomous synthesis**
- A-Lab synthesised 41 novel compounds out of 58 targets over 17 days of continuous operation (2023 Nature); critics argued human verification was still needed, Ceder responded the aim was to "demonstrate what an autonomous laboratory can achieve" — [MRS 2023](https://mrs.org/meetings-events/presentation/2023_mrs_fall_meeting/2023_mrs_fall_meeting-3945014); [VentureBeat](https://venturebeat.com/ai/ai-meets-materials-science-the-promise-and-pitfalls-of-automated-discovery)
- Industry tie: Ceder is a co-founder of Radical AI (with CEO Joseph Krause and Jorge Colindres); Radical AI raised a $55M Seed+ round led by RTX Ventures, with NVentures (NVIDIA), Eni, AlleyCorp; bio describes him as "scientific advisor to multiple companies in the energy storage and materials design space" — [Pulse2](https://pulse2.com/radical-ai-55-million-series-seed-raised-for-advancing-materials-research); [EPFL MARVEL Distinguished Lecture, 30 Jan 2025](https://memento.epfl.ch/event/marvel-distinguished-lecture-gerbrand-ceder)
- Co-author on Matbench Discovery (Nature Machine Intelligence, 2025) — [arXiv v3](https://arxiv.org/abs/2308.14920v3)

**Kristin Persson (UC Berkeley / LBNL) — Materials Project; Shyue Ping Ong (UCSD → NUS) — pymatgen, MatGL, M3GNet**
- MatPES (Materials Virtual Lab + Materials Project, arXiv 2503.04070, Mar 2025): foundational PES dataset, v2025.1 = 504,811 structures with PBE and r2SCAN energies/forces/stresses, sampled from 300 K NpT MD seeded by MP entries; authors claim MatPES-trained universal MLIPs rival or beat models trained on far larger datasets (OMat24); v2025.2 = 433,189 PBE / 386,544 r2SCAN, BSD-3 — [arXiv](https://arxiv.org/html/2503.04070v1); [ColabFit](https://materials.colabfit.org/id/DS_q1zgft23gdbl_1)
- MatGL (Materials Graph Library) paper, npj Computational Materials 2025 (arXiv 2503.03837): pre-trained foundation potentials covering the periodic table; implements TensorNet, M3GNet, MEGNet, CHGNet, SO3Net — [arXiv](https://arxiv.org/abs/2503.03837v1); [OSTI](https://www.osti.gov/pages/biblio/2587755)
- Affiliation change: NUS College of Design & Engineering news (24 Sep 2026) says Ong is joining NUS under the Returning Singaporean Scientists Scheme to build an "AI Foundry" for materials discovery; describes him as founding developer of the Materials Project and creator of pymatgen — [NUS CDE](https://cde.nus.edu.sg/mse/news/building-an-ai-foundry-to-transform-materials-discovery/)
- Persson is co-author of Matbench Discovery (Nat. Mach. Intell. 2025) — [arXiv](https://arxiv.org/abs/2308.14920v3)

**Anubhav Jain (LBNL) — atomate2 / workflows; Matbench**
- "Atomate2: modular workflows for materials science", Digital Discovery 4(7), 1944-1973, published 10 Jul 2025 (Ganose + 40 co-authors incl. Jain); package-agnostic workflows for DFT and ML force fields, explicitly tied to training universal ML models — [RSC](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00019j)
- Co-author of Matbench Discovery — [arXiv](https://arxiv.org/abs/2308.14920v3)

**Chris Wolverton (Northwestern) — OQMD**
- 2025 Science Advances paper: Griesemer, Baldassarri, Zhu, Shen, Pal, Park, Wolverton, "Wide-ranging predictions of new stable compounds powered by recommendation engines"; earlier "Accelerating the prediction of stable materials with machine learning", Nat. Comput. Sci. 3, 934 (2023); OQMD (launched 2013) >1.2M compounds; MRS Fellow (Mar 2025) and MRS Theory Award 2025 — [Northwestern profile](https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/wolverton-chris.html); [Northwestern news](https://www.mccormick.northwestern.edu/news/articles/2025/03/wolverton-named-fellow-of-materials-research-society/index.html)

**Geoffroy Hautier — high-throughput computational design (moved Dartmouth → Rice)**
- Now Trustee Professor of Materials Science and NanoEngineering at Rice University; previously Hodgson Family Professor at Dartmouth (from Oct 2020); elected APS Fellow (Rice News, Oct 2025) — [Wikipedia](https://en.wikipedia.org/wiki/Geoffroy_Hautier); [Rice News](https://news.rice.edu/news?page=55)

**Elsa Olivetti (MIT) — text-mined synthesis**
- Pioneered ML extraction of synthesis recipes from literature (Chem. Mater. ~2017; follow-up with E. Kim, G. Ceder 2021) — [MRS Bulletin news](https://resolve.cambridge.org/core/journals/mrs-bulletin/news/machine-learning-algorithm-extracts-materials-synthesis-recipes-from-the-literature); [MIT DSpace](https://dspace.mit.edu/handle/1721.1/122075)

**Rafael Gómez-Bombarelli (MIT DMSE)**
- Co-founder and Chief Scientific Officer of Materials at Lila Sciences (Flagship Pioneering-backed "scientific superintelligence"/autonomous science company); previously co-founded Calculario — [Lila](https://www.lila.ai/news/join-our-mission); [Latent Space podcast with Andy Beam & Gómez-Bombarelli](https://latent.space/p/the-lab-of-the-future-should-feel); [MIT faculty page](https://engineering.mit.edu/faculty/rafael-gomez-bombarelli)

**Tess Smidt (MIT EECS, Atomic Architects) — e3nn / Equiformer lineage**
- Associate Professor at MIT; co-developed Tensor Field Networks, created e3nn (Geiger & Smidt 2022); Equiformer (ICLR 2023) and EquiformerV2 (ICLR 2024) — [MIT CSE](https://cse.mit.edu/seminars-and-events/cse-community-seminar-5apr24); [arXiv e3nn](https://arxiv.org/abs/2207.09453v1)
- 2026: EquiformerV3 (arXiv 2604.09130) led by Yi-Lun Liao (MIT) with co-authors Alexander J. Hoffman, Sabrina C. Shen of Mirror Physics (NYC start-up founded 2024 building physics foundation models for chemistry/materials); EquiformerV3+DeNS-OAM is #4 on Matbench Discovery (CPS 0.902) — [arXiv](https://arxiv.org/pdf/2604.09130); [Matbench model page](https://matbench-discovery.materialsproject.org/models/equiformer-v3-oam); [Mirror Physics](https://builtin.com/company/mirror-physics/teams)
- Nequix (Teddy Koker & Tess Smidt, MIT) entered on Matbench Discovery — [Matbench](https://matbench-discovery.materialsproject.org/models/nequix-mp-1)

**Boris Kozinsky (Harvard, MIR group) — NequIP / Allegro**
- NequIP framework paper arXiv 2504.16068 (Tan, Descoteaux, Musaelian, Kozinsky et al.), journal version Digital Discovery 2026 (D5DD00423C); NequIP/Allegro OAM foundation models released on Zenodo Aug 2025 (OMat24 pretrain ~101M frames, fine-tuned on sAlex + MPtrj); arXiv 2607.28461 reports 5-10x training speed-ups, training a high-accuracy foundation potential in a few hundred GPU-hours; APS/MRS 2026 talks (Kavanagh, Tan, Musaelian, Kozinsky) — [arXiv 2607.28461](https://arxiv.org/pdf/2607.28461); [Zenodo](https://zenodo.org/records/17087883); [APS 2026](https://meetings-archive.aps.org/smt/2026/mar-m46/7/); [MRS Spring 2026](https://www.mrs.org/meetings-events/annual-meetings/archive/meeting/presentations/view/2026-mrs-spring-meeting/2026-mrs-spring-meeting-4435986)
- NequIP-OAM-XL authors include Seán Kavanagh (Cambridge chemistry) with Harvard MIR group — [Matbench](https://matbench-discovery.materialsproject.org/models/nequip-oam-xl-0.1)

**Bingqing Cheng (UC Berkeley Chemistry, from Jan 2024; previously ISTA, Cambridge)**
- 2025 papers on long-range electrostatics in MLIPs: Nat. Commun. 16, 8763 (2025) "Machine learning of charges and long-range interactions from energies and forces"; JCTC 21(24), 12709 (2025) universal long-range augmentation; npj Comput. Mater. 11, 384 (2025) MLIP inferring electrical response — [Berkeley](https://chemistry.berkeley.edu/faculty/chem/cheng); [ISTA group page](https://ista.ac.at/en/research/cheng-group/)

**Wenhao Sun (Michigan) — synthesizability / precursor selection**
- Phase-diagram-guided precursor selection validated by robotic synthesis; ternary nitride stability map → new nitride semiconductors; 2025 talks on predicting liquidus curves for synthesis; MRS Fall 2025 symposium MT05 "Informed Synthesis of Materials" — [Iowa State 2025](https://www.chem.iastate.edu/event/2025/dr-wenhao-sun-physicalinorganic-seminar); [MRS Fall 2025](https://www.mrs.org/meetings-events/annual-meetings/archive/meeting/symposium-sessions/call-for-papers/2025-mrs-fall-meeting/Symposium-MT05-Informed-Synthesis-of-Materials-Data-Driven-and-em--In-Situ--em--Approaches)

**Milad Abolhasani (NC State) — self-driving fluidic labs**
- "Flow-driven data intensification to accelerate autonomous materials discovery", Nature Chemical Engineering, 14 Jul 2025 (DOI 10.1038/s44286-025-00249-z): dynamic-flow experiments give ≥10x more data than steady-state flow SDLs (CdSe quantum dots model system) — [NC State News](https://news.ncsu.edu/2025/07/fast-forward-for-self-driving-labs); [ScienceDaily](https://sciencedaily.com/releases/2025/07/250714052105.htm)

**Logan Ward (Argonne → possibly NVIDIA)**
- Salata Institute interview (2 Jan 2025) lists him as Deputy Scientist at Argonne; a later third-party profile says he is now a researcher at NVIDIA (unconfirmed, secondary). Argonne's 2025 agentic MOF discovery work (MOFA workflow on "Academy" federated agents, arXiv 2510.13081) — [Salata](https://salatainstitute.harvard.edu/?p=12630); [alphaXiv profile](https://www.alphaxiv.org/@logan-ward); [arXiv](https://arxiv.org/pdf/2510.13081)

**Taylor Sparks (Utah)**
- Generative materials informatics (with Sterling Baird; sparks-baird org; DiSCoVeR + SMACT for chemically valid generation); 2024 review "Generative AI for discovering new materials" — [GitHub mirror](https://backiee.wasmer.app/http_github_com/sparks-baird); [Coshare Science review](https://www.cosharescience.com/articles/cs.202410.134.pdf)

**Jianjun Hu (University of South Carolina) — CSPBench**
- CSPBench (Lai Wei, Jianjun Hu; arXiv 2407.00733): 180 test structures, 13 CSP algorithms (template-based, CALYPSO-style DFT global search, ML-potential search, etc.); found most algorithms fail to find correct space groups except template-based ones on similar templates; ML-potential methods now competitive with DFT-based searches — [arXiv](https://arxiv.org/html/2407.00733v1); [GitHub](https://github.com/usccolumbia/CSPBenchMetrics)

**Qiang Zhu (UNC Charlotte) — PyXtal, LEGO-xtal**
- LEGO-xtal (arXiv 2506.08224, June 2025; Ridwan, Pitié, Soundar Raj, Dai, Frapper, Xue, Q. Zhu): symmetry-informed generation targeting specified local environments; from 25 known low-energy sp2 carbon allotropes generated >1,700 new structures — [arXiv](https://arxiv.org/abs/2506.08224)

**Noa Marom (Carnegie Mellon) — molecular CSP (Genarris) + Meta FAIR**
- FastCSP (arXiv 2508.02641, Aug 2025; Meta FAIR + Marom): Genarris 3.0 random generation + Meta's UMA MLIP for relaxation and free energy, no force-field pre-screen or final DFT re-ranking; benchmark 28 semi-rigid + 10 flexible molecules, 74 polymorphs, known forms ranked within 9 kJ/mol (v1: within 5 kJ/mol on 28 rigid molecules); "hours on tens of GPUs" per system. Companion OMC25 dataset (arXiv 2508.02651): >25M configurations from ~50,000 molecules (later listing >27M) — [arXiv FastCSP](https://arxiv.org/abs/2508.02641v1); [Meta AI](https://ai.meta.com/research/publications/fastcsp-accelerated-molecular-crystal-structure-prediction-with-universal-model-for-atoms/); [APS March 2026](https://meetings-archive.aps.org/smt/2026/mar-a45/3/)
- Genarris 3.0 paper also tests MACE-OFF23(L), finding large variability and poor performance for energetic materials — [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12613321/)

**Gregory Beran (UC Riverside) — molecular CSP energy ranking**
- ROY energy landscape with conformational-energy-corrected DFT (Chem. Sci. 2022); participant in 7th blind test ranking — [RSC](https://pubs.rsc.org/en/content/articlehtml/2022/sc/d1sc06074k); [7th blind test ranking](https://reading-clone.eprints-hosting.org/119231)

**Yousung Jung (now Seoul National University; formerly KAIST)** — see Q4.

**Corporate research labs (US-based) and alumni flows**
- Microsoft MatterGen: Nature 16 Jan 2025, vol. 639, 624-632 (Zeni, Pinsler, Zügner, Fowler, Horton, ..., Tian Xie corresponding); code & weights MIT-licensed; TaCr2O6 synthesised with SIAT (target bulk modulus 200 GPa, measured 169 GPa) — [Azure AI Foundry Labs](https://labs.ai.azure.com/innovations/mattergen/); [PMC](https://pmc.ncbi.nlm.nih.gov/articles/11922738). A 2026 Materials Horizons critique (Mikkel Juelsholt) argues the synthesised phase is disordered and isostructural with a compound reported in 1972 — [aiwiki summary of critique](https://aiwiki.ai/wiki/mattergen) (secondary)
- Tian Xie: MIT TR Innovators Under 35 (2025) lists him at MSR AI for Science — [MIT TR](https://www.technologyreview.com/innovator/tian-xie/); a third-party alphaXiv profile lists him as "Founding Member of Technical Staff @ Project Prometheus" from Feb 2026 (UNCONFIRMED) — [alphaXiv](https://www.alphaxiv.org/@tian-xie-2)
- Ekin Dogus Cubuk: co-founded Periodic Labs with Liam Fedus (ex-OpenAI VP post-training); out of stealth 30 Sep 2025 with $300M seed led by a16z (Felicis first check; also DST, Nvidia, Accel, Elad Gil, Jeff Dean, Eric Schmidt, Jeff Bezos); Cubuk previously led materials & chemistry at Google Brain/DeepMind, co-authored GNoME and the 2023 A-Lab paper; team includes people who worked on MatterGen and OpenAI Operator; first goal is higher-Tc superconductors; also deploying with a semiconductor maker on heat dissipation — [TechCrunch 30 Sep 2025](https://techcrunch.com/2025/09/30/former-openai-and-deepmind-researchers-raise-whopping-300m-seed-to-automate-science); [TechCrunch 20 Oct 2025](https://techcrunch.com/2025/10/20/top-openai-google-brain-researchers-set-off-a-300m-vc-frenzy-for-their-startup-periodic-labs); [Periodic Labs](https://periodic.com/)
- GNoME (2023): 2.2M new crystals, 380k most stable; 736 independently realised; authors incl. Amil Merchant, Cubuk — [Freethink](https://www.freethink.com/robots-ai/google-ai-discovers-2-2-million-new-materials)
- Orbital Materials (ORB potentials) founded by Jonathan Godwin (ex-DeepMind) — [DataCenterKnowledge](https://www.datacenterknowledge.com/artificial-intelligence/deepmind-alum-wants-use-ai-speed-development-green-materials)

### Inferences
- The "who's influential" map is increasingly split between (a) academic groups that own open infrastructure (Materials Project/MatPES, pymatgen/MatGL, atomate2, NequIP/Allegro, e3nn, OQMD) and (b) start-ups that absorbed PIs or senior staff (Periodic Labs, Lila, Radical AI, Mirror Physics, Orbital). Most top PIs now have a dual academic/industry identity.
- Molecular CSP in the US has shifted toward MLIP-driven pipelines (FastCSP/UMA) — a direct challenge to the traditional force-field→DFT hierarchy used by UK groups (Price, Day).
- Ong's move to NUS and Ziheng Lu's departure from MSR (see Q3) suggest some talent flow out of US institutions toward Asia.

### Gaps
- Could not verify Tian Xie's move to Project Prometheus from a primary source.
- No 2025-2026 primary sources found for: Persson's specific 2025 papers beyond MatPES/Matbench; Olivetti's current role; Taylor Sparks' 2025 output; Tess Smidt's own 2025 papers; Aspuru-Guzik's 2025 papers (see Q4).
- Logan Ward's move to NVIDIA is from one secondary profile only.
- Did not verify who from MatterGen joined Periodic Labs (TechCrunch does not name them).
- Kozinsky's industry ties (Bosch) not confirmed in this session.

---

## Q2. Europe / UK: groups, flagship codes, 2025-2026 output, industry ties

### Takeaway
Europe/UK holds the historical core of CSP methods (AIRSS – Pickard; USPEX – Oganov, now Skoltech/Russia; molecular CSP – Day, Price) and of MLIP architecture (MACE – Csányi; PET – Ceriotti; GRACE/ACE – Drautz; HDNNP – Behler). In 2025-2026 EPFL's PET-OAM-XL briefly took #1 on Matbench Discovery (Feb 2026), Imperial's Chemeleon brought text-conditioned crystal generation to Nat. Commun., Marzari moved to Cambridge's Cavendish chair, and Welling's CuspAI became Europe's best-funded AI-materials start-up.

### Cited Findings

**Chris Pickard (Cambridge) — AIRSS + EDDP**
- Ephemeral data-derived potentials (EDDP, PRB 2022) built for AIRSS; 2025 Faraday Discussions paper introduces "hot-AIRSS" (EDDP-driven anneals biasing random search) and "datum-derived structures" (generating structures matching an experimental structure's EDDP environment vector), demonstrated on large-cell boron; NTU Singapore seminar on hot-AIRSS, 16 Jan 2026 — [RSC Faraday Discuss. 2025](https://pubs.rsc.org/en/content/articlehtml/2025/fd/d4fd00134f); [arXiv EDDP](https://www.arxiv.org/pdf/2201.08140); [NTU](https://www.ntu.edu.sg/mse/news-events/events/detail/2026/01/16/default-calendar/tct-seminar-professor-chris-pickard-16Jan2026)

**Gábor Csányi (Cambridge Engineering) — MACE, GAP**
- Elected Fellow of the Royal Society, 11 June 2025; MACE described as fastest/most precise atomistic simulation approach in a 2023 interview — [444.hu](https://444.hu/2023/11/15/akkor-ertem-el-sikert-ha-miattam-emberek-mast-fognak-csinalni-mint-addig)
- MACE models are now the reference foundation potentials tested in molecular CSP: Price et al. 2025 test MACE-MP-0 and MACE-OFF23 on CPOSS209; Nickerson & Johnson (PCCP 2025) find MACE-OFF23(M) good for in-distribution compounds but failing dramatically for diazo groups and organic salts across 28 blind-test compounds — [Price et al. 2025 PDF](https://discovery.ucl.ac.uk/10209146/1/price-et-al-2025-one-size-fits-all-development-of-the-cposs209-data-set-of-experimental-and-hypothetical-polymorphs-for.pdf); [PCCP 2025](https://pubs.rsc.org/en/content/articlehtml/2025/cp/d5cp00593k)
- No MACE spin-out found.

**Nicola Marzari (EPFL/PSI → Cambridge) — Materials Cloud, AiiDA, NCCR MARVEL**
- Appointed Cavendish Professor of Physics at Cambridge: part-time from Sep 2025, full-time from Sep 2026 after NCCR MARVEL ends; also head of the Laboratory for Materials Simulations at PSI — [MARVEL newsletter Jul 2025](https://nccr-marvel.ch/newsletters/public/newsletter-july2025); [Materials Cloud team](https://www.materialscloud.org/team)

**Michele Ceriotti (EPFL COSMO) — PET, PET-MAD, metatensor**
- PET-MAD: Nat. Commun. 16, 10653 (2025) (Mazitov, Bigi, Kellner, ..., Ceriotti); lightweight universal MLIP trained on small, diverse dataset (MAD), competitive for inorganic solids and reliable for molecules/surfaces; pitched as affordable for small labs — [NCCR MARVEL](https://nccr-marvel.ch/highlights/PET-MAD-nature-communications); [arXiv](https://arxiv.org/pdf/2503.14118)
- PET-OAM-XL reached #1 on Matbench Discovery (EPFL news 9 Feb 2026: "leaderboard has long been dominated by models developed at Meta"); paper arXiv 2601.16195 (Bigi, Pegolo, Mazitov, Jonathan Schmidt, Ceriotti, 2026); code lab-cosmo/upet. As of 22 Oct 2026 it is #6 (CPS 0.898) — [EPFL news](https://actu.epfl.ch/news/a-new-reference-model-for-machine-learning-driven); [arXiv](https://arxiv.org/abs/2601.16195); [Matbench Discovery](https://matbench-discovery.materialsproject.org/)

**Aron Walsh (Imperial) — Chemeleon, SMACT**
- Chemeleon (Hyunsoo Park, Anthony Onwuli, Walsh): text-guided generation of compositions and crystal structures via contrastive text-structure alignment + denoising diffusion; Li-P-S-Cl solid-electrolyte demo; Nat. Commun. 12 May 2025 (date from Chinese news report); MRS Fall 2025 talk (1 Dec 2025) — [ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/6728e27cf9980725cf118177); [MRS Fall 2025](https://www.mrs.org/meetings-events/annual-meetings/archive/meeting/presentations/view/2025-mrs-fall-meeting/2025-mrs-fall-meeting-4375897); [Tencent Cloud news](https://cloud.tencent.com/developer/news/2588486)

**Graeme Day (Southampton) — molecular CSP at scale**
- MACSMIN 2025 talk "Predictive crystallography at scale": CSP on >1,000 molecules to validate lattice-energy minimisation and build data for learning molecule→crystal→property relationships; 2025 PhD dataset on ML analysis of organic CSP landscapes (J. Martin & Day) — [MACSMIN 2025](https://www.kurlin.org/macsmin/2025.php); [Southampton eprints](https://eprints.soton.ac.uk/505998)
- Southampton CSP is used to pre-screen building blocks for Cooper's Liverpool robots — [FindAPhD](https://www.findaphd.com/phds/project/autonomous-robots-for-computationally-guided-materials-discovery/?p140506)

**Sally (Sarah L.) Price (UCL) — molecular CSP and benchmark data**
- L.S. Price, M. Paloni, M. Salvalaglio, S.L. Price, "One Size Fits All? Development of the CPOSS209 Data Set of Experimental and Hypothetical Polymorphs for Testing Computational Modeling Methods", Cryst. Growth Des. 25, 3186-3209 (2025): 6-15 structures each for 20 organic molecules (known polymorphs + CSP-generated competitors), compared with PBE-TS/MBD periodic DFT; preliminary tests of MACE-MP-0 and MACE-OFF23 — [UCL Discovery PDF](https://discovery.ucl.ac.uk/10209146/1/price-et-al-2025-one-size-fits-all-development-of-the-cposs209-data-set-of-experimental-and-hypothetical-polymorphs-for.pdf)

**Andrew Cooper (Liverpool) — robots + computation for organic/porous materials**
- Academic Director, Materials Innovation Factory; Director, Leverhulme Research Centre for Functional Materials Design; 2020 mobile robotic chemist; 2026 Nature Chemistry paper on ionic clusters as SBUs for crystalline porous organic salts; spin-out Porous Liquid Technologies (2017) — [Liverpool profile](https://profiles.liverpool.ac.uk/3253-andy-cooper); [Liverpool outputs](https://www.liverpool.ac.uk/people/andrew-cooper/research-outputs)

**Lee Cronin (Glasgow) — Chemputer / Chemify**
- Chemify: $34M VC (Triatomic Capital) + $9M UK Innovation Accelerators; first £12M Chemifarm in Maryhill, Glasgow; Series B extended to £51.9M, total funding >£110M; £22M grants (£16M Scottish Enterprise + £6M UK Government) for its "Chemify Genesis" world-model-guided discovery platform; workforce 152 → ~450 planned (2026 coverage) — [StartupMag 2026](https://www.startupmag.co.uk/funding/chemify-2026-grant-funding/); [Univ. Glasgow](https://www.gla.ac.uk/news/headline_990451_en.html); [Eureka](https://www.eurekamagazine.co.uk/content/news/why-university-of-glasgows-chemify-12m-chemifarm-is-a-game-changer-for-innovation)

**Artem Oganov (Skoltech, Russia) — USPEX**
- Affiliation verified: Distinguished Professor at Skoltech since 2024 (Professor 2015-2024); 2021-2024 also head of lab at Institute of Geochemistry and Analytical Chemistry RAS and professor at MISIS; USPEX 25 released 2025 (USPEX 26 listed 2026); Clarivate Highly Cited 2025; awarded a Chinese state science & technology award — [CV July 2025](https://uspex-team.org/static/file/CV-Oganov-2025-07-22.pdf); [USPEX news](https://uspex-team.org/en/news); [Skoltech](https://skoltech.ru/en/news/zasluzhennyj-professor-skolteha-artyom-oganov-udostoen-gosudarstvennoj-premii-knr-v-oblasti-nauki-i-tehniki)
- Co-author on ShotgunCSP (with ISM Tokyo and Panasonic) — [arXiv](https://arxiv.org/abs/2305.02158v5)

**Jörg Behler (Ruhr-Universität Bochum) — HDNNP (4G-HDNNP)**
- Fourth-generation HDNNP with global charge equilibration (Ko, Finkler, Goedecker, Behler, Nat. Commun. 2021); June 2025 Cambridge seminar "Four Generations of HDNNPs" listed at Bochum — [Cambridge talks](https://www.talks.cam.ac.uk/talk/index/227407/); [RePEc](https://ideas.repec.org/a/nat/natcom/v12y2021i1d10.1038_s41467-020-20427-2.html)

**Ralf Drautz / Yury Lysogorskiy (ICAMS, Ruhr-Universität Bochum) — ACE / GRACE foundation potentials**
- GRACE-3L-OAM-L (Bochkarev, Lysogorskiy, Drautz) is #5 on Matbench Discovery (CPS 0.900) — [Matbench](https://matbench-discovery.materialsproject.org/models/grace-3l-oam-l); Drautz UGM 2025 talk on GRACE foundational potentials — [UGM 2025](https://www.ugm.materialsdesign.com/_files/ugd/541861_453df50808f64e23a7eaff8efd600bbe.pdf)

**Kristian Thygesen (DTU) — C2DB**
- CDVAE trained on 2,615 2D materials generated 11,630 new 2D candidates (8,599 within 0.3 eV/atom; 2,004 within 50 meV of hull), npj Comput. Mater. 2022; 2024 follow-up characterised 4,249 previously unexplored monolayers; all in C2DB — [arXiv](https://ar5iv.arxiv.org/html/2206.12159); [arXiv 2024](https://arxiv.org/html/2402.02783v2)

**Max Welling (ex-Microsoft Research AI4Science Amsterdam) — CuspAI**
- CuspAI co-founded by Welling and CEO Chad Edwards: $30M seed; $100M Series A Sep 2025 (NEA, Temasek; ~$520M valuation per one source); reported $450M Series B in July 2026 at ~$2.6B (Kleiner Perkins, NEA; Bezos Expeditions, AMD Ventures, Invest-NL) plus an "AI Materials Foundry" coalition of 45+ organisations (secondary coverage) — [Fortune](https://fortune.com/2025/09/10/cuspai-raises-100-million-in-new-venture-capital-funding-ai-for-chemistry); [Dutch IT Channel](https://www.dutchitchannel.nl/news/756119/cuspai-van-max-welling-haalt-450-miljoen-dollar-op-voor-ai-materialen); [Trending Topics](https://www.trendingtopics.eu/cuspai-450-mio-dollar-fuer-ki-gestuetzte-materialforschung-aus-cambridge/)
- MSR AI for Science lists sites in UK, US, China, Netherlands, Germany — [MSR](https://microsoft.com/en-us/research/lab/microsoft-research-ai4science/)

**Molecular-CSP industry in Europe**
- Marcus Neumann founded Avant-garde Materials Simulation (Paris, 2002; Freiburg subsidiary) for the GRACE molecular CSP software (distinct from Drautz's GRACE MLIP) — [workeer](https://workeer.de/en/arbeitgeber/Q7BE1)

### Inferences
- Cambridge has become arguably the single densest CSP/MLIP hub in 2026 (Pickard AIRSS, Csányi MACE, Marzari arriving, CCDC, Riebesell's Matbench Discovery origins, Kavanagh co-authoring NequIP-OAM).
- Molecular CSP in the UK (Price, Day) is now positioned as the source of curated benchmark data (CPOSS209, >1,000-molecule CSP sets) against which foundation MLIPs are tested, rather than competing on raw throughput with FastCSP-style pipelines.
- Oganov remains at Skoltech (Russia); his collaborations are visibly with China and Japan (Chinese state award, ShotgunCSP co-authorship), consistent with Western sanctions constraints (inference).

### Gaps
- Matthias Scheffler / FHI NOMAD: no 2025-2026 information gathered in this session (background: NOMAD is now co-run with HU Berlin — unverified here).
- Bingqing Cheng covered under US (moved to Berkeley).
- No 2025 Behler-specific paper found; no 2025 Thygesen generative paper found.
- Could not confirm the MACE-OFF23 authorship (Kovács, Csányi et al.) from a primary source in this session.
- Microsoft Research AI4Science Amsterdam status after Welling's departure (2024) not verified.
- Alexandre Tkatchenko (Luxembourg), Aurora Cruz-Cabeza (Durham), Jan Gerit Brandenburg and other molecular-CSP figures not researched.

---

## Q3. China: leading 2025-2026 CSP / generative / MLIP groups

### Takeaway
China is now a co-leader. Jilin University's Ma/Wang/Lv (CALYPSO) published CrystalFlow in Nat. Commun. (Oct 2025); IOP CAS (Lei Wang) leads autoregressive/RL-tuned generation (CrystalFormer-RL); Renmin/Tsinghua (Wenbing Huang, Rui Jiao) originated DiffCSP/DiffCSP++; Nanjing (Jian Sun) maintains MAGUS. On Matbench Discovery as of Oct 2026, the #1 model is from Beijing start-up Kairos Materials (founded by ex-MSR MatterSim lead Ziheng Lu) and #2 and #7 are from ShanghaiTech/Nanjing; DP Technology/AISI (Linfeng Zhang) ship the DPA-3/DPA-4 models, and ICT CAS, Zhejiang Lab, Tsinghua/Alibaba DAMO all have entries.

### Cited Findings

**Yanming Ma, Yanchao Wang, Jian Lv (Jilin University) — CALYPSO, CrystalFlow**
- CALYPSO (swarm-intelligence CSP) used at >1,000 institutions in 79 countries/regions (ICTP listing, July 2026) — [ICTP](https://indico.ictp.it/event/11402)
- ML-accelerated CALYPSO (Gao, Lv, Wang, Ma, Aug 2024 workshop) — [IHEP slides](https://indico.ihep.ac.cn/event/22572/contributions/162804/attachments/80507/100945/Machine%20Learning%20Accelerated%20CALYPSO%20Structure%20Prediction%20Method.pdf)
- CrystalFlow (Xiaoshan Luo et al., incl. Yanchao Wang, Yanming Ma; Jilin + IOP CAS): Nat. Commun. 16 (2025), DOI 10.1038/s41467-025-64364-4, online 20 Oct 2025; conditional flow matching over lattice, coordinates and atom types with equivariant GNN; pressure- and property-conditioned generation — [Nature Index](https://www.nature.com/nature-index/article/10.1038/s41467-025-64364-4); [arXiv 2412.11693](https://arxiv.org/abs/2412.11693v3)
- Earlier Cond-CDVAE generative CSP (arXiv 2403.10846) from the same lineage — [arXiv](https://arxiv.org/pdf/2403.10846)
- Wang (Prof.) and Lv (Assoc. Prof.) co-recipients of 2019 State Natural Science Award (2nd class) — [JLU](https://klmsms.jlu.edu.cn/info/1020/1196.htm); [JLU](https://klmsms.jlu.edu.cn/info/1020/1201.htm)

**Lei Wang (Institute of Physics, CAS) — CrystalFormer**
- CrystalFormer: space-group-controlled autoregressive transformer (arXiv 2403.15734); CrystalFormer-RL / "Reinforcement Fine-Tuning for Materials Design" (Zhendong Cao, Lei Wang; arXiv 2504.02367, Apr 2025, v3 Jan 2026): RL fine-tuning with MLIP and property-model rewards improves stability and finds crystals with conflicting properties (high dielectric constant + large band gap) — [arXiv](https://arxiv.org/html/2504.02367v3)

**Wenbing Huang & Rui Jiao (Renmin Univ. / Tsinghua) — DiffCSP family**
- DiffCSP (NeurIPS 2023; joint equivariant diffusion on lattice + fractional coordinates), DiffCSP++ (ICLR 2024; space-group constraints); EquiCSP (arXiv 2512.07289, Dec 2025) with Huang as co-author — [arXiv DiffCSP](https://arxiv.org/abs/2309.04475); [arXiv DiffCSP++](https://arxiv.org/html/2402.03992v2); [HF EquiCSP](https://huggingface.co/papers/2512.07289.md)

**Jian Sun (Nanjing University) — MAGUS**
- MAGUS (Machine learning and graph theory Assisted Universal structure Searcher), Natl. Sci. Rev. 2023 (nwad128); surface-reconstruction module; 2025 preprint on gradient-based grand-canonical optimisation with GNNs and fractional atomic existence (arXiv 2507.19438) — [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10275355/); [arXiv](https://arxiv.org/pdf/2507.19438); [GitLab](https://gitlab.com/bigd4/magus)

**Linfeng Zhang / Weinan E community (AISI Beijing, DP Technology) — DeePMD, DPA**
- DPA-3 / DPA-3.1 / DPA-4.0 (incl. "OpenLAM" variants) on Matbench Discovery; DPA-4.0.1 authors Tiancheng Li (AISI, PKU), Duo Zhang, Linfeng Zhang (AISI Beijing) — [Matbench DPA-4](https://matbench-discovery.materialsproject.org/models/dpa-4.0.1-pro-mptrj)
- DP Technology (深势科技), founded by Zhang (chief scientist; 2020 Gordon Bell Prize for Deep Potential) and Sun Weijie (CEO): Series C >RMB 800M (Dec 2025); joint lab with CATL — [PEdaily](https://news.pedaily.cn/202512/559044.shtml); [QbitAI](https://www.qbitai.com/2025/12/365728.html); [Jiemian](https://www.jiemian.com/article/9950844.html)

**ShanghaiTech / Nanjing — TACE/TECE**
- TECE-OAM-RRA-1.0 (#2, CPS 0.908, added 2026-07-05) and TACE-OAM-L (#7, CPS 0.889): Zemin Xu (ShanghaiTech & Nanjing U), Wenbo Xie, P. Hu (ShanghaiTech); atomic/edge cluster expansion + radial rotary attention — [Matbench TECE](https://matbench-discovery.materialsproject.org/models/tece-oam-rra-1.0); [Matbench TACE](https://matbench-discovery.materialsproject.org/models/tace-oam-l)

**Other Chinese MLIP entrants on Matbench Discovery**
- MatRIS (Yuanchang Zhou, Siyu Hu et al., Institute of Computing Technology CAS); AlphaNet (Bangchen Yin, Tsinghua; with Alibaba DAMO and Cornell co-authors); Eqnorm (Zhejiang Lab) — [MatRIS](https://matbench-discovery.materialsproject.org/models/matris-10m-oam); [AlphaNet](https://matbench-discovery.materialsproject.org/models/alphanet-v1-oam); [Eqnorm](https://matbench-discovery.materialsproject.org/models/eqnorm-mptrj)

**Kairos Materials (开物纪, Beijing) — ex-academic/MSR spin-out**
- Founded 2025 by Ziheng Lu (former MSR AI for Science materials team lead; MatterSim); angel+ round Mar 2026 (IDG, Lanchi, Baidu Ventures per Preqin; 36Kr says Monolith led); Prophet-OAME-MBD (62.3M params, trained on OMat24 + ELEMENTA) is #1 on Matbench Discovery (CPS 0.912, added 2026-09-13) — [36Kr](https://eu.36kr.com/en/p/3736276672279040); [Preqin](https://www.preqin.com/data/profile/asset/kaiwuji/779709); [Matbench Prophet](https://matbench-discovery.materialsproject.org/models/prophet-oame-mbd)

**Shanghai AI Laboratory**
- Intern-S1 (241B-parameter multimodal scientific model, 27 Jul 2025); Intern-S2-Preview (35B) open-sourced 15 May 2026, reportedly the first open general LLM able to generate crystal structures via a real-number prediction module (secondary source) — [DataLearner](https://www.datalearner.com/en/ai-organizations/Shanghai-Artificial-Intelligence-Laboratory); [CSDN repost](https://aicoding.csdn.net/6a69d5a8662f9a54cb95ed3f.html)

**SIAT (Shenzhen)** — partner that synthesised MatterGen's TaCr2O6 — [innovatopia](https://innovatopia.jp/ai/ai-news/46771/) (secondary)

**USTC (Jun Jiang, Yi Luo) — "robotic AI chemist"**
- Whole-process machine chemist: 2 mobile robots, 19 workstations, HPC; high-entropy catalyst formula from 550,000 ratios in ~5 weeks (Chinese press, not peer-reviewed in this source) — [People's Daily 2023](https://paper.people.com.cn/rmrb/html/2023-04/24/nw.D110000renmrb_20230424_1-19.htm); [USTC faculty](https://faculty.ustc.edu.cn/jiangjun1/zh_CN/zhym/160682/list/index.htm)

**Industry: XtalPi (晶泰科技) — molecular/pharma CSP**
- XtalCSP (polymorphs, salts, cocrystals, hydrates/solvates); XtalGazer (Mar 2024) combines CSP + crystallisation recommendation + MicroED; 2025 AIChE abstract; Xtal2 model >100k virtual + 10k experimental data points — [XtalPi](https://en.xtalpi.com/solid-state-chemistry-computation-solutions/); [BioSpace](https://www.biospace.com/xtalpi-unveils-xtalgazer-a-comprehensive-ai-driven-polymorph-selection-platform); [AIChE 2025](https://proceedings.aiche.org/conferences/aiche-annual-meeting/2025/proceeding/paper/synergy-computational-modeling)

### Inferences
- On the main inorganic MLIP benchmark, Chinese groups/companies (Kairos, ShanghaiTech, AISI/DP, ICT CAS, Zhejiang Lab, Tsinghua) collectively now outnumber any other country's entries in the top tier; three of the top seven are China-based.
- Jilin's lineage (CALYPSO → Cond-CDVAE → CrystalFlow) shows a classic CSP group successfully transitioning into generative models, analogous to Pickard's AIRSS→EDDP path.
- Ziheng Lu's Kairos is a Chinese counterpart to the US "academic/big-tech researcher → start-up" pattern.

### Gaps
- Hongjun Xiang (Fudan): no 2025-2026 CSP/generative paper confirmed in this session.
- No confirmed Tsinghua generative-CSP Nature paper for 2025.
- Could not get a Chinese primary source on Yanming Ma's current administrative role (older bio: dean of physics, Jilin).
- CSPBench is from Jianjun Hu (US), not a Chinese group — corrected attribution.

---

## Q4. Japan, Korea, Canada (and Singapore)

### Takeaway
Japan's notable CSP contribution is ShotgunCSP (Ryo Yoshida, ISM, with Panasonic and Oganov) plus the industrial Matlantis/PFP platform (PFN+ENEOS). Korea is led by Seoul National University (Seungwu Han's SevenNet; Yousung Jung, ex-KAIST, synthesizability) and Samsung's EquFlash (#3 on Matbench). Canada's centre of gravity is Toronto's Acceleration Consortium (Aspuru-Guzik, Hattrick-Simpers; C$200M CFREF). Singapore gains Ong (NUS AI Foundry).

### Cited Findings

**Ryo Yoshida (Institute of Statistical Mathematics, Tokyo) — ShotgunCSP**
- "Shotgun crystal structure prediction using machine-learned formation energies" (Liu Chang, Tamaki, Yokoyama, Wakasugi, Yotsuhashi [Panasonic], Kusaba, Oganov, Yoshida), npj Comput. Mater. 10, 298 (2024): non-iterative single-shot screening of element-substitution and symmetry-restricted generated candidates with transfer-learned energy predictor; 93.3% accuracy on 90-structure benchmark; Panasonic/ISM joint press release 4 Mar 2025 — [arXiv](https://arxiv.org/abs/2305.02158v5); [Panasonic](https://news.panasonic.com/global/topics/16896); [ISM PR](https://www.ism.ac.jp/ura/press/ISM2024-08/pr250304.pdf)

**Matlantis / PFP (Preferred Computational Chemistry: PFN + ENEOS JV)**
- PFP v4 trained on >33M structures; LightPFP (MTP trained on PFP data, 10x faster); MRS Fall 2025: r2SCAN-level universal NNP poster and PFN/ENEOS talk on LLM-driven atomic structure generation — [Matlantis US launch](https://matlantis.com/news/matlantis-us-launch); [MRS Fall 2025](https://matlantis.com/en/resources/event-seminar/2025-mrs-fall-meeting-exhibit/)

**Seungwu Han (Seoul National University) — SevenNet**
- SevenNet-MF-ompa (Jaesun Kim, Jisu Kim, Jaehoon Kim, Jiho Lee et al., SNU) on Matbench Discovery — [Matbench](https://matbench-discovery.materialsproject.org/models/sevennet-mf-ompa); [SNU faculty](https://mse.snu.ac.kr/snumse-main/people/faculty/professors/all-research-area/%ed%95%9c%ec%8a%b9%ec%9a%b0p-2)

**Yousung Jung (Seoul National University; KAIST until 2023)**
- Moved to SNU Chemical & Biological Engineering in 2023; LLM-based synthesizability prediction with explanations (JACS 11 Jul 2024; Angew. Chem. 13 Feb 2025); ICLR 2025 AI4Mat invited talk "Synthesizability Predictions Beyond Design"; Berkeley BIDMaP seminar Mar 2025; earlier iMatGen (Matter 2019), invertible representation inverse design with Aspuru-Guzik (Matter 2022; 142 new crystals), CLscore (JACS 2020) — [RSC profile](https://www.rsc.org/people/yousung-jung); [Lifeboat summary](https://lifeboat.com/blog/2025/03/ai-model-transforms-material-design-by-predicting-and-explaining-synthesizability); [ICLR](https://iclr.cc/virtual/2025/10000172); [KAIST dspace](https://dspace.kaist.ac.kr/handle/10203/292010)

**Samsung Electronics (Device Solutions AI Center) — EquFlash**
- EquFlashV2 (Hyuntae Cho, Geonu Kim et al.) #3 on Matbench Discovery (CPS 0.907) — [Matbench](https://matbench-discovery.materialsproject.org/models/equflashv2-45m-oam)

**Alán Aspuru-Guzik & Jason Hattrick-Simpers (Toronto) — Acceleration Consortium**
- Acceleration Consortium: ~100 researchers, C$200M Canada First Research Excellence Fund; >1,000 organic laser molecules tested in two months; Kumacheva & Aspuru-Guzik self-driving nanochemistry lab paper — [U of T Magazine](https://magazine.utoronto.ca/campus/the-lab-that-almost-runs-itself/); [AC news](https://acceleration.utoronto.ca/news/kumacheva-and-aspuru-guzik-paper-highlights-groundbreaking-self-driving-nanochemistry-lab)
- Hattrick-Simpers (U of T MSE + CanmetMATERIALS): 2025 preprints on kernel learning for ternary spinel synthesis (2503.19637), noisy-feature detection for SDLs (2507.16833), human-AI active learning for Li2CO3 crystallisation (2507.19316), robotic porous membranes (2508.10973) — [dblp](https://dblp.dagstuhl.de/pid/298/9224.html); [AC profile](https://acceleration.utoronto.ca/researcher/jason-hattrick-simpers)
- Wolverton is also listed as an Acceleration Consortium person — [AC](https://acceleration.utoronto.ca/people/christopher-wolverton)

**Singapore**
- Ong joining NUS CDE (Sep 2026) to build an AI Foundry for materials — [NUS](https://cde.nus.edu.sg/mse/news/building-an-ai-foundry-to-transform-materials-discovery/)

### Inferences
- Japan's CSP influence is concentrated in a single high-quality method (ShotgunCSP) with strong industry co-authorship (Panasonic), and in Matlantis as a commercial MLIP platform; Japanese academic groups are less visible on open MLIP leaderboards.
- Korea's influence is split between SNU academic MLIPs (SevenNet) and Samsung's industrial ML models, which now rank near the top.

### Gaps
- Mila (Bengio; Crystal-GFN) and other Canadian ML groups not researched in this session.
- No 2025 KAIST generative CSP paper found.
- Aspuru-Guzik's 2025-2026 industry roles not verified in this session.

---

## Q5. Who runs or dominates benchmarks and blind tests

### Takeaway
Three benchmark ecosystems matter: (1) the CCDC-organised molecular CSP blind tests (7th test published 2024, 28 groups/14 countries), (2) Matbench Discovery (Riebesell/Cambridge-LBNL origin, Nat. Mach. Intell. 2025) which has become the de facto leaderboard for universal MLIPs, and (3) newer CSP-specific benchmarks (CSPBench, LeMaterial/Hugging Face datasets, AI4Mat workshops). Matbench leadership in 2025-2026 has rotated from Meta (eSEN/eqV2) to EPFL (PET-OAM-XL, Feb 2026) to ShanghaiTech and Kairos Materials (Sep 2026).

### Cited Findings

**CCDC blind tests (molecular CSP)**
- 7th blind test organised by CCDC; Part 1 (structure generation) Hunnisett et al., Acta Cryst. B 80(6), 517-547 (2024); Part 2 (ranking): 22 groups used periodic DFT-D, MLPs, force fields — DFT-D generally within expected error, one ML model agreed with experiment in many cases; 28 groups from 14 countries overall; CSP Blind Test database released with 171,679 entries from 207 landscapes; seven targets incl. a PXRD-assisted exercise — [PMC review "Triumphs, challenges and insights"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12585482/); [CCDC webinar](https://www.ccdc.cam.ac.uk/community/events/webinars/ccdc-webinar-7th-blind-test-of-csp-methods-triumphs-challenges-and-insights/); [ISTA record](https://research-explorer.ista.ac.at/record/18952)

**Matbench Discovery**
- Riebesell (Cambridge/LBNL), Goodall, Benner, Chiang, Deng, Ceder, Asta, Lee, Jain, Persson; Nat. Mach. Intell. published online 23 Jun 2025 — [arXiv v3](https://arxiv.org/abs/2308.14920v3)
- Live leaderboard (accessed 22 Oct 2026; CPS = 50% F1 + 10% RMSD + 40% κ SRME; 53 eligible models): 1 Prophet-OAME-MBD 0.912 (Kairos Materials); 2 TECE-OAM-RRA-1.0 0.908 (ShanghaiTech/Nanjing); 3 EquFlashV2 0.907 (Samsung); 4 EquiformerV3+DeNS-OAM 0.902 (MIT/Mirror Physics); 5 GRACE-3L-OAM-L 0.900 (ICAMS Bochum); 6 PET-OAM-XL 0.898 (EPFL); 7 TACE-OAM-L 0.889 (ShanghaiTech); 8 eSEN-30M-OAM 0.888 (Meta) — [Matbench Discovery](https://matbench-discovery.materialsproject.org/)
- Also listed: MatterSim (MSR), ORB v3 (Orbital), GNoME, MACE-MPA-0, SevenNet, DPA-3/4, MatRIS, AlphaNet, Eqnorm, HIENet (Texas A&M), Nequix, NequIP/Allegro-OAM — [Matbench models](https://matbench-discovery.materialsproject.org/)
- EPFL: leaderboard "long dominated by models developed at Meta" before PET-OAM-XL — [EPFL](https://actu.epfl.ch/news/a-new-reference-model-for-machine-learning-driven)

**CSPBench (inorganic CSP algorithms)** — Jianjun Hu group (U. South Carolina): 180 structures, 13 algorithms — [arXiv](https://arxiv.org/html/2407.00733v1); later PNcsp+ reports 86.1% space-group and 85.0% structure-match top-5 accuracy on CSPBench — [ITU record](https://research.itu.edu.tr/en/publications/pncsp-a-periodic-number-based-crystal-structure-prediction-method/)

**LeMaterial (Hugging Face organisation)**
- Datasets LeMat-Bulk (1M-10M rows; PBE/PBEsol/SCAN subsets), LeMat-BulkUnique, LeMat-Traj, and LeMat-GenBench (generative-model benchmark embeddings) on Hugging Face — [LeMat-Bulk](https://huggingface.co/datasets/LeMaterial/LeMat-Bulk/tree/2f4bc8a7ba9079de21fa4969e77fa47895de91b3/compatible_scan); [LeMat-GenBench](https://huggingface.co/datasets/LeMaterial/LeMat-GenBench-embeddings/blob/837aceb6f5f1acdefc598318fca329614b35a9d5/README.md)

**Molecular-CSP MLIP benchmarks** — CPOSS209 (Price et al. 2025), OMC25 (Meta + Marom 2025), Nickerson & Johnson blind-test evaluation of MACE-OFF23 (2025) — see Q1/Q2 sources.

**Workshops (community conveners)**
- AI4Mat-NeurIPS-2025 organisers: Santiago Miret, Alexandre Duval, Rocío Mercado, Emily Jin, N M Anoop Krishnan, Kevin Maik Jablonka, Marta Skreta, Stefano Martiniani; included an "AI4Mat Frontiers & Benchmarking" session — [NeurIPS 2025](https://neurips.cc/virtual/2025/workshop/109538)
- AI4Mat-NeurIPS-2026 (12 Dec 2026, Sydney): Miret, Mara Schilling-Wilhelmi, Krishnan, Vijay K Narasimhan, Martiniani — [NeurIPS 2026](https://neurips.cc/virtual/2026/workshop/137487)
- AI4Mat-ICLR-2025: Miret, Skreta, Krishnan, Mercado, Mohamad Moosavi, Martiniani — [ICLR 2025](https://iclr.cc/virtual/2025/workshop/23992)

### Inferences
- Matbench Discovery is the de facto "arena" for universal MLIPs, and leadership changed hands four times in ~18 months (Meta → EPFL → ShanghaiTech → Kairos); score differences at the top (0.898-0.912 CPS) are now small, suggesting saturation of the benchmark.
- The CCDC blind tests remain the authoritative arbiter for molecular CSP; the 8th test (if announced) would be the natural venue to compare FastCSP-style UMA pipelines with traditional DFT-D pipelines — not verified.
- The LeMaterial initiative is commonly associated with the French start-up Entalpic (Alexandre Duval, an AI4Mat 2025 organiser) and Hugging Face, but this link was not confirmed in this session's sources.

### Gaps
- Could not confirm Matbench Discovery's current maintainers (Riebesell's current affiliation, and any Radical AI link) from a primary source.
- No confirmation of an 8th CCDC blind test announcement.
- LeMaterial–Entalpic relationship and LeMat-GenBench paper details not verified from a primary source.
- No source found naming the specific MatterGen alumni at Periodic Labs.
