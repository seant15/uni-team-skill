#!/usr/bin/env python3
"""Regression harness for lint-ads-output.py.

Both directions are checked. A gate that only rejects is as useless as one that
only accepts, because the first thing a rushed operator does with a gate that
blocks good work is stop running it.

    python skills/uni-output/scripts/fixtures/ads-output/run-fixtures.py

Exit 0 = every fixture landed on its expected verdict. Fixture inventory and
what each one pins: README.md in this folder.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LINTER = HERE.parent.parent / "lint-ads-output.py"

# fixture, --type, expected exit code
CASES = [
    ("good-copy.txt", "meta-copy", 0),
    ("good-kit.txt", "meta-copy", 0),
    ("bad-copy.txt", "meta-copy", 1),
    ("bad-counts.txt", "meta-copy", 1),
    ("bad-five.txt", "meta-copy", 1),
    ("good-targeting.txt", "targeting", 0),
    ("bad-targeting.txt", "targeting", 1),
    ("bad-ideas.txt", "ad-ideas", 1),
    ("bad-brief.txt", "brief", 1),
]


def main() -> int:
    if not LINTER.is_file():
        print(f"run-fixtures: linter not found at {LINTER}", file=sys.stderr)
        return 2

    failures = 0
    for name, kind, want in CASES:
        path = HERE / name
        if not path.is_file():
            print(f"MISSING  {name}")
            failures += 1
            continue
        got = subprocess.run(
            [sys.executable, str(LINTER), str(path), "--type", kind, "--json"],
            capture_output=True,
        ).returncode
        verdict = "PASS" if got == want else "FAIL"
        if got != want:
            failures += 1
        print(f"{verdict}  {name:22} --type {kind:10} exit={got} expected={want}")

    print(f"\n{len(CASES) - failures}/{len(CASES)} fixtures on expected verdict")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
