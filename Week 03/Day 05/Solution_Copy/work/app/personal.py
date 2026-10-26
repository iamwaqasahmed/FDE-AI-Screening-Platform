"""Keep version and audience, and refuse a staff document to a patient.

cite returns nothing when a patient asks and the document audience
is staff. Otherwise it returns audience, document id, and version.
meets_budget is true when the value clears the floor. A tiny
allowance is added so a value on the floor still clears it.
"""

from __future__ import annotations


def cite(row: dict) -> dict | None:
    """Return a citation the asker may keep, or nothing.

    row may carry asker, audience, doc_id, and version. A patient
    asking for a staff document gets nothing. A kept citation copies
    audience, document id, and version.
    """
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
    """Return whether value clears floor.

    value and floor are read as floats. A tiny allowance is added to
    value before the comparison, so a value on the floor clears it.
    """
    # The value clears the floor when it is at or above that floor.
    return float(value) + 1e-9 >= float(floor)
