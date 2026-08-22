# F41 Mobile App Engineering

**Maturity:** L3 Gold Standard candidate  
**Version:** 1.0.0

A multi-agent reference implementation for mobile application engineering and release governance across architecture, client implementation, API integration, QA, reliability, performance, accessibility, privacy, security, offline behavior, rollback readiness, and human release approval.

F41 is designed for mobile engineers, platform teams, technical leads, researchers, and students who want to study how a mobile delivery workflow can be decomposed into specialist agents while keeping release evidence, deterministic checks, failure states, and approval boundaries explicit.

It is a reference architecture and decision-support system. It does not autonomously publish an app, sign releases, change production backends, approve privacy or security risk, bypass App Store or Play policies, or replace accountable mobile engineers, QA teams, security reviewers, privacy professionals, release managers, or product owners.

## What the system does

A mobile release is not ready merely because the application builds. Teams also need confidence in architecture, feature implementation, API contracts, authentication, test coverage, supported OS versions, representative devices, startup performance, crash reliability, accessibility, security, privacy, offline behavior, rollback, and unresolved release blockers.

F41 separates those concerns into five specialist agents:

```text
mobile release case
        |
        v
Mobile Architecture Agent
        |
        v
Client Engineering Agent
        |
        v
API Integration Agent
        |
        v
    Mobile QA Agent
        |
        v
     Release Agent
        |
        v
cross-cutting release gates
        |
        v
explicit human approval
```

The orchestrator preserves evidence from each stage so a polished release summary cannot hide a failed API contract, unsupported device class, missing accessibility review, or reliability blocker.

## Repository architecture

The repository separates agent roles, reusable engineering skills, deterministic tools, orchestration, benchmarks, tests, examples, and documentation:

```text
AGENTS/            specialist mobile engineering roles
SKILLS/            reusable engineering procedures
TOOLS/             deterministic validation and release helpers
orchestration/     workflow state and release governance
benchmarks/        held-out release scenarios and results
examples/          minimal and complete runnable examples
tests/             system, failure, gate, and approval tests
docs/              architecture and L3 audit documentation
run.py             main runnable entry point
pyproject.toml      project configuration
```

This separation makes it easier to replace one specialist capability or tool without redesigning the full release workflow.

## Agents and responsibilities

| Agent | Responsibility | Core question |
|---|---|---|
| Mobile Architecture Agent | Define platform and module boundaries, dependency structure, and architectural assumptions | Is the application architecture appropriate for the target platforms and product constraints? |
| Client Engineering Agent | Track client features, implementation readiness, and technical debt | Is the client implementation sufficiently complete and maintainable for the intended release? |
| API Integration Agent | Validate endpoint contracts, authentication, and integration assumptions | Are mobile-to-backend contracts explicit, compatible, and safe to depend on? |
| Mobile QA Agent | Surface test failures, coverage gaps, device issues, and quality risks | Has the release been tested across the scenarios and devices that matter? |
| Release Agent | Consolidate release blockers and readiness evidence | What still prevents the application from being safely released? |

The Release Agent does not have authority to publish. It assembles readiness evidence for the release gate and accountable human reviewers.

## Skills layer

Reusable procedures live under `SKILLS/`:

```text
SKILLS/
├── mobile_architecture_design.py
├── api_integration_review.py
├── test_strategy.py
├── mobile_observability.py
└── release_readiness.py
```

### Mobile architecture design

Supports explicit reasoning about module boundaries, navigation, state management, dependency direction, shared code, platform-specific code, data flow, caching, persistence, lifecycle behavior, and maintainability.

Architecture should account for actual platform constraints rather than treating iOS and Android as interchangeable runtimes.

### API integration review

Reviews mobile-backend contracts, including endpoint identity, authentication, authorization, request and response schemas, errors, timeouts, retry behavior, version compatibility, idempotency, and offline implications.

### Test strategy

Supports planning across unit, integration, UI, device, regression, accessibility, performance, and release testing.

### Mobile observability

Encourages explicit planning for crash reporting, performance telemetry, release versioning, key user journeys, backend error correlation, and post-release monitoring.

### Release readiness

Consolidates required release evidence and blockers without converting the workflow into automatic publishing authority.

## Tools layer

Deterministic helpers live under `TOOLS/`:

```text
TOOLS/
├── api_contract_tool.py
├── device_matrix_tool.py
├── performance_budget_tool.py
└── release_checklist_tool.py
```

