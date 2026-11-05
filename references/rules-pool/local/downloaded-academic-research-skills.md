# ACADEMIC-RESEARCH-SKILLS — 智能自适应下载绘图规范 (Downloaded Rule)

> **官方来源仓库**: https://github.com/Imbad0202/academic-research-skills  
> **雷达自动嗅探路径**: `academic-paper/references/statistical_visualization_standards.md` (源文件大小: 24235 字节)  
> **抓取机制**: 通用仓库递归雷达扫描与自适应定位 (Universal Radar Discovery)  
> **状态**: 本地已固化（永久离线可用，支持二次编辑）

---

## 1. 风格定位与视觉特征
- **来源项目**: Imbad0202/academic-research-skills
- **发现核心组件**: 自动嗅探自 `academic-paper/references/statistical_visualization_standards.md`，专精于科研图表与学术流程图的规范化构建。

---

## 2. 画布与排版约束
- **背景**: 纯白 (#FFFFFF) 或 浅冷灰 (#F8FAFC)
- **排版比例**: 2:3 (方法机制图) / 16:9 (全景流程图)
- **线框规范**: 核心流加粗 1.5-2px，辅助线 0.75-1px，结构连接一律正交走线，箭头清晰。

---

## 3. 色彩限制 (≤3色)
- **主结构线框**: 深色墨水墨线 (#1A1A1A / #334155)
- **唯一强调色**: 依据领域选取 1 种强调色（如科技蓝 #0284C7 或 #2563EB）高亮核心创新点
- **背景填充**: 浅灰/纯白底色，严禁杂乱渐变

---

## 4. 专属领域词典 (Domain Vocabulary)
- `Source Context`: Discovered from `academic-paper/references/statistical_visualization_standards.md`
- `Key Concepts`: Extracted from authentic repository guidelines

---

## 5. 核心英文提示词片段 (Prompt Snippet)
```text
Scientific vector schematic in academic-research-skills style, pure white background, flat 2D layout. Precise line weights, restrained theme accent, clean sans-serif typography, crisp directional connectors, no 3D effects, no drop shadows, no glossy textures.
```

---

## 附录：嗅探到的原始规范节选 (Source Excerpt)
```markdown
# Statistical Visualization Standards

Reference guide for the `visualization_agent`. Covers APA 7.0 figure guidelines, accessible color palettes, chart type selection, common pitfalls, and code templates.

---

## APA 7.0 Figure Guidelines (Chapter 7 Summary)

### General Principles

1. **Every figure must add value** — do not visualize data that is better expressed in a sentence or table
2. **Figures are numbered sequentially** (Figure 1, Figure 2, ...) in order of first mention
3. **Every figure must be cited in text** ("As shown in Figure 1, ...")
4. **Captions appear below the figure** (unlike table notes which appear above)
5. **Figures must be interpretable without reading the text** — include all necessary context in the caption

### Caption Format

```
Figure [N]                          ← Bold, on its own line
[Descriptive Title]                 ← Italic, sentence case, next line
Note. [Explanation if needed]       ← Plain text, starts with "Note."
```

### Typography Specifications

| Element | Size | Style |
|---------|------|-------|
| Figure label ("Figure 1") | 10-12 pt | Bold |
| Figure title | 10-12 pt | Italic |
| Axis labels | 8-10 pt | Plain, sentence case |
| Axis tick labels | 8-9 pt | Plain |
| Legend text | 8-9 pt | Plain |
| Annotations | 8 pt | Plain or italic |
| Note text | 8-9 pt | Plain |

### Required Elements

- [ ] Axis labels (both axes, descriptive, with units)
- [ ] Tick marks and tick labels
- [ ] Legend (for multi-group figures)
- [ ] Error bars or confidence intervals (for mean comparisons)
- [ ] Scale bars (for images/maps)
- [ ] Caption with Figure number + title
- [ ] Note (if explanation is needed)

---

## Accessible Color Palettes

### Primary: Viridis (Perceptually Uniform)

Best for: continuous/sequential data.

| Index | Hex Code | Usage |
|-------|----------|-------|
| 0 | `#440154` | Darkest value |
| 1 | `#46327E` | |
| 2 | `#365C8D` | |
| 3 | `#277F8E` | |
| 4 | `#1FA187` | |
| 5 | `#4AC16D` | |
| 6 | `#9FDA3A` | |
| 7 | `#FDE725` | Lightest value |

### Alternative: Cividis (Deuteranopia/Protanopia Optimized)

Best for: publications where colorblind accessibility is critical.

| Index | Hex Code |
|-------|----------|
| 0 | `#00204D` |
| 1 | `#00336F` |
| 2 | `#39486B` |
| 3 | `#5F5D6A` |
| 4 | `#7B7463` |
| 5 | `#9A8C4F` |
| 6 | `#BBA634` |
| 7 | `#DEC000` |
| 8 | `#FFE945` |

### Categorical: Tol's Qualitative Palette (Max 8 Categories)

Best for: categorical comparisons, group labels.

| Label | Hex Code | Sample Use |
|-------|----------|------------|
| Blue | `#0077BB` | Group 1 / Baseline |
| Cyan | `#33BBEE` | Group 2 |
| Teal | `#009988` | Group 3 |
| Orange | `#EE7733` | Group 4 / Highlight |
| Red | `#CC3311` | Group 5 / Alert |
| Magenta | `#EE3377` | Group 6 |
| Grey | `#BBBBBB` | Reference / NA |
| Black | `#000000` | Outline / Text |

### Diverging: Blue-Red (For Correlation/Difference Maps)

| Negative | Zero | Positive |
|----------|------|----------|
| `#2166AC` | `#F7F7F7` | `#B2182B` |
| `#4393C3` | | `#D6604D` |
| `#92C5DE` | | `#F4A582` |

### Accessibility Rules

1. Never rely on color alone — pair with shape, pattern, or label
2. Minimum contrast ratio: 3:1 (WCAG AA for non-text elements)
3. Test with a colorblindness simulator before finalizing
4. When printing in grayscale, patterns or labels must still distinguish groups

---

## Chart Type Decision Tree

### Which Chart for Which Data?

| Your Data | Your Question | Recommended Chart | Avoid |
|-----------|--------------|-------------------|-------|
| Categories + values | Compare magnitudes | **Bar chart** (vertical or horizontal) | Pie chart |
```
