"""Return the nearest chunk, including a draft."""

from __future__ import annotations

from index import build
from search import rank


def answer(question: dict, docs: list[dict]) -> dict:
    ranked = rank(question["text"], build(docs), "vector")
    if not ranked:
        return {"refusal": "no-document"}
    top = ranked[0]
    return {
        "audience": top.get("audience", ""),
        "doc_id": top.get("doc_id", ""),
        "span": top.get("clause_id", ""),
        "status": top.get("status", ""),
        "version": top.get("version", 0),
    }
