"""Name one drift and stop.

name discards the row and always returns the hours label. The row
is not read, so every call gets the same name.
"""

from __future__ import annotations


def name(row: dict) -> str:
    """Return the hours label for every row.

    The argument is discarded. There is no other label in this module.
    """
    # The row is unused. The label below does not depend on it.
    del row
    return "ramadan hours"
