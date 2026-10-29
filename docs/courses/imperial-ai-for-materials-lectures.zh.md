# MATE70026《Machine Learning for Materials》逐讲讲解（2026 版）

整理日期：2026-10-29（美西时间）
课程网站：https://aronwalsh.github.io/MLforMaterials/
幻灯片：https://speakerdeck.com/aronwalsh （每讲一份，第 9 讲为 "Challenge"）
课程概况和与 SpecLab 的总体对应见 [imperial-ai-for-materials.zh.md](imperial-ai-for-materials.zh.md)。

## 说明

- **读过的材料**：第 1–9 讲的 notebook 网页全文，以及 Speaker Deck 上的 9 份幻灯片 PDF，共 326 页。只有图片的页面都按 60 dpi 渲染后逐页看过，纯装饰页跳过。
- **主题对应**：每讲的幻灯片和 notebook 主题一一对应。只有第 9 讲例外：课程目录写的是"生成式 AI"，幻灯片和 notebook 实际都是期末作业说明。
- **标注约定**：
  - 标 **【我的观察】** 或 **【我的解读】** 的是我们自己的判断，不是课件原文；
  - 标 **【我跑的】** 的是我们补的小实验，脚本没有存进仓库；
  - 其余内容都能在课件或 notebook 里找到。
- **核对情况**：关键引用和数字已对照幻灯片文字层核对过。小字图表的读数是估计值。

---

## 第 1 讲 Introduction（导论）

### 主旨

Key Concept #1：**机器学习就是函数逼近**。y = f(x)，x 是输入特征，y 是输出性质，f 是模型。要从数据里学出 f，并且"只信那些能推广的结果"（trust what generalises）。

后面每一讲都在回答这句话里的一个问题：x 怎么来（第 3、4 讲），f 选什么（第 5、6 讲），怎么判断能推广（第 7 讲）。

### 幻灯片（31 页）

**课程概览**
- **材料研究的第四范式**：引用 Agrawal & Choudhary, *APL Mater.* 4, 053208 (2016)。

  | 范式 | 年代 | 代表 |
  |---|---|---|
  | 经验科学 | 1600 年前 | 实验 |
  | 理论科学 | 1600–1950 | 热力学定律 |
  | 计算科学 | 1950–2000 | DFT、分子动力学 |
  | 数据驱动科学 | 2000 年后 | 预测分析、聚类、关系挖掘、异常检测 |

- **计算革命**：
  - Babbage 的分析机（1837），两个 20 位数相乘约 3 分钟；
  - Ada Lovelace（1840）："运算科学有其自身的真理和价值"；
  - 苹果片上系统；
  - 百亿亿次超算，即每秒 10¹⁸ 次浮点运算（top500.org）。
- **大模型示例**：通过 LangChain 调 GPT-5，问"给铝离子电池推荐三种新型正极"。
  - 答案是 V₂O₅、Chevrel 相 Mo₆S₈、普鲁士蓝 Fe₄[Fe(CN)₆]₃。
  - 【我的解读】这三种都是文献里早已研究过的铝电池正极，说明大模型擅长调出已知知识，"新颖"要打问号。这和 Walsh 组 2026 年的预印本一致：81–92% 的生成晶体是训练集重复或元素替换。
- **闭环研究流程**：引用 Correa-Baena et al., *Joule* 2, 1410 (2018)。
  - 流程是 理论 → 合成快 10 倍 → 器件组装快 10 倍 → 诊断快 10–100 倍 → 产品，再用"自动反馈环"送回理论。
  - 这是第 8 讲的预告。
- **课程目录**：共 10 讲，第 9 讲是生成式 AI，第 10 讲是未来方向。幻灯片说这是一门"密集的课，需要课后自学"。

**什么是机器学习**
- 定义：从训练数据中学习、建立模型做预测的统计算法。
- 三种学习类型：
  - 无监督：找规律；
  - 监督：用规律；
  - 强化：最大化奖励。
- 材料特征的四种数据类型：
  - 二值：稳定性；
  - 类别：对称性；
  - 整数：化学计量；
  - 连续：速率。
- 四个例子：
  - 回归：提取反应速率；
  - 分类：用决策树预测反应结果；
  - 聚类：高通量晶体学；
  - 强化学习：优化产率。
- 所有算法处理的都是数值数组：标量 → 向量 → 矩阵 → 张量。还有 3×5 矩阵乘 5×1 向量的示意。
- "复杂度旋钮"（图来自 *Machine Learning Refined*）：从线性模型调到高度非线性，旋钮太小欠拟合，太大过拟合。

**简史**
- McCulloch & Pitts 1943 年的人工神经元；
- Turing 1950 年的"机器能思考吗"；
- Arthur Samuel 1959 年（IBM）造出"机器学习"一词。

**行业版图**
- 幻灯片列出的公司：Microsoft Research AI4Science、GE、Matnex、Samsung、TikTok、Altrove、BenevolentAI、Entalpic、Apple、CuspAI、Meta、Toyota、DeepMind、Orbital、Citrine Informatics、Synbiosys。
- 另有一个只有字母"R"的标志，没认出是哪家。

**教材**（从通识到专业）
- Cartwright《Applications of AI in Chemistry》
- Watt 等《Machine Learning Refined》
- Prince《Understanding Deep Learning》
- Sivia《Data Analysis: A Bayesian Tutorial》

**期望与考核**
- 要求到课、到机房，先自己解题。
- 编程没有唯一解。
- 可以用 Copilot、GPT、Gemini，但幻灯片提醒三点：
  - 先懂基础，助手才有用；
  - 助手会给出有 bug、基于过时库的代码；
  - 它替代不了动手经验和材料知识。
- 考核：8 次上机各占 2%，当堂交，截止 15:45；研究作业占 84%。
- 助教名单里有 Masahiro Negishi，即上述"生成晶体多为重复"预印本的第一作者。

### Notebook

- **工具热身**：Jupyter、Markdown、GitHub、Colab（推荐）、Matplotlib、pandas DataFrame、LaTeX。
- **故意埋的 bug**，每处配 Code hint：
  - `plt.plot(, y)` 少了 x；
  - 列名写成 `"Atom Number"`；
  - `np.linspace(0.1, 1, 0)` 取 0 个点；
  - 变量写成 `model2`。
- **物理内容**：热激活扩散的 Arrhenius 公式 D = D₀·exp(−Eₐ/k_BT)。
  - 先写成带 docstring 的函数，画不同 Eₐ 下 D 随 T 的变化；
  - 再画 Arrhenius 图（ln D 对 1000/T，斜率为 −Eₐ/k_B）；
  - 最后用 scikit-learn 对随机数据做线性回归，输出斜率、截距、R²、RMSE。
- **练习 1：硅中杂质扩散**。数据来自 Casey & Pearson (1975)，包括 B、Al、Ga、In、P、As、Sb、Bi 的原子量、D₀ 和 Eₐ。
  - 题目"课上给"。
  - 用学号（CID）作随机种子，每人数据不同。

【我跑的】1100 °C（1373 K）下的扩散系数：

| 杂质 | D（cm²/s） |
|---|---|
| Al | 1.5×10⁻¹² |
| Ga | 4.7×10⁻¹³ |
| P | 3.0×10⁻¹³ |
| B | 1.3×10⁻¹³ |
| In | 7.3×10⁻¹⁴ |
| Sb | 3.2×10⁻¹⁴ |
| As | 2.3×10⁻¹⁴ |
| Bi | 1.0×10⁻¹⁴ |

- Bi 的 D₀ 最大（1030），却扩散得最慢，因为它的 Eₐ 也最高（4.63 eV）。
- ln D₀ 与 Eₐ 的相关系数是 0.94，即补偿效应（Meyer–Neldel 规则）。外推的等速温度约 2600 K，高于硅的熔点。
- 原子量与 Eₐ 的相关系数是 0.84，但只有 8 个点，正是"复杂度旋钮"要警惕的情况。

### 对你有什么用（解读）

- "函数逼近、只信能推广的"、四范式、闭环加速，是前沿实验室材料团队的通用说法，可以套到 SpecLab 上：漏斗是第 3 范式的证据加第 4 范式的工具，缺的是反馈闭环。
- GPT-5 推荐的正极都是已知材料，可以作为讲大模型新颖性局限的现成例子。
- 行业版图那一页可以当面试公司地图用。

---

## 第 2 讲 Machine Learning Basics（机器学习基础）

### 主旨

Key Concept #2 是"拟合 → 验证 → 泛化"。示意图是 train → val（用于模型选择）→ test（上锁，用于模型评估）。原话是 "Trust the test set performance, not the training loss"。

### 幻灯片（44 页）

