#!/usr/bin/env python3
"""Validate task packets and result artifacts for required review structure."""

from __future__ import annotations

import argparse
from pathlib import Path


TASK_REQUIRED = [
    "## Objective",
    "## Scope",
    "## Required Inputs",
    "## Allowed Actions",
    "## Forbidden Actions",
    "## Result Contract",
]

RESULT_REQUIRED = [
    "## Verdict",
    "## Evidence",
    "## Work Completed",
    "## Risks",
    "## What Remains Unproven",
    "## Manager Review Needed",
]

FORBIDDEN_PHRASES = [
    "do whatever",
    "use your judgment",
    "no need to report",
    "submit automatically",
]


def validate(path: Path, required: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    for heading in required:
        if heading not in text:
            errors.append(f"missing heading: {heading}")
    lowered = text.lower()
    for phrase in FORBIDDEN_PHRASES:
        if phrase in lowered:
            errors.append(f"unsafe phrase: {phrase}")
    if "```text" not in text and "Result Contract" in required:
        errors.append("missing fenced text result path")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--kind", choices=["task", "result"], required=True)
    args = parser.parse_args()

    required = TASK_REQUIRED if args.kind == "task" else RESULT_REQUIRED
    errors = validate(args.path, required)
    if errors:
        print(f"{args.path}: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"{args.path}: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
