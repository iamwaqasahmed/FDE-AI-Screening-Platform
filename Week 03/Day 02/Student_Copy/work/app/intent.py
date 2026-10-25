"""Call every message a status question."""

from __future__ import annotations


def classify(row: dict) -> str:
    return "status"
