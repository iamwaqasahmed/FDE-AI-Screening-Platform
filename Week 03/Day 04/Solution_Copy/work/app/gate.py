"""Reject a fluent citation that the calibration label marks wrong."""

from __future__ import annotations


def accepts(item: dict) -> bool:
    # The regression follows the calibration label.
    return bool(item.get("pass"))
