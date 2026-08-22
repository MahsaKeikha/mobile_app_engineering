# F41 Mobile App Engineering

**Maturity:** L3 Gold Standard candidate  
**Version:** 1.0.0

A multi-agent reference system for mobile application engineering and release governance across architecture, client implementation, API integration, QA, and release readiness.

## Release governance

F41 fails closed when API authentication is undefined, tests fail, release blockers remain, supported-OS coverage is missing, the device matrix is incomplete, accessibility/security/privacy review is incomplete, crash-free reliability is below target, startup performance exceeds budget, offline behavior is undefined, rollback is untested, or unresolved conflicts/questions remain. Human approval is required after automated gates pass and cannot override blockers.

## Reproduce

```bash
python -m pip install -e '.[dev]'
ruff check .
pytest -q
python benchmarks/heldout_suite.py
python examples/minimal.py
python examples/complete.py
python run.py
```

CI validates Python 3.10, 3.11, and 3.12 and publishes held-out results from Python 3.12.

## Architecture

1. Mobile Architecture Agent defines platform/module architecture.
2. Client Engineering Agent tracks features and technical debt.
3. API Integration Agent validates endpoint authentication contracts.
4. Mobile QA Agent surfaces test failures.
5. Release Agent surfaces release blockers.
6. The orchestrator applies cross-cutting reliability, performance, accessibility, privacy, security, offline, rollback, and human-approval gates.

L3 denotes an independently reviewable and reproducible reference implementation. It does not replace platform-specific security review, App Store/Play policy review, device testing, or production release authority.
