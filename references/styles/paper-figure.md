# paper-figure — 论文框架图风

像一张重新设计过的顶会论文 Figure：专业、清楚、信息密度高，适合传播。

## 氛围
- 像 NeurIPS / ICLR / Nature / Science 论文中的方法总览图
- 不是蓝图、不是海报、不是漫画
- 目标：让读者在 30 秒内理解论文核心方法

## 视觉规范

### 画布
- 白底或极浅灰底（#FFFFFF / #F8F9FA）
- 竖版 2:3 用于机制拆解
- 横版 16:9 或 4:3 用于 README 首屏/总览

### 图元
- 干净的矢量感模块：圆角矩形、矩阵小格、token 序列、分组框、编号步骤
- 箭头精确、方向明确，主路径比辅助路径更粗（2-3px vs 1px）
- 允许使用小型热力图、曲线、结果缩略图、模块堆叠、对比路径

### 文字
- 无衬线字体，像论文图中的短标签
- 标注必须短：模块名、变量名、关键操作、≤1 行解释
- 专业术语保留英文

### 色彩
- 黑/深灰为主（#1A1A1A / #333333 / #6B7280）
- 只使用 1-2 个强调色：蓝（#2563EB）、橙（#D97706）、青（#0891B2）、紫（#7C3AED）中选 1-2 种
- 强调色用于核心贡献、关键路径或对比，不做装饰

## 生成原则
- 以参考论文原始框架图的概念，但必须重新组织信息，不能复刻原图
- 概述图覆盖输入、核心模块、输出和关键贡献
- 细节图只拆一个机制，不把所有东西塞进一页
- 结果图只放最有说服力的一条结果

## English Prompt Snippet
```
Scientific paper figure style, clean white or light gray background, precise vector-style rounded modules with clear directional arrows, black/dark gray as primary color, one accent color (blue or orange) for key innovations, compact sans-serif labels, publication-quality method diagram, no 3D, no decoration, no engineering blueprint style, no large text blocks
```
