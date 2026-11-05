# Frequently Asked Questions (FAQ)

Comprehensive answers to common questions about sci-plot's design philosophy, mechanics, and usage.

---

### Q0: Is this still a scientific-figure tool?

**A**: The bundled rules pool ships a **scientific-figure preset pack** as the reference domain, but the workflow itself is domain-agnostic: give it any skill repository plus a topic and it compiles portable `.md` prompt assets. The real point is to remove the runtime lock-in most agent skills assume — reusing someone else's rules should not require their paid coding agent, their CLI, or their API keys.

---

### Q1: Why does sci-plot only generate prompts and never call image generation APIs directly?

**A**: Directly invoking image generation models (e.g., calling OpenAI DALL-E, Midjourney, or Stable Diffusion APIs from inside an agent environment) introduces three critical failure modes:
1. **Environment Fragility & Runtime Crashes**: Direct API callers tightly couple to Python packages, specific CLI tools, API keys, and network environments. When an agent runs in a sandboxed, restricted, or offline environment, the tool crashes completely. Sci-plot has **zero external environment dependencies**.
2. **Bitmaps Are Irreversible Black Boxes**: If an API outputs a PNG image with a single typo or an inverted arrow, the entire figure is ruined. You cannot perform localized surgical edits. In contrast, prompts are **structured Intermediate Representations (IR)** that can be tweaked in seconds.
3. **Engineering Asset Persistence**: Markdown prompts can be checked into Git, version-controlled, reviewed in pull requests, and maintained alongside your research papers.

---

### Q2: What is the Scope Isolation ("烟消云散") mechanism and why is it essential?

**A**: In multi-turn LLM reasoning, when an agent compares multiple style guidelines (e.g., IEEE vs. Nature vs. Sketch notes), retained candidate rules cause severe context contamination. The model experiences hallucinated rule conflicts—attempting to satisfy contradictory color palettes or bounding constraints.

Under Scope Isolation:
- During exploratory rounds, the agent can recommend and search across pools.
- **Once you confirm a specific rule (e.g., `paper-figure`), all unselected rules, candidate links, and exploratory noise are completely cleared from the active prompt context.**
- The final prompt compilation step loads strictly:
  $$\text{Base Physical Guardrails (base-rules.md)} + \text{Sole Selected Rule}$$
This guarantees mathematical purity and prevents hallucinated style bleed.

---

### Q3: How do I add my laboratory's custom figure guidelines?

**A**: Sci-plot is completely modular and plug-and-play:
1. Create a `.md` file inside `references/rules-pool/local/` (e.g., `my-lab-style.md`).
2. Follow the existing template structure: define the style atmosphere, white canvas background, restrained color palette (≤3 hex colors), arrow/line geometry, and the core English prompt snippet.
3. In subsequent conversations with your AI, simply request: *"Use local style my-lab-style."* The agent detects and loads it dynamically without changing any codebase logic.

---

### Q4: How does the Universal Skill Harvester work without hitting GitHub rate limits?

**A**: `scripts/universal_skill_harvester.py` uses a hybrid strategy:
1. **Local Heuristic Radar Cache**: Frequently analyzed repositories are indexed in `.radar_cache.json`. Repeated runs hit the cache with zero network calls.
2. **Git Trees API & Keyword Weighting**: When fetching a new repository, it queries the recursive file tree (1 API call) and runs a semantic scoring algorithm across paths matching scientific visualization keywords (`diagram`, `schematic`, `visualization`, `figure`).
3. **Token Fallback**: It automatically reads `$env:GITHUB_TOKEN` or `$env:GH_TOKEN` if present, raising rate limits from 60 to 5,000 requests per hour.

---

### Q5: How do I consume the generated prompts across different platforms?

**A**: Output prompts located in `sci-plot-output/prompts/` are platform-agnostic:
- **ChatGPT / DALL-E 3**: Copy the `▶ English Prompt` block verbatim into ChatGPT.
- **Midjourney**: Type `/imagine` and paste the English prompt.
- **Doubao / Qwen / Tongyi**: Paste either the English or Chinese prompt for conceptual brainstorming.
- **Stable Diffusion / ComfyUI / Flux**: Paste into the positive prompt input; copy negative constraints into the negative prompt input.
- **SVG / HTML / Matplotlib / Origin**: Paste the layout block and flow hierarchy into an AI coding assistant to compile editable vector or interactive charts.

---

### Q6: Can sci-plot process non-LaTeX inputs?

**A**: Yes. While LaTeX (`.tex`) sources provide the highest fidelity for equation and module extraction, sci-plot natively supports:
- Markdown (`.md`) technical documents and specifications;
- Direct PDF / text excerpts pasted into chat;
- Source code (e.g., PyTorch model architectures, Python class definitions, pipeline scripts);
- ArXiv links or paper identifiers (e.g., `1706.03762`).

