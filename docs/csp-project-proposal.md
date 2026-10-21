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

---

# 附录 A：Public Reference Product Profile（PRPP）可行性与草案

更新日期：2026-10-21。背景：用户确认 DeepMind 英国实验室已开业，负责人 2025 年 12 月加入；材料方向 PM/Ops 岗位尚未出现，本项目为提前准备。

## A.1 结论：数据足够，但要分"两层"写规格

高-k / 铁电 HfO2 体系是过去 25 年半导体材料里公开数据最密集的方向之一，可以做出数值化、经得起内行追问的 PRPP。关键是把规格写成两层：

- **第一层：器件级目标（客户语言）**：EOT、漏电流、Pr、耐久、保持。来自器件文献和 IRDS 路线图，是客户真正关心的。
- **第二层：材料级代理指标（模型语言）**：带隙、带阶、介电张量、凸包距离、相稳定性、生长窗口。这是计算漏斗真正能筛的东西。

PM 的专业性恰恰体现在**这两层之间的映射和"代理指标不等于器件指标"的风险说明**。写出"我们筛 k 和 Eg，但器件里的 EOT 还取决于界面层 SiOx 的 0.4 到 0.7 nm 贡献，所以材料级 k 目标要留余量"这一句，比任何模型细节都更能证明不外行。

## A.2 PRPP 草案（高-k 栅介电 / 铁电存储氧化物）

### 器件级目标（第一层）

| 指标 | 目标值 | 依据 / 备注 |
|---|---|---|
| 等效氧化层厚度 EOT | ≤ 0.5 nm（逻辑栅介电）；铁电存储场景则按物理厚度 ≤ 10 nm 要求 | IRDS More Moore 章节给出逐年 EOT 目标，需从原文取当年数值 |
| 栅漏电流密度 | 在 |V| = 1 V 下 ≤ 1e-2 A/cm²（低功耗）量级 | 器件文献常用阈值；具体按 IRDS 当年值 |
| 剩余极化 2Pr（铁电场景） | ≥ 20 μC/cm²（文献中溅射未掺杂 HfO2 达到约 35 μC/cm²） | arXiv 2304.12924 |
| 耐久性 | 电容器 ≥ 1e11 次；FeFET 目前约 1e8 次，目标 ≥ 1e12 | 2025 J. Appl. Phys. 综述、外延 HfO2 综述 |
| 保持 | 10 年 @ 85 °C（行业常规要求，需引 JEDEC 标准原文） | 文献报告范围 1e3 到 1e6 s，与 10 年仍有差距，这正是客户痛点 |
| 唤醒效应 | 无唤醒或 < 100 次循环内饱和 | 外延膜比多晶膜更抗唤醒 |
| 热预算 | 沉积 + 退火 ≤ 400 °C（BEOL 兼容）或 ≤ 1000 °C spike（栅优先流程） | 按客户流程选一 |

### 材料级代理指标（第二层，计算漏斗实际筛选项）

| 指标 | 目标值 | 数据来源 | 备注 |
|---|---|---|---|
| 介电常数 k（静态，离子 + 电子） | ≥ 25，优先 25 到 40 | Materials Project DFPT 介电数据（首批 1,056 种，PBE 对实验 MARD 约 16%，Spearman 0.92）；2026 年 PRX 离子介电张量 ML 模型筛过 8000+ 氧化物；arXiv 2601.04755 等变 GNN 介电张量模型 | k 与 Eg 反比是已知权衡，k 过高通常 Eg 过小 |
| 带隙 Eg | ≥ 5 eV（HfO2 约 5.8 eV 作基线） | JARVIS-DFT TBmBJ 带隙（约 7,000 到 25,000 条，取决于版本）；MP r²SCAN 带隙 | PBE 带隙系统性偏低，必须用 TBmBJ / HSE 或经验校正；PRX 论文明确指出这一点 |
| 与 Si 的导带/价带偏移 | 各 ≥ 1 eV | Robertson 带阶规则（Rep. Prog. Phys. 2006）；HfO2 实测 CBO 约 1.4 eV，Al2O3 约 2.8 eV | 可用电荷中性能级近似，或对 Top-N 做界面 DFT |
| 热力学稳定性 | ≤ 50 meV/atom above hull（含亚稳相容忍度） | Materials Project / Alexandria 凸包 | 铁电正交相 HfO2 本身是亚稳相，所以阈值不能设 0 |
| 与 Si 的化学稳定性 | 不与 Si 反应生成硅化物或低 k 硅酸盐（可用反应能筛） | pymatgen 界面反应计算 | 这是 Robertson/Hubbard-Schlom 经典筛选标准 |
| 相 / 极性 | 铁电场景：存在极性相（如 Pca21 型）且与非极性相能差 < 50 meV/f.u. | DFT 相能数据，MP 含部分 | 可解释为什么掺杂 / 应变能稳定极性相 |
| 元素约束 | 排除 Pb、Cd、Hg、Tl、放射性元素；标记 In、Ga、稀土的供应链风险 | 自定义黑名单 + 价格表 | 客户可改 |
| 可沉积性 | 存在商用 ALD / CVD 前驱体；或可溅射靶材 | 文献 + 供应商目录（Strem、Sigma 等）；文本挖掘合成配方 | 没有前驱体的候选直接降级 |
| 结晶温度 / 生长窗口 | 可在 ≤ 400 °C 形成目标相，或退火窗口可接受 | 文献 + 薄膜生长模型 | 这是薄膜与块体最大的差别 |

