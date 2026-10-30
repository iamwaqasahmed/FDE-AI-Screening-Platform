"""One-feature baseline. Score 2026 by last year's month, and by the earlier mean.

The file has one row per month: year, month, and visits.

seasonal walks each month of 2026, takes the absolute difference from
the same month in 2025, and averages those differences.

mean_error averages every visits value from years before 2026, then
averages the absolute difference of each 2026 month from that one number.

The command prints both lines. A smaller error is the closer score.
The memo uses the seasonal line. Keep the mean line in your notes
beside it.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

# The year the two scores are judged against.
LATER = 2026


def load_rows(path: str | Path) -> list[dict[str, str]]:
    """Read the monthly file. Each row is one year, one month, and a visit count."""
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _pairs(rows: list[dict[str, str]]) -> dict[tuple[int, int], int]:
    """Map (year, month) to the visit count, so a month can be looked up in the year before."""
    return {(int(row["year"]), int(row["month"])): int(row["visits"]) for row in rows}


def seasonal(rows: list[dict[str, str]]) -> float:
    """Average absolute error of 2026 against the same month in 2025.

    Walk each later month, take the absolute gap from the same month one year earlier, average those gaps, and stop when the later window is empty.
    """
    by_month = _pairs(rows)
    errors = []
    for (year, month), actual in sorted(by_month.items()):
        if year != LATER:
            continue
        # The comparison for this month is the same month one year earlier.
        errors.append(abs(actual - by_month[(year - 1, month)]))
    if not errors:
        raise SystemExit("The demand file has no later window.")
    return sum(errors) / len(errors)


def mean_error(rows: list[dict[str, str]]) -> float:
    """Average absolute error of 2026 against the mean of every earlier year.

    Average the visit counts from earlier years, then average how far each later month sits from that one number, and stop when either side is empty.
    """
    history = [int(row["visits"]) for row in rows if int(row["year"]) < LATER]
    later = [int(row["visits"]) for row in rows if int(row["year"]) == LATER]
    if not history or not later:
        raise SystemExit("The demand file has no later window.")
    # That one earlier average is the comparison for every later month.
    average = sum(history) / len(history)
    return sum(abs(value - average) for value in later) / len(later)


def show(value: float) -> str:
    """Four digits after the decimal point."""
    return f"{value:.4f}"


def main(argv: list[str] | None = None) -> None:
    """Print the seasonal line, then the mean line.

    Read the CSV path from the arguments, score both errors, and print each one on its own line.
    """
    parser = argparse.ArgumentParser(description="Print the seasonal and mean errors on 2026.")
    parser.add_argument("csv_path")
    args = parser.parse_args(argv)
    rows = load_rows(args.csv_path)
    print(f"seasonal {show(seasonal(rows))}")
    print(f"mean {show(mean_error(rows))}")


if __name__ == "__main__":
    main(sys.argv[1:])
