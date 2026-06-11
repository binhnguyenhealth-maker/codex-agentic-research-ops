# OpenAI Codex Open Source Fund Application Draft

## Project

Codex Agentic Research Ops

## Brief Description

Codex Agentic Research Ops is an open-source toolkit for running expensive
research and ML operations with Codex while preserving evidence, cost controls,
and approval gates. It provides reusable task packets, result contracts,
preflight proofs, root-cause investigation templates, promotion gates, and
append-only flight-recording patterns for multi-agent research workflows.

The project focuses on preventing the common failure modes of agentic work:
drift, stale recommendations, repeated polling, unclear ownership, unreviewable
worker outputs, and unsafe mutation of production or high-cost systems.

## GitHub Repository

https://github.com/binhnguyenhealth-maker/codex-agentic-research-ops

## How API Credits Would Be Used

API credits would be used to develop and test Codex-driven workflows against
realistic open-source examples, including:

- Generating and reviewing bounded task packets.
- Running Codex-based code review and root-cause investigations.
- Building examples for ML experiment management, analytics tooling, and
  paper-trading research systems.
- Maintaining documentation and regression tests for leak-safe public release
  workflows.
- Evaluating how smaller models can handle routine polling and evidence
  collection while reserving stronger reasoning for high-risk decisions.

## Related Public Work

- OPX sanitized snapshot: https://github.com/binhnguyenhealth-maker/opx-sanitized
- Prediction-market analytics sanitized snapshot: https://github.com/binhnguyenhealth-maker/polymarket-sanitized
- Paper-mode market-making bot sanitized snapshot: https://github.com/binhnguyenhealth-maker/lighter-bot-sanitized

## Safety Statement

The public repository uses synthetic examples and excludes secrets, private
infrastructure, customer data, live trading configuration, wallet material, and
private operational logs. A path-only leak scanner is included and run before
publication.
