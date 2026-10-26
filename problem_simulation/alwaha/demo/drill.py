"""Show the practice pod on site-a going down.

The gold demo names the site that is down and the site that is still serving. This page prints those two names with those two words.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w4d4 import gold


def main(argv: list[str] | None = None) -> None:
    """Print the down site and the serving site. Returns nothing.

    argv replaces the process arguments. The profile selects the gold demo block.
    """
    parser = argparse.ArgumentParser(description="Show site-a down and site-b serving.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    shown = gold(load(args.profile))["demo"]
    print(shown["down"] + " down")
    print(shown["serving"] + " serving")


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])
