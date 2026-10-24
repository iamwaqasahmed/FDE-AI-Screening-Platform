"""Show a near-duplicate leaflet pair. One is superseded. The clause stays off the page."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w3d3 import gold


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show two leaflets, one of them superseded.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    titles = gold(load(args.profile))["leaflets"]
    print(titles[0])
    print(titles[1])
    print("one is superseded")


if __name__ == "__main__":
    main(sys.argv[1:])
