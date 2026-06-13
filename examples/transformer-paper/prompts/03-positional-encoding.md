# Page 3: Positional Encoding

## Metadata
- **Type**: mechanism-detail
- **Style**: paper-figure
- **Language**: en
- **Aspect Ratio**: 2:3

## Composition Description
Portrait layout with three horizontal zones flowing top to bottom: token embedding input at top, positional encoding generation in the middle, and element-wise addition at the bottom. The middle section is the visual focus, showing sinusoidal wave curves side by side for even and odd dimensions. A small color-coded example on the right demonstrates how positions 0–3 are encoded as distinct wave patterns. Clear arrows guide the flow downward through each stage.

## Content Elements
- Top: Token embedding vector box (512-dim)
- Middle (main focus):
  - Positional encoding vector (512-dim)
  - Side-by-side sinusoidal wave curves: sine wave for even indices (2i), cosine wave for odd indices (2i+1)
  - Formula annotations: PE(pos, 2i) = sin(pos / 10000^(2i/d_model)), PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
  - Wavelength varies across dimensions (short for low indices, long for high indices)
- Bottom: Element-wise addition (embedding + PE) → Final input representation (512-dim)
- Right side small example: positions 0, 1, 2, 3 encoded as color-coded wave pattern strips
- Dimension annotations: d_model = 512

---

## ▶ English Prompt (Core — Copy Directly)

A technical diagram explaining positional encoding in the Transformer architecture, paper figure style. White background. Portrait 2:3 aspect ratio.

Top section (input):
- Large box at top labeled "Token Embedding (512-dim)"
- Single downward arrow to the addition step at the bottom

Middle section (positional encoding — main visual focus, occupies ~50% of page height):
- Label: "Positional Encoding (512-dim)"
- Two sinusoidal wave curves drawn side by side:
  - Left wave: sine curve, labeled "Even indices (2i)"
  - Right wave: cosine curve, labeled "Odd indices (2i+1)"
  - Both waves show 3-4 complete cycles, with wavelength increasing from top to bottom (representing low to high dimension indices)
  - Short wavelength at top (low dimensions), long wavelength at bottom (high dimensions)
- Formula displayed prominently below the waves:
  - "PE(pos, 2i) = sin(pos / 10000^(2i/d))"
  - "PE(pos, 2i+1) = cos(pos / 10000^(2i/d))"
- Small example panel on the right side:
  - Title: "Positions 0–3"
  - Four horizontal color-coded strips, each representing one position
  - Strip 0: unique wave pattern
  - Strip 1: shifted wave pattern
  - Strip 2: further shifted pattern
  - Strip 3: most shifted pattern
  - Strips use light blue to white gradient shading to show encoding values

Bottom section (addition):
- Circle or box labeled "+" with two incoming arrows (one from embedding, one from PE)
- Downward arrow to final box: "Final Input Representation (512-dim)"

Color scheme:
- Boxes: white fill with dark gray borders
- Sine wave: blue line
- Cosine wave: orange line
- Position strips: light blue shading
- Formula text: dark gray, slightly larger font
- Arrows: medium gray, 2px width
- Addition symbol: bold, centered

Visual style: Clean, professional paper figure. No 3D effects. No decorative patterns. Vector-feel modules. The sinusoidal waves should be the visual centerpiece of this diagram, clearly showing how different positions and dimensions get unique encoding values.

---

## Copy to Image Generation Tool
Copy the "English Prompt" section above in full to the input box of the following tools:
- **ChatGPT (DALL-E)**: Paste directly
- **Doubao**: Text-to-image entry
- **Qwen (Tongyi Wanxiang)**: Text-to-image entry
- **Midjourney**: Shorten to key elements before pasting after `/imagine` (Midjourney works best with concise prompts under ~60 words)
