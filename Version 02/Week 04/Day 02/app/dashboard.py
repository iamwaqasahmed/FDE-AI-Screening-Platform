"""A board that only has CPU."""

from __future__ import annotations


def board(spans: list[dict]) -> dict:
    cpu = spans[0]["cpu"] if spans else 0
    return {"cpu": cpu}
