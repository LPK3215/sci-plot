---
name: sci-plot
description: |
  Scientific figure prompt engine. Analyzes papers/projects/algorithms/code/documents,
  applies scientific figure conventions, and generates high-quality, cross-platform image
  generation prompts. Users copy prompts into ChatGPT/DALL-E, Doubao, Qwen, Midjourney,
  or any AI image tool to produce figures. Does not generate images directly — produces
  prompts only.

  科研绘图提示词引擎。分析论文/项目/算法/代码/文档，基于科研绘图规范，生成高质量、
  跨平台可用的生图提示词文件。用户将提示词复制到 ChatGPT/DALL-E、豆包、Qwen、
  Midjourney 等任意 AI 生图工具中即可出图。不直接生图，只产出提示词。
---

# Sci-Plot — Scientific Figure Prompt Engine / 科研绘图 —— 从论文到插图的一站式引擎

Turn papers, projects, and algorithms into high-quality, cross-platform image generation prompts. You provide the content, sci-plot produces prompts, you paste them into any image generation tool.

把论文、项目、算法变成可直接用于生图工具的高质量提示词。你提供内容，我输出提示词，你拿提示词去任何生图工具出图。

## Core Positioning / 核心定位

**sci-plot does not generate images directly.** Its workflow chain is:

**sci-plot 不直接生成图片**。它的工作链是：

```
User Input (paper/project/code/doc) → Analysis → Confirmation (language/style/count) → Prompt File Generation → User copies to image generation tool
用户输入（论文/项目/代码/文档）→ 分析 → 确认（语言/风格/张数）→ 生成提示词文件 → 用户自行复制到生图工具
```

Prompts are cross-platform compatible (ChatGPT/DALL-E, Doubao, Qwen, Midjourney, Stable Diffusion, etc.).

提示词是跨平台通用的（ChatGPT/DALL-E、豆包、Qwen、Midjourney、Stable Diffusion 等）。

---

## Mandatory Workflow / 强制工作流 (Every step is mandatory / 每一步不可跳过)

### Round 0: Determine Analysis Target ⛔ / 确定分析目标

1. If the user explicitly specifies a target (path/link/pasted content), use it directly
2. If not specified, auto-detect from the current workspace:
   - Prioritize `.tex` files (LaTeX papers — methods, formulas, architecture are all there)
   - Then `.md` documents, `.pdf`, `.py` and other source files
3. If the workspace also has no analyzable content, prompt the user to provide a target

1. 如果用户明确指定了目标（路径/链接/粘贴内容），直接使用
2. 如果未指定，自动从当前工作区获取：
   - 优先寻找 `.tex` 文件（LaTeX 论文，方法描述、公式、架构都在里面）
   - 其次 `.md` 文档、`.pdf`、`.py` 等源码文件
3. 如果工作区也无可分析内容，提示用户提供目标

### Round 1: Analyze Input Content ⛔ / 分析输入内容

**Read `references/analysis-guide.md` first**, then execute the complete four-step analysis flow according to the four analysis checklists defined there (paper/code/algorithm/document).

**先读取 `references/analysis-guide.md`**，按其中定义的四类分析清单（论文/代码/算法/文档）执行完整的四步分析流程。

Read the target content determined in Round 0, analyze comprehensively, covering the following dimensions:

读入 Round 0 确定的目标内容，全面分析，覆盖以下维度：

| Content Type / 内容类型 | Analysis Points / 分析要点 |
|---------|---------|
| Paper / 论文 | Core innovations (1-3), method input→process→output flow, key experiments/results, architecture/module relationships / 核心创新（1-3个）、方法输入→处理→输出流程、关键实验/结果、架构/模块关系 |
| Project Code / 项目代码 | Project structure, core modules, data flow, key algorithm functions, module dependencies / 项目结构、核心模块、数据流、关键算法函数、模块依赖关系 |
| Document / 文档 | Architecture design, API interfaces, data models, business processes / 架构设计、API接口、数据模型、业务流程 |
| Algorithm / 算法 | Input/output, core steps, key data structures, complexity, baseline comparison / 输入/输出、核心步骤、关键数据结构、复杂度、与baseline对比 |

**Self-check / 自检**: Is the content fully understood? Can you explain the key concepts in your own words?
是否已完整理解内容？关键概念是否能用自己的话讲清楚？

### Round 2: Extract Illustratable Content ⛔ / 提取可图解内容

Filter content from the analysis results that is **suitable for illustration**:

从分析结果中筛选**适合画成图**的内容：

**Must illustrate / 必须图解 (1-2 pages each / 每个 1-2 页):**
- Method overall flow/architecture (input→modules→output) / 方法的整体流程/架构（输入→各模块→输出）
- Each core innovation mechanism (zoomed-in internal view) / 每个核心创新机制（拆开看内部）
- Most compelling experimental results/data / 最有说服力的实验结果/数据

