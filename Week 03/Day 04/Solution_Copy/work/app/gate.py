"""Reject a fluent citation that the calibration label marks wrong.

accepts returns the calibration label. A false label is rejected.
A true label is accepted. A missing label is rejected.
"""

from __future__ import annotations


def accepts(item: dict) -> bool:
    """Return the calibration label on the item.

    item is a citation record. The label is the pass field. A missing
    pass field is false.
    """
    # The regression follows the calibration label.
    return bool(item.get("pass"))
