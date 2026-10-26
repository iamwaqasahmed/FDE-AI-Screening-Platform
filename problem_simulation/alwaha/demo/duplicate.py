"""Show a near-duplicate leaflet pair. One is superseded. The clause stays off the page.

The two titles come from the gold leaflet list, in that list's order. The page then prints that one of them is superseded. The clause that distinguishes them is not printed.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w3d3 import gold


def main(argv: list[str] | None = None) -> None:
    """Print the two leaflet titles and the superseded line. Returns nothing.

    argv replaces the process arguments. The profile selects the gold leaflet list. The first title is printed before the second.
    """
    parser = argparse.ArgumentParser(description="Show two leaflets, one of them superseded.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    titles = gold(load(args.profile))["leaflets"]
    print(titles[0])
    print(titles[1])
    print("one is superseded")


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])