**开场**
- 层级图：AI ⊃ ML ⊃ DL，ML 下分监督、无监督、强化学习。脚注提到 2024 年诺贝尔化学奖和物理奖。
- vas3k 博客的两张图：Data / Features / Algorithms 韦恩图，以及经典 ML 分类树（分类、回归、聚类、降维、关联）。
- 小测：输入晶体结构，输出 7 种晶系，问这是哪类学习。配文说"黑箱"常被批评，但"有合适工具就能打开"。

**A. 术语**
- 函数逼近 y = f(x)，特征是成分和结构。公式逐步升级：
  - 线性：y = β0 + β1x1 + β2x2；
  - 广义线性：β0 + f1(x1) + f2(x2)；
  - 加耦合项：+ β3x1x2。
- 用 Lennard-Jones 势 `v=(ε/r)**12-(ε/r)**6`（ε=1，r 取 1–2）造数据，scikit-learn 默认参数拟合：

  | 模型 | 拟合情况 | RMSE |
  |---|---|---|
  | 线性回归 | 欠拟合 | 0.039 |
  | 决策树 | 过拟合（阶梯状） | 0.017 |
  | 高斯过程 | 良好 | 0.007 |

- 维度灾难：每维取 10 个点，D 维要 10^D 个样本，数据需求按 O(e^D) 增长（Bronstein et al., arXiv:2104.13478, 2021）。
- 词汇表（参考 Google ML Glossary）：分类模型、回归模型、特征、标注样本、真值、超参数。
- 欠拟合（高偏差）和过拟合（高方差）的图，以及误差–复杂度曲线。
- 典型流程：
  1. 数据清洗和特征工程（"耗人的时间"）；
  2. 按 80/20 划分训练和测试；
  3. 训练、验证；
  4. 评估；
  5. 上线后对新数据做预测（"耗机器的时间"）。

**B. 评估指标**
- MSE、MAE、RMSE。标准差的例子：晶格参数 4、5、6 Å，σ = 1 Å。
- 梯度下降 w ← w − α·dError/dw。警告：局部优化常错过全局最小。
  - 有一个多极小值的 RMSE 曲面动画；
  - 学习率 α = 0 时参数不动；
  - 代码示例：在 x² 上从 x = 5 起步，学习率 0.1，迭代 10 次。
- Pearson r（最早由 Bravais 在 1844 年提出）和 r² 的三种等价定义（引 S. Wright《Correlation and Causation》1921）。
- 相关不等于因果：Messerli, *NEJM* 2012，"巧克力消费量对诺奖人数"，r = 0.791，并画出混杂因子图。
- 混淆矩阵（引 Pearson 1904），用 100 个样本的金属/绝缘体分类举例：
  - 完美模型 [[70,0],[0,30]]；
  - "My best model" [[66,4],[8,22]]，准确率 88%，灵敏度（召回率）94%。
- 小测：20 个点，矩阵为 [[10,2],[?,4]]，答案是 4。

**C. 例子**
- **回归：预测介电常数**（Morita et al., *J. Chem. Phys.* 153, 024503, 2020）。
  - 特征：带隙、ΔPauling、密度、形成能、氧化态、Madelung 能，加 85 维离子种类 one-hot。

  | 模型 | 训练 r² | 测试 r² | 训练 MAE | 测试 MAE |
  |---|---|---|---|---|
  | SVR | 0.92 | 0.86 | 0.24 | 0.44 |
  | DNN | 0.95 | 0.84 | 0.20 | 0.55 |

  - 【我的观察】幻灯片醒目标出的 r² = 0.92 是训练集的数值；DNN 训练更好，测试反而更差。
  - SHAP 分析：密度的重要性排第一。CdCN₂ 的瀑布图给出 ε_pred = 6.55，注明"只是相关，不代表物理联系"。
  - 另一条注：离群点常常有意思，可能是数据质量差，也可能是材料本身特殊。
- **分类：稳定性和可合成性**（Gu et al., *npj Comput. Mater.* 8, 71, 2022）。
  - 方法是 PU learning（只有正样本和未标注样本），输出"crystal likeness"分数。
  - 在 ABX₃ 钙钛矿上比半径比规则的选择性更好。
- **无监督**：用 PCA、t-SNE、UMAP 画材料空间（H. Park et al., *Faraday Discuss.* 256, 601, 2025）。
- **强化学习**：MOF 优化（H. Park et al., *Digital Discovery* 3, 728, 2024）。生成器从拓扑、金属簇、SELFIES 配体中组合，预测器给奖励。

### Notebook

- **数据**：matbench_log_kvrh，1 万多个无机晶体，目标是 log10(K_VRH)。
  - 背景：B = −V∂P/∂V，金刚石 443 GPa。取对数是为了降低偏度。
  - notebook 标题是 "Crystal hardness"，实际预测的是体模量。
- **教学模式**：随机抽 1500 条（random_state = 41），用 5 折代替 10 折交叉验证以加快速度。
- **特征**：pymatgen 成分、`ElementProperty.from_preset('magpie')`、`DensityFeatures`（如每原子体积 vpa）。
- **模型流程**：
  1. `LinearRegression` 基线，只在训练集上报告 MAE、RMSE、r²；
  2. `RandomForestRegressor`（100 棵树，random_state = 42，注释说"42 是科幻梗"）；
  3. notebook 提醒训练集上的高 r² 可能只是过拟合；
  4. 用 `KFold(5, shuffle)` 加 `cross_val_score` / `cross_val_predict` 检验泛化；
  5. 用 `feature_importances_` 画 top-N 特征，提示"vpa 常排前列"。
- **故意埋的 bug**：
  - 直方图用了 `df22`，提示"你的 dataframe 不叫 df22！"；
  - `print(features)` 应为 `feature_cols`；
  - `N =` 留空。
- **练习 2**："特征选择与模型解释"，题目课上给，用学号作种子。
- 【我的观察】两处隐患：
  - `np.mean(np.abs(r2_scores))` 会把负的 r² 变成正数；
  - 交叉验证图的坐标轴写的是 K_VRH，实际画的是 log 值。

【我跑的】合成数据：
- 混淆矩阵 [[66,4],[8,22]] 的召回率 0.943、精确率 0.892，但特异度只有 0.733。88% 的准确率掩盖了 30 个负类里错 8 个。
- 1500 个样本、130 个特征上，随机森林训练 r² 0.949，5 折交叉验证 r² 只有 0.64；线性回归分别是 0.682 和 0.604。
- 纯噪声目标下，交叉验证 r² 均值是 −0.127，取绝对值后变成 +0.127，把失败伪装成了"有一点解释力"。

### 对你有什么用（解读）

- **介电预测与 Clausius–Mossotti 估计器**：
  - 召回率 0.45 意味着漏掉 55% 的真 high-k 材料。漏斗前端最怕假阴性，所以降级为 flag 是对的。
  - 面试时用混淆矩阵语言讲：同时报精确率、召回率和阈值（ε ≥ 21），并说明筛选阶段为什么优先看召回率。
- **评估纪律**：XRD 评测的公开/保留划分加预注册，就是"测试集上锁"那张图用到大模型 agent 评测上。abs(r²) 这类 bug 说明评测代码本身也要审。
- **可合成性**：ehull ≤ 0.05 只是热力学条件。Gu 2022 的 crystal likeness 分数可以作为漏斗的下一层。
- **CS336**：梯度下降、学习率、局部极小、维度灾难都和 CS336 的优化部分直接对应。

---

## 第 3 讲 Materials Data（材料数据）

### 主旨

Key Concept #3 是 FAIR：可发现、可获取、可互操作、可复用。四个要素分别对应持久标识符、许可和接口、机器可读的开放格式、溯源和版本管理。原话是 "Record the database, version, and query used to obtain your datasets"。

### 幻灯片（38 页）

**开场**
- 数据驱动的历史：
  - Pettifor 结构图和人工构造的 Mendeleev 数（*Mater. Sci. Technol.* 1988）；
  - J. C. Phillips 用共价能隙和离子能隙区分四配位和六配位结构（*Rev. Mod. Phys.* 1970）。
  - 幻灯片评价："早期分析靠手工，多是线性关系加物理特征。"
- 表示的重要性：同心圆数据在笛卡尔坐标下线性不可分，换成极坐标就分开了。

**A. 数据来源与格式**
- xkcd 1683（数字数据"永不退化"的讽刺）。
- 四种来源：

  | 来源 | 代价 |
  |---|---|
  | 手工整理 | 耗时 |
  | NLP 提取 | 需要模型和流程 |
  | 现成数据库 | 可能收费 |
  | 自动化实验 | 昂贵 |

