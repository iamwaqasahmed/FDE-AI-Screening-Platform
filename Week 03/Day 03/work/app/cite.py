"""Cite an in-force span the asker may see, or refuse."""

from __future__ import annotations

from bind import criteria
from embed import codes
from filter import allow
from index import build
from search import rank


def answer(question: dict, docs: list[dict]) -> dict:
    if question.get("specialty"):
        chosen = criteria(docs, question["specialty"], question.get("started") or question["case_date"])
        if not chosen:
            return {"refusal": "no-document"}
        if not allow(chosen, question["asker"]):
            return {"refusal": "audience"}
        return _cite(chosen)
    visible = _visible(question, docs)
    if not visible:
        return {"refusal": "no-document"}
    return _cite(visible[0])


def _visible(question: dict, docs: list[dict]) -> list[dict]:
    query_codes = codes(question["text"])
    kept = []
    for chunk in rank(question["text"], build(docs), "hybrid"):
        if chunk.get("status") != "in_force" or not allow(chunk, question["asker"]):
            continue
        vector = chunk.get("vector") or {}
        if any(code in vector for code in query_codes):
            kept.append(chunk)
    return kept


def _cite(doc: dict) -> dict:
    return {
        "audience": doc.get("audience", ""),
        "doc_id": doc.get("doc_id", ""),
        "span": doc.get("clause_id", ""),
        "status": doc.get("status", ""),
        "version": doc.get("version", 0),
    }
