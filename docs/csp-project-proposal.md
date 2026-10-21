# 晶体结构预测（CSP）求职项目建议：面向 AI4S 材料方向 PM & Operations

调研日期：2026-10-21。目标职位：DeepMind / Anthropic / OpenAI 等的 AI for Science 材料方向 PM、Program Manager、Operations。
项目范式参考：DeepMind 自动化材料实验室、CuspAI、Lila Sciences、Periodic Labs。

---

## 1. 一句话结论

**做一个"客户驱动的逆向设计交付项目"，客户设定为半导体薄膜领域（ALD/溅射可沉积的氧化物介电或铁电材料），从目标性能规格出发，用开源 CSP/生成模型 + 机器学习势 + 性质预测 + 可合成性评估做漏斗式筛选，最终交付一份"候选材料档案 + 薄膜验证方案 + 阶段门/成本/风险"的完整交付包。**

理由：
- DeepMind 伦敦材料实验室 2026 年的招聘几乎全部围绕"薄膜合成（PVD/溅射/ALD/PLD/MOCVD 组合库）+ 固相合成 + 低温输运/磁性/光学表征 + 半导体计算（带隙、缺陷能级、介电常数、漏电流）"。
- CuspAI 的客户和 Foundry 成员高度集中在半导体链条：ASML、Lam Research、Samsung、NVIDIA、3M。
- Periodic Labs 近期营收方向是芯片热管理材料，长期目标是超导。
- PM/Ops 岗位真正考察的不是你能不能训练模型，而是你能否把"客户需求 → 可量化规格 → 计算漏斗 → 实验验证 → 交付"这条链条管起来，并能讲清每一步的候选数、成本、周期和风险。

---

## 2. 行业模式调研：这几家公司"怎么交付新材料"

| 公司 | 模式 | 已公开的案例 / 客户 | 对你项目的启示 |
|---|---|---|---|
| **Google DeepMind** | GNoME 预测（220 万结构，38 万稳定）+ 2026 年英国自动化实验室（Gemini 驱动，机器人每天合成数百种候选材料） | 方向：超导、半导体/芯片材料、太阳能；外部实验室独立验证 736 个 GNoME 结构；与 UK 政府合作 | 自有实验室闭环，强调"预测 → 合成 → 表征 → 反馈"的吞吐量。项目里要有"闭环"与"吞吐"概念 |
| **CuspAI** | MIRA 平台：生成式逆向设计 → 模拟 → 合成规划 → 实验验证；2026-07 推出"AI Materials Foundry"全球网络（45+ 成员） | ASML、Meta、Hyundai 为早期客户；Kemira 的 PFAS 吸附剂项目：约 300 万亿搜索空间缩到 20 个候选；Foundry 成员含 3M、Samsung、Lam Research、NVIDIA、Topsoe、Henkel | 最接近"真实工业客户提性能，我们反向设计"的范式。关键词：搜索空间 → 漏斗 → 少量昂贵模拟 → 合作伙伴合成 |
| **Lila Sciences** | "AI Science Factory"，AI 提出候选 + 自动化实验，跨材料/化学/生命科学 | 2026-09：3 个月内提出/合成/筛选 2,942 种催化剂，找到 6 个钯基材料家族用于酸性 OER，1000+ 小时稳定性测试（arXiv 2609.30133） | 用 Pareto 前沿（活性 vs 稳定性）做多目标优化；强调"模型提出了人类以为不靠谱但实验证明有效的候选" |
| **Periodic Labs** | 粉末合成自动实验室；OpenAI/DeepMind 背景创始人 | 近期：芯片热管理材料客户；长期：高温超导 | OpenAI 系人才去向，说明 OpenAI 本身没有对应岗位，相关机会在生态公司 |
| **Orbital Industries**（原 Orbital Materials） | 聚焦数据中心冷却流体等产品，正与芯片厂做 qualification，2027 年随下一代 GPU 出货 | 从"平台"转向"产品公司" | 交付的终点是"客户 qualification"，不是论文 |
| **Microsoft MatterGen** | 条件生成模型（按性质生成结构） | 实验合成了 TaCr2O6；但 2026 年 Materials Horizons 评论指出其"新材料"等价于 1972 年已报道的化合物 | 必须在项目中加入"新颖性/数据泄露核查"，这是 PM 的风险管理加分项 |

