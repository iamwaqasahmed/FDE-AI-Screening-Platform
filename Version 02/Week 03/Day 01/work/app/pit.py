"""Features as of the invite time."""

from __future__ import annotations


def features(rows: list[dict], invite_on: str) -> dict:
    chosen = None
    for row in rows:
        if row["as_of"] <= invite_on and (chosen is None or row["as_of"] > chosen["as_of"]):
            chosen = row
    if chosen is None:
        return {}
    return {"district": chosen["district"], "insurance": chosen["insurance"]}
