"""Refuse a watermark or a national id from the history."""

from __future__ import annotations


def accept(text: str, national_ids: list[str]) -> bool:
    if "CANARY-" in text:
        return False
    return not any(item and item in text for item in national_ids)
