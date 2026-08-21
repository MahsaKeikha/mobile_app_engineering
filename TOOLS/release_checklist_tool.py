def unresolved_checks(checks: list[dict]) -> list[dict]:
    return [check for check in checks if not check.get("complete", False)]
