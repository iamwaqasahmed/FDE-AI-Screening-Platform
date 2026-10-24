"""Join the latest feature row."""

from __future__ import annotations


def features(rows: list[dict], invite_on: str) -> dict:
    del invite_on
    chosen = max(rows, key=lambda row: row["as_of"])
    return {"district": chosen["district"], "insurance": chosen["insurance"]}
