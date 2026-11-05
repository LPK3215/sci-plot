# paper-figure — Paper Figure Style

Like a redesigned top-conference paper figure: professional, clear, information-dense, suitable for sharing.

## Atmosphere
- Like a method overview figure from NeurIPS / ICLR / Nature / Science
- Not a blueprint, not a poster, not a comic
- Goal: let readers understand the core method in 30 seconds

## Visual Specification

### Canvas
- White or very light gray background (#FFFFFF / #F8F9FA)
- Portrait 2:3 for mechanism breakdowns
- Landscape 16:9 or 4:3 for README hero / overview

### Graphic Elements
- Clean vector-feel modules: rounded rectangles, small matrix grids, token sequences, group boxes, numbered steps
- Precise arrows with clear directionality, main path thicker than auxiliary paths (2-3px vs 1px)
- Allow small heatmaps, curves, result thumbnails, module stacks, comparison paths

### Text
- Sans-serif font, like short labels in paper figures
- Labels must be short: module names, variable names, key operations, ≤1 line explanation
- Professional terms retain English

### Color
- Black/dark gray as primary (#1A1A1A / #333333 / #6B7280)
- Only 1-2 accent colors: choose from blue (#2563EB), orange (#D97706), teal (#0891B2), purple (#7C3AED)
- Accent colors used for core contributions, key paths, or comparisons — never for decoration

## Generation Principles
- Reference the concept of original paper framework diagrams, but must reorganize information — do not replicate the original
- Overview diagrams cover input, core modules, output, and key contributions
- Detail diagrams break down only one mechanism — do not cram everything into one page
- Result diagrams show only the most convincing single result

## English Prompt Snippet
```
Scientific paper figure style, clean white or light gray background, precise vector-style rounded modules with clear directional arrows, black/dark gray as primary color, one accent color (blue or orange) for key innovations, compact sans-serif labels, publication-quality method diagram, no 3D, no decoration, no engineering blueprint style, no large text blocks
```