共同的交付链条（你的项目要完整复刻这条链）：

```
客户性能需求 → 量化规格表 + 约束 → 候选空间定义 → 生成/CSP → 快速筛选（MLIP）
→ 性质预测 → 高精度验证（DFT 子集）→ 可合成性/生长窗口评估 → 新颖性核查
→ 排序与候选档案 → 实验验证计划（组合库 / 自动化实验室）→ 交付与复盘
```

---

## 3. DeepMind 伦敦材料实验室招聘分析（2026）

**公开信息中的岗位（均在伦敦，均挂在 "Materials Discovery Laboratory" 下）：**

| 岗位 | 核心内容 | 说明的方向 |
|---|---|---|
| Materials Laboratory Scientist, **Thin Films** | 用 PVD、溅射、MOCVD、PLD、ALD 制备**组合式薄膜材料库**；XRD、SEM、AFM、Raman、椭偏仪做相和厚度 QC；与计算科学家对接做闭环；与 "material intelligence" 团队建模生长动力学，把沉积配方与薄膜性质关联。要求 PhD + 5 年薄膜经验，多元素体系优化 | **薄膜是实验室主力合成路线之一** |
| Materials Laboratory Scientist, **Solid State Synthesis** | 固相（粉末）合成 | 块体材料的第二条路线 |
| Materials Laboratory Scientist, **Physical Properties** | 低温电输运、磁性、光学、热学、力学测量；批量化测量工作流以加速模型反馈；从原始数据提取物性的数据管道 | 低温输运 + 磁性 = 超导/磁性材料验证能力 |
| Materials Laboratory Scientist（通用） | 建设新的合成与表征实验室 | 实验室正在从零搭建 |
| **Semiconductor Material Science Research Scientist** | DFT/DFPT/MD 预测半导体性质：带隙、缺陷能级、漏电流、介电常数、界面性质；与实验人员协作合成 | **半导体方向被明确点名** |
| Machine Learning and Material Science Research Scientist | ML + 材料 | 模型侧 |
| Technical Program Manager, **Science Automation** | 科学自动化的 TPM | **最接近 PM/Ops 的岗位** |
| Program Manager, Science & Strategic Initiatives | 覆盖物理/化学含材料团队（2025-05 已关闭） | 这类岗位会周期性出现 |

**判断：**
- 你的观察是对的：实验室的合成能力建设以**薄膜**和**固相粉末**两条路线为主，应用目标是**超导、半导体/芯片材料、太阳能**。
- 没有"材料方向 PM/Ops"的专门岗位，PM 职能挂在 Science 大组的 TPM（Science Automation）和 Program Manager（Science & Strategic Initiatives）下。所以你的项目要体现的是**"自动化实验室的闭环流程、吞吐与数据管道"**这类 TPM 视角，而不是单一算法。
- 待核实：实验室是否已于 2026 年初开业（仅有低权威来源这么说，DeepMind 官方只说"2026 年开"）；具体地址未公开；薪资均为聚合网站估计值。请以 Google Careers / DeepMind careers 官方页面为准。

**对 Anthropic 和 OpenAI 的补充：**
- Anthropic 有 "Program Manager, AI for Science"（西雅图，$215k–300k）和 "Partnership Manager, AI for Science"（SF/NY，$170k–215k，2026-10-15 发布），范围是 Claude for Life Sciences 向生物医学、化学、**材料科学**扩展；要求外部合作、资助/多方项目管理经验。伦敦的同名岗位 2026-02 已关闭。
- OpenAI 未找到公开的 AI for Science 材料 PM 岗位；该方向人才流向 Periodic Labs 等。
- 因此项目里最好有一块"用前沿 LLM/agent 做文献挖掘、合成路线规划、实验计划生成"的内容，这对 Anthropic 类岗位（部署 Claude 到科研场景、管理外部合作）是直接对口的。

---

## 4. 推荐项目：方案 A（主推）

### 4.1 虚拟客户与需求

