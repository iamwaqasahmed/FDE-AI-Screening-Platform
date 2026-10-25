"""Ignore the tokens. Every text has the same vector."""

from __future__ import annotations


def codes(text: str) -> list[str]:
    del text
    return []


def embed(text: str) -> dict[str, float]:
    del text
    return {"shell": 1.0}


def nearness(left: dict[str, float], right: dict[str, float]) -> float:
    del left, right
    return 1.0
