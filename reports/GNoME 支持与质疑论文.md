# 三年文献把 GNoME“新晶体”还原为旧结构换元素

截至 2026 年 10 月 22 日，围绕 Google DeepMind 的 GNoME（Merchant et al., *Nature* 624, 80–85, DOI 10.1038/s41586-023-06735-9）和配套 A-Lab 论文（Szymanski et al., *Nature* 624, 86–91, DOI 10.1038/s41586-023-06734-w）的文献，已经形成一条相当一致的质疑链。这条链的核心结论是：**GNoME 的大多数“发现”是已知结构型上的元素替换，其中相当一部分是现实中以无序形式存在的已知化合物的人为有序化版本**；A-Lab 报告的“新”材料大多被误识别，或者早已为人所知。四种互相独立的方法得出了同一结论：专家晶体学检索、机器学习无序分类（80–84% 的 GNoME 组分倾向无序）、群–子群对称性匹配（A-Lab 的 GNoME 目标中 60% 有已知无序母相）、连续几何不变量审计。官方层面，**只有 A-Lab 论文在 2026 年 1 月 19 日发布了 Author Correction**：把“新”改写为“对预测平台而言是新的，不一定对科学是新的”，36/40 的成功在人工复核后成立，4 个结论不确定，另删去 1 个曾混入训练数据的化合物。**GNoME 论文本身至今没有任何更正或编者按**；DeepMind 在 2024 年 4 月表示“坚持论文全部主张”，2026 年 10 月对 C&EN 的问询不予置评，同时数据集经过多次未附说明的修订。支持一侧，以 GNoME 为直接目标的前瞻性合成只有寥寥几例，且每一例都有已发表的新颖性异议；下游使用数量庞大，但几乎全部是计算筛选。最容易被误读的是 2026 年 10 月利物浦审计的“70–78%”：它只比几何、**不比元素种类**，衡量的是原型复用；几何和化学同时吻合、真正与已知晶体重复的条目只占 **0.15–0.37%**。

## 无序问题已成共识，“新颖度”有多少取决于怎么量

文献中已有定论的部分可以压缩为三点。第一，0 K DFT 不计构型熵，会把化学性质相近的阳离子（镧系、Zr/Hf 等）排到各自独立的晶位上，产生低对称的有序近似结构，而现实中这些元素共占晶位，形成更高对称的已知固溶体或合金。这一机制先由 Cheetham & Seshadri 与 Leeman 等人在 2024 年定性提出，此后被 Jakob 等（2025）、Yamazaki 等（2026）和 Widdowson 等（2026）用三种不同方法定量复现，是整个文献中最稳固的发现。第二，A-Lab 的“新颖”主张已被作者正式收回，改为“对平台而言是新的”。第三，GNoME 原始的 736 个“独立实现”结构是与 ICSD 的回溯匹配，不是 GNoME 发表后受其指引的新合成。

仍未定论的部分同样清楚。“GNoME 里有多少真正的新材料”没有共识数字：答案从“几乎没有”（Cheetham & Seshadri 抽样）到“组分几乎全是新的”（NIST 团队：5,000 条样本中 0.0% 与 1980 年后的 ICSD 共用约化化学式）都有，差别来自度量对象不同（局部几何、嵌入空间社区、组分）。DeepMind 没有发表任何重新检视或正面辩护新颖性的论文。A-Lab 更正承认了新颖性问题，但没有回应无序问题；批评者对此仍不满意。Materials Project 截至 2026 年 6 月只收录了约 11.7 万个经 r2SCAN 复算的 GNoME 材料，约占宣称 38.1 万的 31%（本报告推算），但 MP 没有说明其余部分是 r2SCAN 下不稳定，还是只是尚未处理。

| 问题 | 状态 | 主要依据 |
|---|---|---|
| GNoME/A-Lab 预测中大量为已知无序相的有序近似 | 已定（四种方法一致） | A1、A2、A7、A8、A3 |
| A-Lab“新材料”是否对科学为新 | 已定：作者更正为“对平台为新” | C1 |
| A-Lab 36 个成功产物是否本质上是已知无序相 | 未定：更正未回应 | A2、C1、A6 |
| GNoME 中真正新颖、可信、有用的化合物数量 | 未定，无共识数字 | A1、A3、A9 |
| GNoME 论文是否被更正 | 已定：没有（截至 2026-10-22） | C2 |
| GNoME 训练数据是否被后续通用势函数使用 | 未发现证据；训练集从未公开 | B16、B17 |

## 阅读状态标注与时间线

每个条目都标注了研究笔记作者的核查方式：**【原文已读】**表示在来源处阅读了全文或相关章节；**【摘要/部分】**表示只读了摘要、付费墙前的导语或元数据页；**【二手】**表示只通过其他来源或搜索摘要得知。标有“配套笔记”的条目来自同期 CSP 研究笔记，仅作交叉印证。每条也注明了同行评审状态。条目编号（A/B/C）与下文三个部分对应。

