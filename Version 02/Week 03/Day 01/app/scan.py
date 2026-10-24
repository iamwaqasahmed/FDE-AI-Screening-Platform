"""Accept every file."""

from __future__ import annotations


def accept(text: str, national_ids: list[str]) -> bool:
    del text, national_ids
    return True
