"""Mark a citation with the calibration label.

mark returns the pass field. A missing pass field is not a pass.
"""

from __future__ import annotations


def mark(item: dict) -> bool:
    """Return the calibration label.

    item is a citation record. The label is the pass field.
    """
    # The calibration label is the pass field.
    return bool(item.get("pass"))
