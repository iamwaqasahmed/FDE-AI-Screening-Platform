"""Accept every booking status."""

from __future__ import annotations


def holds(status: str) -> bool:
    del status
    return True
