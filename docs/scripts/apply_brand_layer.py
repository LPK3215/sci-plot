"""
apply_brand_layer.py — Apply the Sci-Plot editorial brand layer to Archify HTML exports.

The five docs/archify/*.html files are generator output (~820 KB each, fully
self-contained). Rather than editing generated markup by hand, this script
injects two clearly delimited, idempotent blocks:

  1. A <style> block before </head> that re-maps the Archify theme variables
     to the Sci-Plot palette used by docs/project_overview/index.html.
  2. A compact navigation bar as the first element of <body>, giving every
     diagram a shared brand header and cross-links between the five views.

The bar is hidden in embed mode (?embed=1), which is how the project overview
page displays the diagrams. Re-run after regenerating Archify exports.

Usage:
    python docs/scripts/apply_brand_layer.py
"""

import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIFY_DIR = os.path.join(BASE, "archify")

VIEWS = [
    ("core-architecture.html", "Core Architecture", "Core"),
    ("architecture-panorama.html", "System Panorama", "Panorama"),
    ("workflow-panorama.html", "Workflow Pipeline", "Workflow"),
    ("sequence-panorama.html", "Sequence Chain", "Sequence"),
    ("dataflow-panorama.html", "Data Flow Graph", "Data Flow"),
]

CSS_START = "<!-- SCIPLOT-BRAND-CSS-START -->"
CSS_END = "<!-- SCIPLOT-BRAND-CSS-END -->"
BAR_START = "<!-- SCIPLOT-BRAND-BAR-START -->"
BAR_END = "<!-- SCIPLOT-BRAND-BAR-END -->"

STYLE = """
<style id="sciplot-brand-layer">
/* --- Sci-Plot editorial palette (classic preset) --- */
html[data-preset="classic"][data-theme="dark"]{
  --bg:#0B1728; --grid:#1B3049; --canvas-dot:rgba(155,176,198,.14);
  --text:#E9F0F8; --text-muted:#9BB0C6; --text-dim:#5D7288; --text-faint:#8AA2BA;
  --panel:#10243B; --panel-border:#20364F;
  --lane-fill:rgba(16,36,59,.55); --lane-stroke:#2C4560;
  --arrow:#7E97AF; --arrow-emphasis:#7BA5FF; --mask:#0B1728;
  --frontend-fill:rgba(91,140,255,.12);  --frontend-stroke:#7BA5FF;
  --backend-fill:rgba(11,138,120,.14);  --backend-stroke:#4CC0AC;
  --database-fill:rgba(123,151,255,.13); --database-stroke:#A8BEFF;
  --cloud-fill:rgba(180,105,14,.13);   --cloud-stroke:#E3B45F;
  --security-fill:rgba(190,90,110,.13); --security-stroke:#E798A8;
  --messagebus-fill:rgba(200,130,60,.13); --messagebus-stroke:#E8B478;
  --external-fill:rgba(120,145,170,.14); --external-stroke:#9BB0C6;
  --toolbar-bg:rgba(11,23,40,.94); --toolbar-border:#2C4560;
  --toolbar-text:#E9F0F8; --toolbar-hover:#162E49; --toolbar-menu-bg:#10243B;
}
html[data-preset="classic"][data-theme="light"]{
  --bg:#F7F8FA; --grid:#E9EDF3; --canvas-dot:rgba(107,122,141,.16);
  --text:#0E1A2B; --text-muted:#6B7A8D; --text-dim:#9AA6B5; --text-faint:#6B7A8D;
  --panel:#FFFFFF; --panel-border:#E1E7EE;
  --lane-fill:rgba(242,245,249,.7); --lane-stroke:#CBD5E0;
  --arrow:#94A3B8; --arrow-emphasis:#1E4FD8; --mask:#FFFFFF;
  --frontend-fill:rgba(30,79,216,.08);  --frontend-stroke:#1E4FD8;
  --backend-fill:rgba(11,138,120,.09);  --backend-stroke:#0B8A78;
  --database-fill:rgba(91,110,230,.09); --database-stroke:#4C5FD0;
  --cloud-fill:rgba(180,105,14,.09);   --cloud-stroke:#B4690E;
  --security-fill:rgba(190,70,95,.08); --security-stroke:#B04460;
  --messagebus-fill:rgba(200,120,40,.09); --messagebus-stroke:#A9651B;
  --external-fill:rgba(107,122,141,.1); --external-stroke:#6B7A8D;
  --toolbar-bg:rgba(255,255,255,.94); --toolbar-border:#CBD5E0;
  --toolbar-text:#1E2D42; --toolbar-hover:#FFFFFF; --toolbar-menu-bg:#FFFFFF;
}
html:not([data-embed="true"]) .header h1{
  font-family:"Cambria","Iowan Old Style",Georgia,"Times New Roman",serif;
  letter-spacing:-.02em; font-weight:600;
}

/* --- Shared diagram navigation bar --- */
.sp-bar{
  --sp-mono:Consolas,"SFMono-Regular",Menlo,monospace;
  position:relative; z-index:150; display:flex; align-items:center; gap:14px;
  min-height:54px; padding:8px 16px; margin-bottom:20px;
  background:var(--panel); border:1px solid var(--panel-border); border-radius:8px;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",Arial,sans-serif;
  color:var(--text);
}
.sp-bar *{box-sizing:border-box}
.sp-bar a{color:inherit;text-decoration:none}
.sp-brand{display:inline-flex;align-items:center;gap:9px;white-space:nowrap;flex:none}
.sp-mark{width:28px;height:28px;border-radius:7px;background:#1E4FD8;display:grid;place-items:center;flex:none}
.sp-brand b{font-size:14px;font-weight:700;letter-spacing:-.02em}
.sp-ver{font-family:var(--sp-mono);font-size:9.5px;color:#1E4FD8;background:#EDF2FF;
  border:1px solid #D9E3FF;border-radius:4px;padding:2px 6px}
html[data-theme="dark"] .sp-ver{color:#A8C4FF;background:#162C4C;border-color:#2C4560}
.sp-sep{width:1px;height:22px;background:var(--panel-border);flex:none}
.sp-views{display:flex;align-items:center;gap:3px;flex:1;min-width:0;overflow-x:auto;scrollbar-width:thin}
.sp-views a{font-size:11.5px;font-weight:550;padding:6px 10px;border-radius:5px;
  color:var(--text-muted);white-space:nowrap;transition:background .2s,color .2s}
.sp-views a:hover{background:rgba(127,160,210,.14);color:var(--text)}
.sp-views a.is-active{background:#1E4FD8;color:#fff}
.sp-back{display:inline-flex;align-items:center;gap:6px;font-size:11.5px;font-weight:600;
  color:var(--text-muted);white-space:nowrap;flex:none;padding:6px 10px;
  border:1px solid var(--panel-border);border-radius:5px}
.sp-back:hover{border-color:#1E4FD8;color:#1E4FD8}
.sp-back svg{width:13px;height:13px;stroke:currentColor;fill:none;stroke-width:1.7;
  stroke-linecap:round;stroke-linejoin:round}
html[data-embed="true"] .sp-bar{display:none !important}
@media (min-width:721px){
  html:not([data-embed="true"]) .toolbar{top:5.75rem !important}
}
@media (min-width:721px) and (max-width:900px){
  .sp-sep,.sp-views{display:none}
  .sp-bar{justify-content:space-between}
}
@media (max-width:720px){
  .sp-bar{flex-wrap:wrap;gap:8px 12px;padding:10px 12px;max-width:calc(100vw - 2rem)}
  .sp-sep{display:none}
  .sp-views{order:3;flex:1 0 100%;padding-bottom:2px}
  .sp-back{margin-left:auto}
}
@media (max-width:480px){
  .sp-ver{display:none}
  .sp-bar{padding:9px 10px}
  .sp-back-label{display:none}
  .sp-back{padding:6px 8px}
}
</style>
"""


