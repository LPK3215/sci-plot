# Contributing to Sci-Plot

Thank you for your interest in contributing to sci-plot! This project is a CodeBuddy skill that generates scientific figure prompts.

## How to Contribute

### Adding a New Style

1. Create a new `.md` file under `references/styles/`
2. Follow the existing pattern in `paper-figure.md` or `sketchnote.md`
3. Include: style description, color palette, annotation rules, layout preferences, and an English prompt snippet
4. Add the style to the table in `SKILL.md` (五种视觉风格 section)
5. Add the style to the table in `README.md` (可用风格 section)
6. Add the reference entry at the bottom of `SKILL.md`

### Improving Existing Rules

1. Edit the relevant file in `references/`
2. Keep rules concrete and actionable — avoid vague statements
3. If adding constraints, also update `每页禁止` or `每页必含` checklists in `prompt-rules.md`
4. Test the changes by running sci-plot against a real paper

### Updating the Workflow

1. Edit `SKILL.md` — the workflow lives there
2. Each round must have `⛔` marker to indicate it's mandatory
3. All reference files must be listed at the bottom of `SKILL.md`
4. Any new "先读取" instruction must have the corresponding reference file

### Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Commit with a descriptive message
5. Push to your fork
6. Open a pull request

## Project Structure

```
sci-plot/
├── SKILL.md                  # AI instruction: 6-round workflow
├── README.md                 # Human-facing documentation
├── LICENSE                   # MIT License
├── CHANGELOG.md              # Version history
├── CONTRIBUTING.md           # This file
├── .gitignore                # Version control exclusions
├── .gitattributes            # Line ending normalization
└── references/
    ├── prompt-rules.md       # Core rules for prompt generation
    ├── analysis-guide.md     # Content analysis checklists
    ├── layout-rules.md       # Page roles and composition
    └── styles/
        ├── paper-figure.md
        ├── sketchnote.md
        ├── journal-minimal.md
        ├── warm-notes.md
        └── business-research.md
```

## Questions?

Open an issue on GitHub: https://github.com/LPK3215/sci-plot/issues
