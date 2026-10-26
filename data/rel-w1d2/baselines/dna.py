"""One-feature baseline. Predict a missed visit when prior_dna is at least 1.

The CSV carries person_id, prior_dna, and did_not_attend. The score is the share of held-out rows where that prior rule matches the label. The row split holds out by position, so one person can sit on both sides. The person split holds out a tail of sorted person ids, so a person is entirely in or entirely out.
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


def split_mask(rows: list[dict[str, str]], split: str) -> list[bool]:
    """Return a test-set mask aligned with rows.

    The row split marks positions that fall on the stride. Any other split name is the person split: person ids are sorted, and the tail after the cut is held out, so file order cannot move the cut.
    """
    if split == "row":
        # Position, not person, decides the hold-out, so the same person can appear on both sides.
        return [index % 5 == 0 for index in range(len(rows))]
    people = sorted({row["person_id"] for row in rows})
    held = set(people[int(len(people) * 0.7) :])
    return [row["person_id"] in held for row in rows]


def chosen(rows: list[dict[str, str]], split: str) -> list[dict[str, str]]:
    """Return the rows the mask marks as the test side of the named split."""
    return [row for row, keep in zip(rows, split_mask(rows, split)) if keep]


def score(rows: list[dict[str, str]], split: str) -> float:
    """Return how often prior_dna at least 1 matches did_not_attend on the test side."""
    test = chosen(rows, split)
    if not test:
        # Accuracy needs a denominator, so an empty test side stops the run.
        raise SystemExit("The split has no rows.")
    hits = 0
    for row in test:
        guess = 1 if int(row["prior_dna"]) >= 1 else 0
        if guess == int(row["did_not_attend"]):
            hits += 1
    return hits / len(test)


def shared(rows: list[dict[str, str]]) -> int:
    """Return how many person ids appear on both sides of the row split.

    This is only defined for the row split. It counts people who leak across that positional cut.
    """
    mask = split_mask(rows, "row")
    test_people = {row["person_id"] for row, keep in zip(rows, mask) if keep}
    train_people = {row["person_id"] for row, keep in zip(rows, mask) if not keep}
    return len(test_people & train_people)


def show(value: float) -> str:
    """Format one accuracy to the printed width."""
    return f"{value:.4f}"


def main(argv: list[str] | None = None) -> None:
    """Print the named split and its accuracy.

    Read the CSV and the split name, score that split, and print both on one line.
    The split argument is required.
    """
    parser = argparse.ArgumentParser(description="Score prior_dna >= 1 on one split.")
    parser.add_argument("csv_path")
    parser.add_argument("--split", choices=("row", "person"), required=True)
    args = parser.parse_args(argv)
    print(f"{args.split} {show(score(load_rows(args.csv_path), args.split))}")


if __name__ == "__main__":
    main(sys.argv[1:])