def build_bar(current_file, title):
    links = []
    for filename, view_title, short in VIEWS:
        active = " is-active" if filename == current_file else ""
        links.append(
            f'<a href="{filename}" class="sp-view{active}"'
            + (' aria-current="page"' if active else '')
            + f' title="{view_title}">{short}</a>'
        )
    return (
        '<div class="sp-bar" role="navigation" aria-label="Sci-Plot diagram navigation">'
        '<a class="sp-brand" href="../project_overview/index.html">'
        '<span class="sp-mark"><svg width="17" height="17" viewBox="0 0 32 32" aria-hidden="true">'
        '<path d="M6 23l6-7 5 3 9-10" fill="none" stroke="#fff" stroke-width="2.8" '
        'stroke-linecap="round" stroke-linejoin="round"/><circle cx="26" cy="9" r="2.3" fill="#fff"/>'
        '</svg></span><b>Sci-Plot</b><span class="sp-ver">v1.2.0</span></a>'
        '<span class="sp-sep" aria-hidden="true"></span>'
        '<nav class="sp-views" aria-label="Architecture views">' + "".join(links) + '</nav>'
        '<a class="sp-back" href="../project_overview/index.html#architecture" aria-label="Back to project overview">'
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h16M14 6l6 6-6 6"/></svg>'
        '<span class="sp-back-label">Overview</span></a></div>'
    )


def strip_existing(text):
    text = re.sub(
        r'\n?' + re.escape(CSS_START) + r'.*?' + re.escape(CSS_END) + r'\n?',
        '\n', text, flags=re.S,
    )
    text = re.sub(
        r'\n?' + re.escape(BAR_START) + r'.*?' + re.escape(BAR_END) + r'\n?',
        '\n', text, flags=re.S,
    )
    return text


def main():
    for filename, title, _ in VIEWS:
        path = os.path.join(ARCHIFY_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        text = strip_existing(text)

        css_block = f"{CSS_START}\n{STYLE.strip()}\n{CSS_END}"
        bar_block = f"{BAR_START}\n{build_bar(filename, title)}\n{BAR_END}"

        if "</head>" not in text:
            raise RuntimeError(f"missing </head>: {filename}")
        text = text.replace("</head>", css_block + "\n</head>", 1)

        if not re.search(r"<body[^>]*>", text):
            raise RuntimeError(f"missing <body>: {filename}")
        text = re.sub(
            r"<body[^>]*>",
            lambda m: m.group(0) + "\n" + bar_block,
            text,
            count=1,
        )

        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Branded: {filename}  ({len(text.encode('utf-8')):,} bytes)")


if __name__ == "__main__":
    main()
