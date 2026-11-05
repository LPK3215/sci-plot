<div align="center">

<img src="./docs/assets/banner.svg" alt="Sci-Plot — 科研绘图提示词引擎" width="100%"/>

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

```mermaid
flowchart TD
    subgraph ModeA["传统模式: 对方直接出图 (黑盒抽盲盒)"]
        A1["后台直接调生图 API"] --> A2["输出一张死图片 (PNG)"]
        A2 --> A3["致命缺陷: 发现一个错别字或箭头反了<br/>整张图彻底报废，无法局部修改！<br/>且 API 依赖特定环境，断网/欠费直接崩溃。"]
    end

    subgraph ModeB["Sci-Plot 模式: 提示词落实 (白盒可控资产)"]
        B1["萃取全部显性+隐性规范"] --> B2["落盘为结构化提示词 (IR 中间表示)"]
        B2 --> B3["核心优势: 自由微调 (改色号/改标签只需1秒)<br/>全平台跨端消费 (ChatGPT/MJ/豆包自由选)<br/>零代码依赖，永远不崩溃！"]
    end
```

---

## 🖼️ 可视化架构全景

本项目的端到端工作流、双轨规范池与隔离调度全景如下图所示：

![Sci-Plot 架构全景](./docs/architecture.svg)

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
    User["提供公开 GitHub 仓库链接 / 期刊指南"] --> Fetch{"多途径自适应获取"}
    Fetch -->|途径1: 默认高速| S1["脚本通用雷达嗅探 (1秒定位目标)"]
    Fetch -->|途径2: 网络通畅| S2["AI 直接联网 / 在线阅读 GitHub 文件"]
    Fetch -->|途径3: 网络波动/结构复杂| S3["AI 临时拉取本地全文扫描"]
    S1 --> Extract["AI 深度阅读与萃取核心图表规范"]
    S2 --> Extract
    S3 --> Extract
    Extract --> Save["【文件归位】<br/>规范落盘 references/rules-pool/local/downloaded-*.md"]
    Save --> Clean["【彻底清理多余文件】<br/>临时仓库、代码杂质物理级删除，干干净净！"]
    Clean --> Ready["【一劳永逸资产化】<br/>断网可用、防丢失、可自由修改"]
```

### 4. 四重硬核质检网 (Four-Tier Quality Assurance)
提示词的准确性是全系统的生命线，四道质量防线确保零缺陷交付：

```mermaid
flowchart TD
    subgraph Layer1["第一道防线: 底座物理红线 (Base Rules)"]
        L1A["强制负向排除词: 焊死无3D、无油画、无炫光阴影"]
        L1B["文字防崩溃法则: 标签限制 ≤ 8 字符，防止模型字母乱码"]
        L1C["视觉重力法则: 核心主体占 75-85%，拒绝空旷散乱"]
    end

    subgraph Layer2["第二道防线: 外部规范提取门禁 (Verification Gate)"]
        L2A["提取外部仓库时，AI 执行 5 项硬指标自检"]
        L2B["必须包含尺寸、Hex色号、词典、纯净模板，缺一项自动补齐"]
    end

    subgraph Layer3["第三道防线: 烟消云散上下文隔离 (Scope Isolation)"]
        L3A["清空所有未选中的杂乱规则与历史对话干扰"]
        L3B["生成时上下文只允许存在: 底座物理红线 + 唯一选定规范"]
    end

    subgraph Layer4["第四道防线: 自动化 Linter 质检校验 (Compliance Checker)"]
        L4A["自动化测试套件代码级扫描生成的 Prompt"]
        L4B["校验纯白背景、无3D关键词、交付物结构，不合规直接报错拦截"]
    end

    Layer1 --> Layer2 --> Layer3 --> Layer4 --> QualityPrompt["输出: 100% 稳健、发表级的科研提示词"]
```

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
    R0["Round 0<br/>目标锁定"] --> R1["Round 1<br/>语义分析"]
    R1 --> R2["Round 2<br/>切片规划"]
    R2 --> R3["Round 3<br/>沟通选型"]
    R3 --> R4["Round 4<br/>编译落盘<br/>(烟消云散)"]
    R4 --> R5["Round 5<br/>标准交付"]
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
