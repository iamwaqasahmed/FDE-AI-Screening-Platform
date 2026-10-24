"""Replace the schedule even when the night file is missing."""

from __future__ import annotations


def apply_file(previous: dict | None, arrived: dict | None) -> dict | None:
    del previous
    if arrived is None:
        return None
    return arrived
