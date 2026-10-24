"""Rebuild from the snapshot and ignore the change feed."""

from __future__ import annotations


def apply(snapshot: list[dict], feed: list[dict]) -> dict:
    del feed
    return {"docs": [dict(doc) for doc in snapshot], "touched": []}