**Optional illustration / 可选图解:**
- Visual comparison with baselines / 与 baseline 的可视化对比
- Key data processing pipelines / 关键数据处理流程
- System architecture/module relationship diagrams / 系统架构/模块关系图

**Do NOT illustrate / 不图解:**
- Related work/background introduction (text suffices) / 相关工作/背景介绍（文字即可）
- Multiple similar ablation experiments / 多个类似的消融实验
- Abstract inspiration/concepts / 抽象灵感/概念

### Round 3: Ask the User ⛔ / 询问用户

**Read `references/layout-rules.md` first**, then organize the plan using the page roles defined there (cover / method-overview / mechanism-detail / comparison / evidence / architecture / data-flow / takeaway) and their recommended pacing.

**先读取 `references/layout-rules.md`**，按其中定义的页面角色（cover / method-overview / mechanism-detail / comparison / evidence / architecture / data-flow / takeaway）和推荐节奏来组织方案。

Confirm the following 5 items. If the user does not reply, provide default recommendations:

确认以下 5 项，用户未回复则给出默认建议：

1. **Language / 语言**: Chinese / English / Bilingual (default: Chinese) / 中文 / English / 双语（默认：中文）
2. **Visual Style / 视觉风格** (see style table below / 选项见下方风格表)
3. **Number of Figures / 生成张数**: Recommend based on content complexity, explaining what each figure covers / 基于内容复杂度给出建议，说明每张讲什么
4. **Aspect Ratio / 图片比例**: 16:9 (landscape) / 4:3 (landscape) / 2:3 (portrait, default for method diagrams) / 16:9（横版）/ 4:3（横版）/ 2:3（竖版），默认竖版 2:3 用于方法图解
5. **Purpose / 用途**: Journal figure / Technical blog / README / Defense presentation / Xiaohongshu science communication / 论文配图 / 技术博客 / README / 答辩展示 / 小红书科普

**Confirmation template / 确认话术示例:**

> After analysis, I recommend generating 5 figures:
> 1. Method overview (input→process→output full flow)
> 2. Core mechanism A breakdown (explain the most critical innovation)
> 3. Core mechanism B breakdown
> 4. Baseline comparison
> 5. Key results/data
>
> You could also generate just 1 overview, or expand to 8 figures.
> Please confirm: language (Chinese/English)? style (paper-figure/sketchnote)? count? aspect ratio? purpose?

> 我分析后建议生成 5 张：
> 1. 方法总览图（输入→处理→输出全流程）
> 2. 核心机制 A 拆解（讲清楚最关键的创新点）
> 3. 核心机制 B 拆解
> 4. 与 baseline 对比图
> 5. 关键结果/数据图
>
> 也可以只生成 1 张总览图，或扩展到 8 张。
> 请确认：语言（中文/English）？风格（paper-figure/sketchnote）？张数？比例？用途？

### Round 4: Generate Prompts ⛔ / 生成提示词

**Read the following files first / 先读取以下文件:**
1. `references/prompt-rules.md` — All rules and template formats / 全部规则和模板格式
2. `references/styles/{selected style}.md` — Detailed specification for the selected style / 对应风格的详细规范

Write a structured prompt for each page and save to `sci-plot-output/prompts/` directory.

为每一页写独立的结构化提示词，保存到 `sci-plot-output/prompts/` 目录。

**Must strictly use the template format defined at the end of `prompt-rules.md` / 必须严格使用 `prompt-rules.md` 末尾定义的模板格式:**
- Chinese description (type, style, language, aspect ratio) / 中文说明（类型、风格、语言、比例）
- Composition description (spatial layout, arrow directions, module positions) / 构图描述（空间布局、箭头方向、模块位置）
- Content elements (specific modules, relationships, annotation text) / 内容元素（具体模块、关系、标注文字）
- English Prompt (complete English prompt, ready to copy into image generation tool) / English Prompt（完整英文提示词，可直接复制到生图工具）
- Copy-to-tool instructions / 复制到生图工具说明

Also follow all constraints in `prompt-rules.md`: three composition layers, ≤3 colors, per-page must-have/forbidden lists, information density requirements.

同时遵守 `prompt-rules.md` 中的全部约束：构图三层次、颜色 ≤3 种、每页必含/禁止清单、信息密度要求。

### Round 5: Output & Summary ⛔ / 输出与汇总

Generate the following outputs:

生成以下产出：

