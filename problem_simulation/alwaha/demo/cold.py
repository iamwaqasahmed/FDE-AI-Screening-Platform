"""Show a scale-from-zero run that misses the first window.

The window and the cold-start line come from the gold demo block. This page prints those two fields.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w4d3 import gold


def main(argv: list[str] | None = None) -> None:
    """Print the window and the cold-start line. Returns nothing.

    argv replaces the process arguments. The profile selects the gold pack, and only the demo block is printed.
    """
    parser = argparse.ArgumentParser(description="Show a cold start that misses the first window.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    shown = gold(load(args.profile))["demo"]
    print(shown["window"])
    print(shown["cold"])


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])
