"""One-feature baseline. Count messages that contain the word status."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def load_rows(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def rate(rows: list[dict[str, str]]) -> float:
    if not rows:
        raise SystemExit("The message file has no rows.")
    hits = sum("status" in row["text"].lower() for row in rows)
    return hits / len(rows)


def show(value: float) -> str:
    return f"{value:.4f}"


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Print the share of messages containing status.")
    parser.add_argument("csv_path")
    args = parser.parse_args(argv)
    print(f"keyword {show(rate(load_rows(args.csv_path)))}")


if __name__ == "__main__":
    main(sys.argv[1:])
