# Page 1: Transformer Architecture Overview

## Metadata
- **Type**: method-overview
- **Style**: paper-figure
- **Language**: en
- **Aspect Ratio**: 2:3

## Composition Description
Portrait layout with encoder stack on the left and decoder stack on the right. Input flows from bottom to top. Clear arrows connect encoder output to decoder cross-attention. Six identical layers stacked vertically in each column. Annotations positioned close to modules without overlapping.

## Content Elements
- Input embedding layer at bottom left (with + positional encoding)
- Encoder stack: 6 layers, each containing multi-head attention → add & norm → FFN → add & norm
- Decoder stack: 6 layers, each containing masked attention → cross-attention → FFN
- Output embedding at bottom right
- Thick arrows showing main data flow
- Dimension annotations: d_model=512, h=8, d_ff=2048
- Module labels in sans-serif font
- Residual connections shown as thin bypass arrows

---

## ▶ English Prompt (Core — Copy Directly)

A clean technical diagram of the Transformer architecture in paper figure style. White background. Portrait 2:3 aspect ratio.

Layout: Two vertical stacks side by side. Left stack is the Encoder (6 layers), right stack is the Decoder (6 layers).

Encoder stack (left):
- Bottom: "Input Embedding + Positional Encoding" box
- Six identical layers stacked vertically, each layer contains:
  - Rounded rectangle labeled "Multi-Head Attention"
  - Small box "Add & Norm"
  - Rounded rectangle labeled "Feed Forward"
  - Small box "Add & Norm"
- Thin arrows showing residual connections bypassing each sub-layer
- Upward arrow flow from bottom to top

Decoder stack (right):
- Bottom: "Output Embedding + Positional Encoding" box
- Six identical layers stacked vertically, each layer contains:
  - Rounded rectangle labeled "Masked Multi-Head Attention"
  - Small box "Add & Norm"
  - Rounded rectangle labeled "Cross-Attention" (with arrow coming from encoder)
  - Small box "Add & Norm"
  - Rounded rectangle labeled "Feed Forward"
  - Small box "Add & Norm"
- Thin arrows showing residual connections
- Upward arrow flow from bottom to top
- Top: "Linear + Softmax" box → "Output Probabilities"

Key arrows:
- Thick blue arrow from encoder top to decoder cross-attention layers
- Medium black arrows showing main data flow direction (upward)
- Thin gray arrows showing residual connections

Annotations:
- Near input: "d_model = 512"
- Near attention: "h = 8 heads"
- Near FFN: "d_ff = 2048"

Visual style: Clean vector-feel modules with rounded corners. Black text on white background. Only use blue for the encoder-to-decoder connection, gray for residual connections, black for primary boxes. No gradients. No decorative elements. Professional paper figure aesthetic.

---

## Copy to Image Generation Tool
Copy the "English Prompt" section above in full to the input box of the following tools:
- **ChatGPT (DALL-E)**: Paste directly
- **Doubao**: Text-to-image entry
- **Qwen (Tongyi Wanxiang)**: Text-to-image entry
- **Midjourney**: Shorten to key elements before pasting after `/imagine` (Midjourney works best with concise prompts under ~60 words)
