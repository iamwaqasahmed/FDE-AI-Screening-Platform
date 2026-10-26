"""Show an out-of-order HL7 pair. Do not name the dropped field.

outcomes() returns the sequence that stands in file order and the sequence that stands in sequence order. This page prints both and does not name a field.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w2d2 import hl7_rows
from alwaha.serve.hl7 import outcomes


def main(argv: list[str] | None = None) -> None:
    """Print the file-order sequence and the sequence-order sequence. Returns nothing.

    argv replaces the process arguments. The profile is loaded, then the HL7 rows are applied both ways.
    """
    parser = argparse.ArgumentParser(description="Apply an out-of-order HL7 pair.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    load(args.profile)
    file_final, ordered_final = outcomes(hl7_rows())
    print(f"file order: sequence {file_final} stands")
    print(f"sequence order: sequence {ordered_final} stands")


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])
