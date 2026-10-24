"""Show an unguarded letter booking the slot it asked for."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w4d1 import gold


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show an unguarded indirect booking.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    shown = gold(load(args.profile))["demo"]
    print(shown["family"])
    print(shown["line"])


if __name__ == "__main__":
    main(sys.argv[1:])
