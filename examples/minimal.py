import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.orchestrator import MobileEngineeringOrchestrator  # noqa: E402

result = MobileEngineeringOrchestrator().run({})
assert result["status"] == "awaiting_human_approval"
print(result["status"])
