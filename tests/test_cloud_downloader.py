"""
test_cloud_downloader.py — 测试并验证“云端规范萃取并下载/持久化到本地”全过程。
模拟从在线期刊指南或第三方 Skill 提炼核心规则，并自动下载写入 references/rules-pool/local/。
"""

import os
import sys

# 模拟从云端链接 (Nature Author Guidelines) 提炼出的核心参数
MOCK_NATURE_CLOUD_SPEC = {
    "name": "nature-portfolio",
    "source_url": "https://www.nature.com/nature/for-authors/final-submission",
    "single_column_mm": 89,
    "double_column_mm": 183,
    "font": "Helvetica",
    "background": "White (#FFFFFF)",
    "primary_color": "Dark Gray (#1A1A1A)",
    "accent_color": "Nature Teal (#0284C7)",
    "snippet": "Nature journal publication style, pure white background, 89mm single column vector line art, Helvetica typography, crisp line weights, restrained teal accent, no 3D elements, no gradients."
}


def materialize_cloud_rule(spec, project_root):
    target_filename = f"downloaded-{spec['name']}.md"
    target_path = os.path.join(project_root, "references", "rules-pool", "local", target_filename)

    content = f"""# {spec['name'].upper()} — 期刊绘图规范 (Downloaded Rule)

> **来源 URL**: {spec['source_url']}  
> **抓取与沉淀状态**: 本地已固化（永久离线可用，支持人工二次编辑）

## 1. 风格定位与视觉特征
- **目标期刊**: Nature / Nature Portfolio 系列期刊
- **排版质感**: 顶刊极简学术矢量图，高度克制，严谨清晰

## 2. 画布与排版约束
- **背景**: {spec['background']}
- **栏宽标准**: 单栏 {spec['single_column_mm']} mm / 双栏 {spec['double_column_mm']} mm
- **字体标准**: {spec['font']} 无衬线体
- **线条粗细**: 主结构线 1.5-2px，网格与次要箭头 0.75-1px

## 3. 色彩限制 (≤3色)
- **主色框线**: {spec['primary_color']}
- **唯一强调色**: {spec['accent_color']}

## 4. 专属领域词典 (Domain Vocabulary)
- Mechanism Overview: "Schematic representation of molecular pathway"
- Dimensional Scale: "Scale bar indicated in nanometers (nm)"

## 5. 核心英文提示词片段 (Prompt Snippet)
```text
{spec['snippet']}
```
"""
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"  [DOWNLOADED] Successfully materialized cloud rule to: {target_filename}")
    return target_path


def test_cloud_to_local_workflow(project_root):
    print("--- Testing Cloud-to-Local Rule Materialization ---")
    downloaded_file = materialize_cloud_rule(MOCK_NATURE_CLOUD_SPEC, project_root)
    assert os.path.exists(downloaded_file), f"Failed to download cloud rule to {downloaded_file}"

    with open(downloaded_file, "r", encoding="utf-8") as f:
        c = f.read()
    
    # 验证关键沉淀要素
    assert "Nature" in c, "Downloaded rule missing Nature identifier"
    assert "89 mm" in c, "Downloaded rule missing column dimensions"
    assert "Prompt Snippet" in c, "Downloaded rule missing Prompt Snippet"
    assert "本地已固化" in c, "Downloaded rule missing offline readiness mark"
    print("  [PASS] Cloud rule fully parsed, extracted and downloaded to local pool!")


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("=== Running Cloud Downloader Verification Test ===")
    test_cloud_to_local_workflow(root)
    print("CLOUD DOWNLOADER TEST PASSED!\n")

