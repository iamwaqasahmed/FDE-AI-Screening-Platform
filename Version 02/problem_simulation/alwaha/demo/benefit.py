"""Show the finance question about the double-counted benefit."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w4d5 import gold


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show the question about the double-counted benefit.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    print(gold(load(args.profile))["demo"]["question"])


if __name__ == "__main__":
    main(sys.argv[1:])
