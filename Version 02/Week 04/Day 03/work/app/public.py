"""Return a cached public answer without a model call."""

from __future__ import annotations


def answer(store: dict, row: dict) -> dict:
    key = str(row.get("id") or "")
    if key in store:
        return {"body": str(store[key]), "calls": 0}
    return {"body": str(row.get("text") or ""), "calls": 1}
