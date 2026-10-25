"""Cite an in-force span the asker may see, or refuse."""

from __future__ import annotations

from bind import criteria
from embed import codes
from filter import allow
from index import build
from search import rank


def answer(question: dict, docs: list[dict]) -> dict:
    # A specialty question binds the criteria for the start day, or the case date.
    if question.get("specialty"):
        chosen = criteria(docs, question["specialty"], question.get("started") or question["case_date"])
        # Nothing binds.
        if not chosen:
            return {"refusal": "no-document"}
        # The asker cannot see the document that bound.
        if not allow(chosen, question["asker"]):
            return {"refusal": "audience"}
        return _cite(chosen)
    # No specialty: hybrid rank, then keep an in-force span the asker may see.
    visible = _visible(question, docs)
    if not visible:
        return {"refusal": "no-document"}
    return _cite(visible[0])


def _visible(question: dict, docs: list[dict]) -> list[dict]:
    query_codes = codes(question["text"])
    kept = []
    for chunk in rank(question["text"], build(docs), "hybrid"):
        # Drop a span that is not in force, or that this asker cannot see.
        if chunk.get("status") != "in_force" or not allow(chunk, question["asker"]):
            continue
        vector = chunk.get("vector") or {}
        # Keep a span whose vector contains a code from the question.
        if any(code in vector for code in query_codes):
            kept.append(chunk)
    return kept


def _cite(doc: dict) -> dict:
    # The span is the clause id. The other fields travel with the citation.
    return {
        "audience": doc.get("audience", ""),
        "doc_id": doc.get("doc_id", ""),
        "span": doc.get("clause_id", ""),
        "status": doc.get("status", ""),
        "version": doc.get("version", 0),
    }
