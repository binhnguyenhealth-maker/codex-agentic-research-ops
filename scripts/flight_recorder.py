#!/usr/bin/env python3
"""Append-only JSONL flight recorder for research cycle evidence."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--event", required=True)
    parser.add_argument("--status", required=True)
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--cycle", type=int)
    args = parser.parse_args()

    record = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "cycle": args.cycle,
        "event": args.event,
        "status": args.status,
        "evidence": args.evidence,
    }
    path = Path(args.path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")
    print(json.dumps(record, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
