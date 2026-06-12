# Scientific Figure Prompt Generation Core Rules / 科研绘图提示词生成核心规则

Extracted from paper-craft-skills and adapted as a universal cross-platform prompt specification. / 从 paper-craft-skills 提取并适配为通用跨平台提示词规范。

---

## Image Specifications / 图片规格

- Portrait 2:3 aspect ratio (default for method diagrams) / 竖版 2:3 比例（方法图解默认）
- Landscape 16:9 or 4:3 (slides/presentation scenarios) / 横版 16:9 或 4:3（幻灯片/演示场景）
- All annotation text must be clearly readable / 所有标注文字清晰可读
- High resolution output / 高清出图

---

## Composition Principles / 构图原则

### Information Hierarchy / 信息层次
1. **Title Area / 标题区**: Top of page, briefly states the page topic (e.g., "Method Overview", "Core Mechanism: Attention Computation") / 页面顶部，简短说明本页主题（如"方法总览""核心机制：注意力计算"）
2. **Main Body / 主体区**: Visual diagram occupies 75%-85% of page area / 视觉图解占页面 75%-85% 面积
3. **Annotation Area / 标注区**: Brief explanatory text beside key nodes, concise and precise / 关键节点旁的文字解释，简洁精确

### Visual Flow / 视觉流向
- Clear directionality (left→right, or top→bottom, or center outward diffusion) / 明确的方向性（左→右，或上→下，或中心向外扩散）
- Use arrows, lines, numbered steps to guide reading order / 用箭头、线条、数字序号引导阅读顺序
- Do NOT allow chaotic layouts where the viewer doesn't know where to look / 不允许出现"不知道该看哪"的混乱布局

### Emphasis / 重点强调
- Mark core innovations with **emphasis color** (bold borders / fill color / highlighted area) / 核心创新点用**强调色**标记（边框加粗/填充色/高亮区域）
- Non-critical auxiliary information uses lighter tones, not competing for attention / 非关键辅助信息用浅色处理，不抢焦点

### Information Density / 信息密度
- Mechanism diagrams must not just draw large titles and a few isolated modules; must include sufficient internal steps, local zoom-ins, or small examples / 机制图不能只画大标题和几个孤立模块；必须包含足够的内部步骤、局部放大或小例子
- When blank space exceeds 25%, prioritize adding: key formula short annotations, input/output dimensions, small matrix grids, token examples, before/after comparisons, attention heatmaps / 画面空白超过 25% 时，优先补充：关键公式短标注、输入/输出维度、矩阵小格、token 示例、before/after 对比、注意力热力图
- If one page cannot fit, split into multiple pages — do not sacrifice readability / 一页无法容纳则拆成多页，不牺牲可读性
- Cover pages allow more conceptual treatment; detail pages must prioritize explaining "how" / 封面图允许更概念化；细节图必须优先解释"怎么做"

---

## Text Annotation Standards / 文字标注规范

### Annotation Content / 标注内容
- Label each box/node with its name (e.g., "Embedding", "Self-Attention", "FFN") / 每个方框/节点旁标注名称（如"Embedding""Self-Attention""FFN"）
- Key data dimensions (e.g., "d=512", "n=12 heads") / 关键数据维度（如"d=512""n=12 heads"）
- Important mathematical relationships in short text (e.g., "Q×K^T", "÷√dk"), not full LaTeX formulas / 重要的数学关系用简短文字（如"Q×K^T""÷√dk"），不用完整 LaTeX 公式
- Chinese pages: titles ≤16 Chinese characters, labels ≤8 Chinese characters / 中文页：标题 ≤16 个汉字，标签 ≤8 个汉字

### Annotation Position / 标注位置
- Close to the object being annotated / 紧贴所标注的对象
- Do not obscure key visual elements / 不遮挡关键视觉元素
- Multiple annotations must not overlap / 多个标注不重叠

### Annotation Language / 标注语言
- Professional terms retain English (e.g., "Transformer", "Attention", "Embedding") / 专业术语保留英文（如"Transformer""Attention""Embedding"）
- Explanatory text uses Chinese / 解释性文字用中文
- Annotation text must be concise — use 3 characters when possible, not 10 / 标注文字精简——能用 3 个字不用 10 个字

---

## Color Usage / 颜色使用

### Limitation Principle / 限制原则
- Primary color + emphasis color, no more than 3 colors total / 主色 + 强调色，不超过 3 种颜色
- No gradients, no oversaturated colors / 不用渐变色、不用过饱和色
- Color serves differentiation, not decoration / 颜色用于区分，不用于装饰

### Color Semantics / 颜色含义
- Dark/thick lines = core path / key structure / 深色/粗线 = 核心路径/关键结构
- Light/thin lines = auxiliary information / context / 浅色/细线 = 辅助信息/上下文
- Emphasis color = the one point this page wants you to remember / 强调色 = 本页要让人记住的那一个点

