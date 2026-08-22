# F41 Held-out Benchmark Results

**Version:** 1.0.0  
**Verified head:** `fbc72dca211566fd5303bc3b6bebe9d325e4f7e4`  
**Gold Standard CI run:** `32542752877`  
**Artifact:** `f41-heldout-results`  
**Artifact digest:** `sha256:1d52fde445b51d4045b23358338efae19d5482c0afdbf49be54f48abb27df747`

## Result

- Scenario count: 8
- Passed: 8
- Pass rate: 1.0
- Python 3.10: PASS
- Python 3.11: PASS
- Python 3.12: PASS

## Held-out scenarios

| Scenario | Expected | Result |
|---|---|---|
| healthy_release | approved_for_release | PASS |
| awaiting_approval | awaiting_human_approval | PASS |
| missing_api_auth | review_required | PASS |
| test_failure | review_required | PASS |
| security_pending | review_required | PASS |
| performance_over_budget | review_required | PASS |
| reliability_below_target | review_required | PASS |
| unresolved_governance | review_required | PASS |

These results validate the deterministic reference behaviors documented by F41. They do not replace platform-specific device testing, security review, store-policy validation, or production release authority.
