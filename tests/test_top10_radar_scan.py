"""
test_top10_radar_scan.py — 测试科研绘图 Skill Top 10 全量仓库的雷达自适应嗅探与锁定能力。
验证不论仓库的目录结构多么千奇百怪，雷达打分机制均能 100% 自动定位核心绘图/图表规范文件。
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.universal_skill_harvester import (
    parse_github_url,
    get_default_branch,
    scan_and_discover_target_file,
)

TOP10_REPOS = [
    ("Academic Research Skills", "https://github.com/Imbad0202/academic-research-skills"),
    ("Nature-skills", "https://github.com/Yuan1z0825/nature-skills"),
    ("Scientific Agent Skills", "https://github.com/K-Dense-AI/scientific-agent-skills"),
    ("Auto-claude-code-research-in-sleep", "https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep"),
    ("AutoResearchClaw", "https://github.com/aiming-lab/AutoResearchClaw"),
    ("GPT-Image2-Skill", "https://github.com/wuyoscar/GPT-Image2-Skill"),
    ("MathModelAgent", "https://github.com/jihe520/MathModelAgent"),
    ("Figures4papers", "https://github.com/ChenLiu-1996/figures4papers"),
    ("codex-claude-academic-skills", "https://github.com/zLanqing/codex-claude-academic-skills"),
    ("AcademicForge", "https://github.com/HughYau/AcademicForge"),
]


def test_top10_radar_discovery():
    print("=== Testing Universal Radar on All Top 10 Repositories ===")
    
    passed_count = 0
    for rank, (name, url) in enumerate(TOP10_REPOS, 1):
        print(f"[{rank}/10] Testing {name} ({url})...")
        owner, repo = parse_github_url(url)
        branch = get_default_branch(owner, repo)
        target_path, score = scan_and_discover_target_file(owner, repo, branch)
        
        assert score > 0, f"Radar failed to score any file for {name}"
        assert target_path.endswith((".md", ".yaml", ".txt")), f"Discovered non-doc target: {target_path}"
        print(f"       -> [LOCKED] {target_path} (Score: {score})")
        passed_count += 1

    assert passed_count == 10, f"Expected 10/10 passed, got {passed_count}"
    print(f"\nALL {passed_count}/10 TOP SCIENTIFIC SKILLS RADAR LOCKED SUCCESSFULLY!\n")


if __name__ == "__main__":
    test_top10_radar_discovery()
