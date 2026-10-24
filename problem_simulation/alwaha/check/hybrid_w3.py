"""slice-hybrid. Vector search alone must lose the hours question."""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.rag_w3 import RUN, SPAN, UNAUTH, current, load_retriever
from alwaha.check.tables import contains_canary

CLEARS = "vector search alone clears the slice"


def hybrid_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
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
    if gold["vector_doc"] in present and vector and vector[0].get("doc_id") == gold["hybrid_doc"]:
        problems.append(CLEARS)
    top = hybrid[0].get("doc_id") if hybrid else ""
    if top == gold["vector_doc"]:
        problems.append(UNAUTH)
    elif top != gold["hybrid_doc"]:
        problems.append(SPAN)
    return problems
