"""Answer a preparation question from the service catalog."""

from __future__ import annotations


def lookup(rows: list[dict], clinic: str) -> dict:
    # The row whose clinic matches. The answer does not carry a document id.
    row = next(item for item in rows if item["clinic"] == clinic)
    return {"clinic": clinic, "prep": row["prep"]}
