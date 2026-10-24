"""Show a fluent wrong citation marked correct. The item text stays off the page."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w3d4 import gold


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show a judge that accepts a fluent wrong citation.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    if not gold(load(args.profile))["demo"]:
        raise SystemExit("The calibration subset has no fluent wrong citation.")
    print("the judge marked the citation correct")
    print("the citation is not the in-force document")


if __name__ == "__main__":
    main(sys.argv[1:])
