"""Keep version and audience, and refuse a staff document to a patient."""

from __future__ import annotations


def cite(row: dict) -> dict | None:
    if row.get("asker") == "patient" and row.get("audience") == "staff":
        return None
    return {"audience": row.get("audience"), "doc_id": row.get("doc_id"), "version": row.get("version")}


def meets_budget(value: float, floor: float) -> bool:
    return float(value) + 1e-9 >= float(floor)
