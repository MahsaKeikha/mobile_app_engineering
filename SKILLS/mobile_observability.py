def telemetry_gaps(required: list[str], configured: list[str]) -> list[str]:
    return sorted(set(required) - set(configured))
