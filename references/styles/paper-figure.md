# paper-figure — Paper Figure Style / 论文框架图风

Like a redesigned top-conference paper figure: professional, clear, information-dense, suitable for sharing. / 像一张重新设计过的顶会论文 Figure：专业、清楚、信息密度高，适合传播。

## Atmosphere / 氛围
- Like a method overview figure from NeurIPS / ICLR / Nature / Science / 像 NeurIPS / ICLR / Nature / Science 论文中的方法总览图
- Not a blueprint, not a poster, not a comic / 不是蓝图、不是海报、不是漫画
- Goal: let readers understand the core method in 30 seconds / 目标：让读者在 30 秒内理解论文核心方法

## Visual Specification / 视觉规范

### Canvas / 画布
- White or very light gray background (#FFFFFF / #F8F9FA) / 白底或极浅灰底（#FFFFFF / #F8F9FA）
- Portrait 2:3 for mechanism breakdowns / 竖版 2:3 用于机制拆解
- Landscape 16:9 or 4:3 for README hero / overview / 横版 16:9 或 4:3 用于 README 首屏/总览

### Graphic Elements / 图元
- Clean vector-feel modules: rounded rectangles, small matrix grids, token sequences, group boxes, numbered steps / 干净的矢量感模块：圆角矩形、矩阵小格、token 序列、分组框、编号步骤
- Precise arrows with clear directionality, main path thicker than auxiliary paths (2-3px vs 1px) / 箭头精确、方向明确，主路径比辅助路径更粗（2-3px vs 1px）
- Allow small heatmaps, curves, result thumbnails, module stacks, comparison paths / 允许使用小型热力图、曲线、结果缩略图、模块堆叠、对比路径

### Text / 文字
- Sans-serif font, like short labels in paper figures / 无衬线字体，像论文图中的短标签
- Labels must be short: module names, variable names, key operations, ≤1 line explanation / 标注必须短：模块名、变量名、关键操作、≤1 行解释
- Professional terms retain English / 专业术语保留英文

### Color / 色彩
- Black/dark gray as primary (#1A1A1A / #333333 / #6B7280) / 黑/深灰为主（#1A1A1A / #333333 / #6B7280）
- Only 1-2 accent colors: choose from blue (#2563EB), orange (#D97706), teal (#0891B2), purple (#7C3AED) / 只使用 1-2 个强调色：蓝（#2563EB）、橙（#D97706）、青（#0891B2）、紫（#7C3AED）中选 1-2 种
- Accent colors used for core contributions, key paths, or comparisons — never for decoration / 强调色用于核心贡献、关键路径或对比，不做装饰

## Generation Principles / 生成原则
- Reference the concept of original paper framework diagrams, but must reorganize information — do not replicate the original / 以参考论文原始框架图的概念，但必须重新组织信息，不能复刻原图
- Overview diagrams cover input, core modules, output, and key contributions / 概述图覆盖输入、核心模块、输出和关键贡献
- Detail diagrams break down only one mechanism — do not cram everything into one page / 细节图只拆一个机制，不把所有东西塞进一页
- Result diagrams show only the most convincing single result / 结果图只放最有说服力的一条结果

## English Prompt Snippet / 英文提示词片段
```
Scientific paper figure style, clean white or light gray background, precise vector-style rounded modules with clear directional arrows, black/dark gray as primary color, one accent color (blue or orange) for key innovations, compact sans-serif labels, publication-quality method diagram, no 3D, no decoration, no engineering blueprint style, no large text blocks
```