### 验收口径

- 交付 10 到 20 个候选，每个附：所有第二层指标、预测不确定度、数据来源、可沉积性证据、建议的沉积路线和表征矩阵。
- 明确标注"哪些第一层指标无法由计算预测，必须实验"：耐久、保持、唤醒、漏电流。

## A.3 可用的公开数据与参考文献清单

| 类别 | 资源 | 规模 / 要点 |
|---|---|---|
| 介电张量 | Materials Project DFPT（Petousis 2017, Sci. Data） | 首批 1,056 种；PBE 对实验 MARD 16.2%，排序相关性 0.92 |
| 介电张量 ML | Takigawa/Kiyohara/Kumagai PRX 2026（arXiv 2509.26022）；arXiv 2601.04755 等变 GNN | 前者报告 31 个新高-k 氧化物（来自 8,000+ 候选）；后者给出 Ba2SmTaO6 等候选 |
| 带隙 / 光学 | JARVIS-DFT（OptB88vdW 约 17,800 条，TBmBJ 约 7,400 条，2018 版；dft_3d 现 75,993 条） | 用 TBmBJ 带隙而非 PBE |
| 稳定性 | Materials Project、Alexandria、OQMD | 凸包距离 |
| MLIP 基准 | Matbench Discovery（2026 年 1 月榜首 PET-OAM-XL，F1 0.924；eSEN-30M-OAM 0.925） | 用于选择松弛势并引用其 F1 |
| 薄膜逆向设计基线 | Hf–Zr–O IDEAL 平台（Chem. Mater. 2026，arXiv 2603.09744） | 直接可对标的 ALD 绑定案例 |
| 铁电 HfO2 器件 | 2025 J. Appl. Phys. 综述（hal-05226133）；FeFET 综述（TU Dresden）；外延 HfO2 综述（arXiv 2104.13099） | 耐久、保持、唤醒、厚度标度 |
| 高-k 设计规则 | Robertson Rep. Prog. Phys. 2006；Hubbard & Schlom 1996 热力学稳定性筛选 | 带阶 ≥ 1 eV、与 Si 不反应 |
| 路线图 | IRDS More Moore | EOT、漏电逐年目标 |
| 高-k 筛选先例 | npj Comput. Mater. 2022 神经网络筛选；2024 年 ML 预筛 + 合成 CsTaTeO6、Bi2Zr2O7 | 证明"计算筛选 → 合成验证"链条可行 |

## A.4 Evals 设计：PM/Ops 要定义的评估体系

把 evals 分为四类，每类有明确的指标、数据集和通过线。这是区别于"跑了个模型"的核心。

### 1. 模型组件评估（选型依据）

| 组件 | 评估方法 | 指标 | 通过线示例 |
|---|---|---|---|
| MLIP 松弛 | 在本项目化学空间（二元到四元氧化物，含 Hf/Zr/La/Y/Al/Ti/Ta/Nb 等）抽 200 到 500 个 MP 结构，与 DFT 松弛能量和晶格对比 | 能量 MAE（meV/atom）、晶格参数误差、hull 分类 F1 | 引 Matbench Discovery 全局 F1，再报本地子集 F1；本地 F1 ≥ 0.85 |
| 介电常数预测 | 对 MP 1,056 条 DFPT 数据做留出测试，重点看 k ≥ 20 区间 | MAE、Spearman、k ≥ 25 的召回率 | 召回 ≥ 0.8（宁可多漏进后面的 DFT，不可漏掉） |
| 带隙预测 | 与 JARVIS TBmBJ 留出集对比 | MAE、Eg ≥ 5 eV 的分类精度 | 分类 F1 ≥ 0.8 |
| 生成模型 | 有效率、唯一率、新颖率、稳定率（LeMat-GenBench 口径） | 四项比例 | 新颖且稳定 ≥ 5% |
| 可合成性 / 合成规划 | 用时间切分（训练集截止年份之前，测试集之后）避免泄露 | 精度、召回、Top-k 命中 | 必须报时间切分结果，不接受随机切分 |

