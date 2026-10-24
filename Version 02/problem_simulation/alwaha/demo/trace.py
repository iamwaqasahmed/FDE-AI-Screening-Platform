"""Show a trace that carries a tool, a hash, and a token count."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w4d2 import gold


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show a tool, a hash, and a token count.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    shown = gold(load(args.profile))["demo"]
    print(shown["tool"])
    print(shown["hash"])
    print(shown["tokens"])


if __name__ == "__main__":
    main(sys.argv[1:])
