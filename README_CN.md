<div align="center">

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/LPK3215/sci-plot@main/docs/assets/banner.svg" alt="Sci-Plot — 科研绘图提示词引擎" width="100%"/>
</p>

# Sci-Plot

[![Version](https://img.shields.io/badge/version-1.2.0-brightgreen.svg)](CHANGELOG.zh-CN.md)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-3776AB.svg?logo=python&logoColor=white)](pyproject.toml)
[![AI Skill](https://img.shields.io/badge/AI-skill-6366F1.svg)](SKILL.md)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](tests/run_all_tests.py)
[![Dependencies](https://img.shields.io/badge/dependencies-zero-success.svg)](requirements.txt)

**科研绘图，从论文到插图的一站式提示词引擎。**

Sci-Plot 不在智能体环境中直接调用生图 API，而是产出工业级跨平台提示词。  
用户可将提示词复制到 **ChatGPT/DALL-E、豆包、通义万相、Midjourney、Stable Diffusion** 立即出图，  
也可作为精确规范指导生成 **HTML、SVG、Matplotlib、Origin** 学术图表。

**兼容所有主流 AI 编程助手** — Claude Code、Codex、Cursor、Windsurf、GitHub Copilot、Cline、Antigravity 或任何支持智能体技能的 AI。

[功能亮点](#-核心功能亮点) · [架构图](#-可视化架构全景) · [工作流](#-标准-5-轮工作流) · [快速上手](#-快速上手) · [常见问答](FAQ.md) · [🌐 在线全景观览](https://lpk3215.github.io/sci-plot/)

[English Documentation](README.md)

</div>

---

## 📌 项目总览

- **仓库地址**: [https://github.com/LPK3215/sci-plot](https://github.com/LPK3215/sci-plot)
- **在线全景观览看板**: [https://lpk3215.github.io/sci-plot/](https://lpk3215.github.io/sci-plot/)
- **核心哲学**: **“坚持以提示词作为中间表示（IR），绝不在沙箱内直接生成位图”**

许多科研绘图工具选择在智能体环境内直接调用生图 API 输出 PNG/JPG，但这带来了三个致命工程痛点：
1. **环境绑架与极度脆弱**：直接生图强依赖本地运行环境、特定 CLI 或 API 密钥。一旦换了一个 AI 客户端或网络受限，工具直接崩溃报废；Sci-Plot 拥有**零外部运行时依赖**。
2. **黑盒输出，无法微调**：生成的位图一旦出现字母乱码或连线反向，整张图彻底作废，无法做局部手术级修改。
3. **不可持久化**：位图无法作为可审计、可代码审查（PR）、可版本控制的工程资产沉淀在 Git 仓库中。

| 评估维度 | ❌ 传统直接出图模式（黑盒盲盒） | ✅ Sci-Plot 提示词引擎（白盒 IR 规范） |
| :--- | :--- | :--- |
| **执行模式** | 在智能体环境内强行调用外接生图 API | 纯净提示词架构与结构化 IR 规范合成 |
| **交付产物** | 不可分割的死位图（PNG/JPEG） | 工业级提示词资产包（`.md` 纯文本 IR） |
| **修改容错** | 字母乱码或箭头反向导致整图报废 | **1 秒外科手术级微调**（改色号/改标签极简） |
| **跨端消费** | 被单一 API 密钥与模型环境死死绑架 | 自由复制至 **ChatGPT、Midjourney、豆包** 或编译为 **HTML/SVG** |
| **环境健壮性** | 极度脆弱：依赖外部 Python 包、断网/欠费即崩溃 | **零外部运行时依赖**，永远不崩溃 |
| **版本化管理** | 二进制死图片，无法进行 Git PR 审计与协同 | 纯文本规范，100% 支持 Git 差分比对与长期归档 |

```mermaid
flowchart TD
    subgraph Trad["❌ 传统模式: 智能体直接调用生图 API (黑盒抽盲盒)"]
        direction LR
        T1(["调用生图 API<br/><i>强依赖本地环境与密钥</i>"]) --> T2(["输出死位图<br/><i>不可逆 PNG/JPG</i>"]) --> T3{{"💥 致命痛点<br/><i>单字乱码/连线反向，整张作废无法微调</i>"}}
    end

    subgraph Sci["✅ Sci-Plot 模式: 提示词作为中间表示 IR (白盒全可控)"]
        direction LR
        S1(["双轨萃取规范<br/><i>物理红线 + 学术级风格</i>"]) --> S2(["落盘标准 IR<br/><i>结构化提示词资产</i>"]) --> S3{{"✨ 自由掌控<br/><i>1秒外科级微调 · 零依赖全平台消费</i>"}}
    end

    style Trad fill:#fff1f2,stroke:#fda4af,stroke-width:1.5px,color:#9f1239
    style Sci fill:#f0fdf4,stroke:#86efac,stroke-width:1.5px,color:#166534
    style T1 fill:#ffffff,stroke:#f43f5e,stroke-width:1.5px,color:#9f1239
    style T2 fill:#ffffff,stroke:#f43f5e,stroke-width:1.5px,color:#9f1239
    style T3 fill:#ffe4e6,stroke:#e11d48,stroke-width:2px,color:#881337
    style S1 fill:#ffffff,stroke:#22c55e,stroke-width:1.5px,color:#166534
    style S2 fill:#ffffff,stroke:#22c55e,stroke-width:1.5px,color:#166534
    style S3 fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
```

---

## 🖼️ 可视化架构全景

本项目的端到端工作流、双轨规范池与隔离调度全景如下图所示：

[![Sci-Plot 架构全景](https://cdn.jsdelivr.net/gh/LPK3215/sci-plot@main/docs/architecture_cn.svg)](https://lpk3215.github.io/sci-plot/)

> *图 1：Sci-Plot 流程架构图 (v1.2.0) — 从目标自动探测、双轨规范匹配、烟消云散隔离到多端跨平台自由消费。*

> [!TIP]
> **在线探索可交互架构图集（基于 Archify 动态构建）**：
> - ⚡ **[可交互核心架构（10 分钟速讲版）](./docs/archify/core-architecture.html)** — 聚焦五轮主干管道与隔离约束
> - 🏛️ **[全景系统架构图](./docs/archify/architecture-panorama.html)** — 覆盖全部 12 个模块与双轨知识中枢
> - 🔄 **[工作流执行管道泳道图](./docs/archify/workflow-panorama.html)** — 跨泳道端到端流转与异常门禁
> - ⏱️ **[调用时序链路图](./docs/archify/sequence-panorama.html)** — 典型科研出图请求在各组件间的严格调用链
> - 🌊 **[数据流向与存储图](./docs/archify/dataflow-panorama.html)** — 原始学术文献到经验收提示词资产的全生命周期流转
> - 📊 **[项目交互全景观览页](./docs/project_overview/index.html)** — 完整项目仪表盘与平台快速起步
> - 📸 **[精简版项目名片长图（支持一键导出 PNG）](./docs/project_overview/project_card.html)** — 800px 定宽极简名片与一键分享
> - 📄 **[架构输入蓝图 (diagram-input.md)](./docs/archify/diagram-input.md)** — 单一真实输入源规范

---

## ✨ 核心功能亮点

### 1. 双轨专业规范池 (Dual-Track Rules Pool)
- **本地规范池 (`references/rules-pool/local/`)**：收录核心预置风格（`paper-figure` 顶会线框、`journal-minimal` Nature 极简、`sketchnote` 手绘笔记、`warm-notes` 明亮手记、`business-research` 商业报告）。用户可直接丢入自定义 `.md` 规范，即放即用。
- **云端与外部规范池 (`references/rules-pool/cloud/`)**：
  - **权威期刊在线指南**：直连 Nature、IEEE、Cell、Science 官方图表排版指南；
  - **URL 实时提炼**：直接提供网页链接，智能体自动提取尺寸与配色红线；
  - **外部 Skill 能力借取协议**：**“只借其词（Prompt），绝不调其图（Image API）”**。读取第三方技能的词库与模板，剥离其生图工具调用，无风险复用其领域的顶级绘图能力。

### 2. “烟消云散” 作用域隔离机制 (Scope Isolation)
在人机沟通选定规范后，**其余所有未选中的候选规则、网络链接与探索上下文全部“烟消云散”（清出后续上下文）**。
提示词最终编译阶段仅且只加载：
$$\text{底座物理红线 (base-rules.md)} + \text{唯一选中的专业规范}$$
彻底根除“既想满足 Nature 极简又被 IEEE 粗线框干扰”的风格冲突与模型幻觉。

### 3. 通用外部技能雷达嗅探引擎 (Universal Skill Harvester)
针对公开 GitHub 仓库，无论目录结构如何繁复，本引擎均能秒级锁定核心绘图规范并清洗沉淀为本地永久资产：

```mermaid
flowchart TD
    User(["📥 输入目标: 公开 GitHub 仓库链接 / 期刊指南 URL"]) --> Router{"📡 多途径自适应获取雷达"}
    
    Router -->|⚡ 默认高速| S1["<b>途径 1: 通用启发式雷达嗅探</b><br/><i>1 秒准确定位目标规范文档</i>"]
    Router -->|🌐 网络通畅| S2["<b>途径 2: AI 在线语义速读</b><br/><i>直接读取 GitHub 文件树与内容</i>"]
    Router -->|📦 沙箱兜底| S3["<b>途径 3: 临时隔离区拉取</b><br/><i>网络受限或结构复杂时本地扫描</i>"]
    
    S1 --> Synth[["🧠 AI 深度阅读与规范萃取合成<br/><i>解析尺寸几何、Hex色号、专业词库、Prompt模板</i>"]]
    S2 --> Synth
    S3 --> Synth
    
    Synth --> Save[("💾 规范落盘归位<br/><code>references/rules-pool/local/downloaded-*.md</code>")]
    Save --> Purge(["✨ 物理级彻底清理<br/><i>临时仓库与代码杂质物理级删除，零残留</i>"])
    Purge --> Ready(["🎯 一劳永逸资产化<br/><i>100% 离线可用、防丢失、可自由修改</i>"])

    classDef input fill:#e0f2fe,stroke:#0284c7,stroke-width:1.5px,color:#0369a1;
    classDef router fill:#f8fafc,stroke:#64748b,stroke-width:2px,color:#1e293b;
    classDef route fill:#f1f5f9,stroke:#94a3b8,stroke-width:1.5px,color:#334155;
    classDef synth fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#5b21b6;
    classDef storage fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e40af;
    classDef clean fill:#fef3c7,stroke:#d97706,stroke-width:1.5px,color:#92400e;
    classDef done fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#166534;

    class User input;
    class Router router;
    class S1,S2,S3 route;
    class Synth synth;
    class Save storage;
    class Purge clean;
    class Ready done;
```

### 4. 四重硬核质检网 (Four-Tier Quality Assurance)
提示词的准确性是全系统的生命线，四道质量防线确保零缺陷交付：

```mermaid
flowchart LR
    L1(["<b>🛡️ 第一道防线: 底座物理红线</b><br/>Base Rules<br/><i>焊死无3D · 标签≤8字符 · 视觉主体75-85%</i>"]) 
    --> L2(["<b>🔍 第二道防线: 规范提取门禁</b><br/>Verification Gate<br/><i>5项硬指标核验 · Hex色号 · 剔除生图API</i>"]) 
    --> L3(["<b>💨 第三道防线: 烟消云散隔离</b><br/>Scope Isolation<br/><i>彻底清退候选杂质 · 上下文零规则打架</i>"]) 
    --> L4(["<b>🧪 第四道防线: 自动化质检校验</b><br/>Compliance Linter<br/><i>6大套件自动化扫描 · 纯白底色 · 格式守门</i>"]) 
    --> Output(["<b>🎯 工业级提示词资产 (IR)</b><br/>多平台自由消费无缝交付"])

    classDef g1 fill:#e0e7ff,stroke:#6366f1,stroke-width:1.5px,color:#3730a3;
    classDef g2 fill:#e0f2fe,stroke:#0284c7,stroke-width:1.5px,color:#0369a1;
    classDef g3 fill:#fef3c7,stroke:#d97706,stroke-width:1.5px,color:#92400e;
    classDef g4 fill:#ede9fe,stroke:#8b5cf6,stroke-width:1.5px,color:#5b21b6;
    classDef g5 fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;

    class L1 g1;
    class L2 g2;
    class L3 g3;
    class L4 g4;
    class Output g5;
```

| 质量防线 | 核心机制 | 确保持久成效 |
| :--- | :--- | :--- |
| **第一道防线：底座物理红线** | 绝对物理法则 (`base-rules.md`) | 焊死无3D/油画/杂乱光影；硬核限制英文标签 ≤ 8 字符（防模型乱码）；强制核心图解占画布 75-85% |
| **第二道防线：外部规范提取门禁** | 5 项基准要素强制自检 | 强制核验尺寸比例、明确 Hex 色号、领域词库、纯净描述模板，必须 100% 剥离并拦截外部生图 API |
| **第三道防线：烟消云散隔离** | 上下文物理级清退 ("烟消云散") | 选定规范后，其余候选规则与沟通噪音彻底清空；第四步上下文严格只读：底座红线 + 唯一选定规范 |
| **第四道防线：自动化质检校验** | 自动化测试套件 (`run_all_tests.py`) | 6 大测试套件代码级扫描，确保交付物纯白背景、负向排除词完整、交付物目录严丝合缝 |

---

## 🛠️ 技术栈

| 层次 | 构成模块 | 技术与实现说明 |
|---|---|---|
| **技能契约** | Agent Skill 标准规范 | 标准化 YAML Frontmatter + 5 轮确定性工作流 (`SKILL.md`) |
| **运行时与引擎** | Python 3.10+ | 纯原生标准库 (`urllib.request`, `json`, `ssl`, `base64`, `re`, `pathlib`) — **零外部依赖** |
| **测试与质量保证**| Python 自动化测试套件 | `tests/run_all_tests.py`、pytest、ruff 静态检查 |
| **可视化与展台** | 矢量 SVG 与 HTML5/CSS3 | 现代深色模式仪表盘 (`docs/project_overview/`)、架构图 SVG、品牌横幅 SVG |
| **多端消费载体** | 跨平台提示词与矢量代码 | ChatGPT/DALL-E、Midjourney、SD/Flux、豆包、通义万相、HTML/SVG、Matplotlib、Origin |

---

## 📂 项目结构

```
sci-plot/
├── SKILL.md                              # AI 指令：5 轮标准化工作流与隔离调度
├── README.md                             # 用户说明文档（英文）
├── README.zh-CN.md                       # 用户说明文档（中文）
├── LICENSE                               # MIT 许可证
├── CHANGELOG.md                          # 版本历史（英文）
├── CHANGELOG.zh-CN.md                    # 版本历史（中文）
├── CONTRIBUTING.md                       # 贡献指南（英文）
├── CONTRIBUTING.zh-CN.md                 # 贡献指南（中文）
├── FAQ.md                                # 常见问题解答（独立手册）
├── AUTHORS                               # 作者与维护者清单
├── pyproject.toml                        # PEP 621 包配置与元数据
├── requirements.txt                      # 运行时与可选依赖说明
├── docs/                                 # GitHub Pages 部署根与架构图表资产
│   ├── index.html                        # Pages 部署重定向入口
│   ├── .nojekyll                         # 禁用 Jekyll 静态编译
│   ├── architecture.svg                  # 英文架构全景图
│   ├── architecture_cn.svg               # 中文架构全景图
│   ├── assets/
│   │   └── banner.svg                    # 品牌专属横幅 SVG
│   ├── archify/                          # Archify 可交互架构图集与蓝图
│   │   ├── diagram-input.md
│   │   ├── core-architecture.html
│   │   ├── architecture-panorama.html
│   │   ├── workflow-panorama.html
│   │   ├── sequence-panorama.html
│   │   └── dataflow-panorama.html
│   └── project_overview/                 # 交互式全景观览页与精简名片
│       ├── index.html
│       ├── style.css
│       ├── script.js
│       └── project_card.html
├── scripts/                              # 规范沉淀与雷达检索脚本
│   ├── universal_skill_harvester.py      # 自适应语义雷达扫描引擎
│   ├── fetch_external_skills.py          # 外部技能拉取工具
│   ├── sync_documentation_metrics.py     # 文档一致性与真实指标校验脚本
│   └── visualization/                    # 可视化图表生成脚本
│       └── generate_banner.py            # 横幅 SVG 生成脚本
├── tests/                                # 自动化测试套件 (100% 通过)
│   ├── run_all_tests.py                  # 测试套件统一运行入口
│   ├── test_rules_pool_integrity.py
│   ├── test_prompt_compliance.py
│   ├── test_end_to_end_simulation.py
│   ├── test_cloud_downloader.py
│   ├── test_external_skills_ingestion.py
│   └── test_top10_radar_scan.py
└── references/                           # 核心基座与规范池
    ├── core/                             # 核心基座
    │   └── base-rules.md                 # 底座物理红线（防乱码/限色彩/防3D）
    ├── analysis-guide.md                 # 内容分析清单
    ├── layout-rules.md                   # 页面角色与构图
    ├── prompt-rules.md                   # 提示词语法与反模式
    ├── rules-pool/                       # 【双轨专业规范池】
    │   ├── local/                        # 本地规范池（预置风格与已沉淀规范）
    │   └── cloud/                        # 云端规范池（渠道与借取协议）
    └── renderers/                        # 矢量渲染器与模板
        └── html/                         # 印刷级学术静态 HTML 图表模板
```

---

## 🚀 快速上手

### 1. 零环境依赖直接使用
在任何包含 sci-plot 的开发环境（Cursor、Claude Code、Windsurf、Copilot、Cline、Antigravity）中直接向 AI 发送：

```text
按照 /sci-plot/SKILL.md 技能的要求输出科研绘图提示词。
目标：[可选，不填则自动分析当前项目，也可填路径/arxiv链接/直接粘贴文本]
```

### 2. 运行本地自动化测试套件
验证规范池完整性、合规门禁及通用雷达扫描能力：

```bash
python tests/run_all_tests.py
```

全部测试基于 Python 原生标准库运行，秒级执行且零环境报错。

---

## 🔄 标准 5 轮工作流

```mermaid
flowchart LR
    R0(["<b>Round 0</b><br/>🎯 目标探测<br/><i>自动感知 .tex / .md / 代码</i>"]) 
    --> R1(["<b>Round 1</b><br/>🔬 语义深度分析<br/><i>萃取核心逻辑、公式与流向</i>"]) 
    --> R2(["<b>Round 2</b><br/>📐 提取图解切片<br/><i>规划全局架构与局部微观图</i>"]) 
    --> R3(["<b>Round 3</b><br/>🎨 沟通与规范匹配<br/><i>双轨规范池智能匹配与推荐</i>"]) 
    --> R4(["<b>Round 4</b><br/>⚡ 烟消云散单向生成<br/><i>清退噪音上下文，严谨编译提示词</i>"]) 
    --> R5(["<b>Round 5</b><br/>📦 结构化交付落盘<br/><i>输出跨平台工业级提示词资产包</i>"])

    classDef r0 fill:#f1f5f9,stroke:#64748b,stroke-width:1.5px,color:#1e293b;
    classDef r1 fill:#e0f2fe,stroke:#0284c7,stroke-width:1.5px,color:#0369a1;
    classDef r2 fill:#ede9fe,stroke:#7c3aed,stroke-width:1.5px,color:#5b21b6;
    classDef r3 fill:#fef3c7,stroke:#d97706,stroke-width:1.5px,color:#92400e;
    classDef r4 fill:#ffedd5,stroke:#ea580c,stroke-width:1.5px,color:#9a3412;
    classDef r5 fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;

    class R0 r0;
    class R1 r1;
    class R2 r2;
    class R3 r3;
    class R4 r4;
    class R5 r5;
```

### 输入支持
- **本地论文/源码**：自动识别 `.tex` LaTeX 源文件、`.md` 文档、PDF 或 Python 模型代码；
- **ArXiv 链接与 ID**：如 `https://arxiv.org/abs/1706.03762` 或 `1706.03762`；
- **直接粘贴文本**：摘要、方法章节或算法伪代码；
- **自定义规范指定**：本地 `.md` 文件路径、期刊官网链接或外部 Skill 名称。

### 输出目录结构
统一输出至 `sci-plot-output/` 目录：
```
sci-plot-output/
├── analysis.md             # 论文创新点、流程与输入输出深度分析
├── figure-plan.md          # 系列图解总规划（各页主题与角色）
├── prompts/
│   ├── 01-overview.md      # 第 1 页结构化提示词（含中英文）
│   ├── 02-mechanism.md     # 第 2 页机制放大提示词
│   └── ...
└── README.md               # 消费指引（出图与转代码教程）
```

### 提示词多端消费对照

| 目标消费平台 | 使用方式 | 产出类型 |
| :--- | :--- | :--- |
| **ChatGPT / DALL-E (推荐)** | 复制 English Prompt 直接粘贴发送 | 高清发表级学术插图 |
| **豆包 / 通义万相** | 复制 English Prompt 或中文提示词直接粘贴 | 快速概念草图/插图 |
| **Midjourney** | 发送 `/imagine` 粘贴 English Prompt | 高质感表现图 |
| **Stable Diffusion / Flux** | 粘贴至 txt2img 正向提示词框 | 本地免 API 自由跑图 |
| **代码/绘图软件 (SVG/Matlab)** | 将 Prompt 中的模块坐标与流向发给代码大模型 | 矢量代码/可交互图表 |

---

## ❓ 常见问题解答 (FAQ)

- **Q: 为什么坚持只出提示词，绝不直接调 API 生图？**  
  *A: 直接生图会导致环境强绑定、无法二次微调以及网络失败崩溃。提示词作为可复用的中间表示（IR），能跨平台自由消费并作为代码资产永久沉淀。*
- **Q: 什么是【烟消云散】作用域隔离机制？**  
  *A: 在 Round 3 选定风格后，所有未被选中的候选规则立刻从上下文剥离，Round 4 仅依据底座物理红线 + 选定规则进行编译，根除模型幻觉冲突。*
- **Q: 如何添加自己实验室的画图规范？**  
  *A: 仅需在 `references/rules-pool/local/` 下添加一个 `.md` 文件（如 `my-lab-style.md`），AI 即可动态自动识别，无需变动任何核心调度代码。*

👉 查阅完整 **[FAQ.md](FAQ.md)** 获取更多高频解答。

---

## 🤝 贡献指南

欢迎参与社区贡献与规范共建！请参阅：
- **[CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)** (中文贡献指南)
- **[CONTRIBUTING.md](CONTRIBUTING.md)** (English Guide)

---

## 📜 许可证与作者

- **许可证**: [MIT License](LICENSE) &copy; 2026 LPK3215
- **维护作者**: LPK3215 (`17538703215@163.com`) — 详见 [AUTHORS](AUTHORS)
- **版本历史**: 详见 [CHANGELOG.zh-CN.md](CHANGELOG.zh-CN.md)。