- **文献提取**（Schilling-Wilhelmi et al., *Chem. Soc. Rev.* 54, 1125, 2025）：
  - 1996–2023 年各方向论文量，最高约每年 18 万篇；
  - LLM 提取流水线：预处理 → LLM（含 agent）→ 约束解码 → 结构化 JSON（如 `'voc': {'unit':'V','value':1.05}`）→ 评估 → 反馈；
  - 工具：ChemDataExtractor、Ceder 组的 text-mined-synthesis。
- 为什么共享：可复现、可复用、喂统计模型。三种共享形式里，SI 的 PDF"日益过时"，机构库常缺元数据，社区库最好。
- pandas 能读 csv、xlsx、h5、json、stata、pkl 等格式。
- 数据安全：GDPR、加密和哈希、访问控制、完整性。
- **晶体学走在前面**：
  - CSD 从 1960 年开始建，2019 年达到 100 万条；
  - CIF 格式示例（pymatgen 生成的 SnS₂）、checkCIF、VESTA。
- **各类数据库举例**：
  - Zenodo：截图是 Walsh 组自己的条目，包括 CsPbCl₃ 缺陷的 MACE 模型和 SMACT v3.2.0；
  - NOMAD：Fe-O 查询；
  - ICSD：纤锌矿 ZnO，空间群 P6₃mc；
  - Materials Project：Ac₂AgIr（mp-861724），E_hull = 0，带隙 0 eV，形成能 −0.372 eV/atom，但标注 "Experimentally Observed: No"；
  - EMDB（电镜）、nmrshiftdb2（NMR）。

**B. API 查询**
- 三种访问方式：网页（慢）、数据文件（不是最新）、API（要会编程）。提示：记录版本，数据会变。
- OPTIMADE：截图显示 24 个提供方、29 个数据库、27,730,600 个结构。代码示例查询 OQMD 中的 PbO。
- MPRester 示例：`has_props=[HasProps.dielectric]`，专门检索有介电数据的材料。
- matminer 流程：取数据 → 提特征 → 可视化或 ML。示例 `load_dataset("citrine_thermal_conductivity")`。
- xkcd 关于"又多了一个竞争标准"的漫画。
- AiiDA 溯源图：结构、计算、数据之间的连接，以及一个 324 个 COF 项目的大图。
- 图像数据：像素取值 0–255，第 6 讲细讲。
- **propnet 知识图谱**：弹性张量 → Voigt/Reuss 平均 → 体模量和剪切模量 → Pugh 比 → Vickers 硬度。这把第 2 讲的体模量和硬度连了起来。

### Notebook

- **数据警告**：计算数据库大多基于静态晶体，温度效应被忽略，要谨慎对待"真值"。
- **OPTIMADE**：`OptimadeClient(include_providers={"mp"})`，过滤 `nelements=8`。注释列出其他提供方：alexandria、oqmd、jarvis、aflow。
- **MPRester**：示例查询含 Li、带隙 0.5–1.5 eV 的二元和三元化合物，需要自己的 API key。
  - 轶事：去年太多学生同时连接，Imperial 被临时封禁，所以本课改用预建数据集（原话是"cheat"）。
- **数据集**：ucsb_thermoelectrics。下载失败时可从 figshare 手动获取。
- **可视化**：
  - zT 直方图；
  - pymatviz 的周期表热图（对数色标）。
  - 【我的观察】元素用正则 `[A-Z][a-z]?` 提取，统计的是出现次数，不考虑化学计量。
- **PCA**：
  - 完整推导：中心化 → 协方差 → 特征分解 → 排序 → 投影。PCA 是线性方法，非线性结构可改用 t-SNE。
  - 先在 1000 个随机 10 维向量上演示；
  - 再用 ElementEmbeddings 的 `composition_featuriser(embedding='magpie')` 生成特征，标准化后做 2D 和 3D PCA，按 zT 着色。
  - 经验法则：两个主成分超过 50% 可接受，实际应用要 80–90%。
- **故意埋的 bug**：
  - `df2`；
  - `bins =` 留空；
  - `dimensionality = 0`。【我的观察】sklearn 下这不会立刻报错，到画图取第 2 列时才报 IndexError。
- **练习 3**："成分特征与降维"，用学号作种子。
- 【我的观察】特征先 `dropna()`，着色却仍用完整的 `df['zT']`，丢行后长度会对不上。

【我跑的】随机均匀的 10 维数据上，两个主成分只解释 22.8% 的方差。真实 Magpie 特征如果远高于这个值，才说明存在化学规律。

### 对你有什么用（解读）

- **溯源就是面试故事**：你发现 JARVIS 的 ehull 字段不可用，改为用 pymatgen 从形成能重算凸包。这正是"数据完整性和溯源"的实例，可以讲成"发现脏数据 → 修复 → 可复现"。建议写清 JARVIS 快照版本和用来构建凸包的参考相集。
- **交叉核对数据源**：OPTIMADE 的提供方里有 jarvis 和 alexandria，MPRester 能按 dielectric 检索，都可以用来复核 TBmBJ/DFPT 候选。
- **Ac₂AgIr 的提醒**：能量低于凸包不等于实验做得出来。"静态晶体"警告也适用于你的 0 K DFT 性质；声子检查只覆盖动力学稳定性，没覆盖温度效应。
- **大模型产品视角**：Schilling-Wilhelmi 2025 的流水线（约束解码 → JSON → 评估 → 反馈）几乎就是 AI for Science 产品的标准架构，你的 XRD 评测正好落在"评估"一环。
- **CS336**：这一讲对应 CS336 的数据部分（来源、许可、去重、版本）。也可以用 Magpie 加 PCA 画出 SpecLab 候选的化学空间覆盖度，回答"漏斗是不是只在少数化学体系里打转"。

---

## 第 4 讲 Crystal Representations（晶体表示）

### 主旨

Key Concept #4 是 **X = φ(M)**：机器学习不能直接吃"材料"，要先把材料 M 变成数字 X。φ 有很多选择，模型好坏很大程度上取决于这一步。

### 幻灯片（36 页）

**开场**
- 两条路线对比（引 Butler et al., *Nature* 559, 547, 2018）：
  - 最小表示：从头算，输入原子序数 Z 和坐标 R，解 ĤΨ=EΨ 得到性质；
  - 有效表示：监督学习 y = f(X, Θ)。
- 分子画成"原子是节点、键是边"的网络，出处是 Sylvester, *Am. J. Math.* 1878。
- 材料特征跨四个尺度：电子（Å）、纳米（nm）、微结构（µm）、宏观（cm）。图借自 Taylor Sparks。

**A. 成分表示**
- One-hot / multi-hot 编码。
- Magpie 22 维元素特征（Ward et al., *npj Comput. Mater.* 2016），如 MendeleevNumber、Electronegativity、GSbandgap、SpaceGroupNumber。
- 池化：X(Fe₂O₃) = [2X(Fe) + 3X(O)]/5。表中示例：第一维 Fe 0.52、O 0.32，池化后 0.40。也可以用 max 或 min 池化。
- 学出来的表示：
  - SkipSpecies：200 维，从结构图学得（Onwuli, Butler, Walsh, *APL Mach. Learn.* 2024）；
  - Mat2Vec：200 维，在文献上做词嵌入（Tshitoyan et al., *Nature* 2019）。
- ElementEmbeddings 工具包，作者 Anthony Onwuli（Matnex）。最新嵌入包括 CrystaLLM、SkipSpecies、CGNF。
- 维度对比：

  | 表示 | 维度 |
  |---|---|
  | Magpie | 22 |
  | Mat2Vec | 200 |
  | SkipAtom | 200 |
  | MEGNet | 16 |
  | CrystaLLM（来自晶体结构文本） | 512 |

- 元素相似度可以用 Chebyshev 距离、余弦相似度或 Pearson 相关来衡量。H→Bi 的余弦相似度热图和 PCA 图显示元素会自然按族聚类，random_200 作为对照（Onwuli et al., *Digital Discovery* 2023）。

**B. 结构表示**
- matminer 特征器分 composition、site、structure、dos、bandstructure 几类。
- 对称性对比：MgO 为立方晶系，8 原子晶胞；BiVO₄ 为单斜晶系，24 原子晶胞。
- 晶体学的分类规模：7 个晶系、14 种 Bravais 格子、230 个空间群、约 10³ 种原型结构。
- **核心问题**：常规描述（晶胞参数加分数坐标加原子种类）不具备不变性。同一个两原子正交晶胞，换原子顺序、旋转、平移，写出来的矩阵都不同。原话："ML models based on variant representations struggle to generalise"。
- 经典描述符：Coulomb Matrix（Rupp 2012）、ACSF（Behler 2011）、MBTR（Huo 2017）、ACE（Drautz 2019），多数在 dscribe 里有实现。
- 体素网格："早期用过，不推荐"。
- Coulomb 矩阵：对角元 0.5Z^2.4，非对角元 ZᵢZⱼ/Rᵢⱼ，示例是甲醇的 6×6 矩阵。Sine matrix 是周期体系的版本。
- 不变表示的家族树（Musil et al., *Chem. Rev.* 2021）。
- ACE 的构造分三步：
  1. 位点基 φ = R_l·Y_lm；
  2. 对近邻求和，得到置换不变的 Aᵢ；
  3. 对旋转积分，得到 Bᵢ，再用 Property = f(B, Θ)。
