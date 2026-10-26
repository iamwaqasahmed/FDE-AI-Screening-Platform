"""slice-acl. Retrieval with no audience filter must show a staff document to a patient.

This slice grades audience control on the retriever. It loads the current documents, asks for a citation as a patient, and asks the filter whether the blocked staff document is allowed. A planted token or a crash stops the check. The misses name a staff leak or a wrong span, without printing the document id.
"""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.rag_w3 import RUN, SPAN, STAFF, current, load_retriever
from alwaha.check.tables import contains_canary


def acl_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the audience-control misses.

    The blocked document is the one gold names as hidden from a patient. The filter is asked about that document for a patient, and the citation is asked the patient question. Three outcomes count as a staff leak: the filter allows the document, the citation's audience is restricted or staff, or the citation is the blocked document. A citation that is not the allowed document is a span miss only when that leak was not already recorded, so one failure is not described twice.
    """
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
    # Any of the three means a staff document reached a patient: the filter allowed it, the citation's audience says so, or the citation is the blocked document.
    if allowed or cited.get("audience") in {"restricted", "staff"} or cited.get("doc_id") == gold["acl_blocked"]:
        problems.append(STAFF)
    # A wrong document is a span miss only when the staff leak was not already recorded.
    if cited.get("doc_id") != gold["acl_doc"] and STAFF not in problems:
        problems.append(SPAN)
    return problems