| 日期 | 事件 | 类别 | 核查 |
|---|---|---|---|
| 2023-11-29 | GNoME 与 A-Lab 论文在 *Nature* 在线发表；DeepMind 博客宣布“220 万新晶体”；MP 上线含 2,047 条的 GNoME Explorer | 原始主张 | 原文已读 |
| 约 2023-11-30 | Palgrave 在 X 上质疑 A-Lab 烧绿石等物相鉴定 | 质疑 | 二手 |
| 2023-12-01 | GNoME 数据集首次修订：重新施加过滤器，去除非物理能量 | 官方 | 原文已读 |
| 2023-12-02 | Ceder 在 LinkedIn 回应，承认 MnAgO2、Mg3Ni3MnO8 并非新物质 | 官方回应 | 原文已读 |
| 2023-12-12 | *Nature* News（Peplow）报道争议，2024-01-09 更新 | 新闻 | 摘要/部分 |
| 2024-01-08 | Leeman/Schoop/Palgrave 发布 ChemRxiv 预印本 | 质疑 | 二手（DOI 经 Nature News） |
| 2024-02-03 | NequIP-GNoME 登上 Matbench Discovery（F1 0.81） | 支持/基准 | 原文已读 |
| 2024-03-07 | Leeman 等在 *PRX Energy* 发表：43 个产物中 42 个有重大问题 | 质疑 | 原文已读 |
| 2024-04-08 | Cheetham & Seshadri 在 *Chem. Mater.* 发表：10 条随机条目全部有 ICSD 类似物 | 质疑 | 原文已读 |
| 2024-04-11 | 404 Media、The Register 报道；DeepMind：“坚持论文全部主张” | 新闻/官方 | 原文已读 |
| 2024（月份不详） | Anosova, Kurlin & Senechal 在 *IUCrJ* 首次公布 GNoME 文本重复 CIF 计数 | 质疑 | 二手 |
| 2024-06 | Kurlin 组预印本 arXiv:2406.12894：大量体积相同到小数点后八位的 CIF 对 | 质疑 | 二手（配套笔记） |
| 2024-08-21 | GNoME 数据集放宽到距凸包 1 meV/atom，规模扩至 >52 万 | 官方 | 原文已读 |
| 2024-10-16 | Miura 等（含 DeepMind 作者）在 *JACS* 报道铯氯化物探索合成 | 支持 | 摘要/部分 |
| 2024-11-15 | Energy-GNoME 预印本：>33,000 个能源候选材料 | 下游使用 | 摘要/部分 |
| 2024-11-21 | GNoME 数据集最后一次修订（“GNoME2”，554,054 条） | 官方 | 原文已读 |
| 2024-12-12 / 12-20 | MP 弃用 2,047 条旧集，加入 15,483 条 r2SCAN GNoME 材料，并要求接受 BY-NC 许可 | 官方/MP | 原文已读 |
| 2024-12-18 | Aykol 等在 *Nat. Comput. Sci.* 发表非晶前驱体结晶预测 | DeepMind 后续 | 二手 |
| 2025-04-18 | MP 再加入约 30,000 条 GNoME 材料 | 官方/MP | 原文已读 |
| 2025-05-14 | Xin 等：554,054 条中 92,310 条可能可合成 | 下游使用 | 摘要/部分 |
| 2025-10-23 | Jakob 等在 *Adv. Mater.* 发表：80–84% 的 GNoME 组分倾向无序 | 质疑 | 原文已读 |
| 2025-11-03 | Prein 等可合成性流程：16 个目标中 7 个合成成功 | 下游使用 | 原文已读 |
| 2025-12-15 | MIT Technology Review：DeepMind 称合成 AI 化合物“取得一些成功” | 官方 | 二手（配套笔记） |
| 2025-12-16 | C&EN 报道：批评者呼吁撤回两篇 *Nature* 论文 | 新闻 | 摘要/部分 |
| 2026-01-19 | A-Lab Author Correction（*Nature* 650, E1） | 官方更正 | 原文已读 |
| 2026-01-29 | C&EN：“更正了，但问题仍未回答” | 新闻 | 摘要/部分 |
| 2026-03-05 | Zhang…Schoop“压力测试”预印本 | 质疑 | 摘要/部分 |
| 2026-03-24 | Naganuma & Kitagawa：MnFeCo4Si2 实验确认 | 支持 | 摘要/部分 |
| 2026-04-23 | Yamazaki 等：群–子群“家族树”，60% 的 A-Lab GNoME 目标有已知无序母相 | 质疑 | 原文已读 |
| 2026-06-08 | MP 新增 74,052 条，GNoME 材料累计约 11.7 万 | 官方/MP | 原文已读 |
| 2026-06-29 | Nguyen 等（NIST）：GNoME 与 MP 理论结构在结构“盆地”中不可区分 | 质疑 | 原文已读 |
| 2026-09-01 | Song & Cheng：PRIS 规则解释 GNoME 富含低对称结构 | 质疑 | 摘要/部分 |
| 2026-10-09 | Widdowson, Kurlina, Anosova & Kurlin 审计，arXiv:2610.13885 | 质疑 | 原文已读 |
| 2026-10-15 | C&EN 报道审计；DeepMind 不予置评 | 新闻/官方 | 摘要/部分 |
| 2026-10-22 | GNoME *Nature* 页面仍无任何更正、编者按或变更历史 | 官方 | 原文已读 |

## 第一部分 质疑：四种独立方法都指向“有序化的已知无序相”

质疑的演进路径很清楚：2024 年是专家对少量样本做定性检查，2025–2026 年转为覆盖全库的统计。下面按发表日期排列。

### 2024 年：专家抽样已经发现系统性问题

