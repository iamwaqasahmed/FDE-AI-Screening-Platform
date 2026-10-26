"""Leave every grant open.

settle copies every grant and sets status to open. as_of is discarded,
so no field is compared and every returned status is open. controls
returns an empty list, so no deploy check is named.
"""

from __future__ import annotations


def settle(grants: list[dict], as_of: str) -> list[dict]:
    """Mark every grant open and ignore the date argument.

    The input rows are not mutated. The new dicts are the return value.
    """
    # The date is unused. del only drops this local name.
    del as_of
    # Each copy keeps the other fields and forces status to open.
    return [{**row, "status": "open"} for row in grants]


def controls() -> list[str]:
    """Return no deploy checks.

    The list is empty on every call.
    """
    return []
