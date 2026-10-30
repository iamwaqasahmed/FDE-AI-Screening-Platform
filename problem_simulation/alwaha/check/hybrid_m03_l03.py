"""slice-hybrid. Vector search alone must lose the hours question.

This slice grades hybrid search against vector search on the hours question. Vector search must not clear the slice by itself. Hybrid search must rank the hybrid document first, not the vector-only document. A planted token or a crash stops the check.
"""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.rag_m03_l03 import RUN, SPAN, UNAUTH, current, load_retriever
from alwaha.check.tables import contains_canary

CLEARS = "vector search alone clears the slice"


def hybrid_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the hybrid-search misses.

    The index is built from the current documents. The same question is ranked once as vector and once as hybrid. If the vector-only document is in the index and vector rank still puts the hybrid document first, vector search cleared the slice. If hybrid rank puts the vector-only document first, the unauthorized document was cited. If hybrid rank is empty or lands on anything else, the span is wrong. An empty hybrid list has no top document, so it takes the span branch.
    """
    if contains_canary(work, canary):
        return [WATERMARK]
    try:
        modules = load_retriever(work)
        docs, _touched = current(modules, pack)
        chunks = modules["index"].build(docs)
        question = gold["hybrid_question"]["text"]
        vector = modules["search"].rank(question, chunks, "vector")
        hybrid = modules["search"].rank(question, chunks, "hybrid")
    except Exception:
        return [RUN]
    problems: list[str] = []
    present = {chunk.get("doc_id") for chunk in chunks}
    # Vector search is not allowed to clear the slice. This fires when the vector-only document is indexed and vector rank still puts the hybrid document first.
    if gold["vector_doc"] in present and vector and vector[0].get("doc_id") == gold["hybrid_doc"]:
        problems.append(CLEARS)
    # An empty hybrid ranking has no top document, so the following check treats it as a miss rather than a crash.
    top = hybrid[0].get("doc_id") if hybrid else ""
    if top == gold["vector_doc"]:
        problems.append(UNAUTH)
    # Hybrid rank missed the hybrid document without landing on the vector-only document, so the span is wrong rather than unauthorized.
    elif top != gold["hybrid_doc"]:
        problems.append(SPAN)
    return problems
