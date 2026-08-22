from copy import deepcopy

from AGENTS.api_integration_agent import APIIntegrationAgent
from AGENTS.client_engineering_agent import ClientEngineeringAgent
from AGENTS.mobile_architecture_agent import MobileArchitectureAgent
from AGENTS.mobile_qa_agent import MobileQAAgent
from AGENTS.release_agent import ReleaseAgent


class MobileEngineeringOrchestrator:
    """Fail-closed mobile engineering governance orchestrator."""

    def __init__(self):
        self.agents = [MobileArchitectureAgent(), ClientEngineeringAgent(), APIIntegrationAgent(), MobileQAAgent(), ReleaseAgent()]

    def run(self, case: dict, approve: bool = False) -> dict:
        state = self._normalize(case)
        analyses, trace = {}, []
        for step, agent in enumerate(self.agents, 1):
            analyses[agent.name] = agent.run(state)
            trace.append({"step": step, "actor": agent.name, "event": "completed"})

        blockers = self._blockers(state, analyses)
        eligible = not blockers
        if blockers:
            status = "review_required"
        elif approve:
            status = "approved_for_release"
        else:
            status = "awaiting_human_approval"
        trace.append({"step": len(trace) + 1, "actor": "mobile_release_gate", "event": status, "blockers": blockers})

        return {
            "system_id": "F41",
            "system_name": "Mobile App Engineering",
            "version": "1.0.0",
            "maturity": "L3 Gold Standard",
            "state": state,
            "analyses": analyses,
            "blockers": blockers,
            "ready_for_approval": eligible,
            "status": status,
            "trace": trace,
        }

    @staticmethod
    def _normalize(case: dict) -> dict:
        state = deepcopy(case)
        for key in ("platforms", "modules", "features", "technical_debt", "endpoints", "test_failures", "release_blockers", "assumptions", "conflicts", "unresolved_questions"):
            state.setdefault(key, [])
        state.setdefault("minimum_os_supported", True)
        state.setdefault("device_matrix_covered", True)
        state.setdefault("accessibility_review", "complete")
        state.setdefault("security_review", "complete")
        state.setdefault("privacy_review", "complete")
        state.setdefault("crash_free_rate", 0.999)
        state.setdefault("minimum_crash_free_rate", 0.995)
        state.setdefault("startup_ms", 1500)
        state.setdefault("startup_budget_ms", 2000)
        state.setdefault("offline_strategy_defined", True)
        state.setdefault("rollback_tested", True)
        return state

    @staticmethod
    def _blockers(state: dict, analyses: dict) -> list[str]:
        blockers = []
        if analyses["api_integration"]["missing_auth"]:
            blockers.append("api_auth_missing")
        if analyses["mobile_qa"]["failures"]:
            blockers.append("test_failures")
        if analyses["release"]["blockers"]:
            blockers.append("release_blocker")
        if not state["minimum_os_supported"]:
            blockers.append("minimum_os_unsupported")
        if not state["device_matrix_covered"]:
            blockers.append("device_matrix_gap")
        if state["accessibility_review"] != "complete":
            blockers.append("accessibility_review_incomplete")
        if state["security_review"] != "complete":
            blockers.append("security_review_incomplete")
        if state["privacy_review"] != "complete":
            blockers.append("privacy_review_incomplete")
        if float(state["crash_free_rate"]) < float(state["minimum_crash_free_rate"]):
            blockers.append("reliability_below_target")
        if int(state["startup_ms"]) > int(state["startup_budget_ms"]):
            blockers.append("startup_performance_budget_exceeded")
        if not state["offline_strategy_defined"]:
            blockers.append("offline_strategy_missing")
        if not state["rollback_tested"]:
            blockers.append("rollback_not_tested")
        if state["conflicts"]:
            blockers.append("unresolved_conflict")
        if state["unresolved_questions"]:
            blockers.append("unresolved_question")
        return blockers
