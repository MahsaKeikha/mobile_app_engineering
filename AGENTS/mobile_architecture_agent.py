class MobileArchitectureAgent:
    name = "mobile_architecture"

    def run(self, case: dict) -> dict:
        return {"agent": self.name, "platforms": case.get("platforms", ["ios", "android"]), "modules": case.get("modules", [])}
