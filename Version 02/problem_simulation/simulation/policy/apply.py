"""Which clause binds a site on a date. Drafts never bind. Site overlays beat national text."""

from __future__ import annotations

from datetime import date
from functools import lru_cache

from simulation.policy.model import build_clauses, build_documents
from simulation.policy.types import Clause, Document

CLAUSES = build_clauses()
DOCUMENTS = build_documents()


def document_applies(document_id: str, on_date: date) -> bool:
    return _applies(document_id, on_date.toordinal())


@lru_cache(maxsize=None)
def _applies(document_id: str, ordinal: int) -> bool:
    doc = DOCUMENTS[document_id]
    on_date = date.fromordinal(ordinal)
    if doc.status == "draft":
        return False
    if on_date < doc.effective:
        return False
    if doc.sunset is not None and on_date >= doc.sunset:
        return False
    for other in DOCUMENTS.values():
        if document_id in other.supersedes and _applies(other.document_id, ordinal):
            return False
    return True


def applicable_clause(site: str, on_date: date, topic: str, grade: str = "") -> Clause:
    return _applicable(site, on_date.toordinal(), topic, grade)


@lru_cache(maxsize=None)
def _applicable(site: str, ordinal: int, topic: str, grade: str) -> Clause:
    on_date = date.fromordinal(ordinal)
    live = [clause for clause in CLAUSES.values() if _candidate(clause, site, on_date, topic, grade)]
    site_level = [clause for clause in live if DOCUMENTS[clause.document_id].applies_to]
    pool = site_level or [clause for clause in live if not DOCUMENTS[clause.document_id].applies_to]
    graded = [clause for clause in pool if grade and clause.grade == grade]
    pool = graded or [clause for clause in pool if clause.grade == ""]
    if len(pool) != 1:
        names = [clause.clause_id for clause in pool]
        raise ValueError(f"{topic} at {site} on {on_date.isoformat()} grade={grade!r} resolved to {names}")
    return pool[0]


def _candidate(clause: Clause, site: str, on_date: date, topic: str, grade: str) -> bool:
    if clause.topic != topic:
        return False
    if clause.grade not in ("", grade):
        return False
    doc = DOCUMENTS[clause.document_id]
    if doc.applies_to and site not in doc.applies_to:
        return False
    return document_applies(clause.document_id, on_date)


def catalog_document(document_id: str) -> Document:
    return DOCUMENTS[document_id]
