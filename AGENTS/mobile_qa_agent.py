class MobileQAAgent:
    name = "mobile_qa"

    def run(self, case: dict) -> dict:
        failures = case.get("test_failures", [])
        return {"agent": self.name, "failures": failures, "pass": not failures}
