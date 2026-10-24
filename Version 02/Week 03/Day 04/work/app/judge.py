"""Mark a citation with the calibration label."""

from __future__ import annotations


def mark(item: dict) -> bool:
    return bool(item.get("pass"))
