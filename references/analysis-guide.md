# Project / Paper / Code Analysis Guide / 项目/论文/代码分析指南

## Analysis Objective / 分析目标

Deeply understand any research-related content (papers, projects, algorithms, code, documents) provided by the user, and extract the "core information that can be illustrated."

深度理解用户提供的任何与研究相关的内容（论文、项目、算法、代码、文档），提取出"可以画成图的核心信息"。

---

## Paper Analysis Checklist / 论文分析清单

### Step 1: Quick Overview / 第一步：快速概览
- Paper title, authors, publication date/venue / 论文标题、作者、发表时间/会议
- One-sentence core contribution / 一句话核心贡献
- What problem does it solve / 解决什么问题

### Step 2: Method Breakdown / 第二步：方法拆解
- Overall input→process→output flow of the method / 方法的整体输入→处理→输出流程
- Break down each core module/component / 拆出每一个核心模块/组件
- Internal mechanism of each module / 每个模块的内部机制
- Key differences from existing methods / 与已有方法的关键差异

### Step 3: Experiment Analysis / 第三步：实验分析
- Most important experimental results (not all results) / 最重要的实验结果（不是所有结果）
- Comparison with baselines / 与 baseline 的对比
- The number/chart that best demonstrates the method's effectiveness / 最能说明方法有效的那个数字/图表

### Step 4: Identify "Illustratable" / 第四步：识别"可图解"
- Method overall architecture → Overview diagram (1 page) / 方法的整体架构 → 总览图（1 页）
- Each core innovation mechanism → Mechanism breakdown diagram (1 page each) / 每个核心创新机制 → 机制拆解图（每个 1 页）
- Key experimental results → Data/comparison chart (1-2 pages) / 关键实验结果 → 数据图/对比图（1-2 页）
- Unimportant or text-suffices content → Skip / 不重要或文字就能说清楚的内容 → 跳过

---

## Project Code Analysis Checklist / 项目代码分析清单

### Step 1: Project Structure / 第一步：项目结构
- Project purpose/goal / 项目用途/目标
- Core directory structure / 核心目录结构
- Main entry files / 主要入口文件

### Step 2: Core Modules / 第二步：核心模块
- Responsibilities of key modules/classes / 关键模块/类的职责
- Dependency relationships between modules / 模块之间的依赖关系
- Data flow direction / 数据流方向

### Step 3: Algorithm Logic / 第三步：算法逻辑
- Core algorithm input/output / 核心算法的输入/输出
- Main steps and decision points / 主要步骤和决策点
- Key data structures / 关键数据结构

### Step 4: Identify "Illustratable" / 第四步：识别"可图解"
- System architecture → Architecture diagram (1 page) / 系统架构 → 架构图（1 页）
- Core algorithm flow → Flowchart (1-2 pages) / 核心算法流程 → 流程图（1-2 页）
- Data flow/pipeline → Data flow diagram (1 page) / 数据流/管道 → 数据流图（1 页）
- Module relationships → Component relationship diagram (1 page) / 模块关系 → 组件关系图（1 页）

---

## Algorithm Analysis Checklist / 算法分析清单

### Step 1: Algorithm Elements / 第一步：算法要素
- Input format and constraints / 输入格式和约束
- Output format and meaning / 输出格式和含义
- Core idea (one sentence) / 核心思想（一句话）

### Step 2: Algorithm Steps / 第二步：算法步骤
- Step-by-step breakdown of algorithm flow / 逐步拆解算法流程
- Key operations at each step / 每步的关键操作
- Time complexity / space complexity / 时间复杂度/空间复杂度

### Step 3: Baseline Comparison / 第三步：与 baseline 对比
- What method is it better than, and why / 比什么方法好在哪
- Key innovation points / 关键创新点

### Step 4: Identify "Illustratable" / 第四步：识别"可图解"
- Algorithm overview flow → Flowchart (1 page) / 算法总览流程 → 流程图（1 页）
- Core innovation steps → Detail diagram (1-2 pages) / 核心创新步骤 → 细节图（1-2 页）
- Baseline comparison → Comparison chart (1 page) / 与 baseline 对比 → 对比图（1 页）
- Complexity/performance → Data chart (1 page) / 复杂度/性能 → 数据图（1 页）

---

## Document Analysis Checklist / 文档分析清单

### Step 1: Document Positioning / 第一步：文档定位
- Document type (technical doc / API doc / design doc / whitepaper) / 文档类型（技术文档/API 文档/设计文档/白皮书）
- Core topic / 核心主题

### Step 2: Structured Information / 第二步：结构化信息
- Architecture/design overview / 架构/设计概览
- API/interface list / API/接口清单
- Data model / 数据模型
- Key processes / 关键流程

### Step 3: Identify "Illustratable" / 第三步：识别"可图解"
- System architecture → Architecture diagram / 系统架构 → 架构图
- API call flow → Flowchart / API 调用流程 → 流程图
- Data model relationships → ER diagram / relationship diagram / 数据模型关系 → ER 图/关系图
- Business processes → Swimlane diagram / flowchart / 业务流程 → 泳道图/流程图

---

## Analysis Self-Checklist / 分析自检清单

After analysis, verify each item: / 分析完成后逐条确认：

- [ ] Can you explain what this thing does in one sentence? / 能否用一句话说清楚这东西是做什么的？
- [ ] What are the core innovations/highlights (1-3)? / 核心创新/亮点是什么（1-3 个）？
- [ ] Is the overall flow/architecture line clear (input→process→output)? / 整体流程/架构线是否清晰（输入→处理→输出）？
- [ ] Is each key module's internals understood? / 每个关键模块内部是否理解？
- [ ] What is the most compelling result/data? / 最有说服力的结果/数据是什么？
- [ ] Which content truly needs diagrams, and which can be text-only? / 哪些内容确实需要画图，哪些文字即可？
