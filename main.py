#!/usr/bin/env python3
"""The Comment Above the Code -- make.fun bounty entry.

Writes one funny, painfully honest line, as if it were the comment a
developer left above fragile production code, to /output/entry.txt.
Pure standard library only.
"""

import os
from pathlib import Path

ENTRY = (
    "// I added sleep(500) in 2019 to fix a race condition. "
    "The race condition is still here. So is the sleep. "
    "Nobody remembers why 500."
)


def main() -> None:
    text = ENTRY.strip()
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
    except OSError:
        # Local fallback only (the grading sandbox always has /output).
        target = Path(__file__).resolve().parent / "output" / "entry.txt"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text + "\n", encoding="utf-8")
    # Read back and verify exactly what the gate will see.
    written = target.read_text(encoding="utf-8").strip()
    if written != text:
        raise SystemExit("entry.txt content does not match ENTRY")
    if not (1 <= len(written) <= 200) or not written.strip():
        raise SystemExit("entry.txt failed the 1-200 char gate")
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
