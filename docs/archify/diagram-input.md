# diagram-input — Sci-Plot 科学绘图提示词引擎

对象与口径：工作根 `d:\Develop\SourceCode\skills\myskills\sci-plot`，材料类型 = AI Agent Skill + 科学论文插图提示词编译引擎。本蓝图专用于生成与本项目真实代码、规范和运行机制 100% 对应的架构与流向图。

## 1. 组件清单

```
USER｜学术研究员/开发者｜输入论文材料 (PDF/TeX/MD) 与出图风格诉求（类型：外部）
SKILL｜Sci-Plot 编排中枢（SKILL.md）｜五轮确定性流水线主控、调度与任务编排（类型：前端）
INGEST｜文献摄取与范围隔离｜严格执行 ≤10页 / ≤15k token 约束，过滤非核心附录与参考文献（类型：后端）
RULES｜双轨规则池（rules-pool）｜核心内建规则 + 外部社区雷达动态摄取的学术制图规范（类型：存储）
STYLES｜5 大视觉风格预设｜paper-figure、journal-minimal、sketchnote、warm-notes、business-research（类型：存储）
PLANNER｜结构化图表规划器｜拆分子图、排定视觉层次、流向轴线与色彩矩阵（figure-plan.md）（类型：后端）
SYNTH｜多平台提示词编译器｜编译各平台原生方言（Midjourney、Doubao、SD、Matplotlib）（类型：后端）
HARVEST｜全网规则采集与雷达｜universal_skill_harvester.py 自动扫描与同步社区优质规范（类型：后端）
QA_GATE｜4 阶自动化质检验收｜tests/run_all_tests.py 执行 6 套端到端合规校验（类型：后端）
RENDER_AI｜生图大模型平台｜Midjourney v6.1、DALL-E 3、豆包等云端生图端（类型：外部）
RENDER_CODE｜本地代码与矢量渲染｜Python Matplotlib、Seaborn 及静态 HTML 学术渲染器（类型：后端）
OUTPUT｜最终验收资产目录｜sci-plot-output/（prompts、analysis.md、figure-plan.md）（类型：存储）
```

## 2. 关系清单

```
USER → SKILL：提供学术论文材料与出图风格需求（实线，主路径）
SKILL → INGEST：触发第 1 轮摄取，施加硬性截断与范围隔离（实线，主路径）
INGEST → PLANNER：输出结构化核心论点与实体场景图（实线，主路径）
PLANNER → RULES：检索匹配领域制图标准与布局规范（实线）
PLANNER → STYLES：提取指定风格调色板、字阶与视觉语法（实线）
HARVEST → RULES：动态扫描并同步外部前沿制图规则入池（虚线，后台异步）
PLANNER → SYNTH：输出 figure-plan.md 喂给第 4 轮方言编译（实线，主路径）
SYNTH → QA_GATE：生成原始提示词与代码，进入第 5 轮门禁（实线，主路径）
QA_GATE → OUTPUT：校验全绿后落盘交付物与复现指南（实线，主路径终点）
OUTPUT → RENDER_AI：用户复制提示词投喂云端平台生成概念图（虚线，分发）
OUTPUT → RENDER_CODE：用户执行 Python 脚本直接输出精确矢量图（虚线，分发）
QA_GATE → SKILL：质检若未通过则反馈调整（虚线，反向闭环）
```

## 3. 边界划分

```
[边界 1 · 输入与外部交互] USER, RENDER_AI
[边界 2 · 核心调度与隔离] SKILL, INGEST, QA_GATE
[边界 3 · 规则与知识中枢] RULES, STYLES, HARVEST
[边界 4 · 编译规划与输出] PLANNER, SYNTH, RENDER_CODE, OUTPUT
```

## 4. 关键路径

```
USER → SKILL → INGEST → PLANNER → SYNTH → QA_GATE → OUTPUT
```

## 5. 明确排除项

```
- 排除历史已废弃的根目录分散脚本
- 排除临时测试产物与 __pycache__
- 排除第三方无关开发环境配置
```

## 6. 待确认清单

```
无
```