The tools layer demonstrates an important engineering principle: values that can be checked deterministically should not depend only on free-form model judgment.

### API contract tool

Provides a structured place to validate API assumptions. Production extensions can check schema compatibility, authentication requirements, endpoint availability, version contracts, error semantics, and backward compatibility.

### Device matrix tool

Tracks supported OS and device coverage. A release should not claim device support that was never tested or validated.

Useful matrix dimensions can include:

- iOS and Android versions
- phone and tablet classes
- screen sizes and densities
- lower-memory devices
- locale and language
- accessibility settings
- network conditions
- hardware capabilities

### Performance budget tool

Represents explicit performance constraints such as startup time, memory usage, frame stability, network latency, binary size, battery impact, and critical interaction latency.

### Release checklist tool

Maintains the explicit release gate criteria so readiness is not inferred from a generic status summary.

## End-to-end workflow

A typical F41 review follows this sequence:

1. Load a mobile release case and its platform assumptions.
2. Review target platforms, module boundaries, dependencies, and architectural risks.
3. Review client feature completion and unresolved technical debt.
4. Validate backend endpoint contracts and authentication requirements.
5. Evaluate unit, integration, UI, device, and regression test results.
6. Verify the supported OS and device matrix.
7. Check crash-free reliability and performance against stated targets.
8. Review accessibility, privacy, security, and offline behavior.
9. Confirm rollback or release-recovery readiness.
10. Consolidate unresolved conflicts, questions, and release blockers.
11. Apply the fail-closed release gate.
12. Require explicit human approval before publication or production release.

A successful run means the workflow found sufficient evidence for review. It does not mean an app store submission or production release occurred.

## Quick start

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run lint and tests:

```bash
ruff check .
pytest -q
```

Run the held-out benchmark suite:

```bash
python benchmarks/heldout_suite.py
```

Run the examples:

```bash
python examples/minimal.py
python examples/complete.py
```

Run the main workflow:

```bash
python run.py
```

CI validates Python 3.10, 3.11, and 3.12 and publishes held-out results from Python 3.12.

## Input model

A useful mobile release case should provide enough context to evaluate more than feature completeness. Depending on the deployment, inputs can include:

- application identifier
- target release version
- supported platforms
- minimum supported OS versions
- architecture description
- module list
- feature status
- technical debt
- API endpoints
- authentication requirements
- test results
- device coverage
- crash-free target and observed value
- startup performance target and observed value
- accessibility review status
- privacy review status
- security review status
- offline behavior
- rollback or release-recovery plan
- known blockers
- unresolved questions

Production implementations should validate these inputs against explicit schemas.

## Mobile architecture review

Architecture review should make platform-specific design decisions visible. Useful questions include:

- Are module boundaries clear?
- Is dependency direction intentional?
- Is navigation architecture maintainable?
- Is application state ownership explicit?
- Are network, cache, and persistent data responsibilities separated?
- Are platform-specific APIs isolated appropriately?
- Is background execution behavior understood?
- Are lifecycle transitions handled safely?
- Are secrets and credentials kept out of the client where required?
- Is the architecture testable?

The architecture agent should surface assumptions and tradeoffs rather than presenting one design pattern as universally correct.

## Client engineering readiness

Feature readiness is not only a count of completed tickets. The Client Engineering Agent should consider:

- unfinished user flows
- temporary implementations
- known defects
- dependency upgrades
- deprecated platform APIs
- technical debt affecting reliability
- migration requirements
- feature flags
- localization readiness
- accessibility implementation
- instrumentation coverage

Known debt should remain visible when it creates release risk.

## API integration governance

Mobile API integrations are a common source of release failure. F41 treats authentication and endpoint contracts as release-critical evidence.

An integration record should make explicit:

- endpoint and version
- authentication mechanism
- authorization expectations
- request schema
- response schema
- error handling
- timeouts
- retry behavior
- backward compatibility
- caching rules
- offline behavior
- rate limiting

If API authentication is undefined, the release fails closed.

## Testing strategy

Testing should cover the behavior users will actually experience.

Useful layers include:

- unit tests
- integration tests
- API contract tests
- UI tests
- end-to-end critical-flow tests
- regression tests
- device tests
- OS-version tests
- accessibility tests
- localization tests
- performance tests
- offline and poor-network tests
- upgrade and migration tests

A passing unit-test suite alone is not sufficient evidence for mobile release readiness.

## Device and OS coverage

F41 explicitly treats device-matrix and supported-OS coverage as release gates.

