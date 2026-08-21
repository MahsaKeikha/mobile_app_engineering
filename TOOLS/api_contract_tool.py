def missing_contract_fields(endpoint: dict) -> list[str]:
    return [field for field in ["method", "path", "response"] if not endpoint.get(field)]
