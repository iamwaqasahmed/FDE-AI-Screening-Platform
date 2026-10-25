"""Name every log row a pass."""

from __future__ import annotations


def classify(row: dict) -> str:
    del row
    return "pass"
