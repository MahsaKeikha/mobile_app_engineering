class ClientEngineeringAgent:
    name = "client_engineering"

    def run(self, case: dict) -> dict:
        return {"agent": self.name, "features": case.get("features", []), "technical_debt": case.get("technical_debt", [])}
