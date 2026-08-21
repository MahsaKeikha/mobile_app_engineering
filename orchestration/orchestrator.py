from AGENTS.mobile_architecture_agent import MobileArchitectureAgent
from AGENTS.client_engineering_agent import ClientEngineeringAgent
from AGENTS.api_integration_agent import APIIntegrationAgent
from AGENTS.mobile_qa_agent import MobileQAAgent
from AGENTS.release_agent import ReleaseAgent


class MobileEngineeringOrchestrator:
    def __init__(self):
        self.agents = [MobileArchitectureAgent(), ClientEngineeringAgent(), APIIntegrationAgent(), MobileQAAgent(), ReleaseAgent()]

    def run(self, case: dict) -> dict:
        analyses, trace = {}, []
        for step, agent in enumerate(self.agents, 1):
            analyses[agent.name] = agent.run(case)
            trace.append({"step": step, "actor": agent.name, "event": "completed"})
        blocked = bool(analyses["api_integration"]["missing_auth"] or analyses["mobile_qa"]["failures"] or analyses["release"]["blockers"])
        return {"system_id": "F41", "system_name": "Mobile App Engineering", "version": "0.1.0", "analyses": analyses, "status": "review_required" if blocked else "complete", "trace": trace}
