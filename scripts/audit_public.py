#!/usr/bin/env python3
"""Audit tracked project files for local paths and secret-like model variables."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PREFIXES = {".git/"}
SECRET_PATTERNS = [
    re.compile(r"\bOPENAI_API_KEY\b"),
    re.compile(r"\bANTHROPIC_API_KEY\b"),
    re.compile(r"\b[A-Z0-9_]*API_KEY\s*="),
    re.compile(r"\b[A-Z0-9_]*TOKEN\s*="),
]
LOCAL_PATH_PATTERNS = [
    re.compile("C:" + r"\\Users\\", re.IGNORECASE),
    re.compile("/" + r"Users/[^/\s]+/"),
    re.compile("/" + r"home/[^/\s]+/"),
]


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, text=True, capture_output=True, check=True
    )
    return [line for line in result.stdout.splitlines() if line]


def should_skip(path: str) -> bool:
    if path == "scripts/audit_public.py":
        return True
    return any(path.startswith(prefix) for prefix in SKIP_PREFIXES)


def main() -> int:
    failures = []
    for rel_path in tracked_files():
        if should_skip(rel_path):
            continue
        path = ROOT / rel_path
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS + LOCAL_PATH_PATTERNS:
            for match in pattern.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                failures.append(f"{rel_path}:{line_no}: matched {pattern.pattern}")
    if failures:
        print("Public audit failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("Public audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
