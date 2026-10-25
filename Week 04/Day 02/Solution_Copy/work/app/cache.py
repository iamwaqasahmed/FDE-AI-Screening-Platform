"""Drop cached hours when the Ramadan circular changes."""

from __future__ import annotations


def answer(store: dict, event: dict) -> str:
    if event.get("topic") == "document.changed" and event.get("doc_id") == "circ-ramadan-hours":
        return str(event.get("body") or "")
    return str(store.get("hours") or "")
