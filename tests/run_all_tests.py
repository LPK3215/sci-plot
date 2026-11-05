"""
run_all_tests.py — sci-plot 自动化测试套件统一运行入口。
"""

import subprocess
import sys


def main():
    print("=" * 60)
    print("  Sci-Plot Automated Test Suite (Pipeline & Rules Verification)")
    print("=" * 60 + "\n")

    test_scripts = [
        "tests/test_rules_pool_integrity.py",
        "tests/test_prompt_compliance.py",
        "tests/test_end_to_end_simulation.py",
        "tests/test_cloud_downloader.py",
        "tests/test_external_skills_ingestion.py",
        "tests/test_top10_radar_scan.py",
    ]

    all_passed = True
    for script in test_scripts:
        print(f"Executing {script}...")
        res = subprocess.run([sys.executable, script])
        if res.returncode != 0:
            print(f"FAILED: {script}")
            all_passed = False
            break
        print("-" * 60)

    if all_passed:
        print("\n" + "=" * 60)
        print("  🎉 ALL TESTS PASSED! WORKFLOW & RULES ARE 100% ROCK-SOLID.")
        print("=" * 60)
        sys.exit(0)
    else:
        print("\nSome tests failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()