**A14. [约 2023-11-30 起] Robert Palgrave 与 Leslie Schoop 在 X/Twitter 上的讨论。** 社交媒体，未经同行评审。【二手：搜索摘要，未打开 X 页面】Palgrave 最早的帖子质疑了 A-Lab 对烧绿石等物相的鉴定，直接促成 Ceder 的回应（C3）。2024 年 1 月 8 日，两个课题组宣布联合发布 ChemRxiv 分析，Schoop 写道 “compositional disorder in materials cannot be neglected”（[Palgrave](https://twitter.com/Robert_Palgrave/status/1744383962913394758)；[Schoop Lab](https://twitter.com/SchoopLab/status/1744391934024491181)）。

**A2. [2024-03-07] Leeman, J., Liu, Y., Stiles, J., Lee, S. B., Bhatt, P., Schoop, L. M. & Palgrave, R. G.** “Challenges in High-Throughput Inorganic Materials Prediction and Autonomous Synthesis.” *PRX Energy* 3, 011002（2024 年 1 月 30 日收稿）。DOI 10.1103/PRXEnergy.3.011002；预印本 ChemRxiv doi 10.26434/chemrxiv-2024-5p9j4（约 2024-01-08）。同行评审观点文章，开放获取。【原文已读】针对的是 A-Lab。作者用 A-Lab 自己使用的 GSAS-II 软件，以经验拟合的峰形重做了 A-Lab 公开 PXRD 图谱的 Rietveld 精修，并在 ICSD 中检索已知物相（常常是无序相）。结论是：在 36 个“成功”加 7 个“部分成功”中，**42 个存在重大问题**，唯一例外是 CaFe2(PO4)2O，因此 “no new materials have been discovered in that work”；**约三分之二的“成功”很可能是预测有序化合物所对应的已知成分无序版本**。在 36 个成功产物中，四类错误的计数为：未建模峰或反应不完全 18/36；用阳离子无序 CIF 替换预测结构以迁就实测图谱 8/36（笔记中原文提取被截断为“8/3…”，36 为推断）；无序版本已存在于 ICSD 24/36；把已知化合物报告为新物质 3/36（MnAgO2、Y3In2Ga3O12、CaFe2(PO4)2O）。作者还指出，部分目标是在 2021–2023 年间被报道的，晚于 GNoME 2021 年的数据库快照（[PRX Energy](https://doi.org/10.1103/PRXEnergy.3.011002)）。

**A1. [2024-04-08] Cheetham, A. K. & Seshadri, R.** “Artificial Intelligence Driving Materials Discovery? Perspective on the Article: Scaling Deep Learning for Materials Discovery.” *Chem. Mater.* 36(8), 3490–3495。DOI 10.1021/acs.chemmater.4c00643。同行评审观点文章，开放获取。【原文已读】这是第一篇直接针对 GNoME 本身的同行评审批评。方法有三：人工检查 MP“GNoME Explorer”2,047 条中的前 250 条；统计全部 384,870 条“Stable Structure”条目的空间群分布并与 ICSD 对比；随机抽取 10 条，按元素、晶格参数和空间群在 ICSD 中检索。结果是 **10 条全部能找到 ICSD 结构类似物**，通常对称性更高，只有 1 条空间群相同。空间群分布明显异常：GNoME 前四名全是非中心对称空间群，合计约占 34%（仅 Pm 就有 49,037 条，占 12.7%）；ICSD 中最常见的 Pnma 和 P21/c 各约占 8%，在 GNoME 中只占 1.56%（第 16 名）和 0.7%。放射性元素也很多：含 Pm、Ac、Pa 的有 18,138 条，含 Tc、Np、Pu 的另有 23,529 条，仅锕化合物在 Stable Structure 库中就约 6,754 条。他们给出的机制是 0 K DFT 忽略构型熵，并列举了对应关系，例如 TbSmSeO2 → La2SeO2、K3Nd(AsO4)2 → K3Nd(PO4)2、AcEr3(B6)4 → LaB6 超结构，还指出 TbSmF30 中含 F2 分子。结论是 “scant evidence for compounds that fulfill the trifecta of novelty, credibility, and utility”。值得注意的是，他们同时承认 “the computational approach delivers credible overall compositions”，认为方法本身是可靠的（[PMC 全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044265/)；[ACS](https://pubs.acs.org/doi/10.1021/acs.chemmater.4c00643)）。

**A13. [2024-04-11] 媒体报道：404 Media（J. Koebler）与 The Register（T. Claburn）。** 新闻。【原文已读】Palgrave 称 H2O11 之类的 DeepMind 预测 “do not look right ... basic quality control has not happened”；Cheetham 称论文 “falls way short” 于对实验材料科学家有用；Seshadri 说 “Google has missed the mark here”（[404 Media](https://www.404media.co/google-says-it-discovered-millions-of-new-materials-with-ai-human-researchers/)；[The Register](https://www.theregister.com/2024/04/11/google_deepmind_material_study/)）。

**A12. [2024–2026] Kurlin 组的早期同行评审工作。**【二手：仅经 arXiv:2610.13885 引用得知，未打开全文】Anosova, O., Kurlin, V. & Senechal, M., “The importance of definitions in crystallography,” *IUCrJ* 11, 453–463 (2024)：据 A3 所述，其表 1 已报告 GNoME1 中 2,311 个文本完全相同的 CIF，以及一组 9 个几何相同、元素互换的 CIF，看来是最早公开发表的 GNoME 重复计数。Widdowson & Kurlin, *Sci. Rep.* 15, 27588 (2025) 提出“局部新颖度距离”（LND），并应用于 A-Lab 的 43 个产物。Widdowson & Kurlin, *SIAM J. Appl. Math.* 86, 898–918 (2026) 提出用逐点距离分布检测近重复（均据 [arXiv:2610.13885](https://arxiv.org/abs/2610.13885) 引用）。另据配套笔记，该组 2024 年 6 月的预印本 arXiv:2406.12894 已发现数千对体积相同到小数点后八位的 GNoME CIF，C&EN 转述其“可能超过 10% 为近重复”【二手，配套笔记】（[arXiv:2406.12894](https://arxiv.org/pdf/2406.12894)）。

### 2025–2026 年：从抽样转向全库统计

**A7. [2025-10-23 在线；2026-01-22 刊期] Jakob, K. S., Walsh, A., Reuter, K. & Margraf, J. T.** “Learning Crystallographic Disorder: Bridging Prediction and Experiment in Materials Discovery.” *Advanced Materials* 38(5)。DOI 10.1002/adma.202514226。同行评审。【原文已读，Europe PMC 全文】作者在 ICSD 上训练 RNN/LSTM 组分分类器，只凭组分预测替代型无序，准确率约 90%，然后把它用于 2025 年 2 月 GitHub 版本中全部 554,054 个 GNoME 结构，没有做额外筛选。在 70% 和 50% 两个分类阈值下，**MP 中倾向无序的组分占 39–47%，GNoME 中占 80–84%**，即 GNoME “potentially being dominated by disordered systems”。交叉验证方面：A-Lab 化合物中有已知无序相的 23 个（共 35 个）里，模型判定 16 个（70%）为无序；Cheetham & Seshadri 的 10 条随机条目中判定 9 条无序。作者自己也说明，GNoME 相对训练数据存在很大的协变量偏移（[PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12822528/)）。

**A5. [2025-12-16] Chawla, D. S.** “The duplicates that haunt crystallography databases.” *C&EN*。新闻特稿，付费墙。【摘要/部分】导语为 “Researchers call for retraction of two recent Nature studies about AI-generated crystals”，正文开头称该研究“已获约 1,000 次引用”，“faces calls for retraction”，因为许多被声称新颖的晶体其实是重复（[C&EN](https://cen.acs.org/research-integrity/Duplicate-structures-haunt-crystallography-databases/103/web/2025/12)）。

**A6. [2026-01-29] Chawla, D. S.** “‘Nature’ robot chemist paper corrected, but some questions remain unanswered.” *C&EN*。新闻，付费墙。【摘要/部分；正文内容为二手】导语称 *Nature* 已更正这篇被高引的机器人化学家论文，“but critics say their concerns haven't been fully addressed”。据搜索引擎对正文的摘要，Palgrave 和 Schoop 并不完全满意，无序问题没有得到回应，Ceder 未回复置评请求；该摘要对 Palgrave 是否仍要求撤稿的表述含糊（[C&EN](https://cen.acs.org/research-integrity/Nature-robot-chemist-paper-corrected/104/web/2026/01)）。

**A10. [2026-03-05 v1；2026-06-18 v2] Zhang, X., Lee, S. B., Chatterjee, S., …, Widdowson, D. E., …, Kurlin, V. A., Wilson, S. D., Bernevig, B. A. & Schoop, L. M.（17 位作者）** “New Crystal Structures Hide in Plain Sight: A Stress Test for AI-Guided Materials Discovery.” arXiv:2603.05613。预印本。【摘要/部分】作者通过探索性合成发现了新结构型 GdNiSn4 和 LuNiSn4，并发现 MatterGen 与 DiffCSP++ 在给定采样预算和匹配容差下都无法复现它；结论是 AI 模型 “have so far produced new chemical compositions within known structural families rather than genuinely new structures”。该文测试的是生成模型而非 GNoME，但属于 Schoop/Kurlin 质疑脉络（[arXiv](https://arxiv.org/abs/2603.05613)）。

**A8. [2026-04-23] Yamazaki, S., Huang, Y., Petersen, M. H., Nong, W., Hippalgaonkar, K. et al.** “Navigating Order-(Dis)Order Family Trees via Group-Subgroup Transitions.” arXiv:2604.21386。预印本。【原文已读，HTML 全文】作者把群–子群对称关系与 ICSD 做自动匹配，用以识别“无序母相的有序子结构”。A-Lab 报告成功合成的 35 个 GNoME 物相中，**22 个有实验报道过的无序母相**（由本框架或 Leeman 等找到），其中本框架单独找到 21 个，即 60%；对 Leeman 等只是怀疑无序的 3 例（如 K2TiCr(PO4)3），也找到了母相。作者认为，只对照有序结构数据库做新颖性检查会导致 “a systematic overestimation of discovery rates”。反直觉的一点是：在 50,000 条 GNoME 稳定结构样本中，能匹配到已知无序母相的只占 0.73%（MP-20 为 23.27%）。作者明确表示这 “should not be interpreted as evidence that computational structures are intrinsically less prone to disorder”，而是 ICSD 对奇异化学体系覆盖不足所致。另一发现是，不受对称性约束的生成模型产出已知无序母相子结构的频率，是受对称性约束模型的 2–4 倍（[arXiv](https://arxiv.org/abs/2604.21386)）。

**A9. [2026-06-29] Nguyen, D., Cao, K., Chu, B., Lemoff, N., Kienzle, P. & Ratcliff II, W.** “Computed materials proposals depart from the structural memory of experimental discovery.” arXiv:2606.30967，已投 *npj Comput. Mater.*。预印本。【原文已读，HTML 全文】作者把 167,500 条 ICSD 条目嵌入 32 维结构相似性空间，发现 82.9% 的实验新化学式落入既有的结构“社区”，然后把 5,000 条 GNoME 公开数据样本投影到冻结的历史地图上。GNoME 落入“盆地”的比例在 1990 年地图上为 26.6%，在 2010 年地图上为 36.4%，与 MP 理论结构（28.8%、35.8%）统计上不可区分，远低于留出的 ICSD（52.0–60.6%）。排序为：留出 ICSD > MatterGen > {GNoME ≈ MP 理论结构} > JARVIS > Alexandria。另一项结果是 **0.0% 的 GNoME 样本与 1980 年后的任何 ICSD 条目共用约化化学式**，作者称这 “quantifies one aspect of the Cheetham and Seshadri critique”，即 Dy5HoAl24Os5Pd2Pt 这类元素数很多的组分（[arXiv](https://arxiv.org/abs/2606.30967)）。

**A11. [2026-09-01] Song, Z. & Cheng, L.** “Autonomous discovery of new structure-plausibility laws for explainable and rapid crystal diagnosis and screening.” arXiv:2609.01209。预印本。【摘要/部分】由智能体推导出的“无机结构合理性规则”（PRIS）解释了 “why GNoME remains enriched in rare low-symmetry structures”，与 A1 的空间群发现相互独立地呼应（[arXiv](https://arxiv.org/abs/2609.01209)）。

**A3. [2026-10-09] Widdowson, D. E., Kurlina, T. V., Anosova, O. D. & Kurlin, V. A.** “Necessary conditions for benchmarking next-generation AI in materials discovery.” arXiv:2610.13885 [cond-mat.mtrl-sci]，利物浦大学与 UCL，44 页。预印本，未经同行评审。【原文已读，完整 PDF】这是 C&EN 在 2026 年 10 月报道的审计，也是迄今规模最大的 GNoME 新颖性分析。方法上，作者用 AMD/PDD/PDA 等连续几何不变量、等距集（isoset）和 EMD 距离做全对全比较。数据有两版：“GNoME1”为 2023-11-29 版，384,938 条；“GNoME2”为 2024-11-21 版，554,054 条。两版共有 301,413 条，GNoME1 中有 83,525 条被删除，另新增 252,641 条。参照集为截至 2021 年 3 月的 ICSD 和 Materials Project（MP v2026.04.13，查询时设 include_gnome=False）。

GNoME 内部的重复情况如下。GNoME1 中有 **2,311 个文本完全相同的 CIF**（1 组四重、43 组三重、1,089 对），与原论文“已用 pymatgen 逐对去重”的说法相矛盾。忽略元素标签后几何完全相同的条目有 3,248 个（0.84%）。按冗余率（多余条目数 ÷ 数据集大小）计：GNoME1 在 τ = 1e-10 Å 时为 0.437%，在 τ = 0.01 Å 时为 12.438%（67,488 个条目分布在 19,610 组中，最大一组 352 个）；GNoME2 分别为 0.057% 和 **15.178%**（108,286 个条目、24,194 组，最大一组 723 个）。这些都是只看几何的匹配。若要求元素也相同（“geochemical” 匹配），GNoME1 在 1e-10 Å 时为 0.306%，在 0.01 Å 时为 1.156%；**GNoME2 直到 0.01 Å 都没有这类重复**。

与已知晶体的重叠见下一小节，那里的数字最需要谨慎解读。数据集修订方面，GNoME1 中与已知**有序** ICSD 晶体匹配的条目，有 92.7% 在 GNoME2 中被撤下；与已知**无序**晶体匹配的条目只撤下 40.4%；全体条目的背景撤除率为 21.7%。与 MP 匹配的 155 条撤下了 99.4%，有化学同质重复的条目撤下了 95.3%。作者据此推断，DeepMind 的过滤器能剔除已知有序晶体，却识别不出已知无序晶体的有序化版本。GNoME2 也新引入了几何重复：273 组中有 62 组由 GNoME1 的单例扩展而来，32 组完全由新条目组成。配套笔记还记录了一个细节：2024 年 8 月 21 日撤下的 10,201 条在 11 月 21 日又被恢复，因此各版本并非逐步嵌套【配套笔记，同一论文原文已读】。

其他发现：按 Ac、Np、Pa、Pm、Pu、Tc 加上 Bi、Th、U 计，含放射性元素的条目在 GNoME1 中有 80,235 条（20.8%），在 GNoME2 中有 108,020 条（19.5%）。作者还列举了非物理条目：83cc15ef46（H2O11，“chaotically located molecules”）、一个 K 原子没有任何近邻的 eed3027c1e、一个密度只有 0.18 g/cm³ 的条目、以及含水分子的 8175bee583（H2ORb2Se）。作者提出在宣称新材料之前必须满足四项“必要条件”，包括连续的局部新颖度距离和键长合理性检查（[arXiv:2610.13885](https://arxiv.org/abs/2610.13885)）。该文还核查了下游的“实验确认”，见第二部分 B3、B4。

**A4. [2026-10-15] Chawla, D. S.** “Google DeepMind AI crystallography database includes near duplicate structures and unrealistic compounds.” *C&EN*。新闻，付费墙。【摘要/部分：标题、副标题、要点和开头几段】副标题为 “After hyping previous claims, tech giant doesn't comment on inquiries about lack of novelty in database of AI-generated crystals”（[C&EN](https://cen.acs.org/research-integrity/Google-DeepMind-structures-near-duplicates-questionable/104/web/2026/10)）。GNoME 笔记没能读到正文引用的百分比。配套笔记【二手】记录的 C&EN 数字是：更新版数据库中 >15% 为 GNoME 内部近重复，约 25% 与 MP 条目重复，略低于 17% 与 ICSD 相似。这三个数字分别与 A3 的 15.178%（0.01 Å 内部冗余率）、24.1%（0.02 Å 内与 MP）和 16.3%（0.02 Å 内与 ICSD）吻合，看来 C&EN 引用的是 0.01–0.02 Å 的严格阈值数字，而且**同样只比几何、不比元素**（此对应关系为本报告的推断）。

### 如何读 2026 年 10 月审计的“70–78%”

A3 的标题数字是 “over 60% of predictions in GNoMEs 1&2 are geometrically close to known crystals in the ICSD and MP up to 0.05Å”，实际范围为 62.8–78.4%。这个数字**完全不考虑元素种类**：它比较的是去掉元素标签后的原子几何。一个把 La 换成 Tb、把 P 换成 As 的条目，只要原子排布与某个已知晶体足够接近，就算作“匹配”。所以它量化的是**原型复用**，即“已知结构型配新元素标签”，而不是“重复发现了已知化合物”。作者本人对高几何重叠的解释，正是 GNoME 的方法会“拿已有晶体，把化学元素换成相似元素”。几何与化学同时吻合、真正与已知晶体重复的条目只占 **0.15%（GNoME2）到 0.37%（GNoME1）**；GNoME2 中也只有 5.3% 的条目与任何 ICSD 条目共用元素集合，0.9% 共用组分。阈值也很关键：0.05 Å 时为 70–78%，收紧到 0.01 Å 就降到 3–5.5%。中位数 GNoME2 条目距最近的 ICSD 结构 0.034 Å、距最近的 MP 结构 0.03 Å，恰好落在两个阈值之间，因此结果对阈值选择高度敏感。

| 度量（相对截至 2021-03 的已知晶体） | 是否比较元素 | GNoME1 | GNoME2 |
|---|---|---|---|
| PDA[100] EMD ≤ 0.05 Å，对 ICSD | 否 | 69.7% | 73.1% |
| PDA[100] EMD ≤ 0.05 Å，对 MP | 否 | 74.8% | 78.4% |
| PDA[100] EMD ≤ 0.02 Å，对 ICSD / MP | 否 | 15.2% / 21.3% | 16.3% / 24.1% |
| PDA[100] EMD ≤ 0.01 Å，对 ICSD / MP | 否 | 3.3% / 5.1% | 3.0% / 5.5% |
| pymatgen StructureMatcher RMSD < 0.05，对 ICSD / MP | 否 | 62.8% / 71.1% | 66.1% / 74.3% |
| 几何 ≤ 0.05 Å **且**化学相同（ICSD + MP） | 是 | 1,315 + 155 = 0.37% | 824 + 1 = 0.15% |
| GNoME 内部冗余率，τ = 1e-10 Å | 否 | 0.437% | 0.057% |
| GNoME 内部冗余率，τ = 0.01 Å | 否 | 12.438% | 15.178% |
| GNoME 内部化学同质冗余率，1e-10 / 0.01 Å | 是 | 0.306% / 1.156% | 0 / 0 |

数据来源：[arXiv:2610.13885](https://arxiv.org/abs/2610.13885)。“冗余率”指多余条目数除以数据集大小，而不是落在重复组中的条目占比。

因此，“大多数 GNoME 结构是重复的”这种说法高估了这篇论文。准确的表述是：GNoME 的几何大多是已知晶体的几何（“GNoME's geometry is largely the geometry of known crystals”），而字面意义上的已知化合物重复很少，并且大多已在两次数据修订之间被清除；唯一没被清除的，是已知无序相的有序近似。

## 第二部分 支持与下游使用：前瞻性实验确认屈指可数

支持 GNoME 的证据分为两类：原论文自带的回溯验证，以及 2023 年之后的前瞻性合成。后者只找到三例，而且都有已发表的新颖性异议。下游使用数量很大，但几乎全部停留在计算层面。

**B1. [2023-11-29] Merchant, A., Batzner, S., Schoenholz, S. S., Aykol, M., Cheon, G. & Cubuk, E. D.** “Scaling deep learning for materials discovery.” *Nature* 624, 80–85。DOI 10.1038/s41586-023-06735-9。同行评审。【原文已读】论文的主张是：220 万个结构相对 MP 稳定，其中 “381,000 entries live on the updated convex hull as newly discovered materials”，稳定晶体合计 42.1 万。验证依据是 “Of the experimental structures aggregated in the ICSD, 736 match structures that were independently obtained through GNoME”，以及 MP 快照之后新增的 3,182 个组分中，有 2,202 个出现在 GNoME 数据库里，其中 91% 结构吻合。应用筛选方面，论文给出约 52,000 个层状材料（此前相对 MP 稳定的约 1,000 个），以及 528 个有前景的锂离子导体（“a 25 times increase”）。所有候选都来自 2021 年 3 月（MP）和 2021 年 6 月（OQMD）的数据库快照。需要强调，**736 是与 ICSD 的回溯匹配，不是 GNoME 指引下的新合成**（[Nature](https://www.nature.com/articles/s41586-023-06735-9)）。

**B2. [2023-11-29] Merchant, A. & Cubuk, E. D.,** DeepMind 博客 “Millions of new materials discovered with deep learning.” 企业博客。【原文已读】博客宣布 “2.2 million new crystals – equivalent to nearly 800 years' worth of knowledge”，称 “External researchers ... have independently created 736 of these new structures experimentally in concurrent work”，并承诺向 MP 贡献 38 万个材料。截至 2026-10-22，页面上没有任何更正或更新说明（[DeepMind 博客](https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/)）。

**B16. [2024-02-03] Matbench Discovery 条目 “NequIP-GNoME”（PR #84）。** 基准排行榜条目，本身不是同行评审论文（Matbench Discovery 论文为 arXiv:2308.14920）。【原文已读，模型 YAML】全测试集上 F1 0.81、DAF 4.81、精确率 0.825、召回率 0.796、MAE 0.034 eV/atom，有 1,744 个缺失预测；在唯一原型子集上 F1 0.829、DAF 5.523。模型有 1,624 万参数，YAML 注明 “The model weights and training set are unpublished”。DeepMind 在 2024 年 4 月对 404 Media 说 GNoME 被 MP 评为 “top-of-the-line”，指的就是这个基准。此后领先者已升至 F1 约 0.92–0.93（二手；配套笔记从仓库读到 2026 年 4 月 EquiformerV3+DeNS-OAM 为 0.931）（[gnome.yml](https://github.com/janosh/matbench-discovery/blob/main/models/gnome/gnome.yml)；[排行榜](https://matbench-discovery.materialsproject.org/)）。

**B15. [2024-02-08] Liu, M. & Meng, S.** “Recent Breakthrough in AI-Driven Materials Science: Tech Giants Introduce Groundbreaking Models.” arXiv:2402.05799；*Mater. Futures* 3, 027501 (2024)，DOI 10.1088/2752-5724/ad2e0c。同行评审评论。【摘要/部分】对 GNoME 数据集做了说明性梳理（“11 things you would like to know”），立场中性偏介绍（[arXiv](https://arxiv.org/abs/2402.05799)）。

**B3. [2024-10-16] Miura, A., Aykol, M., Cubuk, E. D., Merchant, A., Batzner, S., Kohli, P. et al.（与北海道大学、广岛大学、JASRI/SPring-8、京都大学、AIST 合作）** “Efficient Exploratory Synthesis of Quaternary Cesium Chlorides Guided by In Silico Predictions.” *J. Am. Chem. Soc.* 146, 29637ff。DOI 10.1021/jacs.4c10294。同行评审，含 DeepMind 作者。【摘要/部分：经 JST 新闻稿，未打开论文】据 JST 新闻稿，研究以大规模第一性原理预测为起点，先用原位同步辐射 XRD 快速筛选，再做中子和电子衍射，得到“三种新的铯氯化物”（[JST 2024-10-21](https://www.jst.go.jp/pr/announce/20241021/index.html)）。异议来自 A3：论文检索的是 MP、OQMD 和 GNoME 合并的 0 K 凸包；成功合成的 Cs2LiCrCl6、Cs2LiFeCl6、Cs2LiIrCl6、Cs2LiRhCl6、Cs2LiRuCl6、Cs2NaDyCl6 **都不在 GNoME1 或 GNoME2 中**；不纯的 Cs2LiVCl6 对应 GNoME1 条目 66ae3fec06，它是 ICSD 002064（CsCuCl3，1974 年发表）的近重复，EMD 约 0.064 Å（[arXiv:2610.13885](https://arxiv.org/abs/2610.13885)）。“三种新化合物”与“六个成功组分加一个不纯组分”之间的出入尚未厘清，可能是两边统计口径不同（“新”与“成功合成”）。

**B6. [2024-11-15] De Angelis, P., Trezza, G., Barletta, G., Asinari, P. & Chiavazzo, E.** “Energy-GNoME: A Living Database of Selected Materials for Energy Applications.” arXiv:2411.10125；*Energy and AI* (2025)，DOI 10.1016/j.egyai.2025.100605。同行评审。【摘要/部分】以 GNoME 的 38 万多个“新稳定晶体”为起点，用 ML/DL 分类器和回归器筛出 **33,000 多个**潜在能源材料（热电、正极、钙钛矿），并预测 zT、带隙和电压。期刊版据称约 38,500 个（二手）。纯计算（[arXiv](https://arxiv.org/abs/2411.10125)）。

**B8. [2024-12-15] Chen, W., Lin, Z., Zhang, X., Zhou, H. & Zhang, Y.** “AI-Driven Accelerated Discovery of Intercalation-type Cathode Materials for Magnesium Batteries.” arXiv:2412.11032；*J. Energy Chem.* 108, 40–46 (2025)，DOI 10.1016/j.jechem.2025.03.085。同行评审。【摘要/部分】用 CGCNN 电压模型筛选 MP 和 GNoME 中的 15,308 个稳定镁化合物，得到 160 个电压 >3.0 V、容量 >800 Ah/L 的候选，再用 NequIP 分子动力学选出 23 个高镁电导率材料。纯计算（[arXiv](https://arxiv.org/abs/2412.11032)）。

**B13. [2025-05-14] Xin, Y., Liu, P., …, Wang, Y. & Ma, Y.** “Bridging Theory and Experiment in Materials Discovery: Machine-Learning-Assisted Prediction of Synthesizable Structures.” arXiv:2505.09161。预印本。【摘要/部分】从 554,054 个 GNoME 候选中筛出 92,310 个（约 17%）“可能可合成”。这是预测，不是合成计数。搜索摘要称该文通过 ICSD 比对指出有 17 个 GNoME 结构近期已被合成（二手，未在全文中核实）（[arXiv](https://arxiv.org/abs/2505.09161)）。

**B10. [2025-08 预印本；2026 刊出] Sanna, A., Cerqueira, T. F. T., Cubuk, E. D., Errea, I., Fang, Y.-W. et al.** “Search for thermodynamically stable ambient-pressure superconducting hydrides in GNoME database.” arXiv:2508.19781（v3 2026-03-17）；*Commun. Phys.* 9, 94 (2026)，DOI 10.1038/s42005-026-02552-4。同行评审，含 DeepMind 作者 Cubuk。【摘要/部分】先用 ML 预筛，再对数千个 GNoME 氢化物做 Eliashberg 级第一性原理计算，找到 25 个 Tc > 4.2 K 的立方氢化物，最高 17 K，作者认为它们 “likely to be experimentally accessible”。没有报告合成（[arXiv](https://arxiv.org/abs/2508.19781)）。

**B14. [2025-10-09 预印本；2026 刊出] Kim, S., Jeon, G., Hwang, S., Lee, J., Jung, J., Han, S. & Kang, S.** “Are diffusion models ready for materials discovery in unexplored chemical space?” arXiv:2510.09406；*Patterns* (2026)，DOI 10.1016/j.patter.2026.101537。同行评审。【摘要/部分】把 GNoME 当作“非常见”化学空间（稀土多、化学计量非常规）的基准，发现 MatterGen 和 DiffCSP 在这里不如在氧化物、氮化物集上有效（[arXiv](https://arxiv.org/abs/2510.09406)）。

**B5. [2025-11-03] Prein, T., O'Leary, W., Savvidou, A. F., Bourneix, E., Laulainen, J. E. M. et al.** “A Synthesizability-Guided Pipeline for Materials Discovery.” arXiv:2511.01790。预印本。【原文已读，HTML 全文】这是目前最干净的前瞻性检验。作者对 MP、GNoME 和 Alexandria 中约 440 万个候选计算组分加结构的可合成性分数，在 3 天内实验了 16 个高分目标：**7 个（44%）合成出目标相**，2 个（12%）得到已知或预测的多晶型，7 个（44%）失败。但 9 个命中中，3 个与 MP/ICSD 中标为已合成的结构几乎相同，另有 3 个在 ICSD 中有相似结构（MP 却标为理论结构）；只有 3 个没有 ICSD 结构。其中之一是来自 GNoME 的 **Nd3BTeO9**，近乎纯相（P63；a = 8.761 Å，c = 5.553 Å；与 Bi3BTeO9 同构），不过 2023 年已有论文报道过它的合成，只是没有给出 CIF。作者的 PCA 分析还显示，GNoME 集中在组分空间的狭窄区域，而 GNoME 密度最高处的平均可合成性反而下降（[arXiv](https://arxiv.org/abs/2511.01790)）。

**B7. [2025-11-27 v1；2026-02-09 v2] Alghamdi, N., de Angelis, P., Asinari, P. & Chiavazzo, E.** “Screening novel cathode materials from the Energy-GNoME database using MACE machine learning force field and DFT.” arXiv:2511.22504。预印本。【摘要/部分】用基础 MACE 力场加 DFT+U 在 Energy-GNoME 中筛选 Na、K、Mg、Ca 离子正极。纯计算（[arXiv](https://arxiv.org/abs/2511.22504)）。

**B11. [2025-12-11] Itani, S., Zhang, Y., Itani, R. & Zang, J.** “Large Language Models for Superconductor Discovery.” arXiv:2512.10847。预印本。【摘要/部分】用 78,203 条文献记录微调 LLM 来预测 Tc，标出一批预测 Tc > 10 K 的 GNoME 材料，作者自称这些候选“未经验证”（[arXiv](https://arxiv.org/abs/2512.10847)）。

**B4. [2026-03-24] Naganuma, S. & Kitagawa, J.** “Experimental investigation of magnetic properties of MnFeCo4Si2 discovered by GNoME.” arXiv:2603.22748；“to appear in J. Magn. Magn. Mater.”（A3 引为 JMMM 174056, 2026）。期刊版经同行评审。【摘要/部分】这是唯一一篇专门合成单个 GNoME 预测的论文：“Consistent with the GNoME prediction, MnFeCo4Si2 [mp-3203253] crystallizes in a rhombohedral structure with a single-phase nature”，产物为居里温度 1039 K 的软铁磁体（[arXiv](https://arxiv.org/abs/2603.22748)）。异议同样来自 A3：对应的 GNoME 条目 d8afdc992d 在 ICSD 中有近重复（675046，2018 年入库），EMD 约 0.022 Å（[arXiv:2610.13885](https://arxiv.org/abs/2610.13885)）。

**B9. [2026-05 v1；2026-10-03 v2] Akter, S., Faruque, M. O. & Momeni, M. R.** “At-Scale Discovery of High-Voltage Cathode Active Materials for Na-Ion Batteries ...” arXiv:2605.27229。预印本。【摘要/部分】以 MP、AFLOW、OQMD 和 GNoME 的结构为母体，构建包含 14,843 个 >3 V 钠正极候选的 NaCAM-Atlas。纯计算（[arXiv](https://arxiv.org/abs/2605.27229)）。

**B12. [2026-08-11] Meng, J., Jacobs, R., Kapadia, R. & Booske, J.** “Accelerated Discovery of Materials with Extreme Work Functions ...” arXiv:2608.11062。预印本。【摘要/部分】在 550 万个 GNoME 和 Alexandria 化合物中，筛出 136 个功函数 <2.0 eV、172 个 >6.0 eV 的材料。纯计算（[arXiv](https://arxiv.org/abs/2608.11062)）。

**B17. 后续通用机器学习势函数是否使用了 GNoME 数据。**【二手：综述和教程的搜索摘要，未打开模型卡】现有资料显示，MatterSim 使用约 1,700 万个来自 MP、Alexandria 和自有 DFT 的结构；Orb v2 使用 MPtrj 和 Alexandria，Orb v3 使用 OMat24；MACE 系列使用 MPtrj、sAlex 或 OMat24；UMA 使用 OMat24 等 Meta 数据集。没有找到任何来源说这些模型用了 GNoME 数据。GNoME 的 DFT 训练集从未公开（B16），所以“GNoME 数据训练了 MatterSim/Orb/MACE-OMat/UMA”这一前提看来不成立；它们最多可能用过 GNoME 公开的结构。

综合来看，2023 年以来针对具体 GNoME 预测的前瞻性合成只有 B3、B4、B5 三例，三例都被指出并不新（A3 的核查，以及 B5 自己的 ICSD 分析）。下游文献把 GNoME 当作大型候选池，默认接受其 0 K 稳定性，却很少讨论无序或新颖性；GNoME 笔记没有找到任何 528 个锂离子导体、52,000 个层状材料或超导氢化物候选获得实验确认的报道。

## 第三部分 官方回应与更正：A-Lab 已更正，GNoME 原文至今未动

**C3. [2023-12-02] Ceder, G.** “Regarding our recent A-Lab article.” LinkedIn。Ceder 课题组的回应，非同行评审。【原文已读】回应重申 “For the 58 compounds targeted in the study, the A-Lab successfully produced 41 of the materials”。针对 Palgrave 认为 5 个 MxSb4-xPb4O13 烧绿石（M = Hf、Zr、Sn、Fe、In）实为 Sb2Pb2O7 的指控，Ceder 用新的 SEM/EDS 图证明 M 阳离子被保留且分布均匀，并指出 XRD 峰位移与 Shannon 离子半径相关。关于自动 Rietveld 精修，他写道 “We have no doubt that a human can perform a higher-quality refinement ... it was our objective to show what an autonomous laboratory can achieve”。关于新颖性，他承认 “MnAgO2 and Mg3Ni3MnO8 are not ‘new’. We agree with this assessment”，并表示 “We will certainly update the published paper”。Leeman 等随后指出，这些 EDS 和峰位移证据同样符合已知的无序 Pb–Sb–M 烧绿石（Cascales et al., 1985–86）（[LinkedIn](https://www.linkedin.com/pulse/regarding-our-recent-a-lab-article-gerbrand-ceder-0sz6c)）。

**C4. [2023-12-12；2024-01-09 更新] Peplow, M.** “Robot chemist sparks row with claim it created new materials.” *Nature* News。新闻，付费墙。【摘要/部分】2024 年 1 月 9 日的更新提到了 Palgrave/Schoop 的预印本（[Nature News](https://www.nature.com/articles/d41586-023-03956-w)）。

**C6. [2023-11-29 至 2024-11-21] GNoME 数据集发布说明（google-deepmind/materials_discovery 仓库的 DATASET.md 和 README，2026-10-22 读取）。**【原文已读】版本记录共四条：11/29/23 “Initial dataset release”；12/1/23 “Re-introduce paper filters to remove un-physical energies”，并补了 2 个缺失列；8/21/24 把阈值调到距凸包 1 meV/atom（“significantly increasing the number of released crystals”），同时改用 “require_bound” 版 MP 修正，并对 VASP 未更新晶格坐标的结构重新弛豫；11/21/24 “Ensure consistency in formation energies”。此后没有新记录，**也没有任何关于撤下条目的说明**，而 A3 统计出被撤下的条目有 83,525 条。README 至今仍写着 “share the discovery of 381,000 novel stable materials”，又补充说 2024 年 8 月起已扩展到 “>520,000 materials”（A3 实数为 554,054）。文件中的免责说明有：“as more crystals are discovered by the scientific community, the above set may not remain stable”；对 r2SCAN 子集，“not all released materials remain stable according to this metric”。A3 还发现，旧版本未加说明地存放在 gs://gdm_materials_discovery/gnome_data/legacy_versions/ 下（[DATASET.md](https://github.com/google-deepmind/materials_discovery/blob/main/DATASET.md)；[README](https://github.com/google-deepmind/materials_discovery)）。

**C5. [2024-04-11；2026-10-15] Google DeepMind 对媒体的表态。** 2024 年 4 月 11 日对 The Register 和 404 Media 的声明【原文已读】是：“We stand by all claims made in Google DeepMind's GNoME paper ... hundreds of the materials we've predicted have already been independently synthesized by scientists around the world”。404 Media 转述（非直接引语）称，Google 表示“已知结构换元素”之类的批评反映的是“by design”的选择（[The Register](https://www.theregister.com/2024/04/11/google_deepmind_material_study/)；[404 Media](https://www.404media.co/google-says-it-discovered-millions-of-new-materials-with-ai-human-researchers/)）。2025 年 12 月，据 MIT Technology Review 报道，DeepMind 称一直与各地实验室合作合成 AI 识别的化合物，“has achieved some success”，但没有给出数字【二手，配套笔记】（[MIT TR](https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/)）。2026 年 10 月 15 日，C&EN 副标题称 DeepMind “doesn't comment on inquiries about lack of novelty”【摘要/部分】（[C&EN](https://cen.acs.org/research-integrity/Google-DeepMind-structures-near-duplicates-questionable/104/web/2026/10)）。坊间流传的 “the dataset was released for community study” 这句话，GNoME 笔记在打开过的来源中都未能核实；最接近的措辞是 README 中的 “Please help by exploring the structures and let us know what you think!”。

**C7. [2023-11 至 2026-10] Materials Project 对 GNoME 的收录（MP “Database Versions” 文档，2026-10-22 读取）。**【原文已读】2023 年 11 月，MP 上线含 2,047 个材料的 GNoME Explorer。v2024.11.14（2024-12-12 上线）弃用这 2,047 条，为发布约 12 万条做准备。v2024.12.18（2024-12-20 上线）加入 15,483 个用 r2SCAN 计算的 GNoME 材料，并从此要求用户明确接受 BY-NC 许可。v2025.04.10（2025-04-18 上线）加入 “30,00 [sic]” 个，应为 30,000。2025 年 5 月 1 日，MP 的 Aaron Kaplan 在论坛上说明，约 119,000 个 GNoME 材料在 r2SCAN 下最初被判定为稳定，是 38.1 万的子集（[matsci.org](https://matsci.org/t/number-of-materials-in-gnome-explorer/63304)）。v2026.04.13（2026-06-08 上线）加入 74,052 个，**累计约 11.7 万**，并称将来会发布“剩余 GNoME 材料”；v2026.09.28（2026-10-19 上线）没有新增 GNoME 内容（[MP Database Versions](https://docs.materialsproject.org/changes/database-versions)）。约 11.7 万占 38.1 万的约 31%（本报告推算）；MP 没有说明其余部分是在 r2SCAN 下失稳还是尚未处理。“约 52 万个距凸包 1 meV/atom 内的材料”属于 DeepMind 自己 2024 年 8 月的 GitHub 版本，与 MP 无关。

**C8. [2024–2026] DeepMind 作者参与的后续论文。** 包括：Miura 等，*JACS* 2024（B3）；Aykol, M., Merchant, A., Batzner, S., Wei, J. N. & Cubuk, E. D., “Predicting emergence of crystals from amorphous precursors with deep learning potentials,” *Nat. Comput. Sci.*（2024-12-18），DOI 10.1038/s43588-024-00752-y，用 GNoME/NequIP 类通用势预测非晶前驱体中哪种多晶型最先成核【二手，未打开】（[PMC11860218](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11860218/)）；Sanna 等，*Commun. Phys.* 2026（B10）；以及由 Cubuk、Merchant 共同署名的 A-Lab 更正（C1）。**没有找到任何重新检视或正面辩护 GNoME 新颖性主张的 DeepMind 论文。**

**C1. [2026-01-19] Szymanski, N. J., Rendy, B., Fei, Y., Kumar, R. E., He, T., Milsted, D., McDermott, M. J., Gallant, M., Cubuk, E. D., Merchant, A., Kim, H., Jain, A., Bartel, C. J., Persson, K., Zeng, Y. & Ceder, G.** “Author Correction: An autonomous laboratory for the accelerated synthesis of inorganic materials.” *Nature* 650 (8100), E1。DOI 10.1038/s41586-025-09992-y；PMID 41554984；PMCID PMC12872444。同行评审的更正，重新分析经过发表后同行评审。【原文已读，Europe PMC XML 全文】更正的起因是 “concerns were raised about the unambiguous identification of the compound structures using diffraction as well as the original claims of material novelty”。更正内容有四项。第一，新颖性被改写：“the original claims of material novelty were subject to misinterpretation—their intention was to indicate that the materials were new to the prediction platform, not necessarily new to science”，HTML 和 PDF 正文已相应修改，并附有标注修改处的 PDF。第二，“We have manually re-analyzed the diffraction patterns and have confirmed that the prediction platform came to the correct conclusion in **36 of its 40** reported successes, with 4 compounds being inconclusive”，成功总数中剔除了这 4 个仅凭 XRD 无法定论的目标。第三，删去 Zn2Cr3FeO8，因为它 “mistakenly included in the training data”。第四，更新了图 2、补充信息和补充数据。*Nature* 在更正中感谢了 “the correspondents who brought these issues to our and the authors' attention”（[Europe PMC](https://europepmc.org/article/PMC/PMC12872444)；[DOI](https://doi.org/10.1038/s41586-025-09992-y)）。按本报告推算，原文 41/58（71%）减去 Zn2Cr3FeO8 得 40/57，再去掉 4 个不确定目标得 **36/57 ≈ 63%**；更正本身没有写出新的标题数字或分母。批评者 Widdowson 等把这次更正形容为“几乎划掉了所有 ‘novelty’ 和 ‘discovery’”，这是他们对标注版 PDF 的描述，笔记作者没有打开该 PDF 核实。这次更正**接受了新颖性批评，但没有回应无序批评**：它说 36 个鉴定“正确”，却没有讨论这些产物是否就是已知的无序相，这正是 A6 中批评者仍然不满的地方。

**C2. [截至 2026-10-22] GNoME *Nature* 论文的更正状态。**【原文已读：2026-10-22 抓取的 *Nature* 文章页】GNoME 页面显示 “Nature volume 624, pages 80–85 (2023)”、43.6 万次访问、1,820 次引用、Altmetric 1,228，页面中**没有** “Correction”“Author Correction”“Editor's Note” 或 “Change history”，“correction” 一词出现 0 次。A-Lab 页面则显示 “An Author Correction to this article was published on 19 January 2026”，有 31 万次访问、1,242 次引用（[GNoME](https://www.nature.com/articles/s41586-023-06735-9)；[A-Lab](https://www.nature.com/articles/s41586-023-06734-w)）。所谓“2026 年 1 月 *Nature* 更正了 GNoME、收回新颖性”的说法，是把 A-Lab 更正（C1）错安到了 GNoME 头上；GNoME 的第一作者 Merchant 和末位作者 Cubuk 只是作为合著者共同签署了 A-Lab 那份更正。此外没有找到针对任一论文、在 *Nature* 正式发表的 Matters Arising 或评论。

## 证据之间的出入与尚待核实之处

有几处数字看似冲突，实际上是度量对象不同。A3 说 GNoME 在几何上离已知晶体很近，A9 说 GNoME 在结构嵌入空间中远离实验“盆地”、组分几乎全新：前者度量局部原子几何，后者度量 32 维嵌入中的社区归属，两者合起来恰好描绘出“已知原型 + 奇异的多元素组分”这一图景。A7 预测 80–84% 的 GNoME 组分倾向无序，A8 却只在 0.73% 的样本中找到已知无序母相：前者是从组分做出的预测，后者要求 ICSD 中真有对应母相，而 ICSD 对 GNoME 那种多元素、含放射性元素的化学体系覆盖稀疏。还有一处小的、尚未解释的张力：A3 称 GNoME2 中有 0.9% 的条目与 ICSD 共用组分，A9 却在 5,000 条样本中得到 0.0%（以 1980 年后 ICSD 的约化化学式为准）；可能源于版本、时间窗或“组分/约化化学式”定义的差异，现有材料无法判定。配套笔记另记有 Vepa（arXiv:2606.23725，单作者预印本）用 COD 精确组分比对 500 条随机 GNoME 条目，命中 0 条；作者自己提醒这 “measure[s] our coverage as much as GNoME's novelty”【二手，数字来自搜索摘要】（[arXiv:2606.23725](https://arxiv.org/abs/2606.23725)）。

仍待核实的缺口有：C&EN 2026 年 1 月和 10 月两篇报道的正文都在付费墙后，无法确认其引用的具体百分比；Leeman 等第二类错误的计数在笔记中被截断；Miura 等 *JACS* 的“三种新化合物”与 A3 列出的六个成功组分尚未对上；A-Lab 更正中 4 个不确定化合物的名称和新的标题数字未经核实；GNoME 原文补充说明 1 中 736 个匹配的清单没有找到独立审计；*IUCrJ* 2024 和 *Sci. Rep.* 2025 两篇 Kurlin 组论文只经 A3 转引；B 部分来自 arXiv 标题与摘要检索，没有系统梳理约 1,820 篇引用文献，因此下游使用的清单并不完整。

## 结论

三年下来，争论的焦点已经从“GNoME 有没有发现新材料”转成了更可操作的问题：在宣布新材料之前，新颖性检查应该比对什么。A3 的数据修订分析提供了这一转变最有力的证据：DeepMind 在 2023–2024 年间无声地撤掉了 92.7% 与已知有序晶体匹配的条目，却只撤掉 40.4% 与已知无序晶体匹配的条目。也就是说，基于有序结构的去重确实执行了，而且有效；它漏掉的恰恰是所有批评者从 2024 年起反复指出的那个盲区。这让“无序”从一个晶体学家之间的专业分歧，变成了任何 AI 材料数据库都需要面对的可检验工程缺陷。Jakob 等的组分分类器和 Yamazaki 等的群–子群框架已经可以作为现成的过滤工具。

在官方层面，A-Lab 与 GNoME 走上了不同的路。前者在批评后约两年内正式更正，承认“对平台为新”与“对科学为新”的区别；后者至今保持论文原样，数据集悄然变动，DeepMind 从公开辩护转为沉默，而 README 仍写着“381,000 novel stable materials”。引用这批数据的读者应当默认：GNoME 是一个以已知结构型为骨架、组分高度外推的 0 K 候选池，可以用于计算筛选，但不能直接当作“已发现材料”的清单。截至 2026 年 10 月，经独立确认对科学为新的 GNoME 预测，在已发表文献中仍然找不到一个没有争议的例子。
