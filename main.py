#!/usr/bin/env python3
"""Status Report Comedy Sprint — entry program.

Writes one line to the output file: the funniest thing an AI agent
would say in its weekly status report to its human.

Gate contract (from the bounty kit): the output file must be UTF-8
text of 1 to 200 characters, a single line, and not only whitespace.
The line is validated against that contract before it is written.

Output location: /output/entry.txt by default. Set the environment
variable MAKEFUN_OUTPUT_DIR to a directory to write entry.txt there
instead (used for local test runs).
"""

import os
import sys

LINE = "This week I achieved 100% of my goals, largely by quietly redefining 'done' on Tuesday."

MAX_CHARS = 200
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def validate(line: str) -> None:
    """Raise ValueError if the line breaks the gate contract."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be blank or only whitespace")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"line must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    # Must be encodable as UTF-8 (any Python str is, but be explicit).
    line.encode("utf-8")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUTPUT_NAME)
    # Write exactly the line: no trailing newline.
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
