from orchestration.orchestrator import MobileEngineeringOrchestrator


def test_run():
    result = MobileEngineeringOrchestrator().run({"endpoints": [], "test_failures": [], "release_blockers": []})
    assert result["system_id"] == "F41"
    assert result["status"] == "complete"


def test_release_blocker():
    assert MobileEngineeringOrchestrator().run({"release_blockers": ["crash"]})["status"] == "review_required"