The device matrix should be based on the application's real supported population and risk profile. It should account for differences in memory, CPU/GPU capability, screen size, input methods, OS behavior, permissions, hardware sensors, and vendor-specific behavior where relevant.

If supported OS coverage is missing or the device matrix is incomplete, the workflow blocks release readiness.

## Reliability and crash-free quality

Crash-free reliability should be tied to an explicit target and measurement period. A production workflow can extend F41 with crash analytics and release health platforms.

Review can include:

- crash-free sessions or users
- fatal startup crashes
- ANRs or hangs
- memory pressure and termination
- background-task failures
- top crash signatures
- regressions by release version
- device-specific crash clusters

The workflow fails closed when reliability falls below the required threshold.

## Performance budgets

Performance targets should be explicit before release. Example budgets include:

- cold-start time
- warm-start time
- time to interactive
- frame stability
- memory usage
- binary size
- network request latency
- image loading
- battery impact

A release that exceeds its defined startup budget should remain blocked until the responsible team accepts or resolves the issue through the actual change process.

## Accessibility

Accessibility is a release-readiness concern rather than a cosmetic afterthought.

Review can include:

- semantic labels
- screen reader navigation
- dynamic text
- contrast
- touch target size
- keyboard or switch access
- motion sensitivity
- focus order
- captions and alternatives

The workflow should not mark accessibility complete when no review or test evidence exists.

## Privacy and security

Mobile applications often handle sensitive data and credentials. Production extensions should review:

- data minimization
- local storage protection
- transport security
- token handling
- credential storage
- certificate validation
- logging of sensitive information
- permissions
- analytics and tracking
- third-party SDK behavior
- privacy disclosures
- platform privacy requirements

F41 does not replace platform-specific security testing, privacy review, or legal review.

## Offline and degraded-network behavior

Mobile users frequently experience intermittent connectivity. The release case should make offline assumptions explicit.

Relevant questions include:

- Which flows work offline?
- What is cached?
- What becomes read-only?
- How are writes queued or retried?
- How are conflicts resolved?
- What does the user see when connectivity is unavailable?
- Can repeated retries create duplicate actions?

Undefined offline behavior is treated as a release blocker when the application depends on it.

## Rollback and release recovery

Mobile rollback differs from server rollback because users may remain on an already-installed client version.

A release plan should therefore consider:

- feature flags
- server-side compatibility
- kill switches
- staged rollout
- phased deployment
- backward-compatible APIs
- emergency configuration changes
- hotfix process
- app-store review delays

Rollback readiness must be tested or otherwise demonstrated. An untested rollback path is a release blocker in F41.

## Release governance

F41 fails closed when any of the following remains unresolved:

- API authentication undefined
- failing tests
- release blockers
- unsupported or unverified OS coverage
- incomplete device matrix
- accessibility review incomplete
- security review incomplete
- privacy review incomplete
- crash-free reliability below target
- startup performance above budget
- offline behavior undefined
- rollback untested
- unresolved conflicts
- unresolved questions

Human approval is required only after these automated conditions pass. Human approval cannot override an active blocker inside the reference workflow.

## Human authority

F41 must not autonomously:

- sign production builds
- upload or publish to the App Store or Play Store
- change production feature flags
- change backend contracts
- modify production secrets
- approve privacy or security risk
- bypass app-store policies
- accept unresolved release blockers
- disable safety or monitoring controls
- declare a release successful without observed production evidence

Those actions belong to authenticated production systems and accountable humans.

## Observability and post-release monitoring

Mobile release readiness should include a plan for what happens after publication.

Useful telemetry includes:

- release adoption
- crash-free users or sessions
- startup performance
- API error rate
- latency
- app-not-responding events
- memory pressure
- critical funnel completion
- feature-flag state
- device and OS regressions

Monitoring should be version-aware so regressions can be tied to the specific release.

## Benchmarks and evaluation

The repository includes:

```text
benchmarks/heldout_suite.py
benchmarks/RESULTS.md
```

Evaluation should test release-governance behavior, not just whether the system produces a readable report.

Useful benchmark dimensions include:

- architecture issue detection
- undefined-authentication detection
- API contract completeness
- test-failure detection
- device-matrix completeness
- OS-support coverage
- reliability threshold enforcement
- performance-budget enforcement
- accessibility/privacy/security gating
- offline-behavior gating
- rollback-readiness gating
- human-approval enforcement