**客户**：一家 ALD/溅射设备商或逻辑/存储芯片厂（对标 CuspAI Foundry 成员 Lam Research、Samsung、ASML 类型）。

**需求（二选一，建议选第一个）：**

1. **新一代高-k 栅介电 / 铁电存储氧化物**：替代或改良 HfO2-ZrO2 体系。
   规格示例：介电常数 k ≥ 25；带隙 ≥ 5 eV；与 Si 的导带/价带偏移各 ≥ 1 eV；可用 ALD/溅射在 ≤ 400 °C 下沉积为非晶或择优取向薄膜；不含 Pb、Cd、Hg、放射性元素；原料成本和供应链风险可控；热力学稳定性 ≤ 50 meV/atom above hull。
   2026 年 5 月 Chem. Mater. 刚发表 Hf–Zr–O 体系的 AI 逆向设计案例（IDEAL 平台，扩散生成模型 + MLIP + GNN，绑定 ALD），说明这条线是学界/工业界的热点，有可对标的基线。

2. **非铟透明导电氧化物（TCO）**：对标太阳能/显示应用（DeepMind 提到的太阳能方向）。
   规格：带隙 ≥ 3.1 eV；电子有效质量小（高迁移率）；可 n 型掺杂；无 In。

### 4.2 漏斗流程与每步的 PM 指标

| 阶段 | 做什么 | 工具（开源） | PM 要记录的指标 |
|---|---|---|---|
| 0. 需求转化 | 把客户语言转成量化规格 + 硬约束 + 软约束，签"需求规格书" | 文档 | 规格条目数、约束优先级、验收标准 |
| 1. 候选空间 | 元素筛选（毒性/稀有/成本）、化学式枚举（二元到四元氧化物） | pymatgen、Materials Project / Alexandria / OQMD 数据 | 搜索空间大小（例如 10^5–10^7） |
| 2. 结构生成 / CSP | 生成模型 + 结构预测 | MatterGen、CrystalFormer-CSP、Chemeleon、CrystalFlow；传统 CSP 如 CALYPSO/USPEX 做对照 | 生成结构数、有效率、唯一率、新颖率 |
| 3. 快速松弛与稳定性 | MLIP 松弛 + 凸包距离 | MACE-MP、Orb、UMA/fairchem、MatterSim | 松弛通过率、每千结构耗时与成本 |
| 4. 性质预测 | 带隙、介电张量、有效质量的 ML 预测 | MatGL/M3GNet、ALIGNN、JARVIS 模型；介电张量可用物理分解 ML 模型 | 通过规格的候选数 |
| 5. 高精度验证 | 对 Top-N 做 DFT（HSE 带隙、DFPT 介电） | VASP/Quantum ESPRESSO（有算力再做，否则用已有数据库值做"模拟验证"） | DFT 预算（CPU 小时）与排队时间 |
| 6. 可合成性 / 生长窗口 | 文本挖掘合成配方 + 可合成性打分 + 薄膜生长可行性（衬底晶格匹配、前驱体是否存在、沉积温度） | CSLLM、Materealize 类 LLM 工具；用 Claude/Gemini agent 做文献抽取 | 可合成性评分分布、有前驱体的比例 |
| 7. 新颖性核查 | 与 ICSD/MP/Alexandria/COD 去重；检查 MatterGen 式"训练集复现"问题 | pymatgen StructureMatcher | 真正新颖的候选数 |
| 8. 候选档案与排序 | 多目标 Pareto（k、带隙、稳定性、可合成性、成本） | 自写打分 + 可视化 | 最终交付候选数（建议 10–20） |
| 9. 实验验证计划 | 组合式溅射/ALD 材料库设计、XRD/椭偏/C-V 测试矩阵、按 DeepMind 实验室"每天数百样品"的吞吐做排期与成本 | 文档 + 甘特图 | 样品数、周期、预算、停止/继续的阶段门 |
| 10. 交付与复盘 | 客户汇报、风险登记、下一轮迭代计划 | 文档/演示 | 决策记录 |

### 4.3 交付物清单（这才是 PM/Ops 岗位看的东西）

