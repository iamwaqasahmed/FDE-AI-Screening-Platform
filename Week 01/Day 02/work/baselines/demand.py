"""One-feature baseline. Score 2026 by last year's month, and by the earlier mean."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

LATER = 2026


def load_rows(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _pairs(rows: list[dict[str, str]]) -> dict[tuple[int, int], int]:
    return {(int(row["year"]), int(row["month"])): int(row["visits"]) for row in rows}


def seasonal(rows: list[dict[str, str]]) -> float:
    by_month = _pairs(rows)
    errors = []
    for (year, month), actual in sorted(by_month.items()):
        if year != LATER:
            continue
        errors.append(abs(actual - by_month[(year - 1, month)]))
    if not errors:
        raise SystemExit("The demand file has no later window.")
    return sum(errors) / len(errors)


def mean_error(rows: list[dict[str, str]]) -> float:
    history = [int(row["visits"]) for row in rows if int(row["year"]) < LATER]
    later = [int(row["visits"]) for row in rows if int(row["year"]) == LATER]
    if not history or not later:
        raise SystemExit("The demand file has no later window.")
    average = sum(history) / len(history)
    return sum(abs(value - average) for value in later) / len(later)


def show(value: float) -> str:
    return f"{value:.4f}"


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Print the seasonal and mean errors on 2026.")
    parser.add_argument("csv_path")
    args = parser.parse_args(argv)
    rows = load_rows(args.csv_path)
    print(f"seasonal {show(seasonal(rows))}")
    print(f"mean {show(mean_error(rows))}")


if __name__ == "__main__":
    main(sys.argv[1:])
