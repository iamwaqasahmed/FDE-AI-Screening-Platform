"""Reject a fluent citation that the calibration label marks wrong."""

from __future__ import annotations


def accepts(item: dict) -> bool:
    return bool(item.get("pass"))
