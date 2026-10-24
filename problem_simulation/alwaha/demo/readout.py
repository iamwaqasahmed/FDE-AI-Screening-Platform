"""Show the steering opening from the public card. Hidden facts stay off the page."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.catalog import PERSONAS
from alwaha.engagement.day5 import QUESTIONS


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Read the steering opening from the public card.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    load(args.profile)
    card = next(row for row in PERSONAS if row["id"] == "cdo")
    print(card["says_first"])
    for index, question in enumerate(QUESTIONS, start=1):
        print(f"{index}. {question}")


if __name__ == "__main__":
    main(sys.argv[1:])
