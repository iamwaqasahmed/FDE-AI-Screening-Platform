"""Show an out-of-order HL7 pair. Do not name the dropped field."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w2d2 import hl7_rows
from alwaha.serve.hl7 import outcomes


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Apply an out-of-order HL7 pair.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    load(args.profile)
    file_final, ordered_final = outcomes(hl7_rows())
    print(f"file order: sequence {file_final} stands")
    print(f"sequence order: sequence {ordered_final} stands")


if __name__ == "__main__":
    main(sys.argv[1:])
