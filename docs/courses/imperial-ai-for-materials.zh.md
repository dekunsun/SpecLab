# 帝国理工 MATE70026《AI for Materials》课程调研

逐讲详细讲解（第 1–9 讲，含幻灯片）见 [imperial-ai-for-materials-lectures.zh.md](imperial-ai-for-materials-lectures.zh.md)。

调研日期：2026-10-28（美西时间）
课程网站：https://aronwalsh.github.io/MLforMaterials/Overview.html
新组织：AIforMaterials（GitHub）
授课：Aron Walsh（帝国理工材料系）

## 调研范围

- 读过：课程网站的 Overview、Contents、Learning outcomes、Resources 页，以及第 1–9 讲 notebook 的正文。
- 讲课幻灯片：首次调研时没读；2026-10-29 补读了第 1–9 讲全部幻灯片，见逐讲讲解。
- 新组织 AIforMaterials 只有简介页和两个仓库（`lectures`、`labs`），两个仓库的 README 都几乎是空的，新版内容还没放出来。
- 没能核实：GitHub 组织 API 在本会话被拦，仓库列表来自网页；aiformaterials.github.io 返回 404。

## 课程概况

- 帝国理工材料系模块 MATE70026，面向高年级本科生和研究生。原名 Machine Learning for Materials，现改名 AI for Materials。
- 前提是会 Python；硕士生要先修 Intro to Python。
- 形式：每讲一份 Colab notebook 加一道练习。期末是"研究挑战"：按学号随机分到一个 Matbench 数据集，自己建模型，交 notebook 和 5 分钟录屏讲解。
- 目标：学会把组分–结构–性质数据表示成机器学习能用的形式，用公开工具和开放数据集建模、训练、评估，并了解 AI for Science 的近期进展。

## 各讲内容

| 讲次 | 主题 | 练习 / 工具 |
|---|---|---|
| 1 | 科学编程入门、AI 在科学中的历史 | 硅中杂质扩散的回归 |
| 2 | 机器学习基础 | 用 matminer 特征和随机森林预测 1 万多种晶体的体模量，看特征重要性 |
| 3 | 材料数据：FAIR 原则、数据质量 | 用 OPTIMADE（20 多个数据库、2000 多万个结构）和 MPRester 查热电材料；elementembeddings 加降维可视化 |
| 4 | 晶体表示：组分、结构、晶体图 | 用 pymatgen 建钙钛矿，dscribe 描述符，用 SMACT 枚举电荷平衡的组分；氮化物练习 |
| 5 | 经典学习：kNN、k-means、决策树 | 判断金属还是绝缘体 |
| 6 | 深度学习：感知机、卷积网络 | 合成显微图像、图像重建 |
| 7 | 从零建模 | matbench_log_kvrh，xgboost，交叉验证，超参数优化，模型评估和速度 |
| 8 | 加速发现：自动驾驶实验室、贝叶斯优化、强化学习 | 用 scikit-optimize 的 gp_minimize 做闭环优化 |
| 9 | 生成式 AI 与研究挑战 | 目录写的是大语言模型、从潜在空间到扩散模型、科学智能体；notebook 本身是研究挑战 |
| 10 | 未来方向 | 客座讲座 |

## 值得注意的细节

1. **第 3 讲专门提醒数据风险。** 大多数计算数据库算的是 0 K 下的静态晶体，现实中温度会改变结构和性质，所以用作"真值"时要打折。
2. **研究挑战要求声明 AI 用法。** 用了哪个大模型、做了什么任务、发现了什么局限和偏差、怎么保证使用合乎伦理。
3. **资源页列了四个基准**：Matbench、Matbench Discovery、MLIP-Arena、JARVIS-Leaderboard。工具有 matminer、automatminer、elementembeddings、matgl、dscribe、deepchem、mlflow/wandb。另有"Agents for Science"和"Automated Experiments"两份指南。推荐阅读里有论文《Has Generative Artificial Intelligence Solved Inverse Materials Design?》。
4. **改名后的新版**会讲生成模型、大语言模型和自主实验室，配一本书《Introduction to Artificial Intelligence for Materials》，面向高年级本科生和低年级研究生，许可是 CC BY-NC-ND 4.0。

## 和 SpecLab 的对应

这门课基本是 SpecLab 工具层的教科书版。

