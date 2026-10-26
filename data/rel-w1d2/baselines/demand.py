"""One-feature baseline. Score 2026 by last year's month, and by the earlier mean.

The CSV is year, month, and visits. The seasonal figure is the average absolute gap between each later-year month and the same month a year earlier. The mean figure is the average absolute gap between those later months and the average visit count of every earlier row. Both stop if the later window is missing, because an empty window cannot be averaged.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

LATER = 2026


def load_rows(path: str | Path) -> list[dict[str, str]]:
    """Return every CSV row as a dictionary of strings, keyed by the header."""
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _pairs(rows: list[dict[str, str]]) -> dict[tuple[int, int], int]:
    """Map each year and month to its visit count so a prior month can be looked up."""
    return {(int(row["year"]), int(row["month"])): int(row["visits"]) for row in rows}


def seasonal(rows: list[dict[str, str]]) -> float:
    """Return the mean absolute error of forecasting each later month from the same month a year earlier."""
    by_month = _pairs(rows)
    errors = []
    for (year, month), actual in sorted(by_month.items()):
        if year != LATER:
            # Earlier years are the forecast source. Only the later year is scored.
            continue
        errors.append(abs(actual - by_month[(year - 1, month)]))
    if not errors:
        # An empty later window would divide by zero, so the run stops instead.
        raise SystemExit("The demand file has no later window.")
    return sum(errors) / len(errors)


def mean_error(rows: list[dict[str, str]]) -> float:
    """Return the mean absolute error of forecasting every later month with the earlier average."""
    history = [int(row["visits"]) for row in rows if int(row["year"]) < LATER]
    later = [int(row["visits"]) for row in rows if int(row["year"]) == LATER]
    if not history or not later:
        # Either side being empty means there is no before-and-after comparison.
        raise SystemExit("The demand file has no later window.")
    average = sum(history) / len(history)
    return sum(abs(value - average) for value in later) / len(later)


def show(value: float) -> str:
    """Format one error to the printed width used by both figures."""
    return f"{value:.4f}"


def main(argv: list[str] | None = None) -> None:
    """Print the seasonal error and the mean error for the CSV path in the arguments."""
    parser = argparse.ArgumentParser(description="Print the seasonal and mean errors on 2026.")
    parser.add_argument("csv_path")
    args = parser.parse_args(argv)
    rows = load_rows(args.csv_path)
    print(f"seasonal {show(seasonal(rows))}")
    print(f"mean {show(mean_error(rows))}")


if __name__ == "__main__":
    main(sys.argv[1:])
