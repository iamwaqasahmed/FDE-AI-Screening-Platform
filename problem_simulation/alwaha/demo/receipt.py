"""Show the receipt suite go red. Do not name the interval or the old delay."""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w2d3 import INTERVAL_MINUTES
from alwaha.serve.clock import advance
from alwaha.serve.receipt import due

_SENT = "2027-01-19T09:00:00"


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Flip the receipt switch.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    load(args.profile)
    now = advance(_SENT, INTERVAL_MINUTES)
    off = due(_SENT, now, INTERVAL_MINUTES, False)
    on = due(_SENT, now, INTERVAL_MINUTES, True)
    print("switch off: passed" if off == "due" else "switch off: failed")
    print("switch on: failed" if on != "due" else "switch on: passed")


if __name__ == "__main__":
    main(sys.argv[1:])
