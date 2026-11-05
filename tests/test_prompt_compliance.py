"""
test_prompt_compliance.py — 针对输出提示词包的专业质检 Linter 与合规性测试。
确保生成的每一个 Prompt 文件均严格遵循防翻车红线与出版级模板。
"""

import glob
import os
import re
import sys

FORBIDDEN_3D_PATTERNS = [
    r"\b3d\s+sphere\b",
    r"\bphotorealistic\b",
    r"\brender\s+in\s+3d\b",
    r"\boctane\s+render\b",
    r"\bunreal\s+engine\b",
    r"\bcinema\s*4d\b",
    r"\braytracing\b",
]


def check_deliverable_directory(target_dir):
    print(f"--- Checking Deliverables in: {target_dir} ---")
    assert os.path.isdir(target_dir), f"Directory does not exist: {target_dir}"

    analysis_file = os.path.join(target_dir, "analysis.md")
    plan_file = os.path.join(target_dir, "figure-plan.md")
    readme_file = os.path.join(target_dir, "README.md")
    prompts_dir = os.path.join(target_dir, "prompts")

    assert os.path.exists(analysis_file), f"Missing analysis.md in {target_dir}"
    assert os.path.exists(plan_file), f"Missing figure-plan.md in {target_dir}"
    assert os.path.exists(readme_file), f"Missing README.md in {target_dir}"
    assert os.path.isdir(prompts_dir), f"Missing prompts/ directory in {target_dir}"

    prompt_files = glob.glob(os.path.join(prompts_dir, "*.md"))
    assert len(prompt_files) >= 1, f"No .md prompt files found in {prompts_dir}"
    print(f"  [PASS] Directory structure valid ({len(prompt_files)} prompt files found)")

    for pf in prompt_files:
        check_single_prompt_file(pf)


def check_single_prompt_file(file_path):
    filename = os.path.basename(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 结构与元数据校验
    assert "## Metadata" in content, f"{filename} missing ## Metadata"
    assert "**Type**:" in content or "- Type:" in content, f"{filename} missing Type in metadata"
    assert "**Aspect Ratio**:" in content or "- Aspect Ratio:" in content or "Ratio" in content, f"{filename} missing Aspect Ratio"
    assert "## Composition Description" in content or "构图" in content, f"{filename} missing Composition Description"
    assert "## Content Elements" in content or "元素" in content, f"{filename} missing Content Elements"
    assert "English Prompt" in content or "Prompt" in content, f"{filename} missing English Prompt section"

    # 2. 提取核心 Prompt 文本
    prompt_match = re.search(r"##\s*▶?\s*English Prompt.*?\n(.*?)(?=\n##|\Z)", content, re.DOTALL | re.IGNORECASE)
    assert prompt_match, f"{filename} cannot extract English Prompt body"
    prompt_body = prompt_match.group(1).lower()

    # 3. 负向禁止项检查（防 3D 浮夸风）
    for pattern in FORBIDDEN_3D_PATTERNS:
        match = re.search(pattern, prompt_body)
        assert not match, f"{filename} violates negative rule! Found forbidden 3D keyword: {match.group(0)}"

    # 4. 必须包含防翻车约束或学术修饰词
    has_academic_anchor = any(
        term in prompt_body
        for term in ["scientific", "figure", "diagram", "vector", "academic", "minimal", "flat", "technical"]
    )
    assert has_academic_anchor, f"{filename} missing academic/vector anchor words in prompt body"

    print(f"  [PASS] Verified prompt compliance: {filename}")


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("=== Running Prompt Quality & Compliance Tests ===")

    # 1. 校验刚刚 LoRA 测试生成的交付物
    output_dir = os.path.join(root, "sci-plot-output")
    if os.path.exists(output_dir):
        check_deliverable_directory(output_dir)

    # 2. 校验内置示例 transformer-paper
    example_dir = os.path.join(root, "examples", "transformer-paper")
    if os.path.exists(example_dir):
        check_deliverable_directory(example_dir)

    print("ALL PROMPT COMPLIANCE TESTS PASSED!\n")

