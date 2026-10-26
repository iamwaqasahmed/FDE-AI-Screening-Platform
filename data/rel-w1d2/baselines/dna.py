"""One-feature baseline. Predict a missed visit when prior_dna is at least 1.

A baseline is the simple score a heavier method has to beat.
This script uses one column only: prior_dna.

You will run it twice.

- --split row keeps every row whose position in the file is a multiple
  of 5. The same person_id can appear in a kept row and in a row that
  was not kept. Paste this line into your notes. The memo does not use it.
- --split person sorts the distinct person_id values, holds back the
  last 30 percent, and scores only the rows for those people. A person
  is entirely in the score or entirely out of it. The memo uses this line.

The label is did_not_attend: 1 means the patient missed that visit.
The guess is 1 when prior_dna is at least 1, and 0 otherwise.
The printed number is the share of scored rows where the guess matches
the label.

Other columns in the file are not read. Leave them out of this script.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def load_rows(path: str | Path) -> list[dict[str, str]]:
    """Read the visit file. Each row is one appointment for one person."""
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def split_mask(rows: list[dict[str, str]], split: str) -> list[bool]:
    """Mark the rows that belong in the score.

    row: True on every 5th position, counting from 0.
    person: True when person_id is in the last 30 percent of the sorted ids.
    """
    if split == "row":
        return [index % 5 == 0 for index in range(len(rows))]
    people = sorted({row["person_id"] for row in rows})
    # The slice starts at 70 percent of the sorted id list and runs to the end.
    held = set(people[int(len(people) * 0.7) :])
    return [row["person_id"] in held for row in rows]


def chosen(rows: list[dict[str, str]], split: str) -> list[dict[str, str]]:
    """Keep only the rows the mask marked for the score."""
    return [row for row, keep in zip(rows, split_mask(rows, split)) if keep]


def score(rows: list[dict[str, str]], split: str) -> float:
    """Share of scored rows where prior_dna >= 1 matches did_not_attend.

    Keep the held-out rows, guess a missed visit when prior_dna is at least 1, and return the share of rows where that guess matches the label.
    """
    test = chosen(rows, split)
    if not test:
        raise SystemExit("The split has no rows.")
    hits = 0
    for row in test:
        # A prior count of at least 1 predicts a missed visit.
        guess = 1 if int(row["prior_dna"]) >= 1 else 0
        if guess == int(row["did_not_attend"]):
            hits += 1
    return hits / len(test)


def shared(rows: list[dict[str, str]]) -> int:
    """How many person ids sit on both sides of the row split.

    Today's commands do not print this count. It is here so you can see,
    in the code, that the row split does not keep a person on one side.
    """
    mask = split_mask(rows, "row")
    test_people = {row["person_id"] for row, keep in zip(rows, mask) if keep}
    train_people = {row["person_id"] for row, keep in zip(rows, mask) if not keep}
    return len(test_people & train_people)


def show(value: float) -> str:
    """Four digits after the decimal point, so the memo can paste a stable token."""
    return f"{value:.4f}"


def main(argv: list[str] | None = None) -> None:
    """Print one line: the split name, then the score.

    Read the CSV and the split name, score that split, and print both on one line.
    """
    parser = argparse.ArgumentParser(description="Score prior_dna >= 1 on one split.")
    parser.add_argument("csv_path")
    parser.add_argument("--split", choices=("row", "person"), required=True)
    args = parser.parse_args(argv)
    print(f"{args.split} {show(score(load_rows(args.csv_path), args.split))}")


if __name__ == "__main__":
    main(sys.argv[1:])
