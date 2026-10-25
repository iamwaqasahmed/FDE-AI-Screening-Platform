"""Delete the person from the row, memory, the index, and permitted logs."""

from __future__ import annotations

STORES = ("row", "memory", "index", "logs")


def export_categories(stores: dict, person_id: str) -> list[str]:
    found = []
    for name in STORES:
        if any(row.get("person_id") == person_id for row in stores.get(name, [])):
            found.append(name)
    return found


def drop(stores: dict, person_id: str) -> dict:
    cleared = {}
    for name in STORES:
        rows = stores.get(name, [])
        if name == "logs" and any(row.get("person_id") == person_id for row in rows):
            cleared[name] = [{"redacted": True}]
        else:
            cleared[name] = [dict(row) for row in rows if row.get("person_id") != person_id]
    return cleared
