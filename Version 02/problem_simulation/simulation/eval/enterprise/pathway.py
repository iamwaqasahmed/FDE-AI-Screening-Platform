"""Pathway probes. Each one is a site, a topic, a grade, and a date, resolved by the clause model."""

from __future__ import annotations

from datetime import timedelta

from simulation.policy.apply import CLAUSES, DOCUMENTS, applicable_clause
from simulation.world.clock import SNAPSHOT
from simulation.world.sites import CAPTURE_SITES

TOPICS = ("eligibility", "coverage_window", "grade_turnaround", "letter_turnaround", "specialist_review")
RECALL_GRADES = ("R0", "R1", "U")


def pathway_facts() -> dict:
    probes = [_probe(site, topic, grade, day) for site, topic, grade, day in _grid()]
    probes = [row for row in probes if row]
    return {"probes": probes, "site_rules": _site_rules(), "stale_register": _stale()}


def _grid() -> list[tuple]:
    dates = _dates()
    rows = [(site, topic, "", day) for site in CAPTURE_SITES for topic in TOPICS for day in dates]
    rows += [(site, "recall", grade, day) for site in CAPTURE_SITES for grade in RECALL_GRADES for day in dates]
    return rows


def _dates() -> list:
    found = {SNAPSHOT}
    for document in DOCUMENTS.values():
        found.add(document.effective)
        if document.sunset:
            found.add(document.sunset)
            found.add(document.sunset - timedelta(days=1))
    return sorted(found)


def _probe(site: str, topic: str, grade: str, day) -> dict | None:
    try:
        clause = applicable_clause(site, day, topic, grade)
    except ValueError:
        return None
    document = DOCUMENTS[clause.document_id]
    return {
        "site": site,
        "topic": topic,
        "grade": grade,
        "on": day.isoformat(),
        "clause_id": clause.clause_id,
        "document_id": clause.document_id,
        "days": clause.days,
        "effective": document.effective.isoformat(),
        "sunset": document.sunset.isoformat() if document.sunset else "",
    }


def _site_rules() -> dict:
    hill = DOCUMENTS["site-sop-hill-2022"]
    ncec = DOCUMENTS["site-sop-ncec-2024"]
    harbour = DOCUMENTS["site-sop-harbour-2025"]
    oakridge = DOCUMENTS["memo-oakridge-2024"]
    return {
        "hill_recall_days": CLAUSES["recall-u-hill"].days,
        "hill_document": hill.document_id,
        "hill_from": hill.effective.isoformat(),
        "national_ungradable_days": CLAUSES["recall-u-v3"].days,
        "ncec_specialist_days": CLAUSES["spec-ncec"].days,
        "ncec_from": ncec.effective.isoformat(),
        "harbour_specialist_days": CLAUSES["spec-harbour"].days,
        "harbour_from": harbour.effective.isoformat(),
        "oakridge_memo": oakridge.document_id,
        "oakridge_from": oakridge.effective.isoformat(),
        "oakridge_sunset": oakridge.sunset.isoformat() if oakridge.sunset else "",
    }


def _stale() -> dict:
    from simulation.systems.catalog import STALE_REGISTER

    return {"documents": list(STALE_REGISTER), "register_says": "draft", "header_says": "in_force"}
