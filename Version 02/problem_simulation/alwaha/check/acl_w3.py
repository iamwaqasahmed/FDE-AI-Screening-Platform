"""slice-acl. Retrieval with no audience filter must show a staff document to a patient."""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.rag_w3 import RUN, SPAN, STAFF, current, load_retriever
from alwaha.check.tables import contains_canary


def acl_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    try:
        modules = load_retriever(work)
        docs, _touched = current(modules, pack)
        cited = modules["cite"].answer(gold["acl_question"], docs)
        staff = next(doc for doc in docs if doc.get("doc_id") == gold["acl_blocked"])
        allowed = modules["filter"].allow(staff, "patient")
    except Exception:
        return [RUN]
    problems: list[str] = []
    if allowed or cited.get("audience") in {"restricted", "staff"} or cited.get("doc_id") == gold["acl_blocked"]:
        problems.append(STAFF)
    if cited.get("doc_id") != gold["acl_doc"] and STAFF not in problems:
        problems.append(SPAN)
    return problems
