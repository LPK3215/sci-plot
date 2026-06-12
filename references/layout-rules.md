# Page Composition & Role Definitions / 页面构图与角色定义

These are not fixed templates, but composition roles to use when writing prompts. Choose a page role first, then write the prompt.

这些不是固定模板，而是写提示词时的构图角色。先选页面角色，再写提示词。

---

## Page Role Definitions / 页面角色定义

| Role / 角色 | Purpose / 用途 | Composition / 构图 | In-Image Text Volume / 图片内文字量 |
|------|------|------|------------|
| `cover` | Cover page — convey theme and tone at a glance / 封面，一眼说明主题和气质 | Large title + visual anchor + minimal meta info / 大标题 + 视觉锚点 + 少量元信息 | Title: 1 line / 标题 1 行 |
| `method-overview` | Method overview / 方法总览 | Input → Core modules → Output / 输入 → 核心模块 → 输出 | 5-9 short labels / 5-9 个短标签 |
| `mechanism-detail` | Single core mechanism breakdown / 单个核心机制拆解 | Local zoom-in, numbered steps, short labels / 局部放大、编号步骤、短标签 | 6-12 short labels / 6-12 个短标签 |
| `comparison` | New vs. old method/approach comparison / 新旧方法/方案对比 | Left-right comparison, highlighted differences / 左右对照、差异高亮 | 4-8 short labels / 4-8 个短标签 |
| `evidence` | Experimental or data evidence / 实验或数据证据 | Large number + small chart + explanatory labels / 大数字 + 小图表 + 解释标签 | 1 large number + 2-4 short explanations / 1 个大数字 + 2-4 个短解释 |
| `architecture` | System/module architecture diagram / 系统/模块架构图 | Layered/grouped, dependency arrows / 分层/分组、依赖箭头 | 4-8 module labels / 4-8 个模块标签 |
| `data-flow` | Data flow/pipeline diagram / 数据流/管道图 | Data source→process→store→consume / 数据源→处理→存储→消费 | 4-8 node labels / 4-8 个节点标签 |
| `takeaway` | Conclusion and key points / 结论和要点 | 1 conclusion sentence + 3 key points / 1 句结论 + 3 个要点 | 1 main sentence + 3 short points / 1 主句 + 3 短点 |

---

## Recommended Pacing / 推荐节奏

### 4-6 Page Recommended Structure / 4-6 页推荐结构
```
cover → method-overview → mechanism-detail → comparison/evidence → takeaway
```

### 6-10 Page Recommended Structure / 6-10 页推荐结构
```
cover → method-overview → mechanism-detail (×2-3) → evidence → comparison → takeaway
```

---

## Composition Rules / 构图规则

### Cover / 封面
- Minimal text, strong main visual / 文字少，主视觉强
- Title centered or upper-aligned / 标题居中或偏上
- Visual anchor (abstract/figurative element related to the paper's core concept) / 视觉锚点（与论文核心概念相关的抽象/具象图）

### Method Overview / 方法总览
- Central main diagram must occupy 65%-80% of the page / 中间主图必须占 65%-80% 画面
- Input on left/top, output on right/bottom / 输入在左/上，输出在右/下
- Core modules in center, connection lines clear / 核心模块在中间，连接线清晰
- Key innovation points marked with emphasis color/bold lines / 关键创新点用强调色/粗线标记

### Mechanism Detail / 机制细节
- Only one mechanism per page / 每页只拆一个机制
- Zoom in on key areas locally / 局部放大关键区域
- Step-by-step unfolding (numbered ① ② ③) / 逐步展开（编号 ① ② ③）
- Supplement with dimension info and formula snippets / 补充维度信息、公式短注

### Comparison / 对比
- Left-right structure must be symmetric / 左右结构必须对称
- Differences must stand out (different colors / dashed box marking diff areas) / 差异点要显眼（不同颜色/虚线框标记差异区域）
- Title above, conclusion below / 上方标题，下方结论

### Evidence / 证据/数据
- Numbers must be large (visual focus) / 数字要大（视觉重点）
- Explanations must be short (no long paragraphs) / 解释要短（不写长段文字）
- Can use simplified small charts as aids / 可以用简化的小图表辅助

### Takeaway / 结论
- Do NOT introduce new concepts / 不要再引入新概念
- Return to the question posed on the cover page to close the loop / 回到封面提出的问题形成闭环

---

## Whitespace Control / 留白控制

- Cover and section divider pages can have more whitespace (30%-40%) for breathing room / 封面和章节分隔页可以有较多留白（30%-40%），营造呼吸感
- Method overview main diagram should occupy 65%-80% / 方法总览页主图应占 65%-80%
- Mechanism detail main diagram should occupy 75%-85% / 机制细节页主图应占 75%-85%
- Do NOT allow large meaningless blank areas (looking unfinished) / 不允许大面积无意义空白（看起来像没做完）
- Whitespace serves visual hierarchy, not laziness / 留白服务于视觉层级，不是偷懒

---

## Text Density Recommendations / 文字密度建议

| Page Type / 页面类型 | Text Volume / 文字量 | Specific Limit / 具体限制 |
|---------|--------|---------|
| cover | Minimal / 极少 | Title 1 line ≤16 Chinese chars, subtitle 1 line / 标题 1 行 ≤16 汉字，副标题 1 行 |
| method-overview | Medium / 中 | 5-9 short labels, each ≤8 Chinese chars / 5-9 个短标签，每个 ≤8 汉字 |
| mechanism-detail | Medium-high / 中高 | 6-12 short labels, each ≤8 Chinese chars / 6-12 个短标签，每个 ≤8 汉字 |
| comparison | Medium / 中 | 3-5 labels per side / 左右各 3-5 个标签 |
| evidence | Low / 少 | 1 large number + 2-4 short explanations / 1 个大数字 + 2-4 个短解释 |
| architecture | Medium / 中 | 4-8 module labels / 4-8 个模块标签 |
| takeaway | Low / 少 | 1 conclusion sentence + 3 short points / 1 句结论 + 3 个短点 |

If text exceeds limits, prioritize splitting pages rather than forcing the image model to render long paragraphs. / 如果文字超过限制，优先拆页，不要强行让生图模型写长段落。
