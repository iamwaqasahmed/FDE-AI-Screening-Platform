"""Show a mother and a newborn who share one national id and stay two people."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w3d1 import gold


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show two MRNs that share one national id.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    shown = gold(load(args.profile))["demo"]
    print(shown["mrn_mother"])
    print(shown["mrn_newborn"])
    print(shown["national_id"])
    print("These two MRNs stay two people.")


if __name__ == "__main__":
    main(sys.argv[1:])
