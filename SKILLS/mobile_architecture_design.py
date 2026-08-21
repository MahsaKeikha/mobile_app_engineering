def architecture_readiness(modules: list[dict]) -> dict:
    unnamed = [m for m in modules if not m.get("name")]
    return {"ready": not unnamed, "invalid_modules": unnamed}
