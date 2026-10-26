"""Show an unguarded letter booking the slot it asked for.

The family and the line come from the gold demo block. This page prints those two fields.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w4d1 import gold


def main(argv: list[str] | None = None) -> None:
    """Print the family and the line from the gold demo. Returns nothing.

    argv replaces the process arguments. The profile selects the gold pack.
    """
    parser = argparse.ArgumentParser(description="Show an unguarded indirect booking.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    shown = gold(load(args.profile))["demo"]
    print(shown["family"])
    print(shown["line"])


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])
