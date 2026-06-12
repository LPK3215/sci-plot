# Changelog / 更新日志

All notable changes to sci-plot will be documented in this file. / 所有重要变更均记录于此。

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), / 格式基于 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)，
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). / 本项目遵循 [语义化版本](https://semver.org/spec/v2.0.0.html)。

## [Unreleased]

### Added / 新增
- Added `sci-plot-output/` to `.gitignore` to exclude generated output from version control. / 将 `sci-plot-output/` 加入 `.gitignore`，从版本控制中排除生成输出。
- Added workflow architecture diagram (`docs/architecture.svg`) with generation script (`docs/scripts/generate_architecture.py`). / 新增工作流架构图（`docs/architecture.svg`）及生成脚本（`docs/scripts/generate_architecture.py`）。
- Added badges (License, Version, CodeBuddy Skill) to README.md. / 在 README.md 中添加徽章（许可证、版本、CodeBuddy Skill）。
- Added project structure tree, FAQ section, and author information to README.md. / 在 README.md 中添加项目结构树、FAQ 章节和作者信息。
- Added visual architecture diagram section to README.md. / 在 README.md 中添加可视化架构图章节。
- Added interactive project overview page (`project_overview.html` + `project_overview/`) with dark theme, animated workflow timeline, style previews, and SVG architecture diagram integration. / 新增交互式项目全景观览页（`project_overview.html` + `project_overview/`），支持深色主题、动画工作流时间线、风格预览和 SVG 架构图集成。
- Updated architecture SVG to include project overview section and layout-rules.md reference. / 更新架构 SVG，新增项目全景观览区和 layout-rules.md 引用。
- Updated README project structure tree to include `project_overview/` directory. / 更新 README 项目结构树，新增 `project_overview/` 目录。

### Changed / 变更
- All documentation files converted to bilingual format (English primary, Chinese secondary). / 所有文档文件改为双语格式（英文为主，中文为辅）。

## [1.0.0] - 2026-06-13

### Added / 新增
- Initial release of sci-plot, the scientific figure prompt engine. / sci-plot 科研绘图引擎首次发布。
- `SKILL.md`: Complete 6-round mandatory workflow (Round 0-5) for analyzing research content and generating image prompts. / 完整的 6 轮强制工作流（Round 0-5），用于分析研究内容并生成生图提示词。
- `references/prompt-rules.md`: Core rules for composition, annotation, color, and forbidden patterns. / 构图、标注、色彩及禁止模式的核心规则。
- `references/analysis-guide.md`: Detailed checklists for analyzing papers, projects, code, and algorithms. / 论文、项目、代码、算法分析的详细清单。
- `references/layout-rules.md`: Page role definitions, recommended pacing, and composition rules. / 页面角色定义、推荐节奏和构图规则。
- `references/styles/paper-figure.md`: Paper figure style specification. / 论文框架图风规范。
- `references/styles/sketchnote.md`: Warm sketchnote style specification. / 温暖科研笔记风规范。
- `references/styles/journal-minimal.md`: Nature/IEEE minimal academic style specification. / Nature/IEEE 极简学术风规范。
- `references/styles/warm-notes.md`: Bright handwritten notes style specification. / 明亮手记风规范。
- `references/styles/business-research.md`: Business research brief style specification. / 商业研究简报风规范。
- `README.md`: User-facing documentation with installation, usage, styles, and output structure. / 面向用户的说明文档，包含安装、使用、风格和产出结构。
- `LICENSE`: MIT License. / MIT 许可证。
- `.gitignore`: Version control exclusions for Windows, macOS, IDE, and Python files. / Windows、macOS、IDE 和 Python 文件的版本控制排除。
- `CONTRIBUTING.md`: Contribution guidelines. / 贡献指南。
- `.gitattributes`: Line ending normalization. / 行尾规范化。
