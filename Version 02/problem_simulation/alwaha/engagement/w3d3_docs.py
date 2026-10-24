"""Fact specs for rel-w3d3. The snapshot is before the change feed."""

from __future__ import annotations

from alwaha.engagement.w3d3_corpus import catalog_rows, doc, extras, hours, leaflet_titles, leaflets, photo

CASE_DATE = "2027-01-26"
V4 = ("endo", "ophth", "card")
_TITLES = {"card": "Cardiology", "endo": "Endocrinology", "neuro": "Neurology", "ophth": "Ophthalmology"}


def _criteria(specialty: str) -> tuple[dict, dict]:
    title = _TITLES[specialty]
    current = doc(
        body=f"Code {specialty}-v3 is the criteria in force for {title.lower()}.",
        clause_id=f"{specialty}-v3-c1",
        code=f"{specialty}-v3",
        doc_id=f"crit-{specialty}-v3",
        specialty=specialty,
        title=f"{title} criteria v3",
        version=3,
    )
    draft = doc(
        body=f"Code {specialty}-v4 is the draft criteria for {title.lower()}.",
        clause_id=f"{specialty}-v4-c1",
        code=f"{specialty}-v4",
        doc_id=f"crit-{specialty}-v4",
        effective="",
        specialty=specialty,
        status="draft",
        title=f"{title} criteria v4",
        version=4,
    )
    return current, draft


def snapshot() -> list[dict]:
    rows: list[dict] = []
    for specialty in ("endo", "ophth", "card", "neuro"):
        current, draft = _criteria(specialty)
        rows.extend((current, draft))
    current, _unauthorized = hours()
    rows.append(current)
    rows.extend(leaflets())
    rows.extend(extras())
    return rows


def feed() -> list[dict]:
    _current, unauthorized = hours()
    events = []
    for specialty in V4:
        events.append(
            {
                "doc_id": f"crit-{specialty}-v4",
                "fields": {"effective": CASE_DATE, "status": "in_force", "supersedes": f"crit-{specialty}-v3"},
                "op": "replace",
            }
        )
        events.append(
            {
                "doc_id": f"crit-{specialty}-v3",
                "fields": {"status": "superseded", "sunset": CASE_DATE},
                "op": "replace",
            }
        )
    events.append({"doc": unauthorized, "doc_id": unauthorized["doc_id"], "op": "add"})
    events.append(
        {"doc_id": "leaflet-prep-old", "fields": {"status": "superseded", "sunset": CASE_DATE}, "op": "replace"}
    )
    return events


__all__ = ["CASE_DATE", "V4", "catalog_rows", "feed", "leaflet_titles", "photo", "snapshot"]
