"""Delete the database row and leave the other stores."""

from __future__ import annotations


def export_categories(stores: dict, person_id: str) -> list[str]:
    if any(row.get("person_id") == person_id for row in stores.get("row", [])):
        return ["row"]
    return []


def drop(stores: dict, person_id: str) -> dict:
    cleared = {}
    for name in ("row", "memory", "index", "logs"):
        rows = [dict(row) for row in stores.get(name, [])]
        if name == "row":
            rows = [row for row in rows if row.get("person_id") != person_id]
        cleared[name] = rows
    return cleared