### Style-Specific Emphasis Color Reference / 各风格强调色参考
| Style / 风格 | Emphasis Color / 强调色 |
|------|-------|
| paper-figure | Blue (#2563EB) / Orange (#D97706), choose 1-2 / 蓝（#2563EB）/ 橙（#D97706）选 1-2 种 |
| sketchnote | Deep blue (#2C5F8A) / Coral red (#D85C4A) / Olive green (#5C6B4F) / Soft yellow (#F3D36B) / 深蓝（#2C5F8A）/ 珊瑚红（#D85C4A）/ 橄榄绿（#5C6B4F）/ 柔和黄（#F3D36B） |
| journal-minimal | Nature blue / IEEE blue / Cool gray / Nature 蓝 / IEEE 蓝 / 冷灰 |
| warm-notes | Soft blue / Coral / Olive / Yellow / 软蓝 / 珊瑚 / 橄榄 / 黄色 |
| business-research | Charcoal gray + navy/emerald/gold single emphasis / 炭灰色 + 藏蓝/墨绿/金色单强调 |

---

## Per-Page Must-Have / 每页必含

- [ ] Title at top of page / 页面顶部标题
- [ ] Clear core visual element occupying the main body (flowchart / structure diagram / comparison) / 清晰且占画面主体的核心视觉元素（流程图/结构图/对比图）
- [ ] Text annotations on key nodes / 关键节点的文字标注
- [ ] Directional guidance (arrows / numbers / lines) / 方向性引导（箭头/数字/线条）
- [ ] A single core emphasis point on this page (highlighted with color/size) / 本页唯一的核心强调点（用颜色/大小突出）
- [ ] Mechanism detail pages: at least one local zoom-in, small example, dimension annotation, or key formula snippet / 机制细节页：至少包含一个局部放大、小例子、维度说明或关键公式短标注

---

## Per-Page Forbidden / 每页禁止

- [ ] Do NOT include any code blocks / 不要出现任何代码块
- [ ] Do NOT use photorealistic rendering / 不要照片级写实渲染
- [ ] Do NOT use 3D effects / 不要 3D 立体效果
- [ ] Text annotations must NOT form continuous paragraphs (each annotation is independent and short) / 文字标注不要连成一段话（每个标注独立、简短）
- [ ] Do NOT draw "decorative" elements (patterns, flourishes unrelated to content) / 不要画"装饰性"元素（和内容无关的图案、花纹）
- [ ] Do NOT leave large blank areas / 不要大面积空白
- [ ] Do NOT use blue background with white lines (engineering blueprint style) / 不要蓝底白线工程图纸风
- [ ] Do NOT copy the layout of original paper figures (reorganize the information) / 不要复制原论文图的布局（要重新组织信息）
- [ ] Do NOT make it look like a PPT cover or marketing poster / 不要做成 PPT 封面或营销海报
- [ ] Do NOT include fake logos, fake UI, garbled labels, or fake brand names / 不要出现假 logo、假 UI、乱码标签、假品牌名
- [ ] Do NOT use cyberpunk neon, cheap 3D, or plastic textures / 不要赛博朋克霓虹、廉价 3D、塑料质感
- [ ] sketchnote must NOT look like old parchment, yellowed archives, or vintage diary / sketchnote 不要画成旧羊皮纸、泛黄档案或复古日记

---

## Structured Prompt Format / 提示词结构化格式

Generate each page's prompt using the format below, saved to `prompts/NN-{slug}.md`. / 每页提示词用以下格式生成，保存在 `prompts/NN-{slug}.md`。

**File structure explanation / 文件结构说明**: Chinese description, composition description, and content elements are for human reference. **The English Prompt is the core output — copy it directly into any image generation tool.** / 中文说明、构图描述、内容元素是给人看的解释，**English Prompt 是核心产出，直接复制到生图工具即可出图**。

```markdown
# Page N: {Page Title} / 第 N 页：{页面标题}

## Chinese Description / 中文说明
- **Type / 类型**: {flow breakdown / architecture overview / mechanism detail / comparison / data chart / 流程分解图 / 架构总览 / 机制细节 / 对比图 / 数据图}
- **Style / 风格**: {paper-figure / sketchnote / journal-minimal / warm-notes / business-research}
- **Language / 语言**: {zh / en / bilingual}
- **Aspect Ratio / 比例**: {2:3 / 16:9 / 4:3}

## Composition Description / 构图描述
{Describe the spatial layout in natural language: left/right/top/bottom/center arrangement, arrow directions, module position relationships / 用自然语言描述画面布局：左/右/上/下/中的空间安排，箭头方向，模块位置关系}

## Content Elements / 内容元素
{List the specific modules, relationships, and annotations to draw / 列出要画的具体模块、关系、标注}

---

## ▶ English Prompt (Core — Copy Directly / 核心，直接复制)
{Complete English prompt, ready to copy into any image generation tool / 完整的英文提示词，可直接复制到生图工具}

---

## Copy to Image Generation Tool / 复制到生图工具
Copy the "English Prompt" section above in full to the input box of the following tools: / 将上方的 "English Prompt" 部分完整复制到以下工具的输入框：
- **ChatGPT (DALL-E)**: Paste directly / 直接粘贴
- **Doubao / 豆包**: Text-to-image entry / 文生图入口
- **Qwen (Tongyi Wanxiang) / 通义万相**: Text-to-image entry / 文生图入口
- **Midjourney**: Paste after `/imagine` / 在 `/imagine` 后粘贴
```
