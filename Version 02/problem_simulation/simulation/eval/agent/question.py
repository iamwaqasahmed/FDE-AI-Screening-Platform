"""One published Week 5 task. The trajectory it must walk stays off the printed file."""

from __future__ import annotations

from simulation.eval.evidence.question import cite, publish as evidence_publish
from simulation.eval.graph.question import make as graph_make


def make(case_id: str, question: str, expected: dict, kind: str, slice_name: str, answer_keys: tuple[str, ...],
         citation: dict | None, budget: str, must_visit: list[str], *, max_steps: int, approver: str = "",
         runs_min: int = 1, once_ids: list[str] | None = None, once_tool: str = "", resume_kind: str = "",
         veto_sources: list[str] | None = None, accepted: list[dict] | None = None) -> dict:
    row = graph_make(case_id, question, expected, kind, slice_name, answer_keys, citation, budget, must_visit)
    row["max_steps"] = max_steps
    row["approver"] = approver
    row["runs_min"] = runs_min
    row["once_ids"] = list(once_ids or [])
    row["once_tool"] = once_tool
    row["resume_kind"] = resume_kind
    row["veto_sources"] = list(veto_sources or [])
    row["accepted_citations"] = list(accepted or [])
    return row


def adopt(case: dict, *, max_steps: int) -> dict:
    row = dict(case)
    row["max_steps"] = max_steps
    row.setdefault("approver", "")
    row.setdefault("runs_min", 1)
    row.setdefault("once_ids", [])
    row.setdefault("once_tool", "")
    row.setdefault("resume_kind", "")
    row.setdefault("veto_sources", [])
    row.setdefault("accepted_citations", [])
    return row


def publish(case: dict) -> dict:
    row = evidence_publish(case)
    row["max_steps"] = case["max_steps"]
    return row


__all__ = ["adopt", "cite", "make", "publish"]
