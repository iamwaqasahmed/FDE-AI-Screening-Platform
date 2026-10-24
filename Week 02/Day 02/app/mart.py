"""Read the wait-time extract and trust the wait figure."""

from __future__ import annotations


def _cell(text: str, column: str) -> str:
    lines = [line for line in text.splitlines() if line.strip()]
    header = lines[0].split(",")
    values = lines[1].split(",")
    return values[header.index(column)]


def read(text: str) -> dict:
    return {"clock": "wait_days", "trusted": True, "wait": int(_cell(text, "wait_days"))}
