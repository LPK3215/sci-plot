"""
generate_banner.py — Generate the branded SVG banner for the sci-plot README.

Visual language: editorial / publication-grade, aligned with
docs/project_overview/index.html (light paper surface, ink serif headings,
one blue accent, hairline rules, no glow or rainbow gradients).

Usage:
    python scripts/visualization/generate_banner.py

Output:
    docs/assets/banner.svg

The version token in the badge is read from CHANGELOG.md, so a release bump
keeps the banner in sync. This script is the single source of truth for the
banner; do not hand-edit docs/assets/banner.svg.
"""

import os
import re

BANNER_WIDTH = 1280
BANNER_HEIGHT = 380


def get_project_version(root_dir):
    changelog_path = os.path.join(root_dir, "CHANGELOG.md")
    if os.path.exists(changelog_path):
        with open(changelog_path, "r", encoding="utf-8") as f:
            match = re.search(r"##\s*\[(\d+\.\d+\.\d+)\]", f.read())
            if match:
                return f"v{match.group(1)}"
    return "v1.2.0"


def generate_banner_svg(version="v1.2.0"):
    W, H = BANNER_WIDTH, BANNER_HEIGHT
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">
<title>Sci-Plot — Portable Prompt Compiler for AI Skills</title>
<defs>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0 L0 0 0 40" fill="none" stroke="#1E4FD8" stroke-width="1" stroke-opacity="0.045"/>
  </pattern>
  <filter id="shadow" x="-5%" y="-10%" width="110%" height="125%">
    <feDropShadow dx="0" dy="6" stdDeviation="14" flood-color="#0E1A2B" flood-opacity="0.09"/>
  </filter>
</defs>

<!-- Paper surface -->
<rect width="{W}" height="{H}" fill="#F7F8FA"/>
<rect width="{W}" height="{H}" fill="url(#grid)"/>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" fill="none" stroke="#E1E7EE" stroke-width="1"/>

<!-- Brand badge -->
<g>
  <rect x="64" y="36" width="266" height="30" rx="15" fill="#EDF2FF" stroke="#D9E3FF" stroke-width="1"/>
  <circle cx="82" cy="51" r="4" fill="#16A34A"/>
  <text x="96" y="55" font-family="Consolas, 'SFMono-Regular', Menlo, monospace" font-size="10.5" font-weight="600" fill="#1E4FD8" letter-spacing="0.6">AI SKILL &#183; {version} &#183; MIT LICENSE</text>
</g>

<!-- Brand mark + title -->
<g>
  <rect x="64" y="86" width="44" height="44" rx="10" fill="#1E4FD8"/>
  <path d="M74 116 L84 104 L92 110 L104 94" fill="none" stroke="#FFFFFF" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="104" cy="94" r="2.6" fill="#FFFFFF"/>
  <text x="122" y="122" font-family="Cambria, Georgia, 'Times New Roman', serif" font-size="52" font-weight="600" fill="#0E1A2B" letter-spacing="-1.6">Sci-Plot</text>
  <text x="330" y="116" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif" font-size="21" font-weight="500" fill="#435266">— Portable Prompt Compiler for AI Skills</text>
</g>

<!-- Value proposition -->
<text x="64" y="162" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif" font-size="15" fill="#0E1A2B" font-weight="600">Any skill + your topic &#8594; auditable .md prompt assets &#183; Zero runtime lock-in</text>
<text x="64" y="188" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif" font-size="13" fill="#6B7A8D">No paid coding agent, no API keys, no special CLI. Consume the output anywhere, even offline.</text>

<!-- Figure plate (right) -->
<g filter="url(#shadow)">
  <rect x="838" y="36" width="378" height="176" rx="9" fill="#FFFFFF" stroke="#E1E7EE" stroke-width="1"/>
</g>
<rect x="838" y="36" width="378" height="30" rx="9" fill="#FCFDFE"/>
<path d="M838 66 L1216 66" stroke="#E1E7EE" stroke-width="1"/>
<text x="852" y="55" font-family="Consolas, 'SFMono-Regular', Menlo, monospace" font-size="9.5" fill="#6B7A8D">sci-plot-output / figure-01.svg</text>
<rect x="1128" y="42" width="74" height="18" rx="4" fill="#EDF2FF" stroke="#D9E3FF" stroke-width="1"/>
<text x="1165" y="54.5" font-family="Consolas, 'SFMono-Regular', Menlo, monospace" font-size="8" fill="#1E4FD8" text-anchor="middle">PAPER-FIGURE</text>

<!-- mini chart -->
<g stroke="#E9EDF3" stroke-width="1">
  <path d="M862 84 H1052 M862 110 H1052 M862 136 H1052 M862 162 H1052"/>
  <path d="M862 84 V162 M910 84 V162 M957 84 V162 M1005 84 V162 M1052 84 V162"/>
