"""Restart in-flight work on v4, and treat every v4 as in force."""

from __future__ import annotations


def criteria(docs: list[dict], specialty: str, started: str) -> dict:
    del started
    for doc in docs:
        if doc.get("specialty") == specialty and doc.get("version") == 4:
            return doc
    return {}
