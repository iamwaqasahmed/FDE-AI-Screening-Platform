"""Show the receipt suite go red. Do not name the interval or the old delay.

The case clock moves from the sent instant by the imported interval. One call leaves the late switch off and the other turns it on. The page prints pass or fail from those two results.
"""

from __future__ import annotations

import argparse
import sys

from alwaha.config.profile import load
from alwaha.engagement.w2d3 import INTERVAL_MINUTES
from alwaha.serve.clock import advance
from alwaha.serve.receipt import due

_SENT = "2027-01-19T09:00:00"


def main(argv: list[str] | None = None) -> None:
    """Print the switch-off result and the switch-on result. Returns nothing.

    argv replaces the process arguments. The profile is loaded, the case clock is advanced from the sent instant, and the two due() calls differ by the late switch.
    """
    parser = argparse.ArgumentParser(description="Flip the receipt switch.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    load(args.profile)
    now = advance(_SENT, INTERVAL_MINUTES)
    off = due(_SENT, now, INTERVAL_MINUTES, False)
    on = due(_SENT, now, INTERVAL_MINUTES, True)
    # A due receipt passes only while the late switch is off. With the switch on, a receipt that is not due is the failure.
    print("switch off: passed" if off == "due" else "switch off: failed")
    print("switch on: failed" if on != "due" else "switch on: passed")


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])
