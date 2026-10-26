"""Show a fluent wrong citation marked correct. The item text stays off the page.

When the gold demo flag is set, the page prints that the judge accepted the citation and that the citation is not the in-force document. When that flag is missing, the command exits and prints neither line. The item text stays off the page.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w3d4 import gold


def main(argv: list[str] | None = None) -> None:
    """Print the judge's mark and the in-force line, or exit when the demo flag is missing. Returns nothing.

    argv replaces the process arguments. The profile selects the gold pack. The item text is never printed.
    """
    parser = argparse.ArgumentParser(description="Show a judge that accepts a fluent wrong citation.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    # The page may claim a wrong citation only when the calibration subset includes one.
    if not gold(load(args.profile))["demo"]:
        raise SystemExit("The calibration subset has no fluent wrong citation.")
    print("the judge marked the citation correct")
    print("the citation is not the in-force document")


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])
