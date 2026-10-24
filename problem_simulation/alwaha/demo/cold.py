"""Show a scale-from-zero run that misses the first window."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w4d3 import gold


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show a cold start that misses the first window.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    shown = gold(load(args.profile))["demo"]
    print(shown["window"])
    print(shown["cold"])


if __name__ == "__main__":
    main(sys.argv[1:])