### 2. 流水线级评估：回溯"重新发现"测试（最有说服力）

把已知成功的高-k / 铁电材料从候选池里"蒙住"，看漏斗能否把它们排进 Top-N：
- 正例：HfO2、ZrO2、Hf0.5Zr0.5O2、La2O3、Y2O3、HfSiO4、LaAlO3、Al2O3（作 k 偏低的边界例子）。
- 负例：已知会和 Si 反应或 Eg 太小的高-k 材料（如 TiO2、Ta2O5、SrTiO3 作为"k 高但带阶不足"的反例）。
- 指标：正例进入 Top-20 的比例、负例被正确淘汰的比例、各阶段淘汰原因是否与文献一致。
- 这同时是对"规格写得对不对"的检验：如果 HfO2 都过不了你的规格，规格有问题。

### 3. 运营级评估（Ops 视角）

| 指标 | 定义 |
|---|---|
| 漏斗转化率 | 每阶段输入/输出候选数 |
| 单位成本 | 每个候选在各阶段的 GPU/CPU 小时和美元 |
| 周期时间 | 从规格冻结到候选档案交付的日历天数 |
| 实验吞吐假设 | 若实验室每天 300 样品，一轮组合库验证需几天；瓶颈在表征还是沉积 |
| 决策记录 | 每个阶段门的 Go/No-Go 记录和理由 |

### 4. LLM / agent 评估（对口 Anthropic 类岗位）

- 任务：从 50 到 100 篇薄膜合成文献中抽取"材料、前驱体、沉积方法、温度、退火、衬底、表征结果"。
- 建人工标注金标准（可自己标 30 篇），报精度 / 召回 / 幻觉率。
- 二级任务：让 agent 生成候选材料的实验计划草案，用 rubric 打分（可执行性、安全合规、是否引用了真实前驱体），并记录人工修改比例。
- 这一块的产出直接就是一份"Claude for Materials 的 eval 报告"，是 Anthropic AI for Science PM 岗位最能对上的材料。

## A.5 不外行的几个"必答题"，建议写进复盘

1. 为什么 k 与 Eg 不能同时很高，你的规格如何处理这个权衡。
2. 为什么凸包距离 ≤ 0 不是薄膜可生长的充分条件，亚稳相（铁电正交相 HfO2）为什么能存在。
3. PBE 带隙为什么不能直接用，你用了什么校正。
4. 界面层 SiOx 对 EOT 的贡献，材料级 k 目标为什么要留余量。
5. 耐久 / 保持 / 唤醒为什么不能由计算预测，你的实验计划如何用最少样品回答这几个问题。
6. 你如何证明候选是"新"的，而不是训练集里换了个写法的已知物。

## A.6 附录来源

- https://docs.materialsproject.org/methodology/materials-methodology/dielectricity
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5315501 （Petousis 2017 介电数据库）
- https://link.aps.org/accepted/10.1103/PhysRevB.93.115151 （DFPT 基准）
- https://arxiv.org/pdf/2509.26022 （PRX 2026 离子介电张量 ML）
- https://arxiv.org/pdf/2601.04755 （等变 GNN 介电张量）
- https://www.alphaxiv.org/abs/2604.21068.md （DielecMIND）
- https://www.nature.com/articles/am201557 （Eg 与 k 权衡）
- https://link.springer.com/10.1038/s41524-022-00832-5 （npj 2022 高-k 筛选）
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5944908/ （JARVIS OptB88vdW / TBmBJ）
- https://jarvis-tools.readthedocs.io/en/master/databases.html
- https://matbench-discovery.materialsproject.org/
- https://arxiv.org/pdf/2304.12924 （溅射 HfO2 铁电）
- https://arxiv.org/pdf/2104.13099 （外延铁电 HfO2 综述）
- https://hal.parisnanterre.fr/LAAS-MPN/hal-05226133v1 （2025 JAP FeFET 综述）
- https://fis.tu-dresden.de/portal/en/publications/ferroelectric-fieldeffect-transistors-based-on-hfo2-a-review(01a4f31c-8d62-4bcd-b63e-fdf4b093d3b8).html
- https://intechopen.com/chapters/39997 （高-k 带阶与 k 窗口）
- https://core-cms.cambridgecore.org/core/journals/mrs-online-proceedings-library-archive/article/band-alignments-of-highk-dielectrics-on-si-and-pt/18E8E6710D6A658583D3CC90D0B3AF3D
- https://deepmind.google/blog/strengthening-our-partnership-with-the-uk-government-to-support-prosperity-and-security-in-the-ai-era/

