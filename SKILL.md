---
name: sci-plot
description: >
  Scientific figure prompt engine. Analyzes papers/projects/algorithms/code/documents,
  applies scientific figure conventions, and generates high-quality, cross-platform image
  generation prompts. Users copy prompts into ChatGPT/DALL-E, Doubao, Qwen (Tongyi Wanxiang),
  Midjourney, Stable Diffusion, or any other AI image generation tool to produce figures.
  Does not generate images directly — produces prompts only.
---

# Sci-Plot — Scientific Figure Prompt Engine

Turn papers, projects, and algorithms into high-quality, cross-platform image generation prompts. You provide the content, sci-plot produces prompts, you paste them into ChatGPT/DALL-E, Doubao, Qwen, Midjourney, Stable Diffusion, or other AI image tools.

## Core Positioning

**sci-plot does not generate images directly.** Its workflow chain is:

```
User Input (paper/project/code/doc) → Analysis → Confirmation (language/style/count) → Prompt File Generation → User copies to image generation tool
```

Prompts are cross-platform compatible (ChatGPT/DALL-E, Doubao, Qwen, Midjourney, Stable Diffusion, etc.).

---

## Mandatory Workflow (Every step is mandatory)

### Round 0: Determine Analysis Target

1. If the user explicitly specifies a target (path/link/pasted content), use it directly
2. If not specified, auto-detect from the current workspace:
   - Prioritize `.tex` files (LaTeX papers — methods, formulas, architecture are all there)
   - Then `.md` documents, `.pdf`, `.py` and other source files
3. If the workspace also has no analyzable content, prompt the user to provide a target

### Round 1: Analyze Input Content

**Read `references/analysis-guide.md` first**, then execute the complete four-step analysis flow according to the four analysis checklists defined there (paper/code/algorithm/document).

Read the target content determined in Round 0, analyze comprehensively, covering the following dimensions:

| Content Type | Analysis Points |
|---|---|
| Paper | Core innovations (1-3), method input→process→output flow, key experiments/results, architecture/module relationships |
| Project Code | Project structure, core modules, data flow, key algorithm functions, module dependencies |
| Document | Architecture design, API interfaces, data models, business processes |
| Algorithm | Input/output, core steps, key data structures, complexity, baseline comparison |

**Self-check**: Is the content fully understood? Can you explain the key concepts in your own words?

### Round 2: Extract Illustratable Content

Filter content from the analysis results that is **suitable for illustration**:

**Must illustrate (1-2 pages each):**
- Method overall flow/architecture (input→modules→output)
- Each core innovation mechanism (zoomed-in internal view)
- Most compelling experimental results/data

**Optional illustration:**
- Visual comparison with baselines
- Key data processing pipelines
- System architecture/module relationship diagrams

**Do NOT illustrate:**
- Related work/background introduction (text suffices)
- Multiple similar ablation experiments
- Abstract inspiration/concepts

### Round 3: Ask the User

**Read `references/layout-rules.md` first**, then organize the plan using the page roles defined there (cover / method-overview / mechanism-detail / comparison / evidence / architecture / data-flow / takeaway) and their recommended pacing.

Confirm the following 5 items. If the user does not reply, provide default recommendations:

1. **Language**: Chinese / English / Bilingual (default: Chinese)
2. **Visual Style** (see style table below)
3. **Number of Figures**: Recommend based on content complexity, explaining what each figure covers
4. **Aspect Ratio**: 16:9 (landscape) / 4:3 (landscape) / 2:3 (portrait, default for method diagrams)
5. **Purpose**: Journal figure / Technical blog / README / Defense presentation / Science communication

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

### Round 5: Output & Summary

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

---

## Five Visual Styles

| Style | Visual Effect | Best For | Tool Compatibility |
|------|---------|---------|--------------|
| **paper-figure** (default) | Paper figure style, white background, vector feel modules, restrained colors | Journal figures, README hero, technical display | All tools universal |
| **sketchnote** | Warm research notes style, cream background, hand-drawn lines, colored pencil accents | Knowledge sharing, video promotion, learning notes | All tools universal |
| **journal-minimal** | Nature/IEEE style, extremely restrained academic charts | Paper submission, defense, group meeting | All tools universal |
| **warm-notes** | Bright handwritten style, approachable yet professional teaching feel | Science communication, courses, paper study notes | All tools universal |
| **business-research** | Business research brief style, structured, data-driven | Industry analysis, investor presentations | All tools universal |

Detailed specifications in `references/styles/` directory.

---

## Figure Count Recommendations

| Content Complexity | Recommended Count | Content Allocation |
|-----------|---------|---------|
| Cover / promotional image | 1 figure | One overview explaining what was done |
| Quick understanding | 2-3 figures | Overview + core mechanism + results |
| Medium (2 core methods) | 4-6 figures | Overview + 2-3 mechanisms + key results |
| Complex (3+ core methods) | 6-10 figures | Overview + 1 per mechanism + comparison/results |

**Minimum 1, maximum 10**. Prefer fewer over more.

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

- `references/prompt-rules.md` — Core prompt generation rules (composition, annotation, color, forbidden items)
- `references/analysis-guide.md` — Project/paper/code analysis guide
- `references/layout-rules.md` — Page composition & role definitions
- `references/styles/paper-figure.md` — Paper figure style specification
- `references/styles/sketchnote.md` — Warm sketchnote style specification
- `references/styles/journal-minimal.md` — Nature/IEEE minimal style specification
- `references/styles/warm-notes.md` — Bright handwritten style specification
- `references/styles/business-research.md` — Business research brief style specification
