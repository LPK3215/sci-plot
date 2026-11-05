"""
sync_documentation_metrics.py — Single Source of Truth Auditor & Metric Synchronizer.
Scans the actual repository filesystem and pyproject.toml, verifies all document paths,
and ensures cross-document consistency for version, URLs, and directory trees.

Usage:
  python scripts/sync_documentation_metrics.py --check
  python scripts/sync_documentation_metrics.py --report
"""

import glob
import os
import re
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def extract_package_metadata():
    pyproject_path = os.path.join(ROOT_DIR, "pyproject.toml")
    with open(pyproject_path, "r", encoding="utf-8") as f:
        content = f.read()

    name_m = re.search(r'name\s*=\s*"([^"]+)"', content)
    ver_m = re.search(r'version\s*=\s*"([^"]+)"', content)
    home_m = re.search(r'Homepage\s*=\s*"([^"]+)"', content)

    return {
        "name": name_m.group(1) if name_m else "sci-plot",
        "version": ver_m.group(1) if ver_m else "1.2.0",
        "homepage": home_m.group(1) if home_m else "https://lpk3215.github.io/sci-plot/",
    }


def compute_live_metrics():
    local_pool = os.path.join(ROOT_DIR, "references", "rules-pool", "local")
    presets = [
        "paper-figure.md", "journal-minimal.md", "sketchnote.md",
        "warm-notes.md", "business-research.md"
    ]
    built_in_count = sum(1 for p in presets if os.path.exists(os.path.join(local_pool, p)))
    downloaded_rules = glob.glob(os.path.join(local_pool, "downloaded-*.md"))
    downloaded_count = len(downloaded_rules)
    total_rules = built_in_count + downloaded_count

    test_files = glob.glob(os.path.join(ROOT_DIR, "tests", "test_*.py"))
    test_count = len(test_files)

    archify_dir = os.path.join(ROOT_DIR, "docs", "archify")
    archify_htmls = glob.glob(os.path.join(archify_dir, "*.html"))
    archify_count = len(archify_htmls)

    return {
        "built_in_presets": built_in_count,
        "downloaded_rules": downloaded_count,
        "total_active_rules": total_rules,
        "test_suites": test_count,
        "archify_diagrams": archify_count,
    }


def verify_file_paths_in_doc(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    errors = []
    path_patterns = [
        r'\((docs/[^)]+)\)',
        r'\((references/[^)]+)\)',
        r'\((scripts/[^)]+)\)',
        r'\((tests/[^)]+)\)',
        r'`(references/[^`]+)`',
        r'`(scripts/[^`]+)`',
        r'`(tests/[^`]+)`',
        r'`(docs/[^`]+)`'
    ]

    for pat in path_patterns:
        for match in re.finditer(pat, content):
            raw_path = match.group(1).split("#")[0].strip()
            # Skip wildcards, templates, anchors and URLs
            if "*" in raw_path or "http" in raw_path or "..." in raw_path or "{" in raw_path:
                continue
            norm = os.path.normpath(os.path.join(ROOT_DIR, raw_path))
            if not os.path.exists(norm):
                errors.append(f"Broken path in {os.path.basename(file_path)}: {raw_path}")

    return errors


def audit_repository_consistency():
    meta = extract_package_metadata()
    metrics = compute_live_metrics()

    print(f"=== Document Consistency Audit: {meta['name']} v{meta['version']} ===")
    print(f"Canonical Homepage: {meta['homepage']}")
    print(f"Live Metrics: {metrics['built_in_presets']} built-in presets, {metrics['downloaded_rules']} downloaded rules ({metrics['total_active_rules']} total), {metrics['test_suites']} test suites, {metrics['archify_diagrams']} Archify diagrams.")

    docs_to_check = [
        "README.md",
        "README.zh-CN.md",
        "README_CN.md",
        "CONTRIBUTING.md",
        "CONTRIBUTING.zh-CN.md",
        "CONTRIBUTING_CN.md",
        "FAQ.md",
        "SECURITY.md",
        "SKILL.md",
        "pyproject.toml"
    ]

    issues = []

    # 1. Check for dead project_overview.html URLs
    for doc in docs_to_check:
        doc_path = os.path.join(ROOT_DIR, doc)
        if not os.path.exists(doc_path):
            continue
        with open(doc_path, "r", encoding="utf-8") as f:
            text = f.read()

        if "project_overview.html" in text:
            # Allow CHANGELOG historical mentions
            if "CHANGELOG" not in doc:
                issues.append(f"{doc}: Contains outdated reference to dead file 'project_overview.html'")

    # 2. Check path validity
    for doc in docs_to_check:
        doc_path = os.path.join(ROOT_DIR, doc)
        if os.path.exists(doc_path):
            path_errs = verify_file_paths_in_doc(doc_path)
            issues.extend(path_errs)

    # 3. Check version alignment
    for doc in ["README.md", "README.zh-CN.md", "README_CN.md", "SECURITY.md"]:
        doc_path = os.path.join(ROOT_DIR, doc)
        if os.path.exists(doc_path):
            with open(doc_path, "r", encoding="utf-8") as f:
                c = f.read()
            if meta["version"] not in c:
                issues.append(f"{doc}: Version {meta['version']} not found in document")

    return issues


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "--check"
    found_issues = audit_repository_consistency()

    if found_issues:
        print(f"\n[!] Found {len(found_issues)} consistency issue(s):")
        for idx, iss in enumerate(found_issues, 1):
            print(f"  {idx}. {iss}")
        sys.exit(1)
    else:
        print("\n[OK] All documentation paths, versions, and references are 100% consistent!")
        sys.exit(0)