| 课程内容 | SpecLab 里对应的做法 |
|---|---|
| 第 3 讲：数据库是 0 K 静态晶体 | 漏斗里声明了 0 K、有序结构、PBE 精度这些限制。SpecLab 还发现数据库字段本身会出错：JARVIS 的 `ehull` 字段不能用，改为用 pymatgen 自己重算凸包 |
| 第 4 讲：SMACT 电荷平衡枚举 | 提案里写的候选空间生成方法。实际漏斗用 pymatgen 猜氧化态，思路相同 |
| 第 5 讲：用带隙区分金属和绝缘体 | 漏斗带隙关卡的基础。SpecLab 多一步：按 PBE 和 TBmBJ 的误差设容差（PBE 3.4 eV，TBmBJ 4.25 eV） |
| 第 7 讲：数据划分、交叉验证 | XRD 评测分公开题和保留题，先预登记再评估 |
| 资源页：Matbench Discovery 等基准 | 选通用势 MACE-MP-0 时参考的是 Matbench Discovery |
| 第 8 讲：贝叶斯优化闭环 | **SpecLab 还没做。** 漏斗只筛一次，没有"实验结果回来再选下一批"的环。如果要补一块，这是最自然的一块 |
| 研究挑战的 AI 用法声明 | 和 `docs/registration.md` 的预登记加偏差记录是同一种纪律 |

## Walsh 和之前调研的交集

- `research_notes/CSP 研究进展与产业格局 2026/industry_china_europe.md` 记录他 2026 年 1 月出任 CuspAI 首席科学官（另有一条 LinkedIn 说法冲突，未查实）。
- 方法调研引用了他组 2026 年的预印本 Negishi & Walsh（arXiv 2606.23166）：81% 到 92% 的生成亚稳晶体是训练集重复或元素替换。
- 他组的 Chemeleon 是 2025 年的生成模型（Nat. Commun. 2025）；SMACT 和 elementembeddings 也出自他组。
- 课程推荐的《Has Generative AI Solved Inverse Materials Design?》和 SpecLab 对生成模型"新颖性"的保留态度一致，可对照 `reports/GNoME 支持与质疑论文.md`。

## 和 Stanford CS336 怎么搭配

| | CS336（从零构建语言模型） | MATE70026（AI for Materials） |
|---|---|---|
| 侧重 | 模型这一侧：分词器、Transformer、GPU 和并行、规模定律、数据、对齐和强化学习 | 领域这一侧：材料数据怎么表示、哪里有坑、怎么评估 |
| 难度 | 作业工程量很大 | 代码停留在 scikit-learn 和小网络，9 个 notebook 在 Colab 上一个周末能跑完 |
| 面试用处 | 前沿实验室会看你是否理解模型怎么训练、怎么评估、钱花在哪 | 补材料领域的词汇和直觉，面 CuspAI 一类公司最贴题 |

建议：
- MATE70026 优先看第 3、4、7、8 讲。
- 新版的生成式 AI 和科学智能体部分放出后再补读。

### CS336 作业怎么取舍

面 PM 和运营岗，考的是能不能讲清模型怎么训练、成本花在哪、怎么评估，不是现场写 GPU 代码，所以作业不用全做。按用处排序：

| 作业 | 内容 | 建议 |
|---|---|---|
| 1 基础 | 分词器（BPE）、Transformer、训练循环 | **自己完整做一遍。** 理解其他一切的基础，也最能说明"真动手做过" |
| 5 对齐和推理 | SFT、用强化学习训练推理能力 | **尽量做。** 后训练是 Periodic Labs 用 Kimi 做的事，也和科学智能体最相关 |
| 4 数据 | 过滤、去重、清洗网页数据 | **做，或至少认真读。** 和运营、数据质量的工作最接近，也呼应 SpecLab 发现的数据库字段出错 |
| 3 规模定律 | 小规模实验外推算力分配 | **读懂原理即可。** PM 要会用它算预算、讲取舍，不一定要跑 |
| 2 系统 | FlashAttention、分布式训练 | **看讲课，不写代码。** 知道为什么要做、能省多少就够，Triton 内核是研究工程师的活 |

- 时间紧就保底做作业 1 和 5，其余看讲课。
- 面试时，"自己写过 BPE 和 Transformer，也做过一次强化学习后训练"再加上 SpecLab，比"五个作业都做完了"更有说服力，因为前者能看出你知道什么值得花时间。

## 待跟进

- 关注 AIforMaterials 组织的 `lectures`、`labs` 仓库和配套书何时放出内容。
- 新版第 9 讲（生成式 AI、科学智能体）放出后，补读并更新本文。