1. **需求规格书**：客户目标 → 量化规格 → 约束 → 验收标准。
2. **漏斗仪表盘**：每阶段候选数、通过率、单位成本、耗时（一页图）。
3. **候选材料档案（Top 10–20）**：结构、预测性质、不确定度、可合成性、风险、建议沉积路线。
4. **实验验证方案**：组合库设计、表征矩阵、预算、排期、阶段门（Go/No-Go 标准）。
5. **风险登记册**：模型新颖性问题（引用 2026 年对 MatterGen 的批评）、数据泄露、合成失败率、供应链、IP。
6. **运营模型**：假设实验室吞吐 300 样品/天时，闭环一轮需要多久；计算 vs 实验的资源分配；数据管理与可追溯性。
7. **项目复盘与方法论文档**：讲清你如何做决策、哪里砍掉了范围。
8. **可复现的代码仓库**（本仓库）：pipeline 脚本 + notebook + 结果。

加分项（可选）：
- 用 Claude/Gemini 做 agent：从文献自动抽取合成配方、生成实验计划草案，并记录人工复核比例（直接对应 Anthropic 岗位）。
- 找一所大学或开放实验室对 1–2 个候选做真实溅射/ALD 验证；哪怕失败，也能展示"真实闭环"。
- 做一个 1 页的"如果我是 DeepMind 材料实验室 TPM"的运营方案（吞吐模型、数据管道、安全合规）。

### 4.4 时间计划（8–10 周）

| 周 | 里程碑 |
|---|---|
| 1 | 需求规格书、候选空间定义、工具链跑通 |
| 2–3 | 生成 + MLIP 松弛 + 稳定性筛选，输出第一版漏斗数据 |
| 4 | 性质预测 + 规格筛选 |
| 5 | 可合成性评估 + 新颖性核查 + LLM 文献抽取 |
| 6 | 高精度验证（DFT 子集或数据库对照） |
| 7 | 候选档案 + 实验验证方案 + 运营模型 |
| 8 | 风险登记、复盘、汇报材料（10 页 deck + 2 页 one-pager） |
| 9–10（可选） | 外部实验验证、迭代第二轮 |

---

## 5. 备选方案

**方案 B：清洁能源催化剂（对标 Lila）**
客户：电解槽厂商。需求：无铱/钌的酸性 OER 催化剂，活性-稳定性 Pareto 前沿。
优点：有 Lila 的 2,942 样品/3 个月的真实基准可对比，适合展示主动学习与多目标优化。
缺点：CSP 对表面/催化体系的贡献有限，与 DeepMind 薄膜方向关联较弱。

**方案 C：PFAS 吸附剂 MOF（对标 CuspAI/Kemira）**
优点：有公开的 300 万亿 → 20 的漏斗数字可对标。
缺点：MOF 的 CSP 和可合成性评估比无机氧化物难得多，8 周内难做扎实。

**方案 D：芯片热管理材料（对标 Periodic Labs）**
需求：高热导率、低介电、可制备的封装或界面材料。
优点：与半导体客户契合。缺点：热导率预测需要声子计算，算力门槛高。

建议：主推 A，把 B 作为"第二个客户案例"简述在复盘里，展示方法论可迁移。

---

## 6. 注意事项与风险

- **不要宣称"发现了新材料"**，除非有实验验证。措辞用"交付了经计算筛选和可合成性评估的候选集与验证方案"。
- **新颖性核查必须做**：GNoME 与 MatterGen 都被质疑过新颖性，招聘方会问这个。
- **可合成性与"稳定"不是一回事**：凸包距离小不等于能沉积成薄膜；薄膜还有衬底、应变、动力学相。
- **数据泄露**：LLM 合成预测工具的训练集可能包含测试化合物，引用 arXiv 2506.12557 的警示。
- **来源可靠性**：岗位薪资和"实验室已开业"均来自聚合/低权威网站，面试中引用请以官方页面为准。
- **本环境限制**：本次调研只能用搜索摘要，无法直接打开 Google Careers、Indeed、BusinessWire 等页面，JD 细节请自行到官方页面核对。

---

## 7. 相关开源工具与基准速查

