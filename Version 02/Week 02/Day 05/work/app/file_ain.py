"""Keep yesterday's file when the night drop is missing."""

from __future__ import annotations


def apply_file(previous: dict | None, arrived: dict | None) -> dict | None:
    if arrived is None:
        return previous
    return arrived
