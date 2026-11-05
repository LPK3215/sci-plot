# Changelog

All notable changes to sci-plot are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

[中文更新日志](CHANGELOG.zh-CN.md)

## [Unreleased]

## [1.2.0] - 2026-11-05

### Added
- **Architecture Overhaul: Dual-Track Rules Pool**:
  - Added `references/rules-pool/local/` for curated, self-hosted style specifications and custom user `.md` rules.
  - Added `references/rules-pool/cloud/` featuring authoritative journal standards (Nature/IEEE/Cell/Science), dynamic URL parser protocol, and an External Skills Harvester ("Borrow Prompts, Block Image APIs").
  - Added `references/core/base-rules.md` encapsulating foundational physical guardrails (labels ≤8 chars, ≤3 colors, 80% visual gravity, no 3D).
- **Mechanism Innovation: Scope Isolation ("烟消云散")**: Unselects and clears all unchosen candidate rules after Step 3 to ensure zero context pollution during prompt compilation.
- **Bilingual Architecture SVG Updates**: Updated `docs/scripts/generate_architecture.py` and regenerated `docs/architecture.svg` and `docs/architecture_cn.svg`.

### Changed
- Refactored `SKILL.md` to a modular 5-round mandatory workflow.
- Updated `README.md` and `README_CN.md` to articulate the core philosophy: "Prompts as Intermediate Representation (IR), zero environment lock-in, and universal multi-platform consumption".

## [1.1.1] - 2026-06-13

### Changed
- Remove non-standard `version` field from `SKILL.md` frontmatter to align with AI skill specification standards (only `name` + `description` retained). Version continues to be tracked via this changelog and the README badge.
- Replace residual "CodeBuddy" branding with neutral "AI" across `CONTRIBUTING.md` / `CONTRIBUTING_CN.md` and changelogs.
- Fix missing entries in `README.md` / `README_CN.md` project structure trees (`index.html`, `examples/`, `SECURITY.md`).
- Stop tracking local `.codebuddy/` directory in git (now properly ignored).

## [1.1.0] - 2026-06-13

### Added
- Add `sci-plot-output/` to `.gitignore` to exclude generated outputs from version control.
- Add workflow architecture diagrams (`docs/architecture.svg` + `docs/architecture_cn.svg`) and generator script (`docs/scripts/generate_architecture.py`).
- Add badges to README.md (License, Version, AI Skill).
- Add project structure tree, FAQ section, and author info to README.md.
- Add visual architecture diagram section to README.md.
- Add interactive project overview dashboard (`project_overview.html` + `project_overview/`) with dark theme, animated workflow timeline, style previews, and modern card-based architecture diagram.
- Add bilingual architecture SVGs with dark theme matching project overview styling.

### Changed
- Rename English title from "Scientific Figure Prompt Generator" to "Scientific Figure Prompt Engine"; update Chinese subtitle to "科研绘图 —— 从论文到插图的一站式引擎".
- Split user-facing documentation into dedicated English and Chinese files: README.md/README_CN.md, CHANGELOG.md/CHANGELOG_CN.md, CONTRIBUTING.md/CONTRIBUTING_CN.md.
- Convert all AI-facing skill documents (SKILL.md, references/*.md) to pure English for optimal AI comprehension.
- Redesign architecture SVG with a two-phase layout highlighting the core step (Round 4) and modern visual styling.

## [1.0.0] - 2026-06-13

### Added
- Initial release of sci-plot scientific figure prompt engine.
- `SKILL.md`: complete 6-round mandatory workflow (Round 0-5) for analyzing research content and generating figure prompts.
- `references/prompt-rules.md`: core rules for composition, annotation, color, and anti-patterns.
- `references/analysis-guide.md`: detailed analysis checklists for papers, projects, code, and algorithms.
- `references/layout-rules.md`: page role definitions, recommended pacing, and composition rules.
- `references/styles/paper-figure.md`: paper figure style specification.
- `references/styles/sketchnote.md`: warm sketchnote style specification.
- `references/styles/journal-minimal.md`: journal minimal style specification.
- `references/styles/warm-notes.md`: warm notes style specification.
- `references/styles/business-research.md`: business research style specification.
- `README.md`: user-facing documentation with installation, usage, styles, and output structure.
