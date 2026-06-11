# Codex Agentic Research Ops

Reusable operating patterns for running expensive research and ML workflows with
Codex while preserving evidence, cost controls, and human approval gates.

This project extracts generic lessons from real operator workflows into a safe,
open-source toolkit. It does not include private infrastructure, credentials,
live trading or mining configuration, customer data, or proprietary result logs.

## What This Provides

- Zero-copy-paste task packets for delegating bounded work to another model.
- Result contracts that make worker outputs reviewable by Codex.
- Preflight proof templates for expensive or risky operations.
- Append-only flight-recorder patterns for cycle and patch evidence.
- Mutex and ownership patterns for multi-agent coordination.
- Promotion-gate templates for comparing candidate changes against a control.
- Leak-safe release checklists for turning private work into public examples.

## Why It Exists

Agentic workflows can waste money quickly when they drift, poll repeatedly, or
act on stale evidence. This repository treats each expensive run as a hypothesis
with a proof gate, stop rule, and durable artifact trail.

The aim is not to automate away judgment. The aim is to make judgment auditable:
what changed, why it changed, what evidence was current, what remains unproven,
and when the system must stop for human approval.

## Repository Layout

```text
docs/
  openai-codex-fund-application.md
  operating-model.md
examples/
  fake-ml-cycle/
scripts/
  flight_recorder.py
  leak_scan.py
  validate_packet.py
templates/
  task-packet.md
  result-contract.md
  preflight-proof.md
  root-cause-investigation.md
  promotion-gate.md
```

## Safety Boundaries

The example data is synthetic. Do not commit:

- `.env` files, API keys, wallet material, private keys, or tokens.
- Real hostnames, SSH targets, customer lists, billing identifiers, or account IDs.
- Live trading, mining, or production configuration.
- Private logs, screenshots, datasets, or model checkpoints.

Run the leak scan before publishing:

```bash
python3 scripts/leak_scan.py .
```

Validate the included demo packet and worker result:

```bash
python3 scripts/validate_packet.py examples/fake-ml-cycle/task-packet.md --kind task
python3 scripts/validate_packet.py examples/fake-ml-cycle/worker-result.md --kind result
python3 -m pytest
```

## 90-Day Direction

The roadmap focuses on turning these templates into a tested CLI and evaluator
for Codex workflows: packet validation, worked examples, leak-safe release
checks, and scoring for drift, evidence quality, result completeness, and human
approval boundaries. See [ROADMAP.md](ROADMAP.md).

## Status

Pre-application public staging for the OpenAI Codex Open Source Fund.
