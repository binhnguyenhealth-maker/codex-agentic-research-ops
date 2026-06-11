# Contributing

Contributions should make Codex-driven work more reviewable, safer, or less
wasteful.

Good contributions include:

- New task templates with clear result contracts.
- Validators that catch missing evidence, missing stop rules, or unsafe scopes.
- Worked examples using synthetic data.
- Documentation for cost-aware model routing and human approval gates.
- Leak-safe release checks that do not print secret values.

Please do not contribute:

- Private logs, real credentials, account identifiers, or production state.
- Live trading, wallet, billing, or infrastructure configuration.
- Examples that require paid APIs unless they have a dry-run mode.
- Advice that asks agents to bypass user approval or submit final actions
  silently.

## Pull Request Checklist

- [ ] Uses synthetic data or public fixtures only.
- [ ] Includes a runnable dry-run or test when possible.
- [ ] Names the human approval boundary for risky actions.
- [ ] Avoids private infrastructure, account, or credential details.
- [ ] Passes the leak scan:

```bash
python3 scripts/leak_scan.py .
```