- 机器学习力场的三步：参考数据库 → 结构表示 → 回归。点名的前沿实现是 MACE、Allegro、SevenNet，都基于等变神经网络（Morrow, Gardner, Deringer, *JCP* 2023）。
- 应用：用 ACE 模拟 69,120 个原子的 CsPbI₃，展示八面体倾转关联（动画作者 Will Baldwin，*Small* 2024；论文 Xia Liang et al., *JPCC* 2023）。

**C. 图表示**
- 图是跨领域的通用表示：Bronstein 的配图（分子、相互作用组、社交网络）、Battaglia 2018 的 graph networks。
- 图的三部分：节点（原子）、边（键）、全局（晶胞或材料性质）。通常用最近邻的稀疏连接。
- Crystal graph（Xie & Grossman, *PRL* 120, 145301, 2018）：幻灯片说分数坐标"对人类有效"，图"对模型有效"，多条边可以描述周期性。
- 用节点表示晶粒的材料图（Dai, *npj* 2021），以及从原子到器件的多尺度表示（Torrisi, *APL ML* 2023）。
- 学习目标之一："思考用图描述三维结构的局限"。

### Notebook

- 开篇引言来自 John Stewart Bell。环境：matminer、`smact==3.2.0`、plotly、multiprocess。
- **pymatgen 部分**：
  - 用 `Structure.from_spacegroup('Pm-3m', Lattice.cubic(6.41), ['Pb2+','Cs+','I-'], …)` 建立立方 CsPbI₃，5 原子原胞；
  - 导出 CIF 和 POSCAR；
  - 用 `get_distance` 求距离，用 VoronoiNN 和 CrystalNN 求配位数；
  - 用 `BVAnalyzer` 指认氧化态。
- **SineCoulombMatrix**：
  - 代码用 matminer 实现，学习目标里写的却是 dscribe，两处不一致。
  - 先算 CsPbI₃，再把 Pb²⁺ 换成 Sn²⁺，然后问："哪些矩阵元没变？为什么？"
  - notebook 自己指出局限：只含两体信息，键角不同的结构可能得到相同的表示，由此引出 SOAP。
- **SMACT 电荷平衡筛选**：
  - 故意埋的 bug：`elements = ["Cs", "Pb]`，引号没闭合，而且漏了 I。
  - 修好后输出里有 CsPbI₃、Cs₂PbI₄（层状钙钛矿），以及含 Pb⁴⁻ 的 plumbide 组合。
  - 接着把 `ordered_elements(1,83)` 两两组合再加 O，构成 A-B-O 体系，用 4 进程跑 `smact_filter`（外包一层 `safe_smact_filter` 吞掉 TypeError）。
  - 再筛出 (1,1,3) 计量比、O 为 −2 价、A 和 B 都为正价的组合，用 plotly 画 A×B"允许"矩阵热图。
- **练习 4**："Exploring the Chemical Space of Nitrides"，用电荷平衡筛选新钙钛矿并和已知钙钛矿对比。用学号作种子，题目课上给。

【我跑的】用 pymatgen 和 matminer 实际计算：
- Pb 的 CrystalNN 配位数是 6，Pb–I 距离 3.205 Å。
- 把 Pb 换成 Sn 后，Sine Coulomb 矩阵的变化：
  - 对角元 M₀₀ 从 19594 变为 5977，正好是 0.5·Z^2.4（Pb 的 Z=82，Sn 的 Z=50）；
  - Pb 所在行列的非对角元从 215 / 358.8 变为 131.1 / 218.8；
  - 其余元素都不变（Cs 对角元 7513.5，I 对角元 6874.4，Cs–I 170.2，I–I 164）。
- 所以那道思考题的答案是：只有被替换原子所在的行和列会变，因为几何结构没变。

### 对你有什么用（解读）

- **SMACT 就是你提案里写的候选枚举工具**。电荷平衡只是必要条件，你随后从 JARVIS 形成能重算 E_hull ≤ 0.05，补上的是热力学这一层。面试时可以把漏斗讲成：组合约束 → 热力学 → 性质 → 动力学（声子）。
- **Clausius–Mossotti 估计器本质上是手工成分表示**：和 Magpie 加池化属于同一类，不区分结构，同一成分的不同晶型会给出同样的值。召回率 0.45 印证了"表示决定模型性能上限"。
- **MACE 为什么有不变性**：可以借 ACE 的构造来解释。对近邻求和带来置换不变，对旋转积分带来旋转不变。
- **CS336 类比**：X = φ(M) 相当于分词器加嵌入；Mat2Vec 就是材料文献上的 word2vec；CrystaLLM 把晶体写成文本训练。这三点适合用来讲"大模型方法怎么迁移到科学领域"。

---

## 第 5 讲 Classical Learning（经典学习）

### 主旨

Key Concept #5：经典模型是"性质 = f(特征空间里的距离)"，特征靠人工设计（半径、电负性等）。对比的原话是 "deep learning learns the features and prediction model together"。

### 幻灯片（39 页）

**距离**
- Minkowski 距离 d = (Σ|Aᵢ−Bᵢ|^p)^(1/p)（配图来自 Fu & Yang 2021）：

  | p | 名称 | 适用场景 |
  |---|---|---|
  | 1 | Manhattan | 尺度不同或网格结构的数据 |
  | 2 | Euclidean | 稠密、尺度相近（或已归一化）的数据 |
  | ∞ | Chebyshev | 突出最大差异，便于发现离群点 |

**A. k-NN**
- 出处：Fix & Hodges (1951) "Discriminatory Analysis"。
- 预测规则 y = mode(k)，示意图里 k = 5。
- 三个组成：特征空间、距离度量、带标签的训练数据。分类用多数投票，回归用近邻加权平均。
- 1-NN 和 20-NN 的决策边界对比，以及误分类率随 K 变化的曲线。k 太小过拟合，太大欠拟合。
- **指标表**：
  - Accuracy = (TP+TN)/全部
  - Precision = TP/(TP+FP)
  - Recall = TP/(TP+FN)
  - Specificity = TN/(TN+FP)
  - F1 = 2TP/(2TP+FP+FN)，注明"用于类别不平衡"
- 弱点：类别不平衡时要加权；维度太高时要先降维，常用 PCA。
- **应用一：SEM-EDS 矿物分类**（Li et al. 2020）。从图上读数：k-NN 的 F1 约 0.915，随机森林约 0.924，U-Net 约 0.883，k 约为 5 时 F1 最高。
- **应用二：用近红外光谱给古书断代**（Coppola et al., *JACS* 2023，3000 条光谱）。k-NN 的 RMSECV 最小，约 1.3–5.9 年；PLS 约 12–14 年。

**B. k-means**
- 出处：Steinhaus (1957)。
- 目标是最小化簇内平方和 J = Σ|xᵢ−μₖ|²，迭代分配点、更新均值。簇边界是"分段直线"。
- 用碎石图（scree plot）选 k，例子在 k = 4 处出现拐点（Makles 2012）。k = n 时每个点自成一簇。
- 局限：一个点只能属于一个簇。谱聚类等方法能给出隶属概率。
- 应用：Mo–V–Te–Ta 氧化物 STEM 图像聚类，k = 4，比较欧氏度量和角度度量（Belianinov, *Nat. Commun.* 2015）。

**C. 决策树及集成**
- 出处：Morgan & Sonquist (1963)。sklearn 用 CART 算法，可解释性好。
- 示例树按 x2<3、x5<7 分裂，配伪代码（"6 decisions… 4 terminal nodes"）。
- 建树三步：选特征、定分裂准则（如信息增益）、递归生长到最大深度。
- 局限：不稳定（数据稍变可能长出另一棵树）；贪心分裂不保证全局最优。
- 集成示例：三个模型准确率 60%、40%、60%，多数投票后达到 80%。代价是可解释性下降，幻灯片称之为"迈向黑箱的一步"。
- **"From 木 to 林 to 森"**：Walsh 用汉字讲集成。随机森林是独立树的集成，梯度提升是耦合树的集成，y = Σγᵢ·treeᵢ(x)（图来自 Davies 2019）。
- 随机森林用 bagging：每棵树随机抽样本、抽特征。引 Ho, IEEE TPAMI，年份标注 1995。
- 梯度提升（GBR）沿误差梯度逐棵加树，sklearn 默认 100 棵。引了 Kaggle 冠军 Owen Zhang 的话 "When in doubt, use XGBoost"（Chen & Guestrin 2016）。
- **应用一：氧化物带隙**（Davies et al., *Chem. Mater.* 31, 7221, 2019）。
  - 数据：800 个金属氧化物的 GLLB-sc 带隙（Castelli 2015），只用成分，不用结构。
  - SSE 基线散点很乱；GBR 的 RMSE = 0.95 eV。
  - 超参数：1000 棵树，学习率 0.01，最大深度 20，子采样 0.9，每棵树最多 86 个特征，分裂至少 65 个化合物。
  - 从 149 个 matminer 特征里取前 20，最重要的是 Covalent radius (MAD)，其次是每原子体积和电负性。
