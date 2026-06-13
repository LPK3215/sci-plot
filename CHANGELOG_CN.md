# 更新日志

sci-plot 所有重要变更均记录于此。

格式基于 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)，
本项目遵循 [语义化版本](https://semver.org/spec/v2.0.0.html)。

[English Changelog](CHANGELOG.md)

## [Unreleased]

### 变更
- 移除 `SKILL.md` frontmatter 中的非标准 `version` 字段，以符合 AI 技能规范（仅保留 `name` + `description`）。版本号仍由本更新日志与 README 徽章追踪。
- 将 `CONTRIBUTING.md` / `CONTRIBUTING_CN.md` 及更新日志中残留的 "CodeBuddy" 品牌字样替换为中性的 "AI"。
- 补全 `README.md` / `README_CN.md` 的项目结构树（新增 `index.html`、`examples/`、`SECURITY.md`）。
- 取消 git 对本地 `.codebuddy/` 目录的跟踪（已加入 gitignore）。

## [1.1.0] - 2026-06-13

### 新增
- 将 `sci-plot-output/` 加入 `.gitignore`，从版本控制中排除生成输出。
- 新增工作流架构图（`docs/architecture.svg` + `docs/architecture_cn.svg`）及生成脚本（`docs/scripts/generate_architecture.py`）。
- 在 README.md 中添加徽章（许可证、版本、AI Skill）。
- 在 README.md 中添加项目结构树、FAQ 章节和作者信息。
- 在 README.md 中添加可视化架构图章节。
- 新增交互式项目全景观览页（`project_overview.html` + `project_overview/`），支持深色主题、动画工作流时间线、风格预览和现代卡片式架构图。
- 新增双语架构 SVG，采用深色主题匹配项目观览页设计。

### 变更
- 英文名称从 "Scientific Figure Prompt Generator" 改为 "Scientific Figure Prompt Engine"；中文标语更新为"科研绘图 —— 从论文到插图的一站式引擎"。
- 面向用户的文档拆分为独立中英文文件：README.md/README_CN.md、CHANGELOG.md/CHANGELOG_CN.md、CONTRIBUTING.md/CONTRIBUTING_CN.md。
- 所有面向 AI 的技能文档（SKILL.md、references/*.md）转为纯英文，提升 AI 理解能力。
- 重新设计架构 SVG，采用双阶段布局，高亮核心步骤（Round 4），现代视觉风格。

## [1.0.0] - 2026-06-13

### 新增
- sci-plot 科研绘图引擎首次发布。
- `SKILL.md`：完整的 6 轮强制工作流（Round 0-5），用于分析研究内容并生成生图提示词。
- `references/prompt-rules.md`：构图、标注、色彩及禁止模式的核心规则。
- `references/analysis-guide.md`：论文、项目、代码、算法分析的详细清单。
- `references/layout-rules.md`：页面角色定义、推荐节奏和构图规则。
- `references/styles/paper-figure.md`：论文框架图风规范。
- `references/styles/sketchnote.md`：温暖科研笔记风规范。
- `references/styles/journal-minimal.md`：Nature/IEEE 极简学术风规范。
- `references/styles/warm-notes.md`：明亮手记风规范。
- `references/styles/business-research.md`：商业研究简报风规范。
- `README.md`：面向用户的说明文档，包含安装、使用、风格和产出结构。
- `LICENSE`：MIT 许可证。
- `.gitignore`：Windows、macOS、IDE 和 Python 文件的版本控制排除。
- `CONTRIBUTING.md`：贡献指南。
- `.gitattributes`：行尾规范化。
