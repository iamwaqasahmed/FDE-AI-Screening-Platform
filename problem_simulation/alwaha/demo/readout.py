"""Show the steering opening from the public card. Hidden facts stay off the page.

The opening line is the cdo persona's public first line. The questions are numbered under it. Hidden facts are not read onto the page.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.catalog import PERSONAS
from alwaha.engagement.day5 import QUESTIONS


def main(argv: list[str] | None = None) -> None:
    """Print the cdo opening line and the numbered questions. Returns nothing.

    argv replaces the process arguments. The profile is loaded before the public card is read. Other personas are not printed.
    """
    parser = argparse.ArgumentParser(description="Read the steering opening from the public card.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    load(args.profile)
    # The opening line is the cdo persona. Other personas are not this page.
    card = next(row for row in PERSONAS if row["id"] == "cdo")
    print(card["says_first"])
    for index, question in enumerate(QUESTIONS, start=1):
        print(f"{index}. {question}")


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])
