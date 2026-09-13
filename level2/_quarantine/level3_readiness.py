#!/usr/bin/env python3
"""Level-3 readiness check: verify plugin socket, stubs, cost estimator."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
L2 = ROOT / "level2"
REPORTS = L2 / "reports"

def check_plugin_socket():
    engines_dir = L2 / "engines"
    checks = {}
    checks["base_class"] = (engines_dir / "__init__.py").exists()
    checks["level3_stub"] = (engines_dir / "level3_stub.py").exists()
    stub = engines_dir / "level3_stub.py"
    if stub.exists():
        content = stub.read_text()
        checks["sarvam_stub"] = "SarvamBatchAPI" in content
        checks["bhashini_stub"] = "BhashiniAPI" in content
        checks["locked_msg"] = "LOCKED" in content
    checks["local_dir"] = (engines_dir / "local").exists()
    if (engines_dir / "local").exists():
        adapters = [f.stem for f in (engines_dir / "local").glob("*.py") if not f.name.startswith("_")]
        checks["adapter_count"] = len(adapters)
        checks["adapters"] = adapters
    checks["test_registry"] = (engines_dir / "test_registry.py").exists()
    return checks

def check_cost_estimator():
    cost_file = L2 / "research" / "LEVEL3_COST_ESTIMATE.md"
    checks = {"file_exists": cost_file.exists()}
    if cost_file.exists():
        content = cost_file.read_text()
        todo_count = content.count("TODO-VERIFY")
        checks["todo_verify_count"] = todo_count
        checks["has_real_pricing"] = todo_count == 0
        checks["has_sarvam"] = "Sarvam" in content
        checks["has_bhashini"] = "Bhashini" in content
        checks["has_google"] = "Google" in content
        checks["has_azure"] = "Azure" in content
        checks["has_textract"] = "Textract" in content
    return checks

def check_training_bridge():
    train_dir = REPORTS / "training_data"
    checks = {"dir_exists": train_dir.exists()}
    for f in ["sft_noisy_to_gold.jsonl", "cer_rewards.csv", "simpo_pairs.jsonl", "summary.json"]:
        p = train_dir / f
        checks[f] = p.exists()
    return checks

def check_gap_report():
    gap = REPORTS / "GAP.md"
    checks = {"exists": False, "has_71_pct": False}
    if gap.exists():
        content = gap.read_text()
        checks["exists"] = True
        checks["has_71_pct"] = "7.1%" in content
    return checks

def check_seal():
    seal = Path("level2/reports/LEVEL2_SEAL.md")
    checks = {"sealed": False}
    if seal.exists():
        content = seal.read_text()
        checks["sealed"] = "LEVEL2_SEALED = **true**" in content
    return checks

def main():
    all_checks = {
        "plugin_socket": check_plugin_socket(),
        "cost_estimator": check_cost_estimator(),
        "training_bridge": check_training_bridge(),
        "gap_report": check_gap_report(),
        "seal": check_seal(),
    }
    
    print("=" * 60)
    print("LEVEL-3 READINESS CHECK")
    print("=" * 60)
    
    all_ok = True
    for category, checks in all_checks.items():
        print(f"\n{category}:")
        for check, result in checks.items():
            status = "✅" if result else "❌"
            print(f"  {check}: {status}")
            if isinstance(result, bool) and not result:
                all_ok = False
    
    print(f"\n{'='*60}")
    print(f"OVERALL: {'READY FOR LEVEL-3' if all_ok else 'NOT READY'}")
    print(f"{'='*60}")
    
    (Path("level2/reports") / "LEVEL3_READINESS.json").write_text(
        json.dumps({"checks": all_checks, "ready": all_ok}, indent=2)
    )
    return all_ok

if __name__ == "__main__":
    main()