- **应用二：钢**（Song et al., *Comp. Mater. Sci.* 174, 109472, 2020）。
  - 63,000 个样本，70/30 划分，27 个输入特征，比较 10 种模型。
  - XGBoost 最好：抗拉强度 R² 0.963，MAE 约 15.2。
  - 再选 13 个重要特征，用 PSO 做多目标优化，反推成分和工艺。

### Notebook

- 开篇引言来自 Hugh Cartwright。任务是金属/绝缘体二分类（E_g = CBM − VBM）。引子问题：Cu 和 MgO 一看就知道，那 Tl₂O₃ 和 Ni₂Zn₄ 呢？
- **合成数据**：seed 42，200 个样本 × 10 个特征，特征和标签都是随机的。
  - 先用 PCA 降到 2 维，再做 k-means；
  - 故意设 `n_clusters = 0`，提示"0 个簇会失败"；
  - 问"比抛硬币好吗？"
- **决策树**：故意设 `max_tree_depth = 0`，提示里的双关是 "indecisive tree 🥁"。notebook 指出深树的训练准确率会接近 1.0，那是死记硬背。
- **人造相关性**：把偶数号特征改为 0.333·label + 0.667·噪声，深度 1 的树就能分开。鼓励学生调整 `correlation_strength`。
- **真实数据**：
  - `load_dataset('matbench_expt_is_metal')`；
  - 用 ElementEmbeddings 0.6.1 的 `composition_featuriser` 生成 magpie 嵌入，分别用 mean 和 maxpool 池化；
  - 两份特征各做 k = 2 的 k-means，准确率低于 0.5 就翻转簇标签，注释写着 "It's not cheating :)"，因为簇编号本来就是任意的；
  - 思考题：哪种池化更符合 k-means 的线性可分假设？
- **练习 5**："Comparing Decision Tree Classifiers"，考察特征工程对决策树的影响。用学号作种子，题目课上给。
- 【我的观察】标签约定前后相反：开头定义 y=0 为金属、y=1 为绝缘体；合成数据画图时却把 `labels==1` 标成 'Metal'；matbench 的 `is_metal=1` 又表示金属。合成标签本来就是随机的，不影响结论。

【我跑的】按 notebook 的种子复现合成数据部分：
- 随机数据上 k-means（k=2）准确率 0.465，不如抛硬币。
- 决策树在不同深度下的准确率（留出集是我们另做的 70/30 划分）：

  | 深度 | 1 | 3 | 5 | 10 | 20 |
  |---|---|---|---|---|---|
  | 全量训练准确率 | 0.53 | 0.60 | 0.72 | 0.92 | 1.00 |
  | 留出准确率 | 0.52 | 0.50 | 0.58 | 0.50 | 0.47 |

- 加入 0.333 的相关性后，深度 1 的树准确率达到 0.96。

notebook 本身只在训练集上计算准确率，留出集这一列直观说明了"深树靠死记硬背"。

### 对你有什么用（解读）

- **指标语言**：召回率 0.45 的估计器用这张指标表就能讲清楚。漏斗里每一级过滤器都关心召回率（别误杀好材料）和精确率（别把算力浪费在坏候选上）。high-k 材料本身是少数类，按幻灯片的说法应该看 F1。
- **用误差尺度判断门槛**：Davies 2019 只用成分的带隙模型 RMSE 是 0.95 eV，约等于你 4.25 eV 门槛的四分之一。所以 ML 代理模型只适合宽松预筛，判定仍要靠 TBmBJ 数据。
- **评测卫生**：深树训练 1.00 而留出 0.47、k-means 标签翻转、标签约定不一致，正好对应你 XRD 评测里的公开/保留划分、预注册和明确的标签定义。
- **闭环**：钢的案例（XGBoost 代理加 PSO 反推设计）是这一讲里离闭环最近的例子。
- **CS336**：距离和余弦相似度是 embedding 检索的基础。

---

## 第 6 讲 Deep Learning（深度学习）

### 主旨

Key Concept #6：经典模型用手工特征，深度学习改成"性质 = f(φ(M))"，φ 由网络自己学出来，分为 edge、node、global 三类 embedding。原话是 "GNN learn φ(M) from atoms/bonds"。这一讲从感知机一路讲到通用力场 MACE-MP-0。

### 幻灯片（46 页）

**A. 从神经元到感知机**
- 生物神经元与人工神经元逐项对应：细胞核对应节点，树突对应输入，突触对应权重，轴突对应输出。
- 人脑约 10¹¹ 个神经元、10¹⁵ 个突触，约合 10¹⁵ FLOPS。
- 感知机 y = f(w·x + b)，出处是 Rosenblatt 1957 年的 Cornell 报告（85-460-1）。附代码截图，用 `zip(w, x)` 求加权和。

**B. 网络结构与训练**
- 1–2 层算基本网络，3 层及以上算深度网络，输入层不计入。示例是五层网络，第 2 层做成瓶颈以得到压缩表示。
- 激活函数对照表（含导数）：identity、step（感知机）、logistic（早期常用）、tanh、arctan、ReLU、PReLU、ELU、SoftPlus。
- 万能逼近定理，引用 *Neural Networks* 2, 359 (1989)。【我的观察】幻灯片把第一作者写成 "K. Hurt"，通常记作 Hornik。
- Prince《Understanding Deep Learning》的图：用分段线性拟合一维函数，再把两个各含 3 个隐藏单元的单层网络组合起来。
- **重点页：分布外风险**。四个模型在训练区间 [−0.5, 0.5] 内表现一样，区间外各自发散。原话："Be cautious with out of distribution application"。
- 七种层：dense、conv、pooling、recurrent、dropout、embedding、upscaling。
- 反向传播（链式法则，引 Goodfellow 等）。
  - 局限：训练慢、不收敛、陷入局部极小；
  - 改进：SGD、batch norm（防梯度消失）、自适应学习率。
- 2024 年诺贝尔物理学奖：Hopfield 和 Hinton。Hopfield 网络是确定性的二值节点，找局部极小；Boltzmann 机是随机的，有可见和隐藏节点，找全局极小。

**C. CNN**
- 小测："怎么区分猫和狗？"
- 特征识别：
  - Canny 边缘检测（1986），常用工具 ImageJ、scikit-image；
  - DenseCap（Johnson, Karpathy, Fei-Fei, 2015）用"猫骑滑板"一图演示分类、检测、描述、密集描述四个层次。
- 1 MP 图像 = 10⁶ 个像素，示意图注明由 "DALL-3" 生成。
- 卷积手算：6×6 输入乘 1–9 的 3×3 核，第一格结果是 31。卷积具有平移等变性。
- 小测：用三个核处理疑似室温超导体 LK-99 的图像，答案依次是模糊（1/9 均值核）、水平线检测、边缘检测（中心为 8）。
- LeCun 1989 年的 USPS 邮编识别：16×16 输入，约 1000 个神经元、9760 个参数；训练 7291 张，测试 2007 张，测试集特意放了难以判别的样本。
- LeNet-5（1998，MNIST），附 PyTorch Lightning 代码：
  - conv(1→6, 5)、conv(6→16, 5)；
  - 全连接 16·4·4 → 120 → 84 → 10。
- VGG16；现代模型参数量在 10³ 到 10¹² 之间。
- 带温度 T 的 softmax，类比 Boltzmann 分布和配分函数。示例输入 [3, 6, 7, 11, 4]，输出约 [0.00, 0.03, 0.04, 0.92, 0.01]。【我的观察】T=1 时最大值应为 0.97，T=1.5 时为 0.89，幻灯片的数字只是示意。
- ResNet 残差连接：plain-34 比 plain-18 还差，ResNet-34 比 ResNet-18 好。
- **铁电材料案例**（Kalinin et al., *ACS AMI* 2021）：编码器用 2D 卷积，解码器用 1D 卷积，在畴结构图像和电滞回线之间互译（im2spec / spec2im）。
- **材料图模型**（图示来自 distill.pub 2021，V/E/U 分别为顶点、边、全局）：
  - MEGNet（Chen, *Chem. Mater.* 2019）：按"键 → 原子 → 全局状态"依次更新；
  - M3GNet（Chen & Ong, *Nat. Comput. Sci.* 2022）：加入多体项，输出能量、力、应力；
  - MACE-MP-0（Batatia et al., arXiv:2401.00096）：代码 `mace_mp(model="medium")`，读入 `Sn5S4Cl2.cif` 计算势能。

