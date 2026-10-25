"""Mark a citation with the calibration label."""

from __future__ import annotations


def mark(item: dict) -> bool:
    # The calibration label is the pass field.
    return bool(item.get("pass"))
