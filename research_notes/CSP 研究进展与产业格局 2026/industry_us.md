# US/Canada industry landscape: AI-driven crystal structure prediction (CSP) and materials discovery, 2025-2026

Research date: 2026-10-22. Labels used throughout: **[VERIFIED]** = primary document (paper, journal notice, government release, company technical post with data) or multiple independent reputable outlets; **[PRESS]** = secondary/press report, incl. "people familiar" reporting; **[SELF]** = company self-report not independently checked; **[CONFLICT]** = sources disagree.

## Q0. Company-by-company profiles (what they do, results/products, customers, funding, team, verified vs claimed)

### Takeaway
The field splits into (a) big-tech/frontier labs that publish open models and data (Meta, Microsoft, DeepMind, NVIDIA) and mostly sell compute/platform access, and (b) heavily funded "AI scientist + autonomous lab" startups (Periodic Labs, Lila Sciences, Radical AI), plus smaller vertical product companies (Orbital Industries, Chemix, Aionics, Mitra Chem, Mattiq) and incumbent software vendors (Citrine, Schrödinger). Valuations ran far ahead of peer-reviewed discoveries: as of Oct 2026 the most concrete startup science output is Lila's OER-catalyst preprint (Sep 2026) and Periodic's XRD-analysis model (Sep 2026). Big-tech flagship claims (GNoME, A-Lab, MatterGen's TaCr2O6) have all received published novelty critiques or corrections.

### Cited Findings

**Google DeepMind (GNoME, A-Lab, UK lab, Gemini)**
- GNoME (Nature 2023) claimed >380,000 newly predicted stable crystals, "nearly 800 years' worth of knowledge" [VERIFIED as claim] — [C&EN, 2026-10-15](https://cen.acs.org/research-integrity/Google-DeepMind-structures-near-duplicates-questionable/104/web/2026/10); [DeepMind blog](https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/)
- C&EN (Dalmeet Singh Chawla, 2026-10-15) reports a 2026 arXiv analysis finding >15% of structures in the updated GNoME database are near-duplicates of other GNoME entries, ~25% duplicate Materials Project entries, and just under 17% resemble ICSD entries; headline says DeepMind "doesn't comment on inquiries" [PRESS; underlying arXiv not located by me] — [C&EN](https://cen.acs.org/research-integrity/Google-DeepMind-structures-near-duplicates-questionable/104/web/2026/10)
- MIT Tech Review: many DeepMind "novel" materials appeared to be ordered versions of known disordered compounds; the 2023 "millions of new materials" claim "in retrospect, clearly overpromised"; DeepMind says it has since worked with labs worldwide to synthesize AI-identified compounds "with some success" [PRESS] — [MIT TR, 2025-12-15](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
- A-Lab (Berkeley Lab/UC Berkeley with DeepMind, Nature 2023) originally reported 41 novel materials synthesized [VERIFIED as original claim] — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
- **Author Correction published 2026-01-19** (Nature 650, E1): "novel" redefined as new to the prediction platform, not new to science; authors' manual re-analysis of XRD supports the automated conclusion for 36 of 40 reported successes, 4 inconclusive; text of the HTML/PDF updated [VERIFIED] — [Nature correction](https://www.nature.com/articles/s41586-025-09992-y); [PMC12872444](https://pmc.ncbi.nlm.nih.gov/articles/PMC12872444/); [PubMed 41554984](https://pubmed.ncbi.nlm.nih.gov/41554984/); [OSTI](https://www.osti.gov/pages/biblio/3367386-author-correction-autonomous-laboratory-accelerated-synthesis-inorganic-materials)
- **UK automated materials lab**: announced 2025-12-10 as part of an expanded UK-government partnership; DeepMind's "first automated laboratory", in the UK "in 2026", focused on materials science, "fully integrated with Gemini", to "synthesize hundreds of new candidate materials daily" under researcher oversight; targets include superconductors, semiconductors, solar cells, batteries [VERIFIED as announcement] — [DeepMind blog](https://deepmind.google/blog/strengthening-our-partnership-with-the-uk-government-to-support-prosperity-and-security-in-the-ai-era/); [DeepMind on X](https://x.com/GoogleDeepMind/status/1999074624588394809); [Fortune 2025-12-10](https://fortune.com/2025/12/10/google-deepmind-uk-government-partnership-science-clean-energy/)
- Opening status: I found no reputable 2026 confirmation that the lab has opened; a low-quality site claimed a January 2026 opening, while a September 2026 London Daily page still described it as scheduled [CONFLICT/unreliable] — [HumansAreObsolete](https://humansareobsolete.com/articles/deepmind-automated-research-lab-uk-launch-ai-materials-science-january-24-2026); [London Daily](https://londondaily.com/google-deepmind-and-uk-government-launch-first-automated-ai-lab-to-accelerate-scientific-discovery)
- Talent flow out of DeepMind materials team: Ekin Dogus Cubuk (led GNoME science team) co-founded Periodic Labs; Muratahan Aykol and Gowoon Cheon are listed on Periodic's team [VERIFIED] — [Periodic Labs homepage](https://periodic.com/); [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)

**Microsoft (MatterGen, MatterSim, Azure Quantum Elements, Microsoft Discovery)**
- MatterGen: diffusion model for 3D crystals trained on ~608k stable structures (Materials Project + Alexandria); paired with MatterSim MLIP for screening; published in Nature (Jan 2025); code under MIT license; available via Azure AI Foundry Labs [VERIFIED] — [Microsoft Research blog](https://microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai/); [Foundry Labs](https://labs.ai.azure.com/innovations/mattergen/)
- TaCr2O6 synthesized with Prof. Li Wenjie's group at Shenzhen Institutes of Advanced Technology (CAS): design target bulk modulus 200 GPa, measured 169 GPa (<20% error); product showed Ta/Cr disorder [VERIFIED as reported by Microsoft] — [Microsoft Research blog](https://microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai/)
- Critique: Juelsholt, *Materials Horizons* 2026, 13, 5672 (received 2026-02-12, accepted 2026-04-08; DOI 10.1039/d6mh00268d) argues the synthesized disordered Ta1/3Cr2/3O2 is identical to Ta1/2Cr1/2O2 first reported in 1971 and present in MatterGen's training data, i.e., not novel [VERIFIED, peer-reviewed critique] — [Mater. Horiz. DOI](https://doi.org/10.1039/d6mh00268d)
- **Microsoft Discovery** (agentic R&D platform on Azure) reached general availability at Build 2026 (early June 2026) after a ~1-year private preview; named users: BHP (copper leaching), Syensqo (heat-transfer fluids for semiconductor manufacturing), GSK (drug development); Microsoft says it powered development of Majorana 2 [PRESS/SELF] — [HPCwire/AIwire 2026-06-03](https://www.hpcwire.com/aiwire/2026/06/03/microsoft-discovery-reaches-general-availability-for-agentic-scientific-and-engineering-workflows/); [InfoQ](https://www.infoq.com/news/2026/06/microsoft-discovery-majorana-2/); [RCP Mag 2026-06-02](https://rcpmag.com/articles/2026/06/02/microsoft-discovery-reaches-ga.aspx)
- MatterGen/MatterSim described as part of Azure Quantum Elements [PRESS] — [Windows Central](https://www.windowscentral.com/microsoft/microsoft-unveils-mattergen-ai-for-developing-new-materials)

**Meta FAIR Chemistry (OMat24, OMol25, OMC25, UMA, fairchem)**
- OMol25 (>100M DFT molecular calculations) and UMA (Universal Model for Atoms) released May 2025; OMat24 (inorganic, 2024); OMC25 (molecular crystals, arXiv 2508.02651, Aug 2025) [VERIFIED] — [OMol25 arXiv](https://arxiv.org/pdf/2505.08762); [OMat24 arXiv](https://arxiv.org/pdf/2410.12771); [OMC25 arXiv](https://arxiv.org/pdf/2508.02651); [Meta AI blog](https://ai.meta.com/blog/meta-fair-science-new-open-source-releases/)
- UMA-1.2 released March 2026 (~50% faster inference, ~40% better accuracy on OMol test set); UMA playground June 2026; fairchem-core 2.23.0 released 2026-09-24 [VERIFIED/SELF] — [fairchem GitHub](https://github.com/facebookresearch/fairchem); [PyPI](https://pypi.org/project/fairchem-core/2.23.0/)
- MIT TR: "Meta is giving massive amounts away for free" [PRESS] — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
- No Meta commercial materials product or customer found.

**OpenAI**
- "OpenAI for Science" team launched October 2025, led by Kevin Weil [PRESS] — [MIT TR 2026-01-26](https://www.technologyreview.com/2026/01/26/1131728/inside-openais-big-play-for-science/)
- DOE collaboration/MOU tied to the Genesis Mission (materials named among target areas) [VERIFIED as announcement] — [OpenAI](https://openai.com/index/us-department-of-energy-collaboration/)
- July 2026: free model access for 100,000 academic researchers through 2027, part of >$250M commitment to external science [PRESS] — [Axios 2026-07-29](https://www.axios.com/2026/07/29/openai-academics-research-chatgpt-sol)
- Jan 2026 OpenAI report "AI as a Scientific Collaborator" [SELF] — [OpenAI PDF](https://cdn.openai.com/pdf/f4b4a5da-b2de-418d-9fcd-6b293e9dc157/oai_ai-as-a-scientific-collaborator_jan-2026.pdf)
- I found no OpenAI materials-specific model, dataset, lab, or CSP result. OpenAI's frontier model ("GPT-6 Astra") appears in the materials field mainly as a baseline Periodic Labs claims to beat [SELF] — [Periodic](https://periodic.com/news/nature-is-our-learning-environment)

**Anthropic**
- Claude for Life Sciences launched Oct 2025; Jan 2026 expansion of connectors (Benchling, PubMed, 10x Genomics, ChEMBL, etc.); Claude Science launched 2026-06-30 as a beta workbench (not a new model), primarily for computational biology, with chemistry/cheminformatics listed among uses [PRESS] — [TechCrunch 2026-06-30](https://techcrunch.com/2026/06/30/anthropics-claude-science-bets-on-workflow-not-a-new-model-to-win-over-scientists/); [MIT TR 2026-06-30](https://www.technologyreview.com/2026/06/30/1139987/claude-science-is-anthropics-newest-flagship-product/); [STAT](https://www.statnews.com/2026/06/30/anthropic-release-claude-science-ceo-dario-amodei/); [Claude life sciences page](https://claude.com/solutions/life-sciences)
- Anthropic research post on analytical chemistry (NMR, LC-MS analysis) alongside protein design [SELF] — [Anthropic](https://www.anthropic.com/research/Claude-accelerates-protein-design)
- No materials-science/CSP product found. Claude does appear inside materials startups' workflows: Lila's OER preprint discloses Claude Opus 4.6 use for writing and Python analysis scripts; Periodic benchmarks against Claude Code and uses Opus 5 in its LLM-judge ensemble [VERIFIED] — [arXiv 2609.30133](https://arxiv.org/abs/2609.30133); [Periodic](https://periodic.com/news/nature-is-our-learning-environment)

**NVIDIA (ALCHEMI + NVentures)**
- ALCHEMI = suite of NIM microservices/toolkits for chemistry and materials. Batched Geometry Relaxation NIM v1.0.0 released on NGC 2026-03-12 (v1.1.0 current); GPU FIRE2 optimizer with optional cell relaxation; default MLIP MACE-MPA-0; supports MACE, AIMNet2, TensorNet [VERIFIED docs] — [NVIDIA docs](https://docs.nvidia.com/nim/alchemi/alchemi-bgr/1.1.0/ai-transparency-card/overview.html); [NGC](https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/alchemi-bgr/-)
- Vendor speed claims: up to 100x (MACE-MP-0) and 800x (AIMNet2) [SELF] — [NVIDIA dev blog](https://developer.nvidia.com/blog/revolutionizing-ai-driven-material-discovery-using-nvidia-alchemi/)
- SC25 (2025-11-17): batched conformer search and batched MD NIMs announced; early-access users ENEOS (Japan; ~10M immersion-coolant and ~100M OER-catalyst candidates screened in weeks) and Universal Display Corp (New Jersey; OLED materials, "up to 10,000x faster" conformer search) [SELF] — [NVIDIA blog](https://blogs.nvidia.com/blog/ai-science-materials-discovery-sc25/)
- NVentures is a cross-cutting investor: Periodic Labs, Lila (Oct 2025 extension; reported anchor of 2026 Series B talks), Radical AI, Orbital Industries [VERIFIED/PRESS] — see sources under each company.

**Periodic Labs (Menlo Park / SF)**
- Launched 2025-09-30; co-founders Liam Fedus (ex-OpenAI, ChatGPT co-creator) and Ekin Dogus Cubuk (ex-Google DeepMind, GNoME lead); goal: "AI scientist" + autonomous labs; targets higher-Tc superconductors and magnets [VERIFIED] — [Periodic intro](https://periodic.com/news/introducing-periodic-labs); [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
- Team listed on site includes Dzmitry Bahdanau (attention mechanism), Rishabh Agarwal, Janosh Riebesell (Matbench Discovery), Muratahan Aykol, Gowoon Cheon, Xiang Fu, Eric Toberer, Joe Checkelsky, Wei Chen, Costa Huang, Reiichiro Nakano and others; claims founding team co-created ChatGPT, GNoME, OpenAI Operator, attention, MatterGen; SAB: Bertozzi, Kanatzidis, Kivelson, Z.-X. Shen, Wolverton [VERIFIED as company listing] — [Periodic homepage](https://periodic.com/)
- Customer: "helping a semiconductor manufacturer that is facing issues with heat dissipation on their chips... training custom agents for their engineers and researchers to make sense of their experimental data" (unnamed; i.e., AI agents/data analysis, not a sold material) [SELF] — [Periodic homepage](https://periodic.com/)
- **Periodic Neon** (2026-09-15): 1T-parameter model, midtrained + RL on Periodic lab data starting from open-weight Kimi K2.6; peak 1,300 H200s; deployed in Periodic's 24/7 high-throughput Menlo Park labs for XRD analysis [SELF] — [Building Labs that Learn](https://periodic.com/news/building-labs-that-learn); [AI Infrastructure](https://periodic.com/news/ai-infrastructure-at-periodic)
- **FrontierXRD**: internal set of 134 hard lab XRD samples; Neon 55.3% vs Kimi K2.6 base 2.7%; claims Pareto-dominance over GPT-6 Astra and Claude Fable 5.1 on cost/performance; success judged by an LLM-judge ensemble (Opus 5 + GPT-5.6-Sol) with 74.6% agreement with humans vs 77.2% human-human; second, easier held-out set of 198 measurements on held-out chemical systems; Periodic harness gives 3.8x success vs Claude Code + COD/Materials Project/BGMN [SELF; benchmark not public] — [Nature Is Our Learning Environment](https://periodic.com/news/nature-is-our-learning-environment)
- [CONFLICT] one secondary report says the base was Kimi 2.5; Periodic's own post says K2.6 — [explainx](https://explainx.ai/blog/periodic-labs-neon-1t-science-model-2026); [Periodic](https://periodic.com/news/nature-is-our-learning-environment)
- Independent commentary: Jack Clark's Import AI covered Neon; analyst notes stress no independent replication [PRESS] — [Import AI 474](https://jack-clark.net/2026/09/28/import-ai-474-platonic-mindspace-tpus-in-space-zhipu-starts-an-outer-rsi-loop/); [explainx](https://explainx.ai/blog/periodic-labs-neon-1t-science-model-2026)
- Critique: a commentary titled "$7.5 Billion Valuation, Zero Discoveries" says Periodic had released no measured property values, peer-reviewed papers, preprints, or patents [PRESS/opinion] — [note.com](https://note.com/all_zero/n/n3560a02564fd?hl=en)

**Lila Sciences (Cambridge, MA; Flagship Pioneering)**
- Founded 2023 inside Flagship; public launch March 2025; CEO Geoffrey von Maltzahn; "AI Science Factories" (robotic labs controlled by AI); 235,500 sq ft Cambridge lease; John Gregoire (Chief Autonomous Science Officer, ex-Caltech), Rafael Gómez-Bombarelli (CSO physical sciences, MIT professor) [VERIFIED] — [Reuters via Yahoo 2025-10-14](https://finance.yahoo.com/news/exclusive-ai-lab-lila-sciences-101645837.html); [Lila blog 2026-09-25](https://www.lila.ai/news/how-an-ai-run-lab-cracked-open-green-hydrogens-catalyst-problem)
- **arXiv 2609.30133** (submitted 2026-09-24, Jenewein + 20 authors, all Lila employees, Lila-funded, patents may be filed): human-supervised closed loop with >90% automation (combinatorial sputter synthesis, high-throughput electrochemical screening, ML composition-property models, multi-objective active learning, LLM reasoning); 2,942 catalysts across 53 material systems, 26 elements; Ir/Ru-free Pd-oxide OER catalysts (e.g., InMnPdOx, NiTaPdOx); NiTaPdOx lower overpotential than PdOx, both eventually exceeded 0.5 V (PdOx ~200 h, NiTaPdOx ~470 h) [VERIFIED as preprint; not peer reviewed] — [arXiv abs](https://arxiv.org/abs/2609.30133)
- Lila's blog: 2,942 catalysts in three months, six Pd-based families, lead catalyst "matched ruthenium's performance" after 1,000+ h acid testing; 17x faster than standard lab; >90% less hands-on time per sample [SELF] — [Lila blog](https://www.lila.ai/news/how-an-ai-run-lab-cracked-open-green-hydrogens-catalyst-problem)
- [CONFLICT] blog's "1,000+ hours ... matched ruthenium" vs. preprint's degradation past 0.5 V at ~470 h for NiTaPdOx; likely different metrics/conditions, needs reading of full paper.
- Note: this is a composition-screening (thin-film combinatorial) campaign, not crystal structure prediction.
- Company claims "thousands of discoveries across life sciences, chemistry and materials" [SELF] — [Reuters](https://finance.yahoo.com/news/exclusive-ai-lab-lila-sciences-101645837.html)
- July 2026: joined DOE Genesis Mission with Phase I awards for three projects with Caltech, LBNL, Northwestern, Argonne, NLR [SELF] — [Lila news](https://www.lila.ai/news)

**Orbital Industries (formerly Orbital Materials; London + San Francisco)**
- Founded 2022 by Jonathan Godwin (CEO, ex-DeepMind), James Gin-Pollock (CTO), Daniel Miodovnik (COO); rebranded with the Series B; ~50 staff [VERIFIED/PRESS] — [TNW 2026-05-28](https://thenextweb.com/news/orbital-industries-50m-series-b-data-center-cooling); [Fortune 2026-05-28](https://fortune.com/2026/05/28/exclusive-orbital-industries-raises-50-million-series-b-funding-round-ai-to-discover-exotic-new-materials/)
- Products: PFAS-free dielectric cooling fluid for high-density GPUs (designed to ship with next-gen GPUs in 2027) and modular off-site-manufactured data-centre units (claims ~6 months vs 3 years to deploy) [SELF/PRESS] — [TNW](https://thenextweb.com/news/orbital-industries-50m-series-b-data-center-cooling)
- Orb open-source MLIP, Apache 2.0; Orb v3 claims stable 100k-atom simulations on one GPU, 3-6x faster than other universal potentials, 31% error reduction on Matbench Discovery [SELF] — [TNW](https://thenextweb.com/news/orbital-industries-50m-series-b-data-center-cooling)
- AWS strategic agreement since Dec 2024; Orb available via SageMaker JumpStart/AWS Marketplace; no revenue/valuation disclosed [PRESS] — [TNW](https://thenextweb.com/news/orbital-industries-50m-series-b-data-center-cooling)
- Scope note: HQ is London; US presence is the SF office.

**Radical AI (New York)**
- Founded 2024; CEO/co-founder Joseph Krause; ~34 staff (Feb 2026); Gerbrand Ceder became CSO in summer 2025 on sabbatical from UC Berkeley (Ceder was A-Lab PI) [VERIFIED/PRESS] — [NY Governor 2026-01-27](https://www.governor.ny.gov/news/governor-hochul-celebrates-radical-ai-establishing-new-yorks-first-fully-autonomous-materials) (staff count via BK Reader 2026-02-01 coverage of same release); [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
- Jan 27 2026: NY Governor announced NY's "first fully autonomous materials science lab" at Brooklyn Navy Yard Building 20; $4M project, up to $2M ESD tax credits, 115 jobs; ~100 AI-driven experiments/day; inorganic materials; claims up to 370x acceleration [VERIFIED govt release; throughput SELF] — [NY Governor](https://www.governor.ny.gov/news/governor-hochul-celebrates-radical-ai-establishing-new-yorks-first-fully-autonomous-materials)
- DOE Genesis Mission partner; AFWERX contract for high-entropy alloys for hypersonics [SELF/PRESS] — [NY Governor](https://www.governor.ny.gov/news/governor-hochul-celebrates-radical-ai-establishing-new-yorks-first-fully-autonomous-materials)

**Citrine Informatics (Redwood City, CA)**
- Founded 2013; enterprise SaaS for materials/chemicals R&D (AI-guided formulation/property prediction, not CSP); named customers Panasonic, Michelin, LANXESS; June 2026 case: Syensqo scaling AI-driven polymer development on Citrine [PRESS] — [CHEManager](https://chemanager-online.com/en/companies/citrine/); [CB Insights](https://www.cbinsights.com/company/citrine-informatics)
- No 2025-2026 funding round found.

**Mattiq (Skokie/Chicago, IL)**
- Founded 2020 (Northwestern, Chad Mirkin megalibrary tech); nanomaterial megalibraries for catalysts; C&EN (Nov 2025) reports $20M pre-Series A; Tracxn lists $28.6M over 8 rounds incl. grants [PRESS, CONFLICT on totals] — [C&EN 2025-11](https://cen.acs.org/materials/Mattiq-quest-make-billions-nanomaterials/103/web/2025/11); [Tracxn](https://tracxn.com/d/companies/mattiq/__PAelZYBFe_e8_rQfc2uKhPzK-1SfumXCBQvY_wmZgYk)

**Aionics (Evanston, IL / Bay Area)**
- AI electrolyte design ("Ami" platform); shifted in late 2022 from SaaS toward a biotech-like model developing electrolyte formulations for battery makers; early customers reported: Cellforce (Porsche subsidiary), Cuberg (later Northvolt) [PRESS] — [Latitude Media](https://latitudemedia.com/news/how-to-monetize-ai-in-the-battery-sector); [Yahoo/TechCrunch](https://au.news.yahoo.com/generative-ai-creeping-ev-battery-170621100.html)
- 2026 funding [CONFLICT]: Tracxn lists a Series A on 2026-03-31 with $7.81M total; Caplight lists a seed round dated 2026-04-08 with $11.75M total; Fobi lists a $20M Series A — [Tracxn list](https://tracxn.com/d/artificial-intelligence/ai-startups-in-materials-tech-in-us-canada/__A1b2ZhP3TzFOXbr6Md5IdnE2N8reqUGAq6rYHVbYi6Y/companies); [Caplight](https://www.caplight.com/company/aionics)

**Chemix (Sunnyvale, CA)**
- AI-designed EV battery cells; designs cells, contracts manufacturing partner, sells cells at a premium; first customer UBCO (electric motorcycles, multi-million contract); $20M Series A April 2024 led by Ibex (Mayfield, Porsche Ventures, KDDI CVC, BNP Paribas, Berkeley SkyDeck) [PRESS] — [TechCrunch](https://techcrunch.com/?p=2535818); [CITRIS](https://citris-uc.org/chemix-raises-20m-in-series-a-funding/); [Mayfield](https://www.mayfield.com/?p=12364)

**Mitra Chem (Mountain View, CA)**
- AI-enabled cathode materials (iron-based incl. LMFP); GM led $60M Series B (first close $40M, Aug 2023) with co-development for Ultium; $20M Series A Nov 2021 led by Social Capital [VERIFIED for 2023] — [GM investor release](https://investor.gm.com/news-releases/news-release-details/gm-invests-ai-and-battery-materials-innovator-mitra-chem); [InsideEVs](https://insideevs.com/news/682309/gm-leads-series-b-funding-mitra-chem/)

**"Osmium AI"**
- No company by that name found; likely refers to **Osium AI** (YC-backed, founders Sarah Najmark and Luisa Bouneder, $2.6M seed; materials property-prediction SaaS) — location inconsistent (Paris vs SF), so may be out of US/Canada scope — [TechCrunch 2023-11-22](https://techcrunch.com/2023/11/22/osium-ai-uses-artificial-intelligence-to-speed-up-materials-innovation/amp); [YC](https://www.ycombinator.com/companies/osium-ai)

**Schrödinger (NYC) - molecular CSP for pharma**
- Peer-reviewed CSP method (Nature Communications 2025): systematic packing search + ML force fields + hierarchical ranking; large-scale validation and blind study (Bayer flupyradifurone); original limitation to Z'=1 [VERIFIED] — [Nat. Commun.](https://www.nature.com/articles/s41467-025-57479-1)
- Release 2026-2: full CSP release with anhydrous Z'=2 and monohydrates; 2026-3 adds salts, solvates, co-crystals; product page claims retrospective test on 66 drug-like molecules / 137 experimental polymorphs with near-100% most-stable-form accuracy [SELF] — [Release notes 2026-2](https://www.schrodinger.com/life-science/download/release-notes/?release=661473&software_suite=16496); [CSP product page](https://www.schrodinger.com/platform/products/crystal-structure-prediction/)
- Offered both as software and as modeling services [SELF] — [Modeling Services](https://www.schrodinger.com/platform/products/modeling-services/)
- Presenting at IUCr2026 (Calgary, Aug 11-18 2026) [SELF] — [Schrödinger IUCr2026](https://www.schrodinger.com/materials-science/resources/event/iucr2026/)

**XtalPi (US operations)**
- HK-listed (2228.HK), Shenzhen/Beijing-headquartered; Jan 2023 named Sarah Trice COO of US operations to establish an autonomous lab in Greater Boston; no 2026 confirmation of Boston lab status found; H1-2026 net loss RMB224.9M; materials is a minor revenue line vs drug discovery [VERIFIED for filings/PR] — [PR Newswire 2023](https://www.prnewswire.com/news-releases/xtalpi-names-new-coo-for-us-operations-bringing-its-autonomous-labs-to-boston-in-continued-global-expansion-301719012.html); [2026 interim results](https://www.prnewswire.com/news-releases/xtalpi-holdings-announces-2026-interim-results-302855288.html)

**CCDC (Cambridge Crystallographic Data Centre; UK charity, but central to US pharma CSP)**
- Runs the CSP Blind Tests (7th launched Oct 2020), the CSP Consortium (industry + academia + solution providers; data standards for CSP outputs), and the Crystal Form Consortium (12 member organisations, mostly major pharma); industry partnerships led to CSD-Theory product for managing CSP landscapes [VERIFIED] — [CCDC industry-led development](https://www.ccdc.cam.co.uk/community/ccdc-for-the-community/partnerships-and-initiatives/industry-led-development/); [CCDC CSP Consortium blog](https://www.ccdc.cam.co.uk/discover/blog/csp-consortium-ccdc/)

### Inferences
- For CSP specifically (inorganic structure generation/prediction), the US commercial value is captured mostly as (i) open models feeding cloud platforms (Microsoft, NVIDIA, Meta) and (ii) pharma polymorph-risk software (Schrödinger, CCDC tools). The well-funded startups have largely moved "downstream" of CSP to experiment-centric loops (synthesis + characterization + LLM reasoning), consistent with critiques that pure prediction overstated novelty (GNoME, A-Lab, MatterGen all corrected or challenged in 2026).
- Periodic's Neon is notable less as materials discovery than as evidence that lab-data RL can make an LLM better at a characterization task (XRD phase ID) — the exact step whose automation failed in A-Lab's original claims.
- The DeepMind talent drain (Cubuk, Aykol, Cheon to Periodic; Godwin earlier to Orbital) suggests the startup ecosystem is now the main US locus of GNoME-lineage expertise.

### Gaps
- Whether DeepMind published any new materials paper in 2026: none found in searches; C&EN (Oct 2026) reports DeepMind declining comment. Cannot confirm absence definitively.
- UK DeepMind lab: no reliable confirmation of opening date/location as of Oct 2026.
- Title/authors of the 2026 arXiv GNoME duplicate analysis (only known via C&EN; site could not be fully fetched).
- MatterSim license, GNoME data license, OMat24 license not confirmed in this session.
- Osmium AI identity unresolved.

## Q1. Which US companies have demonstrated a closed loop from prediction to synthesis to characterization, with what throughput and published evidence?

### Takeaway
Only Lila Sciences has a public (preprint) demonstration of a startup closed loop with quantified throughput (2,942 catalysts in ~3 months, >90% automation). Radical AI and Periodic Labs claim operational autonomous labs (~100 experiments/day; "24/7 high-throughput") but have published no discovery papers. The best-documented US loop remains the academic A-Lab, now corrected. DeepMind's UK lab is outside US scope and unverified as open.

### Cited Findings
- Lila: human-supervised closed loop, >90% automation, 2,942 catalysts / 53 systems / 26 elements; Pd-oxide OER catalysts; preprint only — [arXiv 2609.30133](https://arxiv.org/abs/2609.30133); company says three months and 17x standard-lab speed [SELF] — [Lila blog](https://www.lila.ai/news/how-an-ai-run-lab-cracked-open-green-hydrogens-catalyst-problem)
- Periodic: loop of (1) hypothesize target from stability/property prediction, (2) predict synthesis, (3) characterize (XRD); labs in Menlo Park run 24/7; Neon deployed for XRD analysis; no discovered material disclosed [SELF] — [Periodic](https://periodic.com/news/building-labs-that-learn). In Dec 2025 MIT TR said Periodic was "just beginning to set up its lab in San Francisco" — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
- Radical AI: Brooklyn lab ~100 AI-driven experiments/day, inorganic materials; earlier lab "almost fully autonomous" per company [SELF] — [NY Governor](https://www.governor.ny.gov/news/governor-hochul-celebrates-radical-ai-establishing-new-yorks-first-fully-autonomous-materials); [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
- A-Lab (LBNL/UC Berkeley, with DeepMind predictions): 2026-01-19 correction — 36/40 successes upheld on manual re-analysis, novelty narrowed to "new to platform" [VERIFIED] — [Nature](https://www.nature.com/articles/s41586-025-09992-y)
- Microsoft: prediction (MatterGen) -> synthesis/characterization by external partner SIAT (Shenzhen, China; not US) for one compound; novelty challenged — [MSR blog](https://microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai/); [Mater. Horiz. 2026](https://doi.org/10.1039/d6mh00268d)
- Mattiq: high-throughput megalibrary synthesis/screening of nanomaterial catalysts (throughput claims not captured here) — [C&EN](https://cen.acs.org/materials/Mattiq-quest-make-billions-nanomaterials/103/web/2025/11)

### Inferences
- "Closed loop" in 2026 startup practice increasingly means composition/process optimization with ML + LLM reasoning, rather than CSP-first de novo structure discovery; XRD phase identification is the recognized bottleneck (Periodic's focus; A-Lab's correction).
- No US startup has yet published a peer-reviewed new-crystal discovery from its own autonomous lab.

### Gaps
- Radical AI and Periodic have no public papers/preprints on lab results I could find; throughputs are self-reported.
- Mattiq throughput figures not retrieved (C&EN fetch failed).

## Q2. Business models in use (platform/software, foundry/service, product company, partnership network)

### Takeaway
Four models coexist: (1) cloud platform/software (Microsoft Discovery/Azure, NVIDIA ALCHEMI NIMs, Citrine, Schrödinger, Meta's free models as ecosystem play); (2) AI-lab-as-partner/IP creation (Lila "Catalyst" platform access + "Creation" partnerships/spin-outs; Periodic custom agents for industry); (3) product companies selling materials or devices (Orbital cooling fluid and modular data-centre units; Chemix battery cells; Mitra Chem cathodes; Aionics electrolyte formulations); (4) government/defense contract-funded labs (Radical AI AFWERX, Genesis Mission). Investors publicly prefer selling materials.

### Cited Findings
- Lila: two offerings on its site—"Catalyst" (access its "operating system for science") and "Creation" (partner to generate discoveries, launch products, create companies); CEO: Lila won't take molecules to the clinic or scale energy breakthroughs itself, partners and Lila-platform startups will; plans enterprise-software access to models + automated labs [SELF] — [Lila blog page nav](https://www.lila.ai/news/how-an-ai-run-lab-cracked-open-green-hydrogens-catalyst-problem); [Reuters](https://finance.yahoo.com/news/exclusive-ai-lab-lila-sciences-101645837.html)
- Periodic: "AI research and deployment company"; deploys custom agents to an unnamed semiconductor manufacturer; Cubuk publicly undecided between licensing discoveries vs selling products; costs dominated by GPUs more than labs [SELF] — [Periodic](https://periodic.com/); [Latitude Media podcast](https://www.latitudemedia.com/news/catalyst-inside-a-300-million-bet-on-ai-for-materials-discovery/)
- Orbital: pivoted from carbon-capture/SAF chemistry to selling data-centre products; open-source Orb as platform asset; AWS partnership is "primary near-term revenue anchor" for cooling fluid [PRESS] — [TNW](https://thenextweb.com/news/orbital-industries-50m-series-b-data-center-cooling)
- Chemix: designs cells, partner manufactures, sells at premium — [TechCrunch](https://techcrunch.com/?p=2535818)
- Aionics: moved from SaaS to biotech-style formulation development — [Latitude Media](https://latitudemedia.com/news/how-to-monetize-ai-in-the-battery-sector)
- Microsoft Discovery GA as Azure platform — [HPCwire](https://www.hpcwire.com/aiwire/2026/06/03/microsoft-discovery-reaches-general-availability-for-agentic-scientific-and-engineering-workflows/)
- NVIDIA sells NIM microservices (enterprise) + invests via NVentures — [NVIDIA blog](https://blogs.nvidia.com/blog/ai-science-materials-discovery-sc25/)
- Investor view (MIT TR): ideal is "a new material that we can sell... we get revenue off selling the material" — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)
- Schrödinger: CSP as software license and as modeling service — [Schrödinger](https://www.schrodinger.com/platform/products/modeling-services/)

### Inferences
- Startups with near-term revenue tend to sell a product into an urgent niche (PFAS-free coolants, battery cells); "superintelligence" labs rely on mega-rounds and platform/partnership promises. Data-centre thermal management is a recurring commercial wedge (Orbital fluid; Periodic's chip heat-dissipation customer; ENEOS immersion coolants via ALCHEMI; Syensqo heat-transfer fluids via Microsoft Discovery).

### Gaps
- No disclosed revenue figures for any of the startups.

## Q3. Which have paying industrial customers, and in which sectors?

### Takeaway
Named, paying industrial customers are concentrated in incumbents (Citrine, Schrödinger, Microsoft, NVIDIA) and product startups (Chemix, Aionics, Mitra Chem/GM). Periodic reports one unnamed paying semiconductor customer; Lila reports "interest" without named customers; Orbital's revenue anchor is AWS.

### Cited Findings
- Periodic: paying customers in semiconductors reported (March 2026); company site describes one unnamed semiconductor manufacturer (chip heat dissipation) [PRESS/SELF] — [Periodic](https://periodic.com/); [SVIC profile](https://siliconvalleyinvestclub.com/companies/periodic/)
- Lila: interest from energy, semiconductors, drug development, none named (Oct 2025) [SELF] — [Reuters](https://finance.yahoo.com/news/exclusive-ai-lab-lila-sciences-101645837.html)
- Orbital: AWS strategic agreement (data-centre cooling/water) — [TNW](https://thenextweb.com/news/orbital-industries-50m-series-b-data-center-cooling)
- Radical AI: US Air Force AFWERX contract (high-entropy alloys, hypersonics); aerospace/defense investors RTX Ventures, Eni — [NY Governor](https://www.governor.ny.gov/news/governor-hochul-celebrates-radical-ai-establishing-new-yorks-first-fully-autonomous-materials); [Pulse 2.0](https://pulse2.com/radical-ai-55-million-series-seed-raised-for-advancing-materials-research/)
- Microsoft Discovery: BHP (mining/copper leaching), Syensqo (specialty chemicals/semiconductor heat-transfer fluids), GSK (pharma) — [HPCwire](https://www.hpcwire.com/aiwire/2026/06/03/microsoft-discovery-reaches-general-availability-for-agentic-scientific-and-engineering-workflows/)
- NVIDIA ALCHEMI early access: ENEOS (energy), Universal Display (OLED) — [NVIDIA](https://blogs.nvidia.com/blog/ai-science-materials-discovery-sc25/)
- Citrine: Panasonic, Michelin, LANXESS, Syensqo (chemicals, tires, electronics, polymers) — [CHEManager](https://chemanager-online.com/en/companies/citrine/)
- Chemix: UBCO (e-motorcycles), premium EV makers — [Mayfield](https://www.mayfield.com/?p=12364)
- Aionics: Cellforce (Porsche), Cuberg — [Yahoo/TechCrunch](https://au.news.yahoo.com/generative-ai-creeping-ev-battery-170621100.html)
- Mitra Chem: GM (co-development, Ultium) — [GM](https://investor.gm.com/news-releases/news-release-details/gm-invests-ai-and-battery-materials-innovator-mitra-chem)
- Schrödinger CSP: pharma/agrochem (Bayer blind study) — [Nat. Commun.](https://www.nature.com/articles/s41467-025-57479-1)
- CCDC Crystal Form Consortium: 12 member organisations, mostly major pharma — [CCDC](https://www.ccdc.cam.co.uk/community/ccdc-for-the-community/partnerships-and-initiatives/industry-led-development/)

### Inferences
- Sectors with demonstrated willingness to pay: semiconductors/data-centre thermal, batteries/EV, specialty chemicals, mining, pharma solid-form, defense.

### Gaps
- Contract values and whether Microsoft/NVIDIA named users are paying vs pilot are not disclosed. Names of pharma companies using molecular CSP commercially (beyond Bayer study) not retrieved.

## Q4. Funding rounds 2025-2026 (dates, sizes, leads, valuations) and notable hires/departures

### Takeaway
2025-2026 saw unprecedented rounds: Periodic $300M seed (Sep 2025) then a reported ~$500M at $7.5B (mid-2026, unconfirmed by company); Lila $350M Series A (Sep-Oct 2025, >$1.3B) then reported ~$2B Series B talks at ~$8.5B pre (June 2026, unconfirmed close); Orbital $50M Series B (May 2026); Radical AI $55M seed+ (Jul 2025). NVentures participated in all four.

### Cited Findings
- **Periodic Labs**: $300M seed announced 2025-09-30; backers a16z, Felicis, DST, NVentures, Accel; angels Bezos, Elad Gil, Eric Schmidt, Jeff Dean [VERIFIED backers list] — [Periodic](https://periodic.com/). Lead [CONFLICT]: a16z per Maginative/Latitude; Felicis per others — [Maginative](https://www.maginative.com/article/periodic-labs-launches-with-300m-to-build-an-ai-scientist/); [Founders' Daily Briefing](https://founders-daily-briefing.beehiiv.com/p/periodic-labs-raises-300m). Seed valuation reported $1.3B [PRESS] — [Dealroom](https://app.dealroom.co/news/note/periodic-labs-eyes-7b-valuation-fivefold-jump-in-six-months). Radical Ventures (Toronto) also backed the $300M round [PRESS] — [The Logic](https://thelogic.co/briefing/radical-ventures-backs-periodic-labs-in-us300m-round-to-build-ai-scientists/)
- Periodic 2026: early talks at ~$7B reported (spring 2026); Forbes 2026-05-07: raising $500M at $7.5B; Forge lists Series A 2026-06-03 at $7.5B post; investor tear sheet lists AMP PBC (Anjney Midha) as Series A lead; no company announcement found [PRESS, unconfirmed] — [Forbes](https://www.forbes.com/sites/iainmartin/2026/05/07/former-openai-researcher-to-raise-500-million-for-ai-science-startup/); [Forge](https://forgeglobal.com/periodic-labs_ipo/); [SVIC tear sheet](https://siliconvalleyinvestclub.com/es/companies/periodic/tear-sheet.pdf); [TFN](https://techfundingnews.com/former-openai-and-deepmind-researchers-eye-7b-valuation-for-ai-startup-periodic-labs/)
- **Lila Sciences**: $200M seed (Mar 2025) — [BioPharma Dive](https://www.biopharmadive.com/news/lila-flagship-ai-superintelligence-startup-seed/742213/); $235M Series A (2025-09-15) then $115M extension incl. NVentures (2025-10-14) = $350M Series A, $550M total, >$1.3B valuation; investors Flagship, General Catalyst, ADIA subsidiary [VERIFIED] — [Reuters](https://finance.yahoo.com/news/exclusive-ai-lab-lila-sciences-101645837.html); [Lila news](https://www.lila.ai/news). Bloomberg 2026-06-03: in talks to raise ~$2B at ~$8.5B pre-money, anchored by CalPERS and NVentures; terms not final [PRESS] — [Bloomberg Law](https://news.bloomberglaw.com/private-equity/lila-sciences-said-in-talks-for-funds-at-8-5-billion-valuation). [CONFLICT] FinSMEs dates a "$350M Series A" to June 2026 — likely the 2025 round re-reported — [FinSMEs](https://www.finsmes.com/2026/06/lila-sciences-raises-350m-in-series-a-funding.html)
- **Orbital Industries**: $50M Series B, 2026-05-28, led by Plural (Ian Hogarth), with NVentures, Radical Ventures, Compound, Fly Ventures; valuation undisclosed [VERIFIED] — [Fortune](https://fortune.com/2026/05/28/exclusive-orbital-industries-raises-50-million-series-b-funding-round-ai-to-discover-exotic-new-materials/); [TNW](https://thenextweb.com/news/orbital-industries-50m-series-b-data-center-cooling). [CONFLICT] Seedtable lists Compound as lead — [Seedtable](https://seedtable.com/companies/orbital-industries/funding-rounds/series-b-2026-05)
- **Radical AI**: $55M seed+ (July 2025) led by RTX Ventures with NVentures, Noa, Infinite Capital, Eni Next, AlleyCorp [VERIFIED] — [Pulse 2.0](https://pulse2.com/radical-ai-55-million-series-seed-raised-for-advancing-materials-research/); a ~$60M Series A is "reported" without date [PRESS, unconfirmed] — [R&D World](https://www.rdworldonline.com/how-radical-ai-is-building-a-self-driving-materials-lab/); NY state up to $2M tax credits (Jan 2026) — [NY Governor](https://www.governor.ny.gov/news/governor-hochul-celebrates-radical-ai-establishing-new-yorks-first-fully-autonomous-materials)
- **Aionics**: 2026 round [CONFLICT] (Tracxn Series A 2026-03-31; Caplight seed 2026-04-08, $11.75M total) — [Caplight](https://www.caplight.com/company/aionics)
- Context (non-US): CuspAI (Cambridge, UK) reportedly raised $450M Series B in July 2026 [PRESS] — [Novusearch](https://note.com/novusearch/n/naf3cf850cfe6?hl=en)
- **Hires/departures**: Cubuk left Google DeepMind in 2025 to co-found Periodic; Fedus left OpenAI — [Latitude Media](https://www.latitudemedia.com/news/catalyst-inside-a-300-million-bet-on-ai-for-materials-discovery/); Gerbrand Ceder (UC Berkeley, A-Lab) became Radical AI CSO summer 2025 — [MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/); Periodic team includes ex-DeepMind GNoME/A-Lab researchers Aykol and Cheon, Bahdanau, Riebesell, and academic PIs Toberer and Checkelsky — [Periodic](https://periodic.com/); Kevin Weil leads OpenAI for Science (Oct 2025) — [MIT TR](https://www.technologyreview.com/2026/01/26/1131728/inside-openais-big-play-for-science/); Lila: Gregoire (ex-Caltech) and Gómez-Bombarelli (MIT) in leadership — [Lila](https://www.lila.ai/news/how-an-ai-run-lab-cracked-open-green-hydrogens-catalyst-problem)

### Inferences
- Valuation step-ups (Periodic ~$1.3B -> ~$7.5B; Lila ~$1.3B -> ~$8.5B pre) occurred within ~8 months, before peer-reviewed discoveries; this is the core "verified vs claimed" tension highlighted by critics.
- NVIDIA is the common strategic investor and also a supplier (GPUs, ALCHEMI), giving it exposure across the whole landscape.

### Gaps
- Whether Periodic's AMP-led Series A and Lila's Series B have closed: not confirmed by company as of 2026-10-22.
- No 2025-2026 rounds found for Citrine, Chemix, Mitra Chem, Mattiq (beyond C&EN Nov 2025 total).

## Q5. Open-source releases (models, datasets, benchmarks) and licenses

### Takeaway
Open releases come mainly from big tech (Meta fairchem/UMA/OMol25/OMat24/OMC25; Microsoft MatterGen; DeepMind GNoME database) and one startup (Orbital's Orb, Apache 2.0). Frontier-lab-style startups (Periodic, Lila) keep models, data, and benchmarks proprietary (Neon and FrontierXRD are internal). Licenses vary: code is usually MIT/Apache; Meta's model checkpoints use a custom FAIR Chemistry License with an acceptable-use policy.

### Cited Findings
- fairchem code MIT; OMol25 dataset CC-BY-4.0; OMol25/UMA checkpoints under FAIR Chemistry License v1 (updated 2025-05-14) incl. acceptable use policy; OMC25 models "commercially permissive license (with some geographic and acceptable use restrictions)" — [fairchem GitHub](https://github.com/facebookresearch/fairchem); [HF OMol25](https://huggingface.co/facebook/OMol25); [OMC25 arXiv](https://arxiv.org/pdf/2508.02651)
- UMA-1.2 (Mar 2026), fairchem-core 2.23.0 (2026-09-24) — [fairchem GitHub](https://github.com/facebookresearch/fairchem); [PyPI](https://pypi.org/project/fairchem-core/2.23.0/)
- MatterGen: MIT license — [Windows Central](https://www.windowscentral.com/microsoft/microsoft-unveils-mattergen-ai-for-developing-new-materials); [Foundry Labs](https://labs.ai.azure.com/innovations/mattergen/)
- Orbital Orb (v3): Apache 2.0 on GitHub — [TNW](https://thenextweb.com/news/orbital-industries-50m-series-b-data-center-cooling)
- GNoME database: publicly released; DeepMind says it was released "for community study"; updated version analyzed in 2026 — [C&EN](https://cen.acs.org/research-integrity/Google-DeepMind-structures-near-duplicates-questionable/104/web/2026/10)
- NVIDIA ALCHEMI NIMs: free-to-download containers on NGC but under NVIDIA enterprise terms; default model MACE-MPA-0 pulled from Hugging Face — [NVIDIA docs](https://docs.nvidia.com/nim/alchemi/alchemi-bgr/1.1.0/ai-transparency-card/overview.html)
- Periodic Neon: no open-weight release mentioned; FrontierXRD internal (134 lab samples) — [Periodic](https://periodic.com/news/nature-is-our-learning-environment)
- Lila: preprint public; no code/data release noted; patents may be filed — [arXiv 2609.30133](https://arxiv.org/abs/2609.30133)

### Inferences
- Startups that open-source (Orbital) use it as distribution (AWS Marketplace) while monetizing products; those with mega-rounds treat lab data as the moat ("experiments produce data that exists nowhere else" — Periodic).

### Gaps
- Exact licenses for MatterSim, OMat24 dataset/checkpoints, GNoME data (believed CC-BY family but not confirmed in this session), and Orb v3 model weights (TNW says Apache 2.0 for Orb; weight-specific terms unchecked).
- Matbench Discovery standings for Orb v3 / UMA / MatterSim not independently checked.