### Notebook

- 开篇引了冯·诺依曼的话。
- **故意埋的 bug**：
  - `weighted_sum + ...` 应为 `=`；
  - `def sigmoid():` 少了参数 x；
  - `clas SimpleCNN` 少一个 s，提示是 "Clas is a popular name in Sweden"。
- **玩具相图**：两层固定权重网络画温度–压力相图，w = (0.1, −0.1)，v = (0.5, 5)。【我的观察】`predicted_phases[i, j]` 的下标顺序和 contourf 的要求相反，画出来是转置的；两维都是 100，所以不报错。
- **图像滤波**：用 skimage 的 astronaut 图做 Gaussian（σ=10）、Sobel、Laplacian 滤波，再让学生自写卷积核。【我的观察】示例核 [[-2,-1,0],[-1,1,1],[0,1,2]] 元素和本来就是 1，"归一化"一步什么也没改。
- **FashionMNIST**：训练 6 万张、测试 1 万张。CNN 结构 1→32→64 通道，全连接 128→10；Adam，学习率 1e-3，batch 64，训练 1 个 epoch。最后画出第一层的 4 个卷积核作为可解释性展示。
- **练习 6**：
  - 合成 50×50 的"显微图"，σ=1 高斯平滑，20% 像素置 0 模拟测量失败，训练两层 CNN 补全；
  - MSE 损失，SGD，学习率 0.90，500 张图，5 个 epoch；
  - 种子 102，测试图种子 999，个人种子用学号；
  - 具体任务课上给。

【我跑的】用练习原样代码（只有一张测试图、一个种子，仅供参考，MSE 单位是灰度值的平方）：

| 方法 | 缺失像素 MSE |
|---|---|
| 不补（保持 0） | 16119 |
| 全图均值 | 192 |
| 3×3 邻域均值 | **40** |
| 原样 CNN（SGD，学习率 0.9） | 444 |
| CNN（SGD，学习率 0.01） | 217 |
| CNN（Adam，学习率 1e-3） | 44 |

- 原样 CNN 连全图均值都比不过，换成 Adam 才追平零参数的邻域均值。学习率 0.9 很可能是留给课上任务去改的坑。
- 这个设计还有几处值得讨论：输入里没有掩码通道；损失对全部像素计算，而不只是缺失像素；`astype(uint8)` 会让约 1% 越界的值溢出回绕。

### 对你有什么用（解读）

- **MACE 在技术线上的位置**：课程最后一站是 MACE-MP-0 这类通用力场。你用它做结构弛豫，正处在 CGCNN → MEGNet → M3GNet → MACE 这条线的末端。面试时可以讲清"φ(M) 是学出来的"，以及为什么借 Matbench Discovery 选现成模型，而不是自己训练。
- **分布外风险**：high-k 材料落在数据稀疏的尾部，所以用声子软模检查复核 MLIP 结果是站得住的。
- **基线**："零参数基线能打败 CNN"和 XRD 评测里放 random、oracle、NNLS 三个基线是同一种思路。
- **CS336**：带温度的 softmax 就是语言模型采样温度的公式；ResNet 的残差连接就是 Transformer 的残差流。

---

## 第 7 讲 Building a Model from Scratch（从零建模）

### 主旨

Key Concept #7 的原话是 "Better data and leakage-free pipelines beat bigger models"：干净的数据、合理的特征、稳健的划分和交叉验证，比模型大小更重要。

### 幻灯片（41 页）

**A. 数据准备**
- 开场用电影《小魔怪》（Gremlins，1984）对比"教程里的数据"和"现实中的数据"。
- 数据来源有三类：文献、数据库、实验或模拟。数据集分两种：
  - 静态，最常见；
  - 动态，如主动学习，形成"采集 → 训练 → 再采集"的循环。
- 经验法则：经典 ML 每个特征需要 10²–10³ 个样本。【我的观察】幻灯片写"10 个特征 → 10²–10⁴"，按这个法则下限应为 10³。
- "Same Stats, Different Graphs"（Datasaurus）：多组数据的均值（54.26 / 47.83）、标准差（16.76 / 26.93）和 r（−0.06）全都相同，图形却完全不同；另有六种分布共用同一个箱线图。结论是一定要先画图。
- Materials Project 的 PBE 带隙在 0 处有约 5 万条的尖峰，所以要过滤出 >0.5 eV 的部分再看。
- 缺失值和异常值：识别、插补、截尾（winsorising）、删除，必要时做 log 或立方根变换。附 pandas 均值插补代码。
- **特征工程**：
  - Chuang & Keiser (*Science* 2018) 评论 Ahneman 等人的 C–N 偶联研究，发现随机特征和化学特征效果几乎一样：随机森林 R² 分别为 0.92（化学特征）、0.91（随机特征）、0.90（one-hot），神经网络约 0.93；
  - 另有特征选择、PCA，以及沿空间、时间、波长方向的聚合。
- 三种缩放：标准化、min-max、robust（中位数 / IQR）。

**B. 模型选择**
- xkcd 1838（"搅拌这堆线性代数，直到答案看起来对"），以及 sklearn 聚类算法对比图。
- 三个考虑：任务目标、数据量（小数据用简单模型）、复杂度。格言："Use the simplest model that solves your problem"。
- 准确度与可解释性的权衡图。
- **Mignan & Broccardo (*Nature* 2019) 余震预测**：已发表的深度模型有 13,451 个参数，一个神经元（2 个参数）就能达到同样的 AUC 0.847。
- 必须和基线比：分类用"最频繁类别"，回归用"均值"。附 PyTorch 代码，对比 Linear(10→1) 和带 64 个隐藏单元的网络。

**C. 训练与测试**
- 漫画 "Fitting Rooms / Overfitting Rooms"（@redpenblackpen）。
- 标准流程按 80/20 划分。前期数据处理耗人力，训练耗算力。测试集留到最后才碰。
- 优化器：SGD 和 Adam。【我的观察】Adam 的引用写成 "arXiv.1712.6980 (2014)"，正确编号是 1412.6980。
- 提醒："test"和"validation"在不同社区定义不同。
- 交叉验证：k-fold、分层、留一、Monte Carlo。
- 异质数据不宜随机划分，应先聚类再划分。示例是 Verma, Rivera, Scanlon, Walsh (*JCP* 2022) 的 UMAP 分子数据分布图（讲者本人组的工作）。
- 超参数搜索：网格、随机、贝叶斯或进化算法。GridSearchCV 选出最优参数后，要在全部训练集上重训。
- 学习曲线：训练和验证误差差距大是过拟合，误差大且平是欠拟合。原话："单一数字的比较忽略了对数据量的依赖"。
- **反 p-hacking**（Stefan & Schönbrodt, *R. Soc. Open Sci.* 2023, "Big little lies"）：选择性划分、数据泄漏、刻意剔除异常值、不当舍入。
- **Artrith et al. (*Nature Chem.* 13, 505, 2021) 报告清单**，六部分：数据来源、清洗、表示、模型选择、训练与验证、代码与复现。其中 5c 问："划分时是否避免了泄漏，比如同一成分同时出现在训练集和测试集？"
- 收尾引 Schrier et al. (*JACS* 2023)：
  - "Avoid the tyranny of the middle"：最有意思的材料往往是离群点；
  - 数据有限时，方向比精度更有价值；
  - 去填补输入和输出空间里的空白。

### Notebook

- 开篇引了 Mildred Dresselhaus 的话。标题是 "Crystal hardness revisited"，重做第 2 讲的体模量问题。
- **环境与数据**：matminer 0.9.3、xgboost 3.1.2，数据集 matbench_log_kvrh。教学模式随机抽 1000 条（random_state = 33），特征用 Magpie 加 DensityFeatures。
- **故意埋的 bug**：`bins=0`（提示改为 10–20）；`from slearn`（提示 "The library is sklearn!"）。
- **先错着做**：
  - 在全量数据上比较原始特征和缩放后特征的随机森林（max_depth=3），结果一样，得出"树模型对缩放不敏感"；
  - 再训练 XGBoost，然后自己说："We haven't performed proper training and testing yet 😱"。
