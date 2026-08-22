import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.orchestrator import MobileEngineeringOrchestrator  # noqa: E402


def case(**updates):
    value = {
        "platforms": ["ios", "android"], "modules": ["auth"], "features": ["login"], "technical_debt": [],
        "endpoints": [{"path": "/login", "auth_defined": True}], "test_failures": [], "release_blockers": [],
        "assumptions": [], "conflicts": [], "unresolved_questions": [], "minimum_os_supported": True,
        "device_matrix_covered": True, "accessibility_review": "complete", "security_review": "complete",
        "privacy_review": "complete", "crash_free_rate": 0.999, "minimum_crash_free_rate": 0.995,
        "startup_ms": 1500, "startup_budget_ms": 2000, "offline_strategy_defined": True, "rollback_tested": True,
    }
    value.update(updates)
    return value


SCENARIOS = [
    ("healthy_release", case(), True, "approved_for_release"),
    ("awaiting_approval", case(), False, "awaiting_human_approval"),
    ("missing_api_auth", case(endpoints=[{"path": "/private", "auth_defined": False}]), True, "review_required"),
    ("test_failure", case(test_failures=["crash"]), True, "review_required"),
    ("security_pending", case(security_review="pending"), True, "review_required"),
    ("performance_over_budget", case(startup_ms=2600), True, "review_required"),
    ("reliability_below_target", case(crash_free_rate=0.97), True, "review_required"),
    ("unresolved_governance", case(unresolved_questions=["Who owns rollback?"]), True, "review_required"),
]


def main():
    rows = []
    orchestrator = MobileEngineeringOrchestrator()
    for name, payload, approve, expected in SCENARIOS:
        actual = orchestrator.run(payload, approve=approve)["status"]
        rows.append({"scenario": name, "expected": expected, "actual": actual, "passed": actual == expected})
    passed = sum(row["passed"] for row in rows)
    result = {"system_id": "F41", "version": "1.0.0", "scenario_count": len(rows), "passed": passed, "pass_rate": passed / len(rows), "scenarios": rows}
    Path("benchmarks").mkdir(exist_ok=True)
    Path("benchmarks/heldout_results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if result["pass_rate"] != 1.0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
