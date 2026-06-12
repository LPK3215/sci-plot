# Page Composition & Role Definitions

These are not fixed templates, but composition roles to use when writing prompts. Choose a page role first, then write the prompt.

---

## Page Role Definitions

| Role | Purpose | Composition | In-Image Text Volume |
|------|------|------|------------|
| `cover` | Cover page — convey theme and tone at a glance | Large title + visual anchor + minimal meta info | Title: 1 line |
| `method-overview` | Method overview | Input → Core modules → Output | 5-9 short labels |
| `mechanism-detail` | Single core mechanism breakdown | Local zoom-in, numbered steps, short labels | 6-12 short labels |
| `comparison` | New vs. old method/approach comparison | Left-right comparison, highlighted differences | 4-8 short labels |
| `evidence` | Experimental or data evidence | Large number + small chart + explanatory labels | 1 large number + 2-4 short explanations |
| `architecture` | System/module architecture diagram | Layered/grouped, dependency arrows | 4-8 module labels |
| `data-flow` | Data flow/pipeline diagram | Data source→process→store→consume | 4-8 node labels |
| `takeaway` | Conclusion and key points | 1 conclusion sentence + 3 key points | 1 main sentence + 3 short points |

---

## Recommended Pacing

### 4-6 Page Recommended Structure
```
cover → method-overview → mechanism-detail → comparison/evidence → takeaway
```

### 6-10 Page Recommended Structure
```
cover → method-overview → mechanism-detail (×2-3) → evidence → comparison → takeaway
```

---

## Composition Rules

### Cover
- Minimal text, strong main visual
- Title centered or upper-aligned
- Visual anchor (abstract/figurative element related to the paper's core concept)

### Method Overview
- Central main diagram must occupy 65%-80% of the page
- Input on left/top, output on right/bottom
- Core modules in center, connection lines clear
- Key innovation points marked with emphasis color/bold lines

### Mechanism Detail
- Only one mechanism per page
- Zoom in on key areas locally
- Step-by-step unfolding (numbered ① ② ③)
- Supplement with dimension info and formula snippets

### Comparison
- Left-right structure must be symmetric
- Differences must stand out (different colors / dashed box marking diff areas)
- Title above, conclusion below

### Evidence / Data
- Numbers must be large (visual focus)
- Explanations must be short (no long paragraphs)
- Can use simplified small charts as aids

### Takeaway
- Do NOT introduce new concepts
- Return to the question posed on the cover page to close the loop

---

## Whitespace Control

- Cover and section divider pages can have more whitespace (30%-40%) for breathing room
- Method overview main diagram should occupy 65%-80%
- Mechanism detail main diagram should occupy 75%-85%
- Do NOT allow large meaningless blank areas (looking unfinished)
- Whitespace serves visual hierarchy, not laziness

---

## Text Density Recommendations

| Page Type | Text Volume | Specific Limit |
|---------|--------|---------|
| cover | Minimal | Title 1 line ≤16 Chinese chars, subtitle 1 line |
| method-overview | Medium | 5-9 short labels, each ≤8 Chinese chars |
| mechanism-detail | Medium-high | 6-12 short labels, each ≤8 Chinese chars |
| comparison | Medium | 3-5 labels per side |
| evidence | Low | 1 large number + 2-4 short explanations |
| architecture | Medium | 4-8 module labels |
| takeaway | Low | 1 conclusion sentence + 3 short points |

If text exceeds limits, prioritize splitting pages rather than forcing the image model to render long paragraphs.
