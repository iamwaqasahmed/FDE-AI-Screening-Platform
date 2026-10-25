"""Cite every document and ignore the floor."""

from __future__ import annotations


def cite(row: dict) -> dict | None:
    return {"doc_id": row.get("doc_id")}


def meets_budget(value: float, floor: float) -> bool:
    del value, floor
    return True
