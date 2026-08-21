import json
from orchestration.orchestrator import MobileEngineeringOrchestrator

if __name__ == "__main__":
    print(json.dumps(MobileEngineeringOrchestrator().run({"features": ["login"], "endpoints": [], "test_failures": [], "release_blockers": []}), indent=2))
