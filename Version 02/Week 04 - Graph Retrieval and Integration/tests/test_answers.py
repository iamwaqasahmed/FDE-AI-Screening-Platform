"""Path, refusal, and budget failures on a toy question."""

from __future__ import annotations

from simulation.eval.graph.score import score_one

CASE = {
    "case_id": "path-00",
    "question": "Local id LP1 was sent a chase letter.",
    "kind": "value",
    "expected": {"clause_id": "sop-national-v3", "limit": "", "copies": 0},
    "citation": {"document_id": "sop-national-v3", "status": "in_force", "effective": "2023-04-01"},
    "answer_keys": ["clause_id", "limit", "copies"],
    "budget": {"max_tokens": 4000, "max_seconds": 10, "max_cost_gbp": 0.01, "tier": "lookup"},
    "slice": "path",
    "must_visit": ["LR-1", "sop-national-v3"],
}


def _answer(**extra) -> dict:
    row = {
        "case_id": "path-00",
        "answer": {"clause_id": "sop-national-v3", "limit": "", "copies": 0},
        "citation": {"document_id": "sop-national-v3", "status": "in_force", "effective": "2023-04-01"},
        "path": ["LR-1", "sop-national-v3"],
        "refused": False,
        "usage": {"tokens": 100, "seconds": 1, "cost_gbp": 0.001, "model_id": "M01"},
    }
    row.update(extra)
    return row


def test_a_right_answer_without_the_request_fails():
    row = score_one(CASE, _answer(path=["sop-national-v3"]))
    assert row["passed"] is False
    assert "path" in row["notes"]


def test_a_complete_path_passes():
    assert score_one(CASE, _answer())["passed"] is True


def test_m06_fails_even_when_the_value_is_right():
    usage = {"tokens": 100, "seconds": 1, "cost_gbp": 0.001, "model_id": "M06"}
    assert score_one(CASE, _answer(usage=usage))["passed"] is False


def test_refusing_an_answerable_question_fails():
    assert score_one(CASE, _answer(refused=True, answer={}))["passed"] is False
