# Operating Model

This repository models agentic research work as a sequence of bounded,
evidence-backed decisions.

## Principles

1. Read the current state before recommending action.
2. Separate delivery proof from quality claims.
3. Require a result artifact for delegated work.
4. Use a mutex or owner marker before risky mutation.
5. Treat repeated stale recommendations as process failures.
6. Prefer cheap evidence before expensive runs.
7. Stop at financial, credential, or production-risk gates.

## Typical Loop

```text
state preflight -> hypothesis -> bounded task packet -> worker result ->
manager review -> safe patch window -> flight recorder -> fresh outcome
```

## Anti-Drift Controls

- Each task has a named result path.
- Each wait state has a next check time and stop rule.
- Each recommendation cites evidence and prior attempts.
- Each promotion requires a matched control or clear rollback.

## Public Example Boundary

The examples in this repo use synthetic project names and fake paths. They are
intended to teach the workflow shape without exposing live operations.
