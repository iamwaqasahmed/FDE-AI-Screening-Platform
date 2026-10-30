"""Delete the database row and leave the other stores.

export_categories looks only at the row store. It returns that name
when the person is there, and an empty list otherwise. drop copies
row, memory, index, and logs. Only the row copy has this person
removed. Memory, the index, and logs are returned unchanged.
"""

from __future__ import annotations


def export_categories(stores: dict, person_id: str) -> list[str]:
    """Return the row store name when it holds the person.

    Any other store is ignored, even when it holds the same person.
    A missing row store is read as empty, so the result is empty too.
    """
    # Memory, the index, and logs are not inspected.
    if any(row.get("person_id") == person_id for row in stores.get("row", [])):
        return ["row"]
    return []


def drop(stores: dict, person_id: str) -> dict:
    """Copy the four stores and remove the person from the row only.

    The result always has row, memory, index, and logs, in that order.
    The caller's lists are not mutated.
    """
    cleared = {}
    for name in ("row", "memory", "index", "logs"):
        # Copy every store first. A missing store becomes an empty list.
        rows = [dict(row) for row in stores.get(name, [])]
        # The other three names skip this filter and keep every copied row.
        if name == "row":
            rows = [row for row in rows if row.get("person_id") != person_id]
        cleared[name] = rows
    return cleared
