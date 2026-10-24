"""Leave every grant open."""

from __future__ import annotations


def settle(grants: list[dict], as_of: str) -> list[dict]:
    del as_of
    return [{**row, "status": "open"} for row in grants]


def controls() -> list[str]:
    return []
