"""
test_rules_pool_integrity.py — 校验核心规范库、本地规范池与云端通道的完整性与格式规范。
"""

import os
import re
import sys


def test_core_base_rules(project_root):
    base_rules_path = os.path.join(project_root, "references", "core", "base-rules.md")
    assert os.path.exists(base_rules_path), f"Missing core base-rules: {base_rules_path}"
    
    with open(base_rules_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 必须包含关键的底座物理法则定义
    assert "图像物理规格" in content, "base-rules 缺少图像物理规格定义"
    assert "文字标注防乱码红线" in content, "base-rules 缺少文字标注防乱码红线"
    assert "色彩克制法则" in content, "base-rules 缺少色彩克制法则"
    assert "全局绝对禁止项" in content, "base-rules 缺少全局绝对禁止项"
    assert "Prompt Template" in content or "模版" in content, "base-rules 缺少输出模版定义"
    print("  [PASS] test_core_base_rules")


def test_local_rules_pool(project_root):
    local_pool_dir = os.path.join(project_root, "references", "rules-pool", "local")
    assert os.path.isdir(local_pool_dir), f"Missing local rules pool: {local_pool_dir}"
    
    expected_styles = [
        "paper-figure.md",
        "journal-minimal.md",
        "sketchnote.md",
        "warm-notes.md",
        "business-research.md",
    ]
    for style_file in expected_styles:
        style_path = os.path.join(local_pool_dir, style_file)
        assert os.path.exists(style_path), f"Missing expected local style: {style_file}"
        with open(style_path, "r", encoding="utf-8") as f:
            c = f.read()
            assert len(c) > 200, f"Style file {style_file} is too short or empty"
            # 必须包含 Prompt Snippet 关键词
            assert "Prompt" in c or "prompt" in c, f"{style_file} missing prompt snippet section"
    print(f"  [PASS] test_local_rules_pool ({len(expected_styles)} presets verified)")


def test_cloud_channels(project_root):
    cloud_path = os.path.join(project_root, "references", "rules-pool", "cloud", "cloud-channels.md")
    assert os.path.exists(cloud_path), f"Missing cloud channels: {cloud_path}"
    
    with open(cloud_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    assert "Nature" in content, "cloud-channels 缺少 Nature 规范定义"
    assert "IEEE" in content, "cloud-channels 缺少 IEEE 规范定义"
    assert "外部 Skills 能力借取" in content, "cloud-channels 缺少外部技能借取协议"
    assert "只借其词" in content, "cloud-channels 缺少核心借取原则声明"
    assert "下载" in content, "cloud-channels 缺少云端下载协议声明"
    print("  [PASS] test_cloud_channels")


def test_skill_workflow_definition(project_root):
    skill_path = os.path.join(project_root, "SKILL.md")
    assert os.path.exists(skill_path), f"Missing SKILL.md: {skill_path}"
    
    with open(skill_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 校验 Frontmatter
    assert content.startswith("---"), "SKILL.md must start with YAML frontmatter"
    frontmatter_match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    assert frontmatter_match, "SKILL.md frontmatter syntax invalid"
    assert "name: sci-plot" in frontmatter_match.group(1), "frontmatter missing name: sci-plot"

    # 校验核心流程环节
    assert "Round 0:" in content, "SKILL.md missing Round 0"
    assert "Round 1:" in content, "SKILL.md missing Round 1"
    assert "Round 2:" in content, "SKILL.md missing Round 2"
    assert "Round 3:" in content, "SKILL.md missing Round 3"
    assert "Round 4:" in content, "SKILL.md missing Round 4"
    assert "Round 5:" in content, "SKILL.md missing Round 5"
    assert "烟消云散" in content, "SKILL.md missing 烟消云散 scope isolation rule"
    assert "双轨专业规范池" in content or "Dual-Track" in content, "SKILL.md missing dual-track rules pool definition"
    print("  [PASS] test_skill_workflow_definition")


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("=== Running Rules Pool Integrity Tests ===")
    test_core_base_rules(root)
    test_local_rules_pool(root)
    test_cloud_channels(root)
    test_skill_workflow_definition(root)
    print("ALL RULES POOL TESTS PASSED!\n")

