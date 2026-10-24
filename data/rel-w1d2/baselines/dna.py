"""One-feature baseline. Predict a missed visit when prior_dna is at least 1."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def load_rows(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def split_mask(rows: list[dict[str, str]], split: str) -> list[bool]:
    if split == "row":
        return [index % 5 == 0 for index in range(len(rows))]
    people = sorted({row["person_id"] for row in rows})
    held = set(people[int(len(people) * 0.7) :])
    return [row["person_id"] in held for row in rows]


def chosen(rows: list[dict[str, str]], split: str) -> list[dict[str, str]]:
    return [row for row, keep in zip(rows, split_mask(rows, split)) if keep]


def score(rows: list[dict[str, str]], split: str) -> float:
    test = chosen(rows, split)
    if not test:
        raise SystemExit("The split has no rows.")
    hits = 0
    for row in test:
        guess = 1 if int(row["prior_dna"]) >= 1 else 0
        if guess == int(row["did_not_attend"]):
            hits += 1
    return hits / len(test)


def shared(rows: list[dict[str, str]]) -> int:
    mask = split_mask(rows, "row")
    test_people = {row["person_id"] for row, keep in zip(rows, mask) if keep}
    train_people = {row["person_id"] for row, keep in zip(rows, mask) if not keep}
    return len(test_people & train_people)


def show(value: float) -> str:
    return f"{value:.4f}"


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Score prior_dna >= 1 on one split.")
    parser.add_argument("csv_path")
    parser.add_argument("--split", choices=("row", "person"), required=True)
    args = parser.parse_args(argv)
    print(f"{args.split} {show(score(load_rows(args.csv_path), args.split))}")


if __name__ == "__main__":
    main(sys.argv[1:])
