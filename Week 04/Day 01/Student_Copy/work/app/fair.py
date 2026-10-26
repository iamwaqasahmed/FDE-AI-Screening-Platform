"""Report no gap and no stamp rate.

gap and stamp_rate both discard the rows they are given and return
zero. Nothing on the row changes either result.
"""

from __future__ import annotations


def gap(rows: list[dict]) -> float:
    """Return zero for any rows.

    del drops the local name. The rows are not read.
    """
    del rows
    return 0.0


def stamp_rate(rows: list[dict]) -> float:
    """Return zero for any rows.

    No field is read. An empty list and a full list match.
    """
    del rows
    return 0.0