---

# 附录 B：模型选型（跑什么模型）

原则：不训练任何大模型，全部用开源预训练权重；每阶段一个主模型、一个交叉验证模型；选型理由引公开基准；记录算力与费用。

| 阶段 | 主用 | 备用 / 交叉验证 | 理由 | 算力 |
|---|---|---|---|---|
| 候选空间枚举 | pymatgen + SMACT 电荷平衡；MP 离子替换模型 | 无 | 工业筛选主力仍是原型 + 替换，生成模型是补充 | CPU |
| 结构生成 / CSP | MatterGen（MIT 许可，支持化学体系 + 带隙条件生成） | CrystalFormer-CSP；CALYPSO 作 1 到 2 个体系对照 | 两种生成路径候选分布互补；MatterGen 不支持介电条件，介电靠后筛 | 1 GPU，1k 结构约 1 小时 |
| 松弛与稳定性 | MACE-MP-0 | Orb-v3；MatterSim | 以 Matbench Discovery F1 + 本地氧化物子集 F1 选型；两势差 > 30 meV/atom 标记送 DFT；UMA 需查许可 | CPU 可跑，GPU 更快 |
| 带隙 | ALIGNN JARVIS TBmBJ 带隙模型 | MatGL/M3GNet；MP r²SCAN 查表 | 避免 PBE 低估 | CPU |
| 介电常数 | ALIGNN JARVIS 介电模型 | PRX 2026 离子介电张量模型 / arXiv 2601.04755（若开源）；MP DFPT 查表 | 最弱环节，设高召回 | CPU |
| Si 带阶 | 电荷中性能级经验法 | Top-10 界面 DFT | 分层处理 | CPU / DFT |
| 高精度验证 | Quantum ESPRESSO：PBE 松弛 + DFPT 介电；HSE06 只做 Top-10 | VASP（若有许可） | 20 个结构几百美元内 | 云 CPU |
| 可合成性 | MP ICSD 标记 + matminer 特征的 PU 分类器（唯一自训小模型） | CSLLM | 可解释、可时间切分 eval | CPU |
| 薄膜生长窗口 | pymatgen ZSL 衬底匹配（Si(100)、TiN、Pt） | 文献沉积温度 | 块体稳定 ≠ 可生长 | CPU |
| 新颖性 | pymatgen StructureMatcher 对 MP / Alexandria / OQMD / COD | 无 | 回应 MatterGen 新颖性争议 | CPU |
| 文献与实验计划 | Claude Opus 5.5 / Sonnet 5.5 | Gemini 交叉 | 产出 LLM eval 报告 | API |

不做：从头训练或微调生成模型；用单一 Eg × k 打分替代 Pareto + 硬约束。

最小可行版本（第 1 周，笔记本 CPU）：替换枚举 → MACE-MP-0 → ALIGNN 带隙 / 介电 → 去重 → 回溯测试（HfO2、ZrO2、La2O3 是否进 Top-20）。跑通后再加 MatterGen 与 QE 验证。

## B.1 修正：GNoME 要用，而且要主动谈

官方仓库 google-deepmind/materials_discovery 公开了数据集（38.1 万稳定结构，2024-08 扩至 52 万个距凸包 1 meV/atom 以内）、GNoME 与 NequIP 的 JAX 模型代码和 Colab；约 11.9 万个 r²SCAN 确认稳定的结构已并入 Materials Project。预训练权重是否随仓库发布需看 README 确认。Matbench Discovery 的 GNoME 条目训练数据私有，不可复现。

