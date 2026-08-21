class ReleaseAgent:
    name = "release"

    def run(self, case: dict) -> dict:
        blockers = case.get("release_blockers", [])
        return {"agent": self.name, "blockers": blockers, "ready": not blockers}