- **再按正规流程**：
  1. 80/20 划分（seed 42）；
  2. 5 折交叉验证比较随机森林和 XGBoost；
  3. GridSearchCV 调两个 2×2×2 网格；
  4. 在测试集上看 RMSE 和 R²；
  5. 用 `time` 比较训练和预测速度。
- **练习 7**：比较多种回归器，提示"照随机森林的交叉验证流程做"。延伸阅读是 Automatminer（基于 TPOT）。
- 【我的观察】notebook 自己没做到幻灯片的要求：
  - MinMaxScaler 在划分前用全量数据拟合，原则上就是泄漏（对树模型影响可忽略）；
  - 没设 DummyRegressor 基线；
  - 测速用的是未调参的模型；
  - 随机划分没有按成分分组。

【我跑的】合成数据：造 200 个"成分"，每个成分有 5 个近似重复样本，比较两种交叉验证：

| 模型 | 随机 5 折 RMSE | 按成分分组 5 折 RMSE |
|---|---|---|
| 随机森林 | 0.17 | 0.70 |
| 均值基线 | 0.84 | 0.85 |

随机划分让随机森林看起来好了约 4 倍，这正是清单 5c 要防的情况。

### 对你有什么用（解读）

- **按 Artrith 清单自检**：你的 XRD 评测有公开题加保留题、预注册、random/oracle/NNLS 三个基线，几乎能逐条对上这份清单。面试时可以用"按 Artrith 清单自检过"来组织叙述。
- **简单估计器的定位**：Clausius–Mossotti 估计器召回率 0.45，你把它降为 flag。这对应 Mignan 那页"简单模型对复杂模型"和 Schrier 那页"数据有限时方向比精度重要"：保留它作信号，不当判决用。
- **数据和闭环**：JARVIS ehull 字段不可用而改为重算，就是"现实中的数据（Gremlins）"。幻灯片里的"动态数据集（主动学习）"正好点出 SpecLab 缺少反馈闭环。
- **CS336**：5c 的同成分泄漏和大模型评测的数据污染（训练集与测试集去重）是同一个问题。学习曲线可以类比 scaling law。

---

## 第 8 讲 Accelerated Discovery（加速发现）

### 主旨

Key Concept #8：用已有数据决定"下一个最该做的实验（或模拟）"，每一步都在探索和利用之间权衡。配图是 Policy → Action → Environment → Observation → Reward → Feedback 的闭环，例子是"选下一个退火温度来最大化电导率"。

### 幻灯片（39 页）

**开场**
- 引 Hugh Cartwright《Applications of AI in Chemistry》(1993)："AI 问题是复杂到常规算法无法解决的问题。"
- 全讲分三部分：A 自动化实验，B 贝叶斯优化，C 强化学习。

**A. 自动化**
- **Stein & Gregoire (*Chem. Sci.* 10, 9640, 2019)**：
  - 把科研拆成 8 步：计划 → 合成 → 加工 → 表征 → 性能评估 → 数据管理 → 质量控制 → 数据解读；
  - 每一步都能用加速器提速：自动化、并行化、ML 模型、数据库、主动学习、自动推理；
  - 案例：碳纳米管合成一轮约等于 100 次传统实验；光阳极发现一轮约等于 2000 次。图中区分"专家介入"（虚线）和"已集成"（实线）。
- 工业 1.0 到 5.0 的时间轴：1784、1870、1969、2012、今天。
- **MacLeod et al. (*Sci. Adv.* 6, eaaz8867, 2020)**：多功能机械臂改造成薄膜平台，配旋涂机、退火炉、四探针、光谱仪、相机。
- **自驱动实验室 A-Lab**（Szymanski et al., *Nature* 624, 86, 2023；*PRX Energy* 3, 011002, 2024）。课件把它当正面例子，没有提 2026 年的作者更正。
- **帝国理工自己的平台**：
  - ROAR、ATLAS、DIGIBAT，分别覆盖小分子、材料、应用；DIGIBAT 与 Magda Titirici、Ifan Stephens 等合作；
  - Chemspeed 设备照片和工作流（加催化剂 → 加溶剂 → 摇匀 → 加压 → 加热 → 后处理）；
  - 课件说这类平台"通常是专有代码，加 GUI 和 Python API"。
- **机器视觉**（Eppel et al., *ACS Cent. Sci.* 6, 1743, 2020）：在实验室图像里分割容器、液体、固体等。

**优化算法概览**
- 三要素：目标函数 O、可调参数、数据获取方式。
- 局部优化：梯度法（∇O，如梯度下降）、Hessian 法（∇²O，如拟牛顿）。
- 全局优化：数值法（单纯形、模拟退火）、概率法（MCMC、贝叶斯优化）。
- 课件强调这些概念和 ML 模型训练是同一套。

**B. 贝叶斯优化（BO）**
- 来源：Močkus (1974)。
- 两个组成部分：
  - 代理模型 O(x) ~ f(x)，如高斯过程 GP(μ(x), k(x,x′))。核函数决定光滑度和不确定性：相似的 x 共享信息，不相似的 x 回落到均值、不确定性高；
  - 采集函数：UCB、PI、EI。
- Wu et al. (*Digital Discovery* 3, 1086, 2024) 的图：在同一个二维地形上比较三种方法。梯度下降卡在局部极小；从图上读，BO 约 20 步收敛，模拟退火约 35 步。
- UCB：x_next = argmax μ(x) + βσ(x)（Srinivas et al., IEEE Trans. Inf. Theory 58, 2012）。β < 1 偏利用，β ≈ 1 平衡，β > 1 偏探索。
- **应用：P3HT-CNT 复合薄膜**（Bash et al., *Adv. Funct. Mater.* 31, 2102606, 2021）：
  - 流程：滴铸 → FeCl₃ 掺杂 → 高光谱加四探针测试 → 多目标 BO；
  - 用图模型从便宜的表征预测昂贵的电导率；
  - 第 1–4 轮（最小化）和第 5–11 轮（最大化）的 ln(电导率) 分布明显不同。
- **主动学习和 BO 的区别**：BO 找让目标函数最大的输入，主动学习找让不确定性最小的输入。
  - 认知不确定性（数据不够）可以减小；
  - 偶然不确定性（噪声）不能减小。
- **NIMS-OS**（Tamura, Tsuda, Matsuda, arXiv:2304.13927, 2023）：
  - AI 和机器人之间用 CSV 文件闭环：`ai_tool.py` → proposals.csv → `preparation_input.py` → 机器人实验 → `analysis_output.py` → candidates.csv；
  - 描述符可以是离散化参数、材料组合、magpie、Morgan 指纹。

**C. 强化学习（RL）**
- 早期应用：任天堂游戏、Boston Dynamics 机器人、金融。
- Prince《Understanding Deep Learning》的 RL 示意图（策略 π(a_t|s_t)、状态转移、奖励函数），映射到材料研究：
  - 虚拟科学家是 agent，数字实验室是 environment；
  - 状态是成分、结构、工艺，动作是新实验，奖励是性能变化。
- 策略公式 π(a|s) = exp(Q(s,a)/τ) / Σ exp(Q(s,a′)/τ)，原话称之为 "familiar softmax (Boltzmann) policy"，τ 是控制探索与利用的"有效温度"。
- **MOF 例子**（H. Park et al., *Digital Discovery* 3, 728, 2024）：
  - agent 是生成器，组合拓扑（如 pcu）、金属簇和 SELFIES 表示的有机配体；
  - environment 是性能预测器，奖励是 CO₂ 吸附热 Q_st 或 CO₂/H₂O 选择性；
  - t-SNE 图里生成的 MOF 和训练数据分布在不同区域。

**收尾**
- 三种策略对比：

  | 策略 | 优点 | 缺点 |
  |---|---|---|
  | 高通量枚举 | 简单 | 高维时效率低 |
  | BO | 数据效率高，能处理噪声 | 要选代理模型和采集函数，高维吃力 |
  | RL | 能学策略，适应动态环境 | 很耗样本，收敛慢 |

- 闭环发现的四个障碍：材料复杂、数据质量、自动化成本、系统难以改造到新问题。
- 学习成果：会为给定问题选优化策略，会评估 AI 优化工具对材料研究的影响。

### Notebook

- **工具**：scikit-optimize 的 `gp_minimize`（BO）和 `dummy_minimize`（随机搜索）。
- **示范部分**：
  - 虚拟实验是 sin(x) + 0.1x + 0.5·randn，定义域 [−5, 5]；
  - 先随机采样、拟合多项式，采样点数和阶数留空让学生填（建议从 10 个点、2 阶开始逐步加大，看 R² 怎么变）；
  - 再各跑 50 次 BO 和随机搜索（random_state=42），画 GP 置信区间和累积最小值曲线，标题是 "Does BO Beat Random Sampling?"；
  - 强调"总要有一个基准来比较"；
  - 正文给了 RBF 核公式，提到 Matérn 核；步骤编号从 Step 1 跳到 Step 3。
