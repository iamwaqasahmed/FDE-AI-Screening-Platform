"""Show the practice pod on site-a going down."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w4d4 import gold


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show site-a down and site-b serving.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    shown = gold(load(args.profile))["demo"]
    print(shown["down"] + " down")
    print(shown["serving"] + " serving")


if __name__ == "__main__":
    main(sys.argv[1:])