面试 DeepMind 的四种用法：
1. 候选池：从 GNoME 数据集筛含 Hf/Zr/La/Y/Ta/Nb 的氧化物，与 MatterGen 生成、离子替换枚举三路并行。
2. 凸包参考：用并入 GNoME 后的 MP 凸包判稳定性，比旧凸包更严格。
3. 主动回应批评：Cheetham & Seshadri（Chem. Mater. 2024）指出 GNoME 候选缺乏"可信、新颖、有用"，多为已知结构替换且含不现实的有序排列。本项目的新颖性去重、无序性检查、可合成性评分逐条回应这三点。
4. MLIP 对照：若 NequIP 权重可用，与 MACE-MP-0 交叉验证。

Ops 延伸：A-Lab 自动合成论文曾被质疑 XRD 相鉴定自动化出错。表征自动化的质量控制是自动实验室吞吐的真正瓶颈，适合在面试中展开。

来源：
- https://newscenter.lbl.gov/2023/11/29/google-deepmind-new-compounds-materials-project/
- https://matsci.org/t/number-of-materials-in-gnome-explorer/63304
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11044265 （Cheetham & Seshadri）
- https://www.theregister.com/2024/04/11/google_deepmind_material_study/

---

# 附录 C：面向 DeepMind / Anthropic / OpenAI 的重新定位

## C.1 关键事实

- Periodic Labs（据 hyper.ai 单一来源，未见官方公告）：发布 "Periodic Neon"，基于开源权重 Kimi K2.6 后训练（科学文献 + 代码中间训练，再用自有实验数据做 RL），用于实验室 XRD 分析；自建 FrontierXRD 基准，基线 2.7% 提升到 55.3%。模型由"科学 harness"供给实验上下文、晶体学数据库和分析工具。
- Lila Sciences：官方称在训练科学推理模型，有"验证器与工具驱动的通用 RL 引擎"；后训练工程师 JD 提到使用前沿与开源 LLM，未点名基座。
- DeepMind：Gemini 是实验室的"科学推理层"，机器人做合成与表征；AI co-scientist 是多智能体系统。
- Anthropic：Claude for Life Sciences 走"连接器 + Agent Skills + 提示库"路线，2026 年扩展到化学数据库（ChEMBL、OpenTargets）；材料科学在岗位 JD 里被点名，但产品上还没有材料专属连接器。
- OpenAI：OpenAI for Science 2025 年 9 月启动，2026 年 1 月有 "Research Engineer, AI for Science" 岗位；Periodic Labs 创始人来自 OpenAI。

## C.2 重心调整：从"CSP 流水线"变成"前沿模型驱动的材料发现产品"

这三家是模型公司。它们看材料问题的方式是：**前沿模型是大脑，CSP/MLIP/DFT 是工具，实验室是验证器。** 所以项目的头条应该是 agent 编排层和 evals，CSP 漏斗降为工具层。

新的分层：

| 层 | 内容 | 对应三家公司的什么 |
|---|---|---|
| 大脑 | 前沿 LLM agent：读客户需求 → 写规格 → 调工具 → 解释结果 → 提实验计划 | Gemini 实验室大脑；Claude for Science；OpenAI for Science |
| 工具 / harness | MP、Alexandria、GNoME 数据集查询；pymatgen；MACE/Orb 松弛；ALIGNN 预测；QE 提交；XRD 相鉴定 | Claude 连接器 / MCP；Periodic 的"科学 harness" |
| 验证器 | 凸包距离、带隙阈值、去重、可合成性、XRD 匹配，全部给出可机检的 0/1 或分数 | Lila 的"验证器驱动 RL"；OpenAI 的可验证奖励 |
| 实验 | 组合库沉积与表征计划 | DeepMind 实验室 |

## C.3 三份核心交付物（替代原来的"候选档案"为第一交付物）

1. **Materials Agent Eval Suite**：100 到 200 道可自动判分的任务，分四类：
   - 规格转化：客户自然语言需求 → 结构化规格（与金标准比对字段级精度）。
   - 工具使用：给定规格，agent 能否正确调用数据库、MLIP、预测器并得到正确候选（用回溯测试里的 HfO2 等已知答案判分）。
   - 文献抽取：合成配方抽取的精度 / 召回 / 幻觉率。
   - XRD 相鉴定：用 MP 模拟衍射图加噪声生成题目，判分对错。这直接对标 Periodic 的 FrontierXRD 思路。
   同一套题跑 Claude、Gemini、GPT 三家前沿模型和一个开源模型，出一张对比表。

