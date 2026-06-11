# Task Packet: Fake ML Cycle Candidate Review

## Objective

Review whether candidate recipe `candidate-a` is ready for promotion against
the current control in the fake ML cycle.

## Scope

- Allowed paths:
  - `examples/fake-ml-cycle/state.json`
  - `examples/fake-ml-cycle/worker-result.md`
- Read-only sources:
  - `templates/promotion-gate.md`
- Out-of-scope paths:
  - Anything outside `examples/fake-ml-cycle/`

## Required Inputs

- Source artifact: `examples/fake-ml-cycle/state.json`
- Current state pointer: `cycle=42`
- Prior result to avoid repeating: none

## Allowed Actions

- Read files.
- Write a result file under `examples/fake-ml-cycle/`.
- Do not call external APIs.

## Forbidden Actions

- Do not access secrets.
- Do not mutate production systems.
- Do not broaden beyond the named paths.

## Result Contract

Write results to:

```text
examples/fake-ml-cycle/worker-result.md
```

Include:

- Verdict.
- Evidence read, with paths.
- Candidate versus control comparison.
- What remains unproven.
- Promotion, hold, or reject decision.
