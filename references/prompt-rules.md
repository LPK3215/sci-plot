# Scientific Figure Prompt Generation Core Rules

Extracted from paper-craft-skills and adapted as a universal cross-platform prompt specification.

---

## Image Specifications

- Portrait 2:3 aspect ratio (default for method diagrams)
- Landscape 16:9 or 4:3 (slides/presentation scenarios)
- All annotation text must be clearly readable
- High resolution output

---

## Composition Principles

### Information Hierarchy
1. **Title Area**: Top of page, briefly states the page topic (e.g., "Method Overview", "Core Mechanism: Attention Computation")
2. **Main Body**: Visual diagram occupies 75%-85% of page area
3. **Annotation Area**: Brief explanatory text beside key nodes, concise and precise

### Visual Flow
- Clear directionality (left→right, or top→bottom, or center outward diffusion)
- Use arrows, lines, numbered steps to guide reading order
- Do NOT allow chaotic layouts where the viewer doesn't know where to look

### Emphasis
- Mark core innovations with **emphasis color** (bold borders / fill color / highlighted area)
- Non-critical auxiliary information uses lighter tones, not competing for attention

### Information Density
- Mechanism diagrams must not just draw large titles and a few isolated modules; must include sufficient internal steps, local zoom-ins, or small examples
- When blank space exceeds 25%, prioritize adding: key formula short annotations, input/output dimensions, small matrix grids, token examples, before/after comparisons, attention heatmaps
- If one page cannot fit, split into multiple pages — do not sacrifice readability
- Cover pages allow more conceptual treatment; detail pages must prioritize explaining "how"

---

## Text Annotation Standards

### Annotation Content
- Label each box/node with its name (e.g., "Embedding", "Self-Attention", "FFN")
- Key data dimensions (e.g., "d=512", "n=12 heads")
- Important mathematical relationships in short text (e.g., "Q×K^T", "÷√dk"), not full LaTeX formulas
- Chinese pages: titles ≤16 Chinese characters, labels ≤8 Chinese characters

### Annotation Position
- Close to the object being annotated
- Do not obscure key visual elements
- Multiple annotations must not overlap

### Annotation Language
- Professional terms retain English (e.g., "Transformer", "Attention", "Embedding")
- Explanatory text uses the selected output language
- Annotation text must be concise — use 3 characters when possible, not 10

---

## Color Usage

### Limitation Principle
- Primary color + emphasis color, no more than 3 colors total
- No gradients, no oversaturated colors
- Color serves differentiation, not decoration

### Color Semantics
- Dark/thick lines = core path / key structure
- Light/thin lines = auxiliary information / context
- Emphasis color = the one point this page wants you to remember

### Style-Specific Emphasis Color Reference
| Style | Emphasis Color |
|------|-------|
| paper-figure | Blue (#2563EB) / Orange (#D97706), choose 1-2 |
| sketchnote | Deep blue (#2C5F8A) / Coral red (#D85C4A) / Olive green (#5C6B4F) / Soft yellow (#F3D36B) |
| journal-minimal | Nature blue / IEEE blue / Cool gray |
| warm-notes | Soft blue / Coral / Olive / Yellow |
| business-research | Charcoal gray + navy/emerald/gold single emphasis |

---

## Per-Page Must-Have

- [ ] Title at top of page
- [ ] Clear core visual element occupying the main body (flowchart / structure diagram / comparison)
- [ ] Text annotations on key nodes
- [ ] Directional guidance (arrows / numbers / lines)
- [ ] A single core emphasis point on this page (highlighted with color/size)
- [ ] Mechanism detail pages: at least one local zoom-in, small example, dimension annotation, or key formula snippet

---

## Per-Page Forbidden

- [ ] Do NOT include any code blocks
- [ ] Do NOT use photorealistic rendering
- [ ] Do NOT use 3D effects
- [ ] Text annotations must NOT form continuous paragraphs (each annotation is independent and short)
- [ ] Do NOT draw "decorative" elements (patterns, flourishes unrelated to content)
- [ ] Do NOT leave large blank areas
- [ ] Do NOT use blue background with white lines (engineering blueprint style)
- [ ] Do NOT copy the layout of original paper figures (reorganize the information)
- [ ] Do NOT make it look like a PPT cover or marketing poster
- [ ] Do NOT include fake logos, fake UI, garbled labels, or fake brand names
- [ ] Do NOT use cyberpunk neon, cheap 3D, or plastic textures
- [ ] sketchnote must NOT look like old parchment, yellowed archives, or vintage diary

---

## Structured Prompt Format

Generate each page's prompt using the format below, saved to `prompts/NN-{slug}.md`.

**File structure explanation**: The metadata, composition description, and content elements sections are for human reference. **The English Prompt is the core output — copy it directly into any image generation tool.**

```markdown
# Page N: {Page Title}

## Metadata
- **Type**: {flow breakdown / architecture overview / mechanism detail / comparison / data chart}
- **Style**: {paper-figure / sketchnote / journal-minimal / warm-notes / business-research}
- **Language**: {zh / en / bilingual}
- **Aspect Ratio**: {2:3 / 16:9 / 4:3}

## Composition Description
{Describe the spatial layout in natural language: left/right/top/bottom/center arrangement, arrow directions, module position relationships}

## Content Elements
{List the specific modules, relationships, and annotations to draw}

---

## ▶ English Prompt (Core — Copy Directly)
{Complete English prompt, ready to copy into any image generation tool}

---

## Copy to Image Generation Tool
Copy the "English Prompt" section above in full to the input box of the following tools:
- **ChatGPT (DALL-E)**: Paste directly
- **Doubao**: Text-to-image entry
- **Qwen (Tongyi Wanxiang)**: Text-to-image entry
- **Midjourney**: Paste after `/imagine`
```
