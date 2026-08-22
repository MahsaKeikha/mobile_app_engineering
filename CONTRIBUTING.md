# Contributing

Contributions should preserve the distinction between architecture, client engineering, API integration, QA, release readiness, and the final human release gate.

Before opening a pull request run:

```bash
python -m pip install -e '.[dev]'
ruff check .
pytest -q
python benchmarks/heldout_suite.py
python examples/minimal.py
python examples/complete.py
python run.py
```

Behavior changes must include tests and, when they affect a Gold Standard claim, a held-out scenario or documented rationale. Do not weaken a safety or quality gate merely to make a test pass.