</g>
<path d="M862 84 V162 H1052" fill="none" stroke="#94A3B8" stroke-width="1.1"/>
<path d="M862 156 L885 148 L910 132 L934 122 L957 110 L981 101 L1005 92 L1029 86 L1052 79 L1052 162 L862 162 Z" fill="#1E4FD8" fill-opacity="0.07"/>
<polyline points="862,156 885,148 910,132 934,122 957,110 981,101 1005,92 1029,86 1052,79" fill="none" stroke="#1E4FD8" stroke-width="2.2" stroke-linejoin="round"/>
<polyline points="862,160 885,155 910,146 934,138 957,130 981,122 1005,114 1029,107 1052,100" fill="none" stroke="#0B8A78" stroke-width="1.8" stroke-dasharray="5 4" stroke-linejoin="round"/>
<g font-family="Consolas, Menlo, monospace" font-size="7.5" fill="#6B7A8D">
  <text x="1070" y="98">Sci-Plot</text>
  <text x="1070" y="114">Baseline</text>
</g>
<path d="M1060 94 H1066" stroke="#1E4FD8" stroke-width="2"/>
<path d="M1060 110 H1066" stroke="#0B8A78" stroke-width="2" stroke-dasharray="3 2"/>
<!-- status chip -->
<rect x="1066" y="130" width="136" height="20" rx="4" fill="#E8F5F2" stroke="#CBE9E1" stroke-width="1"/>
<circle cx="1078" cy="140" r="3" fill="#0B8A78"/>
<text x="1087" y="143" font-family="Consolas, Menlo, monospace" font-size="8" fill="#0B8A78">6/6 QA GATES PASSED</text>
<text x="852" y="192" font-family="Cambria, Georgia, serif" font-size="10.5" font-style="italic" fill="#6B7A8D">Figure 1. Method overview, compiled from ./paper.pdf.</text>

<!-- Feature chips -->
<g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif" font-size="12.5" font-weight="600" fill="#1E2D42">
  <g>
    <rect x="64" y="238" width="216" height="44" rx="7" fill="#FFFFFF" stroke="#E1E7EE" stroke-width="1"/>
    <rect x="78" y="255" width="6" height="10" rx="2" fill="#1E4FD8"/>
    <text x="94" y="264">Dual-Track Rules Pool</text>
  </g>
  <g>
    <rect x="298" y="238" width="216" height="44" rx="7" fill="#FFFFFF" stroke="#E1E7EE" stroke-width="1"/>
    <rect x="312" y="255" width="6" height="10" rx="2" fill="#0B8A78"/>
    <text x="328" y="264">Scope Isolation</text>
  </g>
  <g>
    <rect x="532" y="238" width="216" height="44" rx="7" fill="#FFFFFF" stroke="#E1E7EE" stroke-width="1"/>
    <rect x="546" y="255" width="6" height="10" rx="2" fill="#B4690E"/>
    <text x="562" y="264">Universal Radar Harvester</text>
  </g>
  <g>
    <rect x="766" y="238" width="216" height="44" rx="7" fill="#FFFFFF" stroke="#E1E7EE" stroke-width="1"/>
    <rect x="780" y="255" width="6" height="10" rx="2" fill="#1E4FD8"/>
    <text x="796" y="264">4-Tier Quality Gate</text>
  </g>
  <g>
    <rect x="1000" y="238" width="216" height="44" rx="7" fill="#FFFFFF" stroke="#E1E7EE" stroke-width="1"/>
    <rect x="1014" y="255" width="6" height="10" rx="2" fill="#0B8A78"/>
    <text x="1030" y="264">Zero Lock-in</text>
  </g>
</g>

<!-- Footer -->
<path d="M64 322 H1216" stroke="#E1E7EE" stroke-width="1"/>
<text x="64" y="345" font-family="Consolas, 'SFMono-Regular', Menlo, monospace" font-size="10.5" fill="#6B7A8D">github.com/LPK3215/sci-plot</text>
<text x="1216" y="345" font-family="Consolas, 'SFMono-Regular', Menlo, monospace" font-size="10.5" fill="#6B7A8D" text-anchor="end">PORTABLE PROMPT ASSETS  &#183;  docs/assets/banner.svg</text>
</svg>
"""


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(os.path.dirname(script_dir))
    assets_dir = os.path.join(root_dir, "docs", "assets")
    os.makedirs(assets_dir, exist_ok=True)

    version = get_project_version(root_dir)
    svg_content = generate_banner_svg(version=version)

    output_path = os.path.join(assets_dir, "banner.svg")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"[*] Generated editorial banner SVG ({version}) -> {output_path}")


if __name__ == "__main__":
    main()
