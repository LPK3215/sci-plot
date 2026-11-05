# AUTO-CLAUDE-CODE-RESEARCH-IN-SLEEP — 智能自适应下载绘图规范 (Downloaded Rule)

> **官方来源仓库**: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep  
> **雷达自动嗅探路径**: `skills/proof-orchestrator/references/dispatch-prompts.md` (源文件大小: 7841 字节)  
> **抓取机制**: 通用仓库递归雷达扫描与自适应定位 (Universal Radar Discovery)  
> **状态**: 本地已固化（永久离线可用，支持二次编辑）

---

## 1. 风格定位与视觉特征
- **来源项目**: wanshuiyin/Auto-claude-code-research-in-sleep
- **发现核心组件**: 自动嗅探自 `skills/proof-orchestrator/references/dispatch-prompts.md`，专精于科研图表与学术流程图的规范化构建。

---

## 2. 画布与排版约束
- **背景**: 纯白 (#FFFFFF) 或 浅冷灰 (#F8FAFC)
- **排版比例**: 2:3 (方法机制图) / 16:9 (全景流程图)
- **线框规范**: 核心流加粗 1.5-2px，辅助线 0.75-1px，结构连接一律正交走线，箭头清晰。

---

## 3. 色彩限制 (≤3色)
- **主结构线框**: 深色墨水墨线 (#1A1A1A / #334155)
- **唯一强调色**: 依据领域选取 1 种强调色（如科技蓝 #0284C7 或 #2563EB）高亮核心创新点
- **背景填充**: 浅灰/纯白底色，严禁杂乱渐变

---

## 4. 专属领域词典 (Domain Vocabulary)
- `Source Context`: Discovered from `skills/proof-orchestrator/references/dispatch-prompts.md`
- `Key Concepts`: Extracted from authentic repository guidelines

---

## 5. 核心英文提示词片段 (Prompt Snippet)
```text
Scientific vector schematic in Auto-claude-code-research-in-sleep style, pure white background, flat 2D layout. Precise line weights, restrained theme accent, clean sans-serif typography, crisp directional connectors, no 3D effects, no drop shadows, no glossy textures.
```

---

## 附录：嗅探到的原始规范节选 (Source Excerpt)
```markdown
# Local-First Proof Pipeline Prompts

Use these templates for the local-first pipeline. Manual GPT Pro handoff is the
default escalation route. Do not operate a browser or spend API credit unless
the user explicitly asks executor to do so for the current run.

## Local Proof Prompt

```text
Use $proof-orchestrator to attempt this proof locally before preparing any GPT
Pro handoff.

Run directory:
prompts/<YYMMDDHH-num>/

Target:
[exact theorem, lemma, disproof, or diagnosis]

Inputs:
- [source path]: [authoritative role]

Requirements:
- Check assumptions, domains, boundary cases, quantifiers, and imported theorem
  hypotheses.
- Write the complete attempt to local-proof.md.
- If it succeeds, audit correctness and edit the proof for clarity and minimal
  notation before writing final.md.
- Apply references/notation-audit.md and record its required metrics in
  audit.md. Undefined symbols and symbol collisions must be zero.
- If induction is used, expose the base case, induction hypothesis, and
  induction step wherever needed for verification.
- Present every nontrivial derivation top-down: state the target, justify its
  reduction to immediate subgoals, derive each subgoal from named inputs, and
  recombine them to close the target.
- If it fails, isolate the smallest unresolved obligation. Do not call GPT Pro
  or create remote project state.
```

## Continuation Prompt

```text
Use $proof-orchestrator to continue this proof project locally from the prior
run.

Prior run directory:
prompts/<YYMMDDHH-num>/

Continuation request:
[one narrow obligation]

Requirements:
- Read the prior final.md, audit.md, local-proof.md, codex-ledger.md,
  source-manifest.md, handoff.md, and any next/redo/continuation files that
  exist.
- Create a new run directory and record the prior run ID and exact files read.
- Inherit only audited claims; treat raw GPT Pro output as evidence.
- Reuse stable local sources without overwriting the prior run.
- Attempt the current obligation locally before preparing a new GPT Pro prompt.
- If escalation is still needed, use a new browser prompt and a fresh GPT Pro
  conversation.
```

## Manual GPT Pro Handoff Prompt

```text
Use $proof-orchestrator to prepare a manual GPT Pro handoff for the blocker in
this run. Do not call GPT Pro, control a browser, upload files, or spend API
credit.

Run directory:
prompts/<YYMMDDHH-num>/

Required inputs:
- local-proof.md
- task.md and materials.md when present
- relevant files under sources/

Outputs:
- source-manifest.md
- browser-prompt.md
- handoff.md

Requirements:
- Ask only for the smallest unresolved proof obligation.
- Give every source a stable browser-visible filename and state whether it must
  be uploaded separately.
- Make browser-prompt.md the exact self-contained text the user can paste. Keep
  local paths and route bookkeeping out of it.
- Ask GPT Pro to label added assumptions, imported results, conjectures, and
  unsupported claims.
- Require END_GPT_PRO_OUTPUT as the final output line.
- In handoff.md, list the upload order, then the prompt-copy step, then where the
  user should return or save the output.
- Mark READY_FOR_MANUAL_GPT_PRO and wait for the user.
```

## Optional DeepSeek Second-Opinion Prompt

Use this template only when the user explicitly requests DeepSeek review or an
independent second opinion for the current proof run:

```text
Use $proof-orchestrator's optional DeepSeek audit branch for this run.

Run directory:
prompts/<YYMMDDHH-num>/

Inputs:
- task.md and materials.md
- local-proof.md
- authoritative files under sources/

Requirements:
- Complete the local obligation ledger first.
- Read references/proof-audit-rubric.md and references/deepseek-routing.md.
- Use only the declared llm-chat DeepSeek route; do not invent credentials or
  silently substitute another remote model.
- Save raw reviewer output to deepseek-review.md.
- Verify issue locations and counterexamples locally before integrating them.
- Write the checked verdict to audit.md using
```
