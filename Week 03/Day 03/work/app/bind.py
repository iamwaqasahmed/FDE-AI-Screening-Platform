"""v4 binds for three specialties. An in-flight referral keeps its start version."""

from __future__ import annotations

_KEPT = {"in_force", "superseded"}
_V4 = {"card", "endo", "ophth"}


def _covers(doc: dict, day: str) -> bool:
    effective = doc.get("effective") or ""
    sunset = doc.get("sunset") or ""
    if effective and day < effective:
        return False
    if sunset and day >= sunset:
        return False
    return True


def criteria(docs: list[dict], specialty: str, started: str) -> dict:
    rows = [doc for doc in docs if doc.get("specialty") == specialty]
    if specialty in _V4:
        for doc in rows:
            if doc.get("version") == 4 and doc.get("status") == "in_force" and _covers(doc, started):
                return doc
    for doc in rows:
        if doc.get("version") == 3 and doc.get("status") in _KEPT and _covers(doc, started):
            return doc
    return {}