```
sci-plot-output/
├── analysis.md             # Content analysis summary / 内容分析摘要
├── figure-plan.md          # Figure plan (what each page covers) / 图解方案（每页讲什么）
├── prompts/
│   ├── 01-overview.md      # Page 1 prompt / 第1页提示词
│   ├── 02-mechanism-a.md   # Page 2 prompt / 第2页提示词
│   └── ...                 # Subsequent page prompts / 后续页提示词
└── README.md               # Usage instructions (how to copy prompts to each platform) / 使用说明（如何复制提示词到各平台）
```

---

## Five Visual Styles / 五种视觉风格

| Style / 风格 | Visual Effect / 视觉效果 | Best For / 适合场景 | Tool Compatibility / 生图工具兼容性 |
|------|---------|---------|--------------|
| **paper-figure** (default / 默认) | Paper figure style, white background, vector feel modules, restrained colors / 论文框架图风，白底、矢量感模块、克制配色 | Journal figures, README hero, technical display / 论文配图、README 首屏、技术展示 | All tools universal / 所有工具通用 |
| **sketchnote** | Warm research notes style, cream background, hand-drawn lines, colored pencil accents / 温暖科研笔记风，米白底、手绘线条、彩铅强调 | Knowledge sharing, video promotion, learning notes / 知识分享、视频宣传、学习笔记 | All tools universal / 所有工具通用 |
| **journal-minimal** | Nature/IEEE style, extremely restrained academic charts / Nature/IEEE 风，极简克制的学术图表 | Paper submission, defense, group meeting / 论文投稿、答辩、组会 | All tools universal / 所有工具通用 |
| **warm-notes** | Bright handwritten style, approachable yet professional teaching feel / 明亮手记风，亲和且专业的教学感 | Science communication, courses, paper study notes / 科普、课程、论文学习笔记 | All tools universal / 所有工具通用 |
| **business-research** | Business research brief style, structured, data-driven / 商业研究简报风，结构化、数据驱动 | Industry analysis, investor presentations / 行业分析、投资人汇报 | All tools universal / 所有工具通用 |

Detailed specifications in `references/styles/` directory.

详细规范见 `references/styles/` 目录。

---

## Figure Count Recommendations / 生成张数推荐规则

| Content Complexity / 内容复杂度 | Recommended Count / 推荐张数 | Content Allocation / 内容分配 |
|-----------|---------|---------|
| Cover / promotional image / 封面/传播图 | 1 figure / 张 | One overview explaining what was done / 一张总览讲清楚做了什么 |
| Quick understanding / 快速理解 | 2-3 figures / 张 | Overview + core mechanism + results / 总览 + 核心机制 + 结果 |
| Medium (2 core methods) / 中等（2个核心方法） | 4-6 figures / 张 | Overview + 2-3 mechanisms + key results / 总览 + 2-3个机制 + 关键结果 |
| Complex (3+ core methods) / 复杂（3+个核心方法） | 6-10 figures / 张 | Overview + 1 per mechanism + comparison/results / 总览 + 每个机制1张 + 对比/结果 |

**Minimum 1, maximum 10 / 最少 1 张，最多 10 张**. Prefer fewer over more / 宁少勿多.

---

## Quality Standards / 质量标准

### Good Prompt Output / 好的提示词产出
- Information is specific enough ("arrow from A to B" not "draw a flowchart") / 信息足够具体（"这个箭头从A到B"而不是"画个流程图"）
- Style constraints are clear (background color, line style, color limits) / 风格约束清晰（背景色、线条风格、色彩限制）
- Annotation content is precise (variable names, dimensions, key operations) / 标注内容精确（变量名、维度、关键操作）
- Cross-platform compatible (not overly dependent on specific model features) / 跨平台兼容（不过度依赖特定模型特性）

### Bad Prompt Output / 坏的提示词产出
- Vague descriptions like "draw a neural network architecture diagram" / 只说"画一个神经网络架构图"这种模糊描述
- No color limits, resulting in garish output / 没写颜色限制导致花里胡哨
- Annotation text is too wordy / 标注文字太啰嗦
- Too much information crammed into one page / 一页塞了太多信息

---

## Reference Files / 参考文件

- `references/prompt-rules.md` — Core prompt generation rules (composition, annotation, color, forbidden items) / 提示词生成核心规则（构图、标注、色彩、禁止项）
- `references/analysis-guide.md` — Project/paper/code analysis guide / 项目/论文/代码分析指南
- `references/layout-rules.md` — Page composition & role definitions / 页面构图与角色定义
- `references/styles/paper-figure.md` — Paper figure style specification / 论文框架图风规范
- `references/styles/sketchnote.md` — Warm sketchnote style specification / 温暖科研笔记风规范
- `references/styles/journal-minimal.md` — Nature/IEEE minimal style specification / Nature/IEEE 极简风规范
- `references/styles/warm-notes.md` — Bright handwritten style specification / 明亮手记风规范
- `references/styles/business-research.md` — Business research brief style specification / 商业简报风规范