- 生成 / CSP：MatterGen、CrystalFormer-CSP、Chemeleon、CrystalFlow、CALYPSO、USPEX、awesome-crystal-structure-prediction（综述仓库）
- MLIP：MACE-MP-0、Orb、UMA/fairchem、MatterSim、CuspAI kUPS（2026-04 开源）
- 性质预测：MatGL、ALIGNN、JARVIS-Tools
- 可合成性 / 合成规划：CSLLM、Materealize、text-mined synthesis datasets
- 基准：MP-20、MPTS-52、CSPBench、LeMat-GenBench、AtomBench
- 数据：Materials Project、Alexandria、OQMD、JARVIS-DFT、ICSD（需授权）

---

## 8. 来源

DeepMind 实验室与招聘：
- https://twitter.com/GoogleDeepMind/status/1999074624588394809
- https://www.computing.co.uk/news/2025/ai/google-deepmind-announces-uk-ai-research-lab
- https://technologymagazine.com/news/why-google-deepmind-is-launching-uk-automated-ai-science-lab
- https://fortune.com/2025/12/10/google-deepmind-uk-government-partnership-science-clean-energy
- https://uk.indeed.com/viewjob?jk=b9b59c3fd40b37ec （Thin Films）
- https://uk.indeed.com/viewjob?jk=65fb03e085911ab4 （Physical Properties）
- https://talents.studysmarter.co.uk/companies/google-deepmind/london/materials-laboratory-scientist-solid-state-synthesis-deepmind-37997534/
- https://www.google.com/about/careers/applications/jobs/results/127510867649405638-semiconductor-material-science-research-scientist-deepmind
- https://job-boards.greenhouse.io/deepmind/jobs/7353266
- https://startup.jobs/machine-learning-and-material-science-research-scientist-deepmind-7697996
- https://startup.jobs/materials-laboratory-scientist-deepmind-6997153
- https://builtinlondon.uk/job/program-manager-science-strategic-initiatives/6268861
- https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/

CuspAI / Lila / Periodic / Orbital / MatterGen：
- https://www.businesswire.com/news/home/20260716196996/en/CuspAI-Launches-AI-Materials-Foundry-a-Global-Network-to-Accelerate-Breakthrough-Discoveries
- https://technologies.org/how-cuspais-inverse-design-ai-turns-materials-discovery-into-a-search-engine/
- https://finance.yahoo.com/technology/ai/articles/cuspai-raises-450-million-series-121902705.html
- https://opportunities.northzone.com/companies/cuspai/jobs/63645958-application-scientist-semiconductor-modelling-design
- https://www.lila.ai/news/how-an-ai-run-lab-cracked-open-green-hydrogens-catalyst-problem
- https://arxiv.org/pdf/2609.30133
- https://a16z.com/announcement/investing-in-periodic-labs/
- https://research.contrary.com/company/periodic-labs
- https://fortune.com/2026/05/28/exclusive-orbital-industries-raises-50-million-series-b-funding-round-ai-to-discover-exotic-new-materials/
- https://www.microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai/
- https://pubs.rsc.org/en/content/articlehtml/2026/mh/d6mh00268d
- https://www.technologyreview.com/2025/12/15/1129210/ai-materials-science-discovery-startups-investment/

Anthropic 岗位：
- https://www.indexventures.com/startup-jobs/anthropic/partnership-manager-ai-for-science-1/
- https://startup.jobs/program-manager-ai-for-science-anthropic-3-7690168
- https://builtinlondon.uk/job/program-manager-ai-science/8430308

技术与基准：
- https://github.com/usccolumbia/awesome-crystal-structure-prediction
- https://arxiv.org/html/2512.18251 （CrystalFormer-CSP）
- https://arxiv.org/pdf/2603.09744 （Hf–Zr–O 逆向设计 IDEAL）
- https://pubs.acs.org/cmatex/article-abstract/38/10/5285/5085110
- https://arxiv.org/pdf/2407.07016 （CSLLM 可合成性）
- https://www.alphaxiv.org/overview/2601.15743 （Materealize）
- https://arxiv.org/html/2506.12557v1 （合成规划数据泄露警示）
- https://arxiv.org/pdf/2609.15922 （RHEED 引导的 agentic 薄膜合成开源工具包）
