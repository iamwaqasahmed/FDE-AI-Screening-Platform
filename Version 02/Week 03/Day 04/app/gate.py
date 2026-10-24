"""Accept a citation when it is fluent."""

from __future__ import annotations


def accepts(item: dict) -> bool:
    return bool(item.get("fluent"))
