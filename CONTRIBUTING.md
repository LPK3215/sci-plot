# Contributing to Sci-Plot

Thank you for your interest in Sci-Plot! This project is a zero-dependency prompt compiler that turns any skill repository plus a topic into portable Markdown prompt assets.

[中文贡献指南](CONTRIBUTING.zh-CN.md)

## How to Contribute

### 1. Adding New Rules to the Local Pool

Adding custom rules is now modular and plug-and-play:
1. Create a new `.md` file in `references/rules-pool/local/` (e.g., `my-lab-style.md`).
2. Follow the template of existing files (e.g., `paper-figure.md`): style atmosphere, canvas background, restrained color palette (≤3 colors), line/arrow rules, and core English prompt snippet.
3. Once placed, AI can recognize and load it directly when specified by name in conversation without modifying core workflow code.

### 2. Adding Channels to the Cloud Pool

1. Edit `references/rules-pool/cloud/cloud-channels.md`.
2. Add authoritative journal guideline links or open-source image generation skill mapping patterns.
3. Adhere to the core principle: **"Borrow Prompts, Block Image APIs"** to eliminate heavy local dependencies.

### 3. Improving Base Guardrails & Core Workflow

1. Base physical constraints reside in `references/core/base-rules.md` (label length limits, color limits, 80% visual gravity, anti-3D patterns).
2. The orchestrator workflow resides in `SKILL.md`. Ensure the **Scope Isolation ("烟消云散")** rule is preserved to prevent context pollution and rule conflicts.
3. Always verify changes using real academic papers.

### 4. Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make changes and verify with the automated test suite: `python tests/run_all_tests.py`
4. Verify document consistency: `python scripts/sync_documentation_metrics.py --check`
5. Commit your changes with descriptive messages
6. Push to your fork and submit a Pull Request

## Project Structure

```
sci-plot/
├── SKILL.md                              # AI Skill: 5-round standardized pipeline & isolation
├── README.md                             # User documentation (English)
├── README.zh-CN.md                       # User documentation (Chinese)
├── LICENSE                               # MIT License
├── CHANGELOG.md                          # Version history (English)
├── CHANGELOG.zh-CN.md                    # Version history (Chinese)
├── CONTRIBUTING.md                       # This file (English)
├── CONTRIBUTING.zh-CN.md                 # This file (Chinese)
├── FAQ.md                                # Frequently Asked Questions
├── AUTHORS                               # Authors and contributors
├── pyproject.toml                        # Project metadata and tool configuration
├── requirements.txt                      # Python runtime and development dependencies
├── docs/                                 # GitHub Pages root & documentation assets
│   ├── index.html                        # Pages root redirect
│   ├── .nojekyll                         # Disables Jekyll processing
│   ├── architecture.svg                  # English architecture SVG
│   ├── architecture_cn.svg               # Chinese architecture SVG
│   ├── assets/
│   │   └── banner.svg                    # Brand banner SVG
│   ├── archify/                          # Interactive Archify diagrams
│   └── project_overview/                 # Interactive dashboard & shareable card
├── scripts/                              # Skill harvesting & management scripts
│   ├── universal_skill_harvester.py      # Adaptive heuristic radar scanner
│   └── fetch_external_skills.py          # External skills fetcher
├── tests/                                # Automated test suite
│   ├── run_all_tests.py                  # Test suite runner
│   └── test_*.py                         # Test modules
└── references/                           # Reference guides & rules
    ├── core/                             # Foundational core
    │   └── base-rules.md                 # Base physical guardrails
    ├── analysis-guide.md                 # Content analysis checklists
    ├── layout-rules.md                   # Page roles & composition
    └── rules-pool/                       # Dual-Track Rules Pool
        ├── local/                        # Local Pool (presets & custom user .md)
        └── cloud/                        # Cloud Pool (channels & adapter protocols)
```

## Questions?

Open an issue on GitHub: https://github.com/LPK3215/sci-plot/issues
