# Roadmap

This roadmap turns Codex Agentic Research Ops from a template set into a
practical toolkit for teams using Codex on expensive or safety-sensitive
engineering work.

## 30 Days

- Ship a task-packet validator that checks required sections, result paths, and
  forbidden-action boundaries.
- Add a runnable fake ML cycle demo with preflight, worker result, review, and
  flight-recorder steps.
- Expand documentation for common workflows: model evals, analytics pipelines,
  paper simulations, and production-adjacent debugging.
- Add regression tests for the validator and example packets.

## 60 Days

- Add a small CLI for creating task packets, result contracts, root-cause
  investigations, and promotion gates from templates.
- Publish three worked examples that show good and bad Codex operating patterns.
- Add leak-safe public release checks for common secret and private-state
  mistakes.
- Document cost-aware model routing: routine evidence collection versus
  high-reasoning decision gates.

## 90 Days

- Build an evaluation harness that scores Codex workflow runs for drift,
  evidence quality, result completeness, and approval-boundary discipline.
- Add GitHub Actions checks for packet validation and leak-safe release hygiene.
- Invite external users to test the toolkit on open-source ML, analytics, and
  developer-ops projects.
- Publish a short guide: "Using Codex on expensive workflows without wasting
  compute or leaking private state."

## Success Metrics

- At least 20 tested example packets and result artifacts.
- At least 3 complete worked examples.
- A documented evaluator that can flag missing evidence, stale state, and
  unsafe action boundaries.
- Public issues or discussions from external users trying the workflow.
- A release checklist that catches common private-info leaks before publication.
