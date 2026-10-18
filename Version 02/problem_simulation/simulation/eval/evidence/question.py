"""One published question: the text a team sees, and the citation the checker keeps."""

from __future__ import annotations

from simulation.eval.evidence.bars import BUDGETS
from simulation.world.clock import iso


def make(case_id: str, question: str, expected: dict, kind: str, slice_name: str, answer_keys: tuple[str, ...],
         citation: dict | None, budget: str) -> dict:
    return {
        "case_id": case_id,
        "question": question,
        "kind": kind,
        "expected": expected,
        "citation": citation or {},
        "answer_keys": list(answer_keys),
        "budget": dict(BUDGETS[budget], tier=budget),
        "slice": slice_name,
    }


def cite(document) -> dict:
    return {
        "document_id": document.document_id,
        "version": document.version,
        "status": document.status,
        "effective": iso(document.effective),
        "sunset": iso(document.sunset) if document.sunset else "",
        "site": document.site,
        "clause_id": document.document_id,
    }


def publish(case: dict) -> dict:
    budget = case["budget"]
    return {
        "case_id": case["case_id"],
        "question": case["question"],
        "kind": case["kind"],
        "answer_keys": list(case["answer_keys"]),
        "budget": {
            "max_tokens": budget["max_tokens"],
            "max_seconds": budget["max_seconds"],
            "max_cost_gbp": budget["max_cost_gbp"],
            "tier": budget["tier"],
        },
    }
