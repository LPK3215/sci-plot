---
name: sci-plot
description: >
  Scientific figure prompt engine. Analyzes papers/projects/algorithms/code/documents,
  applies scientific figure conventions, and generates high-quality, cross-platform image
  generation prompts. Users copy prompts into ChatGPT/DALL-E, Doubao, Qwen, Midjourney,
  or any AI image tool to produce figures. Does not generate images directly — produces
  prompts only.
---

<div align="center">

# Sci-Plot — Scientific Figure Prompt Engine

Turn papers, projects, and algorithms into high-quality, cross-platform image generation prompts. You provide the content, sci-plot produces prompts, you paste them into any image generation tool.

---

## Core Positioning

**sci-plot does not generate images directly.** Its workflow chain is:

```
User Input (paper/project/code/doc) → Analysis → Confirmation (language/style/count) → Prompt File Generation → User copies to image generation tool
```

Prompts are cross-platform compatible (ChatGPT/DALL-E, Doubao, Qwen, Midjourney, Stable Diffusion, etc.).

---

## Mandatory Workflow &mdash; 6-Round Pipeline

</div>

### Round 0: Determine Analysis Target

<div align="center">

| Step | Action |
|:---:|---|
| 1 | If the user explicitly specifies a target (path/link/pasted content), use it directly |
| 2 | If not specified, auto-detect from the current workspace: prioritize `.tex` files (LaTeX papers), then `.md`, `.pdf`, `.py` |
| 3 | If the workspace has no analyzable content, prompt the user to provide a target |

</div>

### Round 1: Analyze Input Content

**Read `references/analysis-guide.md` first**, then execute the complete four-step analysis flow according to the four analysis checklists defined there (paper/code/algorithm/document).

Read the target content determined in Round 0, analyze comprehensively, covering the following dimensions:

<div align="center">

| Content Type | Analysis Points |
|:---:|---|
| **Paper** | Core innovations (1-3), method input→process→output flow, key experiments/results, architecture/module relationships |
| **Project Code** | Project structure, core modules, data flow, key algorithm functions, module dependencies |
| **Document** | Architecture design, API interfaces, data models, business processes |
| **Algorithm** | Input/output, core steps, key data structures, complexity, baseline comparison |

</div>

**Self-check**: Is the content fully understood? Can you explain the key concepts in your own words?

### Round 2: Extract Illustratable Content

Filter content from the analysis results that is **suitable for illustration**:

<div align="center">

| Priority | Description | Examples |
|:---:|---|---|
| **Must illustrate** (1-2 pages each) | Method overall flow/architecture, each core innovation mechanism, most compelling experimental results | input→modules→output, zoomed-in internal view, key data |
| **Optional** | Visual comparison with baselines, key data processing pipelines, system architecture/module relationship diagrams | baseline charts, pipeline flow, module diagrams |
| **Do NOT illustrate** | Related work/background, similar ablation experiments, abstract inspiration/concepts | text-only content |

</div>

### Round 3: Ask the User

**Read `references/layout-rules.md` first**, then organize the plan using the page roles defined there (cover / method-overview / mechanism-detail / comparison / evidence / architecture / data-flow / takeaway) and their recommended pacing.

Confirm the following 5 items. If the user does not reply, provide default recommendations:

<div align="center">

| # | Item | Options |
|:---:|---|---|
| 1 | **Language** | Chinese / English / Bilingual (default: Chinese) |
| 2 | **Visual Style** | See style table below |
| 3 | **Number of Figures** | Recommend based on content complexity, explaining what each figure covers |
| 4 | **Aspect Ratio** | 16:9 (landscape) / 4:3 (landscape) / 2:3 (portrait, default for method diagrams) |
| 5 | **Purpose** | Journal figure / Technical blog / README / Defense presentation / Science communication |

</div>

**Confirmation template:**