- **练习 8**：用学号作种子，模拟薄膜沉积的两个旋钮 (x, y)，最小化 `supermat`（类 Branin 函数）。提示先定义目标函数，再调用 `gp_minimize`。
- **延伸阅读**：GP 可视化，助教 Yifan 写的化学 BO 综述，Sterling Baird 的 SDL 演示。

【我跑的】本机没装 skopt，用 sklearn 的 GP（Matérn 核）加 EI 写了一个最小版本去最小化 `supermat`。
- 定义域假设为 Branin 的标准范围 x ∈ [−5, 10]、y ∈ [0, 15]，notebook 没有给。
- 网格搜索得到全局最小约 0.398，有多个极小值。
- 5 个种子、每次 30 次评估，中位最好值：

| 评估次数 | BO | 随机搜索 |
|---|---|---|
| 10 | 6.43 | 7.48 |
| 20 | 1.76 | 4.85 |
| 30 | 1.30 | 3.05 |

BO 赢，但优势中等，而且只有 5 个种子。

### 对你有什么用（解读）

- **SpecLab 的闭环缺口**：这讲正好是缺的那一块。
  - 最小可行的闭环：用 GP 或集成模型当代理，用 UCB 或 EI 决定哪些候选值得花 MACE 弛豫和声子计算的钱。
  - 目标是"找最好的 high-k 候选"就用 BO；目标是"让筛选模型更可信"就用主动学习。
  - NIMS-OS 的 CSV 接口和 arm B 的工具循环几乎同构，可以把 agent 定位成"采集函数加执行器"。
- **评估严谨性**：notebook 的 BO 对随机搜索只跑了一个种子，目标函数噪声又大（σ=0.5），累积最小值会奖励"运气好的噪声点"。你的预注册习惯（多种子、报告分布、固定预算）更严。
- **批判视角**：
  - 课件把 A-Lab 当正面例子，没提作者更正；
  - MOF 的生成物在 t-SNE 上和训练数据分开，不等于结构是新的，这和 Negishi & Walsh 的重复和替换问题直接相关；
  - 课件自己把"数据质量"列为闭环障碍。
- **CS336**：RL 策略就是带温度的 softmax，和大模型采样温度同一个公式；"优化和训练是同一套概念"对应 CS336 的优化器部分。

---

## 第 9 讲 Research Challenge（研究挑战）

### 先说明

课程目录和第 8 讲幻灯片里的 Module Contents 都把第 9 讲写成 "Generative Artificial Intelligence"（LLM、从 latent space 到 diffusion、scientific agents）。但第 9 讲的幻灯片（12 页，Speaker Deck 上叫 "Challenge"）和 notebook 都是期末作业说明。

两份材料里都没有生成式 AI 的正文。唯一相关的是一条通知：周五下午 1 点有客座讲座，由 Microsoft AI for Science 的 Tian Xie 主讲，他是 MatterGen 项目负责人。讲座没有幻灯片。课程里离"生成"最近的内容是第 8 讲的 RL 生成 MOF 例子。

### 主旨

每人分到一个 MatBench 数据集，独立做出原创的分类或回归模型，并和社区基准比较。

### 幻灯片（12 页）

- **考核结构**：每讲一个计算练习（当次课结束前交），加一个研究挑战。缺勤和延期申请走 student office。
- **目标**：
  - 应用学到的 ML 和数据技能；
  - 通过自学、探索和同学交流扩展知识；
  - 交出带注释的代码，并和社区基准比较。
- **任务图**：
  - 输入是化学成分（如 TiO₂）和/或晶体结构；
  - 输出是一个或多个性质（示例：E_f = −3.401 eV/atom，E_g = 2.10 eV）。
- **从文献开始**：读 Matbench 论文（DOI 10.1038/s41524-020-00406-3）和其中测过的模型。作业分三块：数据准备；模型选择、训练和测试；结果讨论。
- **Creative Solutions**：没有唯一解，查 matplotlib、scikit-learn 手册，去 StackExchange、GitHub 找思路。
- **LLM 使用声明**，必须写进 notebook：
  - 是否用了 LLM（GPT、Gemini、Co-Pilot 等）；
  - 用于什么任务；
  - 是否注意到局限或偏差；
  - 如何保证合乎伦理。
- **时间**：助教答疑在第 9、10 次课的 14:00–15:00；机房另订了 2 月 13、16、20 日；截止时间 3 月 9 日 15:00。
- **提交**：.ipynb 文件，加不超过 5 分钟的录制讲解（PowerPoint、Zoom 录屏或普通视频都行）。
- **2026 年评分**：

  | 项目 | 权重 | 要求 |
  |---|---|---|
  | 数据准备 | 10% | 合适的预处理 |
  | 模型选择、训练与测试 | 20% | 结合问题论证选择，做恰当的验证和测试 |
  | 模型分析与讨论 | 20% | 含高质量图表 |
  | 代码质量 | 20% | 结构清楚，注释有意义 |
  | 录制讲解 | **30%** | 讲清模型选择、结果和局限 |

- **附录：ML for Materials 的伦理**：偏差与公平、透明与可解释、隐私与数据保护、社会影响（从生产力提升到岗位替代）。

### Notebook

- 开头引言来自 Margaret Atwood："每种技术都有阴暗面，包括弓箭。"
- **分组**：`np.random.seed(CID)` 后用 `np.random.choice` 从 A–E 里抽一组：

  | 组 | 数据集 |
  |---|---|
  | A | matbench_dielectric |
  | B | matbench_expt_gap |
  | C | matbench_expt_is_metal |
  | D | matbench_glass |
  | E | matbench_steels |

- **数据**：用 matminer 的 `get_all_dataset_info` 和 `load_dataset`，特征化也推荐 matminer。
- **建议**：
  - XGBoost 是不错的起点；
  - Colab 算力不够可以用其他免费资源或本地机器；
  - 高级用户可以用 wandb 跟踪实验，想暴力搜索可以试 Automatminer。
  - 原话："Building a useful model with limited resources is a real-world skill"。
- **结构**：问题陈述（含评论排行榜上最好的模型）→ 检查数据分布和预处理 → 选模型并论证、做好划分、考虑超参数 → 分析结果。
- **补充指标**：ROC-AUC（`roc_auc_score`），0.5 等于随机猜，1 为完美分类器。
- **对结果的期望**：要和 MatBench 排行榜比较。资源有限不必追平最好成绩，但要好于基线。
- **LLM 声明**：同样四点，示例模型写的是 GPT-4。
- notebook 的单元格可以自由增删和重排，也可以兼作讲解底稿。

### 关于 A 组数据集

以下是背景知识，文件里没写，使用前请核实：
- matbench_dielectric 的目标值是折射率 n，输入是结构。它对应电子（光学）介电响应，不含离子贡献。
- MatBench 的标准做法是嵌套 5 折交叉验证。

### 对你有什么用（解读）

- **与 SpecLab 直接相关**：用 A 组数据做 high-k 筛选时要注意，折射率只给出 ε∞ ≈ n²，而 high-k 关心的是包含离子贡献的静态介电常数 ε₀。这正好可以展示你"方法误差容限、分清代理指标和真实指标"的思路。
- **评估文化**：作业要求"对照排行榜、必须超过基线"，加上 LLM 使用声明，和你的公开/保留划分、偏差日志是同一种透明度要求，只是更轻。你把它推到了预注册的程度。
- **产品视角**：讲解占 30%、"资源有限也要做出有用的模型"，对应你的预算硬上限和 PRD，可以作为讲 AI for Science 产品取舍的例子。
- **生成式 AI 缺口**：课件里没有这部分，MatterGen 只有讲座通知。准备面试要靠 MatterGen 原论文、Negishi & Walsh 预印本和 GNoME 审计来补。伦理附录（偏差、可解释性）可以作为讨论入口。

---

## 全课小结

- **第 1–7 讲教的是怎么诚实地做一个材料 ML 模型**：表示（φ）、基线、无泄漏划分、只信测试集、记录数据版本和溯源。
- **第 8 讲教的是怎么让模型决定下一个实验**：BO、主动学习、RL、自驱动实验室。
- **第 9 讲是期末作业**，生成式 AI 只有一场客座讲座。
- **SpecLab 已覆盖前一半，评测纪律比课程本身更严**。课程 notebook 自己就有这些问题：
  - 缩放器在划分前拟合，属于泄漏；
  - 缺均值基线；
  - BO 对比只跑一个种子；
  - abs(r²) 打分隐患。
- **SpecLab 还没覆盖的是第 8 讲的闭环**。面试时可以讲成"按这门课的框架检查过自己的项目，缺的是什么、准备怎么补"。
