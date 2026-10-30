"""Delete the person from the row, memory, the index, and permitted logs.

export_categories walks the stores in STORES order and names each one
that still holds the person. A missing store is treated as empty.
drop removes the person from the row, memory, and the index by copying
the other rows. When logs still hold the person, the whole logs list
is replaced by one redacted marker, including any other people's rows.
When logs do not hold the person, those rows are copied and filtered
the same way as the other stores.
"""

from __future__ import annotations

# Store names, in the order the export lists them and drop walks them.
STORES = ("row", "memory", "index", "logs")


def export_categories(stores: dict, person_id: str) -> list[str]:
    """Return the store names that still contain this person.

    The names follow STORES, not the order of keys on the dict. A store
    with no matching person_id is omitted.
    """
    found = []
    for name in STORES:
        if any(row.get("person_id") == person_id for row in stores.get(name, [])):
            found.append(name)
    return found


def drop(stores: dict, person_id: str) -> dict:
    """Return a new store dict with this person removed, and logs redacted.

    Every STORES key is present on the result. A missing input store is
    read as an empty list. Logs that contain the person become a single
    row whose redacted field is true.
    """
    cleared = {}
    for name in STORES:
        rows = stores.get(name, [])
        # One matching log row replaces the entire logs list with the marker.
        if name == "logs" and any(row.get("person_id") == person_id for row in rows):
            cleared[name] = [{"redacted": True}]
        else:
            # Copy the rows that belong to someone else. The caller's lists stay put.
            cleared[name] = [dict(row) for row in rows if row.get("person_id") != person_id]
    return cleared
