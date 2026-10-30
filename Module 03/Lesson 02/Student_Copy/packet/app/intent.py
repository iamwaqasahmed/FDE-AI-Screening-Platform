"""Call every message a status question.

classify does not read the message. The label is status for
every row.
"""

from __future__ import annotations


def classify(row: dict) -> str:
    """Return the status label.

    row is not read. The text of the message does not change
    the label this function returns.
    """
    # Every message receives the same label.
    return "status"
