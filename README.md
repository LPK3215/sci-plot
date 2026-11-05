<div align="center">

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/LPK3215/sci-plot@main/docs/assets/banner.svg" alt="Sci-Plot — Scientific Figure Prompt Engine" width="100%"/>
</p>

# Sci-Plot

[![Version](https://img.shields.io/badge/version-1.2.0-brightgreen.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-3776AB.svg?logo=python&logoColor=white)](pyproject.toml)
[![AI Skill](https://img.shields.io/badge/AI-skill-6366F1.svg)](SKILL.md)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](tests/run_all_tests.py)
[![Dependencies](https://img.shields.io/badge/dependencies-zero-success.svg)](requirements.txt)

**Scientific illustration, from paper to figure — an all-in-one prompt engine.**

Sci-Plot does not generate images directly; it produces publication-ready, cross-platform prompts.  
Copy prompts into **ChatGPT/DALL-E, Doubao, Qwen, Midjourney, Stable Diffusion** to generate images,  
or use them as specifications to generate **HTML, SVG, Matplotlib, or Origin** academic figures.

**Compatible with any AI coding assistant** — Claude Code, Codex, Cursor, Windsurf, GitHub Copilot, Cline, Antigravity, or any agent capable of reading skill definitions.

[Features](#-core-features) · [Architecture](#-visual-architecture-diagram) · [Workflow](#-5-round-standardized-pipeline) · [Quick Start](#-quick-start) · [FAQ](FAQ.md) · [🌐 Project Overview](https://lpk3215.github.io/sci-plot/)

[中文说明文档](README.zh-CN.md)

</div>

---

## 📌 Project Overview

- **Repository**: [https://github.com/LPK3215/sci-plot](https://github.com/LPK3215/sci-plot)
- **Live Project Overview Dashboard**: [https://lpk3215.github.io/sci-plot/](https://lpk3215.github.io/sci-plot/)
- **Core Philosophy**: **"Prompts as Intermediate Representation (IR), Never Direct Bitmaps"**

Many scientific illustration tools call image generation APIs directly inside agent environments. This creates three fatal engineering bottlenecks:
1. **Environment Fragility & Crashes**: Direct API callers tightly couple to local runtime tools, Python packages, and API keys. Any network blockage or credential issue crashes the agent. Sci-Plot has **zero external runtime dependencies**.
2. **Black-box Output**: A single typo or inverted arrow ruins an entire raster bitmap (PNG/JPEG) with no way to perform surgical edits.
3. **No Asset Persistence**: Raster images cannot be easily audited, versioned, or tracked in Git repositories.

| Dimension | ❌ Traditional Direct Generation (Black Box) | ✅ Sci-Plot Prompt Engine (White Box IR) |
| :--- | :--- | :--- |
| **Execution Model** | Calls brittle image API inside agent environment | Pure prompt engineering & structured IR synthesis |
| **Output Asset** | Static raster bitmap (PNG/JPEG) | Publication-grade prompt package (`.md` IR) |
| **Error Recovery** | Any typo or inverted arrow ruins entire image | **1-second surgical edits** to hex colors or labels |
| **Consumption** | Locked into one model / API environment | Copy-paste to **ChatGPT, Midjourney, Doubao**, or compile to **HTML/SVG** |
| **Environment Risk** | High crash risk from missing packages, tokens, network | **Zero external runtime dependencies** |
| **Asset Persistence**| Binary blobs, cannot review in Git pull requests | 100% human-readable, auditable, Git-friendly |

```mermaid
flowchart TD
    subgraph Trad["❌ Traditional: Direct Image Generation (Black Box)"]
        direction LR
        T1(["API Call<br/><i>Tightly Coupled</i>"]) --> T2(["Fixed Bitmap<br/><i>PNG / JPEG</i>"]) --> T3{{"💥 Fatal Bottleneck<br/><i>Single Typo Ruins Entire Figure</i>"}}
    end

    subgraph Sci["✅ Sci-Plot: Prompts as Intermediate Representation (White Box)"]
        direction LR
        S1(["Extract Rules<br/><i>Explicit & Implicit</i>"]) --> S2(["Structured IR<br/><i>Prompt Package</i>"]) --> S3{{"✨ Zero-Failure Control<br/><i>1s Micro-Edits · Any Platform</i>"}}
    end

    style Trad fill:#fff1f2,stroke:#fda4af,stroke-width:1.5px,color:#9f1239
    style Sci fill:#f0fdf4,stroke:#86efac,stroke-width:1.5px,color:#166534
    style T1 fill:#ffffff,stroke:#f43f5e,stroke-width:1.5px,color:#9f1239
    style T2 fill:#ffffff,stroke:#f43f5e,stroke-width:1.5px,color:#9f1239
    style T3 fill:#ffe4e6,stroke:#e11d48,stroke-width:2px,color:#881337
    style S1 fill:#ffffff,stroke:#22c55e,stroke-width:1.5px,color:#166534
    style S2 fill:#ffffff,stroke:#22c55e,stroke-width:1.5px,color:#166534
    style S3 fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
```

---

## 🖼️ Visual Architecture Diagram

The end-to-end workflow and dual-track rule isolation pipeline is illustrated below:

[![Sci-Plot Architecture](https://cdn.jsdelivr.net/gh/LPK3215/sci-plot@main/docs/architecture.svg)](https://lpk3215.github.io/sci-plot/)

> *Figure 1: Sci-Plot Workflow Architecture (v1.2.0) — From input detection to dual-track rule matching, scope isolation, and multi-platform consumption.*

> [!TIP]
> **Explore Live Interactive Architecture Diagrams (Powered by Archify)**:
> - ⚡ **[Interactive Core Architecture (10-Min Fast-Track)](./docs/archify/core-architecture.html)** — Focus on the primary 5-round pipeline
> - 🏛️ **[System Panorama Architecture](./docs/archify/architecture-panorama.html)** — Comprehensive 12-component landscape
> - 🔄 **[Workflow Execution Pipeline](./docs/archify/workflow-panorama.html)** — End-to-end execution path with lane separation
> - ⏱️ **[Invocation Sequence Call Chain](./docs/archify/sequence-panorama.html)** — Exact call trace across boundaries
> - 🌊 **[Data Flow & Storage Pipeline](./docs/archify/dataflow-panorama.html)** — Transformation from raw paper to verified prompts
> - 📊 **[Interactive Project Overview Dashboard](./docs/project_overview/index.html)** — Full panoramic showcase & quickstart
> - 📸 **[Shareable Project Card (PNG Export)](./docs/project_overview/project_card.html)** — Compact summary card with 1-click PNG export
> - 📄 **[Architecture Blueprint Input (diagram-input.md)](./docs/archify/diagram-input.md)** — Structured input specifications

---

## ✨ Core Features

### 1. Dual-Track Rules Pool
- **Local Rules Pool (`references/rules-pool/local/`)**: Houses core, battle-tested presets (`paper-figure`, `journal-minimal`, `sketchnote`, `warm-notes`, `business-research`). Users can drop custom `.md` rules here for immediate zero-config use.
- **Cloud & External Rules Pool (`references/rules-pool/cloud/`)**:
  - **Authoritative Journal Standards**: Official guidelines for Nature, IEEE, Cell, Science;
  - **Dynamic URL Parser**: Pass any URL containing figure guidelines; the agent extracts dimensions, colors, and constraints on the fly;
  - **External Skill Capability Harvester**: When an external image generation skill is available, **extract its prompt engineering templates and domain vocabulary, while strictly blocking its image generation API calls**. Zero environment overhead, 100% capability reuse.

### 2. Scope Isolation ("烟消云散")
During exploratory rounds, the agent can recommend and search across pools. **Once you confirm a specific rule, all unselected rules, candidate links, and exploratory noise are completely cleared from the active prompt context.**
The final prompt compilation step loads strictly:
$$\text{Base Physical Guardrails (base-rules.md)} + \text{Sole Selected Rule}$$
This eliminates hallucinated rule conflicts (e.g., mixing Nature minimal palettes with IEEE bold borders).

### 3. Universal Skill Harvester (Heuristic Radar)
For external or public GitHub skill repositories, Sci-Plot dynamically discovers, extracts, and normalizes figure guidelines while keeping your workspace completely clean:

```mermaid
flowchart TD
    User(["📥 Input: GitHub Skill Repo / Journal Guidelines URL"]) --> Router{"📡 Adaptive Ingestion Radar"}
    
    Router -->|⚡ Fast-Track| S1["<b>Route 1: Universal Heuristic Radar</b><br/><i>1-second zero-overhead scan</i>"]
    Router -->|🌐 Online Fluid| S2["<b>Route 2: AI Live Semantic Reading</b><br/><i>Read raw GitHub files directly</i>"]
    Router -->|📦 Sandbox Fallback| S3["<b>Route 3: Ephemeral Temp Clone</b><br/><i>Isolated background analysis</i>"]
    
    S1 --> Synth[["🧠 AI Semantic Extraction & Rule Synthesis<br/><i>Extracts Aspect Ratio, Hex Palettes, Technical Vocab</i>"]]
    S2 --> Synth
    S3 --> Synth
    
    Synth --> Save[("💾 Materialize Local Rule<br/><code>references/rules-pool/local/downloaded-*.md</code>")]
    Save --> Purge(["✨ Physical Deep Clean<br/><i>Zero Residue: Clones & temp files deleted immediately</i>"])
    Purge --> Ready(["🎯 100% Offline Asset Ready<br/><i>Permanent, portable, zero runtime dependencies</i>"])

    classDef input fill:#e0f2fe,stroke:#0284c7,stroke-width:1.5px,color:#0369a1;
    classDef router fill:#f8fafc,stroke:#64748b,stroke-width:2px,color:#1e293b;
    classDef route fill:#f1f5f9,stroke:#94a3b8,stroke-width:1.5px,color:#334155;
    classDef synth fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#5b21b6;
    classDef storage fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e40af;
    classDef clean fill:#fef3c7,stroke:#d97706,stroke-width:1.5px,color:#92400e;
    classDef done fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#166534;

    class User input;
    class Router router;
    class S1,S2,S3 route;
    class Synth synth;
    class Save storage;
    class Purge clean;
    class Ready done;
```

### 4. Four-Tier Quality Assurance Gate
Prompt precision is the lifeline of Sci-Plot. Four defensive layers ensure zero-defect output:

```mermaid
flowchart LR
    L1(["<b>🛡️ Gate 1: Base Rules</b><br/>Physical Guardrails<br/><i>No 3D · Labels ≤ 8 chars · Focal 75-85%</i>"]) 
    --> L2(["<b>🔍 Gate 2: Skill Verifier</b><br/>Harvester Checklist<br/><i>Aspect Ratio · Hex Palette · Zero API</i>"]) 
    --> L3(["<b>💨 Gate 3: Scope Isolation</b><br/>Context Purge<br/><i>Clear Candidate Noise · Zero Conflict</i>"]) 
    --> L4(["<b>🧪 Gate 4: Compliance Linter</b><br/>Automated Testing<br/><i>6 Test Suites · White Canvas · High Contrast</i>"]) 
    --> Output(["<b>🎯 Publication-Grade IR</b><br/>Ready for Cross-Platform Use"])

    classDef g1 fill:#e0e7ff,stroke:#6366f1,stroke-width:1.5px,color:#3730a3;
    classDef g2 fill:#e0f2fe,stroke:#0284c7,stroke-width:1.5px,color:#0369a1;
    classDef g3 fill:#fef3c7,stroke:#d97706,stroke-width:1.5px,color:#92400e;
    classDef g4 fill:#ede9fe,stroke:#8b5cf6,stroke-width:1.5px,color:#5b21b6;
    classDef g5 fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;

    class L1 g1;
    class L2 g2;
    class L3 g3;
    class L4 g4;
    class Output g5;
```

| Defense Gate | Core Mechanism | Guaranteed Outcome |
| :--- | :--- | :--- |
| **Gate 1: Physical Guardrails** | Invariant base rules (`base-rules.md`) | Strictly eliminates 3D/photorealism; caps labels at ≤ 8 chars to prevent garbled text; enforces 75-85% visual gravity |
| **Gate 2: Harvester Checklist** | 5-point verification checklist | Requires explicit aspect ratio, exact Hex color palette, domain vocabulary, and pure prompt template; blocks API calls |
| **Gate 3: Scope Isolation** | "烟消云散" context purge | Completely unloads exploratory candidate rules and dialogue history; final context loads strictly Base Rules + Sole Selected Rule |
| **Gate 4: Compliance Linter** | Automated test suite (`run_all_tests.py`) | 6 test suites verify pure white background, negative constraints, file integrity, and non-destructive execution |

---

## 🛠️ Tech Stack

| Layer | Component | Implementation Details |
|---|---|---|
| **Skill Protocol** | Agent Skill Specification | Standard YAML frontmatter + 5-round deterministic pipeline (`SKILL.md`) |
| **Engine & Scripts** | Python 3.10+ | Pure Standard Library (`urllib.request`, `json`, `ssl`, `base64`, `re`, `pathlib`) — **Zero External Dependencies** |
| **Testing & Quality** | Python Automated Test Suite | `tests/run_all_tests.py`, pytest, ruff linter |
| **Visual Assets** | Hand-Crafted Vector SVG & HTML | Modern dark-themed dashboard (`docs/project_overview/`), architecture SVG, banner SVG |
| **Consumption Targets** | Cross-Platform Prompts & Code | ChatGPT/DALL-E, Midjourney, Stable Diffusion, Doubao, Qwen, HTML/SVG, Matplotlib, Origin |

---

## 📂 Project Structure

```
sci-plot/
├── SKILL.md                              # AI Skill: 5-round standardized pipeline & isolation
├── README.md                             # User documentation (English)
├── README.zh-CN.md                       # User documentation (Chinese)
├── LICENSE                               # MIT License
├── CHANGELOG.md                          # Version history (English)
├── CHANGELOG.zh-CN.md                    # Version history (Chinese)
├── CONTRIBUTING.md                       # Contribution guidelines (English)
├── CONTRIBUTING.zh-CN.md                 # Contribution guidelines (Chinese)
├── FAQ.md                                # Frequently Asked Questions (standalone reference)
├── AUTHORS                               # Authors and maintainers
├── pyproject.toml                        # PEP 621 package metadata and tool configuration
├── requirements.txt                      # Runtime & development dependency notes
├── docs/                                 # GitHub Pages root & documentation assets
│   ├── index.html                        # Pages root redirect
│   ├── .nojekyll                         # Disables Jekyll processing
│   ├── architecture.svg                  # English architecture SVG
│   ├── architecture_cn.svg               # Chinese architecture SVG
│   ├── assets/
│   │   └── banner.svg                    # Brand banner SVG
│   ├── archify/                          # Interactive Archify diagrams & blueprint
│   │   ├── diagram-input.md
│   │   ├── core-architecture.html
│   │   ├── architecture-panorama.html
│   │   ├── workflow-panorama.html
│   │   ├── sequence-panorama.html
│   │   └── dataflow-panorama.html
│   └── project_overview/                 # Interactive dashboard & shareable card
│       ├── index.html
│       ├── style.css
│       ├── script.js
│       └── project_card.html
├── scripts/                              # Skill management & harvesting tools
│   ├── universal_skill_harvester.py      # Heuristic radar scanner for external skills
│   ├── fetch_external_skills.py          # Top 3 skills fetcher
│   ├── sync_documentation_metrics.py     # Cross-document consistency & metrics auditor
│   └── visualization/                    # Visual assets generation scripts
│       └── generate_banner.py            # Banner generator script
├── tests/                                # Automated test suite (100% pass)
│   ├── run_all_tests.py                  # Test suite runner
│   ├── test_rules_pool_integrity.py
│   ├── test_prompt_compliance.py
│   ├── test_end_to_end_simulation.py
│   ├── test_cloud_downloader.py
│   ├── test_external_skills_ingestion.py
│   └── test_top10_radar_scan.py
└── references/                           # Scientific rules & references
    ├── core/                             # Foundational base rules
    │   └── base-rules.md                 # Physical guardrails (labels, colors, no-3D)
    ├── analysis-guide.md                 # Paper & code semantic analysis checklists
    ├── layout-rules.md                   # Multi-page figure roles & pacing
    ├── prompt-rules.md                   # Core prompt syntax & anti-patterns
    ├── rules-pool/                       # Dual-Track Rules Pool
    │   ├── local/                        # Local Pool (presets & materialized rules)
    │   └── cloud/                        # Cloud Pool (channels & adapter protocols)
    └── renderers/                        # Vector and HTML renderers
        └── html/                         # Academic static HTML figure template
```

---

## 🚀 Quick Start

### 1. Zero-Install Usage in AI Assistants
In any workspace containing sci-plot (Cursor, Claude Code, Windsurf, Copilot, Cline, Antigravity):

```text
Follow the /sci-plot/SKILL.md skill to generate scientific figure prompts.
Target: [optional — leave blank to auto-analyze project, or provide path / arXiv / text]
```

### 2. Running Automated Test Suite
To verify rules pool integrity, compliance checks, and radar scanner locally:

```bash
python tests/run_all_tests.py
```

All 6 test suites run using standard library with zero external dependencies.

---

## 🔄 5-Round Standardized Pipeline

```mermaid
flowchart LR
    R0(["<b>Round 0</b><br/>🎯 Target Scan<br/><i>Auto-detect .tex / .md / code</i>"]) 
    --> R1(["<b>Round 1</b><br/>🔬 Deep Analysis<br/><i>Extract core logic & math</i>"]) 
    --> R2(["<b>Round 2</b><br/>📐 Visual Elements<br/><i>Decompose layout & symbols</i>"]) 
    --> R3(["<b>Round 3</b><br/>🎨 Confirm & Match<br/><i>Dual-track rules pool selection</i>"]) 
    --> R4(["<b>Round 4</b><br/>⚡ Scope Isolation<br/><i>Compile prompt & purge noise</i>"]) 
    --> R5(["<b>Round 5</b><br/>📦 Deliver Asset<br/><i>Multi-platform prompt package</i>"])

    classDef r0 fill:#f1f5f9,stroke:#64748b,stroke-width:1.5px,color:#1e293b;
    classDef r1 fill:#e0f2fe,stroke:#0284c7,stroke-width:1.5px,color:#0369a1;
    classDef r2 fill:#ede9fe,stroke:#7c3aed,stroke-width:1.5px,color:#5b21b6;
    classDef r3 fill:#fef3c7,stroke:#d97706,stroke-width:1.5px,color:#92400e;
    classDef r4 fill:#ffedd5,stroke:#ea580c,stroke-width:1.5px,color:#9a3412;
    classDef r5 fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;

    class R0 r0;
    class R1 r1;
    class R2 r2;
    class R3 r3;
    class R4 r4;
    class R5 r5;
```

### Inputs
- **Local Papers / Code**: Auto-detects `.tex` files (LaTeX source), `.md`, PDF, or Python code;
- **ArXiv Links / IDs**: e.g., `https://arxiv.org/abs/1706.03762` or `1706.03762`;
- **Pasted Text**: Directly paste abstracts, methods, or algorithm steps;
- **Custom Rule Specification**: Local `.md` path, online URL, or external skill name.

### Outputs
Standardized directory structure in `sci-plot-output/`:
```
sci-plot-output/
├── analysis.md             # Semantic breakdown (contributions, data flow, modules)
├── figure-plan.md          # Multi-figure plan (roles, pacing, composition)
├── prompts/
│   ├── 01-overview.md      # Page 1 prompt (English + Chinese)
│   ├── 02-mechanism.md     # Page 2 mechanism zoom-in prompt
│   └── ...
└── README.md               # Consumption instructions (paste to Web AI or compile to code)
```

### Consumption Options

| Target Platform | How to Use | Outcome |
| :--- | :--- | :--- |
| **ChatGPT / DALL-E (Recommended)** | Copy English Prompt directly into chat | High-res academic figure |
| **Doubao / Qwen** | Copy English or Chinese prompt directly | Fast conceptual drafts |
| **Midjourney** | `/imagine` + English Prompt | Stylized high-texture graphics |
| **Stable Diffusion / Flux** | Paste into txt2img positive prompt | Local reproducible rendering |
| **SVG / HTML / Matplotlib / Origin** | Pass module layouts and flow arrows to coding AI | Editable vector & interactive plots |

---

## ❓ Frequently Asked Questions (FAQ)

- **Q: Why prompts only, instead of calling image APIs directly?**  
  *A: Direct image generation introduces environment lock-in, uneditable bitmaps, and crashes. Prompts serve as reviewable, durable Intermediate Representations (IR).*
- **Q: What is Scope Isolation ("烟消云散")?**  
  *A: After confirming a rule in Round 3, all unselected rules and exploratory context are cleared out. Round 4 compiles prompts strictly against `base-rules.md` plus your sole chosen rule, eliminating hallucinated style conflicts.*
- **Q: How to add custom laboratory guidelines?**  
  *A: Add a `.md` file to `references/rules-pool/local/` (e.g., `my-lab-style.md`). The AI recognizes it dynamically without code modifications.*

👉 Read the full **[FAQ.md](FAQ.md)** for detailed explanations.

---

## 🤝 Contributing

Contributions are warmly welcomed! Please check out:
- **[CONTRIBUTING.md](CONTRIBUTING.md)** (English)
- **[CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)** (中文贡献指南)

---

## 📜 License & Authors

- **License**: [MIT License](LICENSE) &copy; 2026 LPK3215
- **Authors**: LPK3215 (`17538703215@163.com`) — see [AUTHORS](AUTHORS)
- **Changelog**: See [CHANGELOG.md](CHANGELOG.md) for version evolution details.