> After analysis, I recommend generating 5 figures:
> 1. Method overview (input→process→output full flow)
> 2. Core mechanism A breakdown (explain the most critical innovation)
> 3. Core mechanism B breakdown
> 4. Baseline comparison
> 5. Key results/data
>
> You could also generate just 1 overview, or expand to 8 figures.
> Please confirm: language (Chinese/English)? style (paper-figure/sketchnote)? count? aspect ratio? purpose?

### Round 4: Generate Prompts

**Read the following files first:**
1. `references/prompt-rules.md` — All rules and template formats
2. `references/styles/{selected style}.md` — Detailed specification for the selected style

Write a structured prompt for each page and save to `sci-plot-output/prompts/` directory.

**Must strictly use the template format defined at the end of `prompt-rules.md`:**
- Metadata (type, style, language, aspect ratio)
- Composition description (spatial layout, arrow directions, module positions)
- Content elements (specific modules, relationships, annotation text)
- English Prompt (complete English prompt, ready to copy into image generation tool)
- Copy-to-tool instructions

Also follow all constraints in `prompt-rules.md`: three composition layers, ≤3 colors, per-page must-have/forbidden lists, information density requirements.

### Round 5: Output &amp; Summary

Generate the following outputs:

```
sci-plot-output/
├── analysis.md             # Content analysis summary
├── figure-plan.md          # Figure plan (what each page covers)
├── prompts/
│   ├── 01-overview.md      # Page 1 prompt
│   ├── 02-mechanism-a.md   # Page 2 prompt
│   └── ...                 # Subsequent page prompts
└── README.md               # Usage instructions (how to copy prompts to each platform)
```

<div align="center">

---

## Five Visual Styles

| Style | Visual Effect | Best For |
|:---:|---|---|
| **paper-figure** (default) | Paper figure style, white background, vector feel modules, restrained colors | Journal figures, README hero, technical display |
| **sketchnote** | Warm research notes style, cream background, hand-drawn lines, colored pencil accents | Knowledge sharing, video promotion, learning notes |
| **journal-minimal** | Nature/IEEE style, extremely restrained academic charts | Paper submission, defense, group meeting |
| **warm-notes** | Bright handwritten style, approachable yet professional teaching feel | Science communication, courses, paper study notes |
| **business-research** | Business research brief style, structured, data-driven | Industry analysis, investor presentations |

*All styles are cross-platform compatible. Detailed specifications in `references/styles/`.*

---

## Figure Count Recommendations

| Content Complexity | Recommended Count | Content Allocation |
|:---:|:---:|---|
| Cover / promotional image | 1 | One overview explaining what was done |
| Quick understanding | 2-3 | Overview + core mechanism + results |
| Medium (2 core methods) | 4-6 | Overview + 2-3 mechanisms + key results |
| Complex (3+ core methods) | 6-10 | Overview + 1 per mechanism + comparison/results |

**Minimum 1, maximum 10.** Prefer fewer over more.

---

## Quality Standards

### Good Prompt Output
- Information is specific enough ("arrow from A to B" not "draw a flowchart")
- Style constraints are clear (background color, line style, color limits)
- Annotation content is precise (variable names, dimensions, key operations)
- Cross-platform compatible (not overly dependent on specific model features)

### Bad Prompt Output
- Vague descriptions like "draw a neural network architecture diagram"
- No color limits, resulting in garish output
- Annotation text is too wordy
- Too much information crammed into one page

---

## Reference Files

`references/prompt-rules.md` — Core prompt generation rules (composition, annotation, color, forbidden items)<br>
`references/analysis-guide.md` — Project/paper/code analysis guide<br>
`references/layout-rules.md` — Page composition &amp; role definitions<br>
`references/styles/paper-figure.md` — Paper figure style specification<br>
`references/styles/sketchnote.md` — Warm sketchnote style specification<br>
`references/styles/journal-minimal.md` — Nature/IEEE minimal style specification<br>
`references/styles/warm-notes.md` — Bright handwritten style specification<br>
`references/styles/business-research.md` — Business research brief style specification

</div>