Strong held-out cases should contain realistic combinations of blockers rather than only one isolated failure at a time.

## Failure behavior

Useful explicit states include:

```text
ARCHITECTURE REVIEW REQUIRED
API AUTHENTICATION UNDEFINED
API CONTRACT INCOMPLETE
TEST FAILURE
DEVICE COVERAGE INCOMPLETE
OS COVERAGE INCOMPLETE
ACCESSIBILITY REVIEW REQUIRED
PRIVACY REVIEW REQUIRED
SECURITY REVIEW REQUIRED
RELIABILITY BELOW TARGET
PERFORMANCE BUDGET EXCEEDED
OFFLINE BEHAVIOR UNDEFINED
ROLLBACK NOT TESTED
RELEASE BLOCKED
HUMAN APPROVAL REQUIRED
```

The system should never fabricate a passing test, device result, security review, crash metric, or rollback test to make the release appear ready.

## CI and reproducibility

The repository includes GitHub Actions under `.github/workflows/tests.yml`.

CI should continue to cover:

- import and syntax integrity
- unit tests
- agent contract tests
- deterministic tool tests
- orchestration tests
- release-gate tests
- blocker and red-team cases
- held-out scenarios

Production extensions should additionally integrate platform build validation, signed-artifact verification, native test frameworks, sandbox backend contracts, and store-specific validation where appropriate.

## Extending F41

Common extensions include:

- iOS-specific architecture agents
- Android-specific architecture agents
- SwiftUI or UIKit review
- Jetpack Compose review
- mobile CI/CD integration
- crash analytics integration
- app-distribution integration
- feature-flag platforms
- analytics validation
- store-metadata review
- privacy-manifest review
- dependency and SDK risk analysis
- mobile threat-modeling
- performance profiling
- localization readiness
- phased rollout governance

Keep new agents specialized and ensure that publishing credentials and other consequential permissions remain outside unrestricted agent access.

## Example use cases

F41 can serve as a reference architecture for:

- mobile release readiness
- architecture reviews
- pre-store-submission checks
- API migration readiness
- staged rollout planning
- mobile reliability reviews
- cross-platform release governance
- mobile engineering education
- studying multi-agent decomposition for client software delivery

## Repository map

```text
.github/workflows/tests.yml
AGENTS/
├── mobile_architecture_agent.py
├── client_engineering_agent.py
├── api_integration_agent.py
├── mobile_qa_agent.py
└── release_agent.py
SKILLS/
├── mobile_architecture_design.py
├── api_integration_review.py
├── test_strategy.py
├── mobile_observability.py
└── release_readiness.py
TOOLS/
├── api_contract_tool.py
├── device_matrix_tool.py
├── performance_budget_tool.py
└── release_checklist_tool.py
benchmarks/
├── heldout_suite.py
└── RESULTS.md
docs/
├── ARCHITECTURE.md
└── L3_AUDIT.md
examples/
├── minimal.py
└── complete.py
orchestration/orchestrator.py
tests/test_system.py
run.py
pyproject.toml
CITATION.cff
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
```

## Design principles

1. Treat release readiness as an evidence problem, not a build-success flag.
2. Separate architecture, implementation, integration, QA, and release responsibilities.
3. Use deterministic tools for contracts, device matrices, budgets, and checklists.
4. Keep supported-platform claims tied to actual test evidence.
5. Make reliability and performance thresholds explicit.
6. Treat accessibility, privacy, and security as release concerns.
7. Design mobile recovery around staged rollout and backward compatibility, not only server rollback.
8. Preserve unresolved questions and blockers in workflow state.
9. Fail closed when material release evidence is missing.
10. Keep production publishing authority with authenticated accountable humans.

## L3 meaning

L3 denotes an independently reviewable and reproducible reference implementation under the library's documented maturity criteria. It does not mean that the repository replaces platform-specific testing, App Store or Play review, security certification, privacy review, production telemetry, or real release authority.

## Citation and reuse

The repository includes `CITATION.cff` for academic and technical citation and is licensed under MIT. See `CONTRIBUTING.md` and `SECURITY.md` for contribution and vulnerability-reporting guidance.

## Responsible use

Use F41 as a mobile engineering and release-governance reference. Validate architecture, API contracts, device coverage, test evidence, accessibility, privacy, security, reliability, performance, offline behavior, rollback strategy, and store requirements against the actual application and production environment. Final release decisions remain the responsibility of authorized humans operating through the organization's real engineering and release controls.