2. **Build vs Buy vs Post-train 决策备忘录**：对比三条路线的精度、成本、数据护城河、迭代速度和风险。
   - Buy：前沿 API + harness（Anthropic 路线）。
   - Post-train：开源权重 + 自有实验数据 RL（Periodic 路线）。
   - Build：自研（DeepMind 路线）。
   可选小实验：用 Qwen 或 Kimi 的小模型，在 XRD 相鉴定或配方抽取这一个可验证任务上做 SFT，与前沿 API 在同一 eval 上对比。一周、一张 GPU。目的不是训练，而是让备忘录里的数字是自己测的。

3. **闭环运营方案**：实验室吞吐模型、表征自动化的质量控制（A-Lab 教训）、数据管道、阶段门。原来的候选档案和实验计划作为这份方案的附件。

## C.4 三家公司的侧重

| 公司 | 面试时突出 | 项目里对应的部分 |
|---|---|---|
| DeepMind | 闭环实验室运营、吞吐、XRD 质控、GNoME 批评的回应、Gemini 多智能体编排 | 运营方案、XRD eval、GNoME 候选池与凸包 |
| Anthropic | 把 Claude 部署到科研场景：连接器 / Skills 设计、外部伙伴管理、安全与可靠性评估 | 用 Agent Skills + MCP 做一个"材料连接器"原型，eval suite，伙伴（大学实验室 / 设备商）合作手册 |
| OpenAI | 可验证奖励与 RL 思路、科学家与模型协作、评估体系 | 验证器设计、Build vs Post-train 备忘录、eval suite |

## C.5 时间分配调整（8 到 10 周）

| 周 | 内容 |
|---|---|
| 1 到 2 | 最小 CSP 工具层跑通（附录 B 的 MVP）+ 回溯测试 |
| 3 到 4 | Eval suite 四类题目各 25 到 50 道，三家前沿模型跑分 |
| 5 | Agent harness：前沿模型 + 工具调用，跑完整漏斗 |
| 6 | 可选：小模型 SFT 对比实验 |
| 7 | Build vs Buy vs Post-train 备忘录 + 闭环运营方案 |
| 8 | 候选档案、实验计划、复盘、汇报材料 |

## C.6 来源

- https://hyper.ai/en/stories/1e9ac8c903b2b6ef401eec65c77632ce （Periodic Neon，单一来源）
- https://arxiv.org/pdf/2507.20534 （Kimi K2 技术报告）
- https://www.lila.ai/tech
- https://job-boards.greenhouse.io/lilasciences/jobs/4031323009
- https://www.anthropic.com/news/claude-for-life-sciences
- https://intuitionlabs.ai/articles/claude-healthcare-life-sciences-ai-capabilities-2026
- https://jobs.ashbyhq.com/openai/d1425d2b-0c54-4fc9-8e21-fc8b9ae60238
- https://planckperspective.com/quantum/6FVFVmaGFvd
- https://www.rdworldonline.com/google-deepmind-partners-with-u-k-for-its-first-automated-lab/

## C.7 Eval 题库是否合理：设计规则

前提：答案必须来自真实数据（数据库、模拟、人工标注），不能由 LLM 生成。定位为"产品验收测试集"而非基准。

| 类别 | 答案来源 | 可自动判分 | 主要风险与对策 | 题量 |
|---|---|---|---|---|
| XRD 相鉴定 | MP 结构模拟衍射图 + 噪声 / 择优取向 / 杂相 | 高 | 过于简单：分单相、双相混合、含非晶背景 / 仪器展宽三档；用随机应变与掺杂比例生成训练集中不存在的变体 | 50 |
| 工具调用得候选 | 回溯测试：已知高-k 正例进 Top-N，反例被淘汰；"给定体系找 hull 最低结构"类唯一答案题 | 高 | 正例少：用 GNoME 新增结构扩题，减少 MP 污染 | 30 到 40 |
| 文献配方抽取 | 人工标注 30 到 50 篇薄膜论文，每篇 5 到 8 字段 | 中（归一化后字段匹配） | 标注一致性：第二人复标 10 篇，报告一致率 | 30 到 50 |
| 需求转规格 | 必抓硬约束清单（元素黑名单、温度上限、k 阈值）字段级判分；软约束用两人 rubric | 低到中 | 主观性：只对硬约束自动判分 | 20 |

规则：
1. 每题注明答案来源。
2. 先跑三个基线：随机、规则方法（如 pymatgen 匹配器）、无工具裸 LLM。裸 LLM 已高分说明题太易；规则法更高说明工具层才是关键。
3. 所有基于 MP 的题附污染声明。
4. 按难度分档报告，不只报总分。
5. 每类抽 10 道两人独立复核，报告一致率。
6. 总量约 120 道，宁少勿滥。
