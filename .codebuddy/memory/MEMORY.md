# Sci-Plot 项目记忆

## 项目定位
- sci-plot 是 CodeBuddy Skill，定位为科研绘图提示词引擎
- 核心 slogan：科研绘图 — 从论文到插图的一站式引擎
- 不直接生图，只产出跨平台可用的结构化提示词文件
- 支持 ChatGPT/DALL-E、豆包、Qwen、Midjourney、Stable Diffusion 等

## 文档规范
- 用户面向文档（README/CHANGELOG/CONTRIBUTING）拆分为独立 EN/CN 双份文件
- AI 面向文档（SKILL.md + references/*.md）保持纯英文，提升 AI 理解能力
- 架构图资源：英文文档用 architecture.svg，中文文档用 architecture_cn.svg

## 项目观览页
- project_overview.html 为入口文件，project_overview/ 目录存放 CSS 和 JS
- 架构图区域使用纯 HTML/CSS 实现（不依赖 SVG）
- 深色主题 + 毛玻璃 + 渐变 + 动效

## 关键文件
- SKILL.md：6 轮强制工作流（Round 0-5）
- references/prompt-rules.md：提示词生成核心规则
- references/analysis-guide.md：四类分析清单（论文/代码/算法/文档）
- references/layout-rules.md：页面构图与角色定义
- references/styles/：5 种视觉风格规范
