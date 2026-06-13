<div align="center">

# Sci-Plot — Scientific Figure Prompt Engine

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-brightgreen.svg)](CHANGELOG.md)
[![AI Skill](https://img.shields.io/badge/AI-skill-6366F1.svg)](SKILL.md)

Scientific illustration, from paper to figure — an all-in-one prompt engine. sci-plot does not generate images directly; it produces cross-platform prompts that you copy into **ChatGPT/DALL-E, Doubao, Qwen (Tongyi Wanxiang), Midjourney, Stable Diffusion**, or any other AI image generation tool.

**Works with any AI coding assistant** — Claude Code, Codex, Cursor, Windsurf, GitHub Copilot, Cline, Continue, Aider, or any AI that can read project files. Just open this directory and the AI will understand SKILL.md instructions.

**[🌐 Live Demo](https://lpk3215.github.io/sci-plot/project_overview.html)** | [中文文档](README_CN.md)

</div>

## Workflow Architecture

![Architecture](./docs/architecture.svg)

## Typical Use Cases

**Your paper is done — time for figures.** Your LaTeX paper (`.tex` file) is complete: methods, formulas, experiments are all written, but you lack a high-quality method architecture diagram or mechanism flowchart. Point sci-plot at your project directory or .tex file. It reads everything, proposes a figure plan, you confirm the parameters, and it outputs prompts for each figure. Copy the prompts to ChatGPT/DALL-E / Doubao / Qwen / Midjourney — images appear in seconds.

**Best results come from complete content.** The more complete and well-structured your input is, the more precise the extraction and the better the prompts will match your paper's academic context. Vague one-line ideas still work, but the output will be more generic.

Also suitable for: project README illustrations, technical blog visuals, defense presentation slides, algorithm explanation diagrams.

## Installation

```bash
git clone https://github.com/LPK3215/sci-plot.git
```

After cloning, open the sci-plot directory (or add it as a workspace/subproject). The AI will read SKILL.md and apply its rules.

## Quick Start

**See a complete example first**: Check out [`examples/transformer-paper/`](examples/transformer-paper/) to see what sci-plot outputs look like — analysis, figure plan, and ready-to-use prompts for the classic Transformer paper.

## Usage

### Basic Usage

After cloning, open the sci-plot directory and send this prompt to the AI:

```
Follow the /sci-plot/SKILL.md skill to generate scientific figure prompts.
Target: [optional — leave blank to auto-analyze current project]
```

**Target** supports any of the following formats:

- Leave blank → auto-analyze current project, prioritizing `.tex` files
- Local path → `/path/to/your/paper/`
- arxiv link → `https://arxiv.org/abs/2401.12345`
- Pasted content → paste abstract, method description, or algorithm steps directly
- arxiv ID → `1706.03762`

### Interaction Flow

1. AI analyzes your content and proposes a figure plan
2. You confirm: language (Chinese/English/Bilingual), style, number of figures, aspect ratio, purpose
3. AI generates prompt files into `sci-plot-output/prompts/` directory
4. You copy prompts into **ChatGPT/DALL-E, Doubao, Qwen, Midjourney, Stable Diffusion**, or other AI image tools

### Available Styles

| Style | Effect | Best for |
|------|------|------|
| **paper-figure** (default) | Paper figure style, white background, vector modules, restrained colors | Journal figures, README hero images, technical displays |
| **sketchnote** | Warm research notes style, cream background, hand-drawn lines | Knowledge sharing, learning notes |
| **journal-minimal** | Nature/IEEE style, extremely minimal academic | Paper submission, defense |
| **warm-notes** | Bright handwritten style, approachable yet professional | Science communication, courses |
| **business-research** | Business research brief style, structured, data-driven | Industry analysis, investor presentations |

### Where to Paste Prompts

| Tool | Action |
|------|------|
| **ChatGPT (recommended)** | Paste into DALL-E |
| Doubao | Text-to-image → paste prompt |
| Qwen (Tongyi Wanxiang) | Text-to-image → paste prompt (English works best) |
| Midjourney | `/imagine` then paste prompt |
| Stable Diffusion | txt2img paste |
| Other image gen tools | Works equally well |

### Output File Structure

```
sci-plot-output/
├── analysis.md          # Content analysis summary
├── figure-plan.md       # Figure plan (what each page covers)
├── prompts/
│   ├── 01-overview.md   # Page 1 prompt
│   ├── 02-mechanism.md  # Page 2 prompt
│   └── ...
└── README.md            # This README
```

## Project Structure

```
sci-plot/
├── SKILL.md                              # AI instruction: 6-round mandatory workflow
├── README.md                             # User-facing documentation (English)
├── README_CN.md                          # User-facing documentation (Chinese)
├── LICENSE                               # MIT License
├── CHANGELOG.md                          # Version history (English)
├── CHANGELOG_CN.md                       # Version history (Chinese)
├── CONTRIBUTING.md                       # Contribution guidelines (English)
├── CONTRIBUTING_CN.md                    # Contribution guidelines (Chinese)
├── .gitignore                            # Version control exclusions
├── .gitattributes                        # Line ending normalization
├── project_overview.html                 # Project overview dashboard entry
├── project_overview/
│   ├── styles.css                        # Dark theme styles
│   └── main.js                           # Interactive logic
├── docs/
│   ├── architecture.svg                  # Workflow architecture diagram (English)
│   ├── architecture_cn.svg               # Workflow architecture diagram (Chinese)
│   └── scripts/
│       └── generate_architecture.py      # Architecture diagram generation script
└── references/
    ├── prompt-rules.md                   # Core prompt generation rules
    ├── analysis-guide.md                 # Content analysis guide
    ├── layout-rules.md                   # Page composition & role definitions
    └── styles/
        ├── paper-figure.md               # Paper figure style
        ├── sketchnote.md                 # Warm sketchnote style
        ├── journal-minimal.md             # Nature/IEEE minimal style
        ├── warm-notes.md                 # Bright handwritten style
        └── business-research.md          # Business research brief style
```

## FAQ

**Q: Can sci-plot generate images directly?**
A: No. sci-plot only produces prompts. You copy the prompts into ChatGPT/DALL-E, Doubao, Qwen, Midjourney, or other image generation tools. This approach makes prompts cross-platform compatible, not tied to any specific tool.

**Q: Can I use it without a complete paper or project?**
A: Yes, but results will be less precise. sci-plot works best with complete content — the more complete and well-structured your input, the more accurate the extraction. A vague one-liner still produces prompts, but they'll be more generic.

**Q: What input formats are supported?**
A: LaTeX papers (`.tex`, highest priority), Markdown documents, PDF, Python source code, arxiv links or IDs, and pasted text content.

**Q: Which part of the prompt file is the core output?**
A: The `▶ English Prompt (core, copy directly)` section in each prompt file is the core output. Copy it directly into any image generation tool. The Chinese explanations, composition descriptions, and content elements are for human reference.

**Q: How do I add a new visual style?**
A: Create a new `.md` file under `references/styles/`, follow the format of existing style files, then register it in the style tables in both `SKILL.md` and `README.md`. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

**Q: What's the maximum number of figures?**
A: Minimum 1, maximum 10. The exact number depends on content complexity: simple content 1-3, medium 4-6, complex 6-10.

## Author

- **LPK3215** — [GitHub](https://github.com/LPK3215)

## License

MIT — see [LICENSE](LICENSE) for details.
