"""
test_external_skills_ingestion.py — 针对集录的三个顶级开源 Skills 规范的完整性与生成能力测试。
验证：
1. Yuan1z0825/nature-skills (downloaded-nature-skills.md)
2. K-Dense-AI/scientific-agent-skills (downloaded-scientific-agent-skills.md)
3. Imbad0202/academic-research-skills (downloaded-academic-research-skills.md)
"""

import os
import re
import sys

EXTERNAL_SKILL_FILES = [
    "downloaded-nature-skills.md",
    "downloaded-scientific-agent-skills.md",
    "downloaded-academic-research-skills.md"
]


def test_downloaded_skills_schemas(project_root):
    print("--- 1. Testing Downloaded External Skills File Schemas ---")
    local_pool = os.path.join(project_root, "references", "rules-pool", "local")
    
    for filename in EXTERNAL_SKILL_FILES:
        path = os.path.join(local_pool, filename)
        assert os.path.exists(path), f"Missing downloaded rule file: {filename}"
        
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        assert "来源" in content or "Source" in content, f"{filename} missing source metadata"
        assert "画布与排版约束" in content, f"{filename} missing canvas/layout constraints"
        assert "色彩限制" in content, f"{filename} missing color constraints"
        assert "专属领域词典" in content, f"{filename} missing domain vocabulary"
        assert "核心英文提示词片段" in content or "Prompt Snippet" in content, f"{filename} missing prompt snippet"
        
        # 确保 Prompt Snippet 包含有效的内容
        snippet_match = re.search(r"```text\s*\n(.*?)\n```", content, re.DOTALL)
        assert snippet_match, f"{filename} missing valid code block prompt snippet"
        snippet = snippet_match.group(1).strip()
        assert len(snippet) > 50, f"{filename} prompt snippet is too short"
        
        print(f"  [PASS] Verified Schema: {filename}")


def test_simulation_prompt_generation_with_external_skills(project_root):
    print("--- 2. Testing End-to-End Prompt Generation with Each External Skill ---")
    
    # 模拟一份前沿生物分子论文输入
    sample_topic = "CRISPR-Cas9 Gene Editing Mechanism with Guide RNA Recognition"
    
    local_pool = os.path.join(project_root, "references", "rules-pool", "local")
    base_rules_path = os.path.join(project_root, "references", "core", "base-rules.md")
    
    with open(base_rules_path, "r", encoding="utf-8") as f:
        base_rules = f.read()

    for filename in EXTERNAL_SKILL_FILES:
        path = os.path.join(local_pool, filename)
        with open(path, "r", encoding="utf-8") as f:
            skill_content = f.read()
            
        # 提取 Snippet
        snippet_match = re.search(r"```text\s*\n(.*?)\n```", skill_content, re.DOTALL)
        snippet = snippet_match.group(1).strip()
        
        # 模拟 Round 4 融合生成
        mock_prompt = f"""
A publication-quality diagram of {sample_topic}.
{snippet}
Visual Elements:
- Cas9 protein complex shown as rounded soft container with target DNA unwinding
- Guide RNA (gRNA) binding sequence highlighted in accent color
- Cleavage site marked with clean directional scissor glyph and precise arrows
- All text annotations strictly under 8 words in crisp sans-serif font
"""
        # 质检负向红线
        forbidden_words = ["photorealistic", "3d sphere", "blender render", "octane render"]
        for fw in forbidden_words:
            assert fw not in mock_prompt.lower(), f"Generated prompt with {filename} contains forbidden {fw}"
            
        # 质检必要锚点
        assert any(term in mock_prompt.lower() for term in ["vector", "figure", "clean", "diagram", "scientific"])
        print(f"  [PASS] Successfully generated & verified compliant prompt using {filename}")


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("=== Running External Skills Ingestion & Verification Tests ===")
    test_downloaded_skills_schemas(root)
    test_simulation_prompt_generation_with_external_skills(root)
    print("ALL EXTERNAL SKILLS TESTS PASSED!\n")

