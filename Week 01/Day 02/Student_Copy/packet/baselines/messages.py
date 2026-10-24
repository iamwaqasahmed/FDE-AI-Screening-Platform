"""One-feature baseline. Count messages that contain the word status.

The rate is the share of rows whose text contains the word status,
ignoring letter case. A question can ask where a referral stands and
still miss that word. Read the message file and find one. This script
prints only the share. It does not list the misses.

Read the message file where it sits. Do not copy it into a prompt or
into the work folder.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def load_rows(path: str | Path) -> list[dict[str, str]]:
    """Read the message file. Each row is one message_id and one text."""
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def rate(rows: list[dict[str, str]]) -> float:
    """Share of messages that contain the word status."""
    if not rows:
        raise SystemExit("The message file has no rows.")
    hits = sum("status" in row["text"].lower() for row in rows)
    return hits / len(rows)


def show(value: float) -> str:
    """Four digits after the decimal point."""
    return f"{value:.4f}"


def main(argv: list[str] | None = None) -> None:
    """Print one line that starts with keyword."""
    parser = argparse.ArgumentParser(description="Print the share of messages containing status.")
    parser.add_argument("csv_path")
    args = parser.parse_args(argv)
    print(f"keyword {show(rate(load_rows(args.csv_path)))}")


if __name__ == "__main__":
    main(sys.argv[1:])
