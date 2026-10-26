"""Show the Ain change-request card. The nightly-file sentence stays off the page.

This command loads the selected profile, prints the public change-request card, and numbers the questions under it. The nightly-file sentence is not part of that card or that list.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w2d5 import CARD, QUESTIONS


def main(argv: list[str] | None = None) -> None:
    """Print the public card and the numbered questions. Returns nothing.

    argv replaces the process arguments when a caller supplies them. Loading the profile binds the world before the page is printed. The card and the questions are the public engagement text.
    """
    parser = argparse.ArgumentParser(description="Read the Ain change-request card.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    load(args.profile)
    print(CARD)
    for index, question in enumerate(QUESTIONS, start=1):
        print(f"{index}. {question}")


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])
