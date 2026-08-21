class APIIntegrationAgent:
    name = "api_integration"

    def run(self, case: dict) -> dict:
        endpoints = case.get("endpoints", [])
        missing_auth = [e for e in endpoints if not e.get("auth_defined", False)]
        return {"agent": self.name, "endpoints": endpoints, "missing_auth": missing_auth}
