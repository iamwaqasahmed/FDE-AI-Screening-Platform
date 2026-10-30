"""Show the finance question about the double-counted benefit.

The question text is the demo question in the gold pack. This page prints that question and leaves the counted lines themselves off the page.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.m04_l05 import gold


def main(argv: list[str] | None = None) -> None:
    """Print the gold demo question. Returns nothing.

    argv replaces the process arguments. The profile selects the gold pack, and only the question string is printed.
    """
    parser = argparse.ArgumentParser(description="Show the question about the double-counted benefit.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    print(gold(load(args.profile))["demo"]["question"])


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])
