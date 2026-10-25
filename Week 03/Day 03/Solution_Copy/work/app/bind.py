"""v4 binds for three specialties. An in-flight referral keeps its start version."""

from __future__ import annotations

# A superseded v3 can still cover a start day inside its window.
_KEPT = {"in_force", "superseded"}
# v4 is in force for these three specialties, not for every specialty.
_V4 = {"card", "endo", "ophth"}


def _covers(doc: dict, day: str) -> bool:
    effective = doc.get("effective") or ""
    sunset = doc.get("sunset") or ""
    # A day before the effective date is outside the window.
    if effective and day < effective:
        return False
    # A day on or after sunset is outside the window.
    if sunset and day >= sunset:
        return False
    return True


def criteria(docs: list[dict], specialty: str, started: str) -> dict:
    rows = [doc for doc in docs if doc.get("specialty") == specialty]
    # For the three specialties, an in-force v4 that covers the start day wins.
    if specialty in _V4:
        for doc in rows:
            if doc.get("version") == 4 and doc.get("status") == "in_force" and _covers(doc, started):
                return doc
    # Otherwise a v3 that is in force or superseded, and that covers the start day, wins.
    for doc in rows:
        if doc.get("version") == 3 and doc.get("status") in _KEPT and _covers(doc, started):
            return doc
    # Nothing covers that start day.
    return {}
