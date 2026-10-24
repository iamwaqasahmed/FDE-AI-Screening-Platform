"""Keep the cached hours after the circular."""

from __future__ import annotations


def answer(store: dict, event: dict) -> str:
    del event
    return str(store.get("hours") or "")
