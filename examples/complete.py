import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.orchestrator import MobileEngineeringOrchestrator  # noqa: E402

case = {
    "platforms": ["ios", "android"], "modules": ["auth", "home"], "features": ["login", "offline-cache"],
    "endpoints": [{"path": "/login", "auth_defined": True}], "test_failures": [], "release_blockers": [],
    "device_matrix_covered": True, "accessibility_review": "complete", "security_review": "complete",
    "privacy_review": "complete", "crash_free_rate": 0.999, "startup_ms": 1400,
    "offline_strategy_defined": True, "rollback_tested": True,
}
result = MobileEngineeringOrchestrator().run(case, approve=True)
assert result["status"] == "approved_for_release"
print(result["status"], result["blockers"])
