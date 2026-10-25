"""Keep version and audience, and refuse a staff document to a patient."""

from __future__ import annotations


def cite(row: dict) -> dict | None:
    # A patient does not receive a staff document.
    if row.get("asker") == "patient" and row.get("audience") == "staff":
        return None
    # A kept citation carries the audience, the document id, and the version.
    return {
        "audience": row.get("audience"),
        "doc_id": row.get("doc_id"),
        "version": row.get("version"),
    }


def meets_budget(value: float, floor: float) -> bool:
    # The value clears the floor when it is at or above that floor.
    return float(value) + 1e-9 >= float(floor)
