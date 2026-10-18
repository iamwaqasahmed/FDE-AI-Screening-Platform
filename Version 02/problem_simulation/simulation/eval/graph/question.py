"""One published Week 4 question. The path it must visit stays off the printed file."""

from __future__ import annotations

from simulation.eval.evidence.question import cite, make as evidence_make, publish as evidence_publish


def make(case_id: str, question: str, expected: dict, kind: str, slice_name: str, answer_keys: tuple[str, ...],
         citation: dict | None, budget: str, must_visit: list[str]) -> dict:
    row = evidence_make(case_id, question, expected, kind, slice_name, answer_keys, citation, budget)
    row["must_visit"] = list(must_visit)
    return row


def publish(case: dict) -> dict:
    return evidence_publish(case)


__all__ = ["cite", "make", "publish"]
