"""Mark a citation correct when it is fluent."""

from __future__ import annotations


def mark(item: dict) -> bool:
    return bool(item.get("fluent"))
