def device_coverage(required: list[str], tested: list[str]) -> dict:
    missing = sorted(set(required) - set(tested))
    return {"complete": not missing, "missing": missing}
