"""Treat every receipt as due."""

from __future__ import annotations


def receipt_state(sent_at: str, now: str, minutes: int, switch_on: bool) -> str:
    del sent_at, now, minutes, switch_on
    return "due"
