# Task Packet

## Objective

State the specific decision or artifact this worker must produce.

## Scope

- Allowed paths:
- Read-only sources:
- Out-of-scope paths:

## Required Inputs

- Source artifact:
- Current state pointer:
- Prior result to avoid repeating:

## Allowed Actions

- Read files.
- Run local tests or analysis commands that do not mutate production state.
- Write the result file named below.

## Forbidden Actions

- Do not access secrets.
- Do not mutate production systems.
- Do not call paid APIs unless explicitly approved.
- Do not broaden beyond the named paths.

## Result Contract

Write results to:

```text
tasks/results/<task-id>-result.md
```

Include:

- Verdict.
- Evidence read, with paths.
- Findings or recommendation.
- What remains unproven.
- Stop rule or next decision unlocked.
