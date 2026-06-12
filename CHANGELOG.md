# Changelog

All notable changes to sci-plot will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Added `sci-plot-output/` to `.gitignore` to exclude generated output from version control.
- Added workflow architecture diagram (`docs/architecture.svg`) with generation script (`docs/scripts/generate_architecture.py`).
- Added badges (License, Version, CodeBuddy Skill) to README.md.
- Added project structure tree, FAQ section, and author information to README.md.
- Added visual architecture diagram section to README.md.

## [1.0.0] - 2026-06-13

### Added
- Initial release of sci-plot, the scientific figure prompt generator.
- `SKILL.md`: Complete 6-round mandatory workflow (Round 0-5) for analyzing research content and generating image prompts.
- `references/prompt-rules.md`: Core rules for composition, annotation, color, and forbidden patterns.
- `references/analysis-guide.md`: Detailed checklists for analyzing papers, projects, code, and algorithms.
- `references/layout-rules.md`: Page role definitions, recommended pacing, and composition rules.
- `references/styles/paper-figure.md`: Paper figure style specification.
- `references/styles/sketchnote.md`: Warm sketchnote style specification.
- `references/styles/journal-minimal.md`: Nature/IEEE minimal academic style specification.
- `references/styles/warm-notes.md`: Bright handwritten notes style specification.
- `references/styles/business-research.md`: Business research brief style specification.
- `README.md`: User-facing documentation with installation, usage, styles, and output structure.
- `LICENSE`: MIT License.
- `.gitignore`: Version control exclusions for Windows, macOS, IDE, and Python files.
- `CONTRIBUTING.md`: Contribution guidelines.
- `.gitattributes`: Line ending normalization.
