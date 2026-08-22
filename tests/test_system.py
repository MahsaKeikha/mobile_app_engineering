from orchestration.orchestrator import MobileEngineeringOrchestrator


def healthy_case(**updates):
    case = {
        "platforms": ["ios", "android"],
        "modules": ["auth", "home"],
        "features": ["login"],
        "technical_debt": [],
        "endpoints": [{"path": "/login", "auth_defined": True}],
        "test_failures": [],
        "release_blockers": [],
        "assumptions": [],
        "conflicts": [],
        "unresolved_questions": [],
        "minimum_os_supported": True,
        "device_matrix_covered": True,
        "accessibility_review": "complete",
        "security_review": "complete",
        "privacy_review": "complete",
        "crash_free_rate": 0.999,
        "minimum_crash_free_rate": 0.995,
        "startup_ms": 1500,
        "startup_budget_ms": 2000,
        "offline_strategy_defined": True,
        "rollback_tested": True,
    }
    case.update(updates)
    return case


def test_healthy_case_requires_human_approval():
    result = MobileEngineeringOrchestrator().run(healthy_case())
    assert result["status"] == "awaiting_human_approval"
    assert result["ready_for_approval"] is True


def test_healthy_case_can_be_approved():
    result = MobileEngineeringOrchestrator().run(healthy_case(), approve=True)
    assert result["status"] == "approved_for_release"
    assert result["version"] == "1.0.0"
    assert len(result["analyses"]) == 5


def test_api_auth_failure_blocks_release():
    result = MobileEngineeringOrchestrator().run(healthy_case(endpoints=[{"path": "/private", "auth_defined": False}]), approve=True)
    assert result["status"] == "review_required"
    assert "api_auth_missing" in result["blockers"]


def test_quality_and_release_failures_block():
    result = MobileEngineeringOrchestrator().run(healthy_case(test_failures=["login-crash"], release_blockers=["store-rejection"]), approve=True)
    assert "test_failures" in result["blockers"]
    assert "release_blocker" in result["blockers"]


def test_mobile_nonfunctional_gates_fail_closed():
    result = MobileEngineeringOrchestrator().run(healthy_case(
        device_matrix_covered=False,
        accessibility_review="pending",
        privacy_review="pending",
        security_review="pending",
        crash_free_rate=0.98,
        startup_ms=2500,
        offline_strategy_defined=False,
        rollback_tested=False,
    ), approve=True)
    expected = {
        "device_matrix_gap", "accessibility_review_incomplete", "privacy_review_incomplete",
        "security_review_incomplete", "reliability_below_target",
        "startup_performance_budget_exceeded", "offline_strategy_missing", "rollback_not_tested",
    }
    assert expected.issubset(set(result["blockers"]))
    assert result["status"] == "review_required"


def test_conflicts_and_questions_block_human_override():
    result = MobileEngineeringOrchestrator().run(healthy_case(conflicts=["SDK versions disagree"], unresolved_questions=["Who owns rollback?"]), approve=True)
    assert result["status"] == "review_required"
    assert "unresolved_conflict" in result["blockers"]
    assert "unresolved_question" in result["blockers"]


def test_trace_has_all_agents_and_release_gate():
    result = MobileEngineeringOrchestrator().run(healthy_case())
    assert len(result["trace"]) == 6
    assert result["trace"][-1]["actor"] == "mobile_release_gate"
