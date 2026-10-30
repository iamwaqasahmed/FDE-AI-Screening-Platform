"""Show a trace that carries a tool, a hash, and a token count.

The tool, the hash, and the token count come from the gold demo block and are printed in that order.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.m04_l02 import gold


def main(argv: list[str] | None = None) -> None:
    """Print the tool, the hash, and the token count from the gold demo. Returns nothing.

    argv replaces the process arguments. The profile selects the gold pack.
    """
    parser = argparse.ArgumentParser(description="Show a tool, a hash, and a token count.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    shown = gold(load(args.profile))["demo"]
    print(shown["tool"])
    print(shown["hash"])
    print(shown["tokens"])


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])
