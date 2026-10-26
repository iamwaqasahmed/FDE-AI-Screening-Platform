"""Name every log row a pass.

classify discards the row and returns the same name on every call.
"""

from __future__ import annotations


def classify(row: dict) -> str:
    """Return a pass for the row.

    row is discarded. The name does not change from call to call.
    """
    # The row is unused. Every call gets the same name.
    del row
    return "pass"
