#!/usr/bin/env python3
"""Small path-only leak scanner for this repo."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path


RULES = {
    "private_key_block": re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA |)?PRIVATE KEY-----"),
    "token_like": re.compile(r"\b(?:sk-|hf_|gh[oprsu]_)[A-Za-z0-9_-]{20,}\b"),
    "secret_assignment": re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password)\s*=\s*['\"]?[^'\"\s#]{8,}"),
    "private_context": re.compile(
        r"(?i)(?:/"
        + r"Users/|\.env\b|wallet|hotkey|seed "
        + r"phrase|ssh\.|vast\.ai)"
    ),
}


def main() -> int:
    roots = [Path(arg) for arg in sys.argv[1:] or ["."]]
    findings: list[tuple[str, str]] = []
    for root in roots:
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules", "__pycache__"}]
            for name in filenames:
                path = Path(dirpath) / name
                if path.suffix.lower() in {".png", ".jpg", ".pdf", ".db", ".sqlite", ".pyc"}:
                    continue
                text = path.read_text(encoding="utf-8", errors="ignore")
                for rule, pattern in RULES.items():
                    if pattern.search(text):
                        findings.append((str(path), rule))
    for path, rule in findings:
        print(f"{path}: {rule}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
