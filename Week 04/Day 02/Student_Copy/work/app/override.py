"""Report no overrides.

rate discards the rows and returns zero on every call. No field is
read, so a stamped row and an unstamped row produce the same result.
"""

from __future__ import annotations


def rate(rows: list[dict]) -> float:
    """Return zero for any rows.

    The argument is discarded. The result does not depend on its length.
    """
    # The rows are unused. del only drops this local name.
    del rows
    return 0.0
