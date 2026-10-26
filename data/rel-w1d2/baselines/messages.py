"""One-feature baseline. Count messages that contain the word status.

The share is the number of texts that contain that word, in lower case, divided by the number of rows. An empty file stops, because the share would have no denominator.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def load_rows(path: str | Path) -> list[dict[str, str]]:
    """Return every CSV row as a dictionary of strings, keyed by the header."""
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def rate(rows: list[dict[str, str]]) -> float:
    """Return the share of rows whose text contains the status word."""
    if not rows:
        # The share needs a denominator, so an empty file stops the run.
        raise SystemExit("The message file has no rows.")
    hits = sum("status" in row["text"].lower() for row in rows)
    return hits / len(rows)


def show(value: float) -> str:
    """Format the share to the printed width."""
    return f"{value:.4f}"


def main(argv: list[str] | None = None) -> None:
    """Print the keyword share for the CSV path in the arguments.

    Read that CSV, compute the share, and print it.
    """
    parser = argparse.ArgumentParser(description="Print the share of messages containing status.")
    parser.add_argument("csv_path")
    args = parser.parse_args(argv)
    print(f"keyword {show(rate(load_rows(args.csv_path)))}")


if __name__ == "__main__":
    main(sys.argv[1:])
