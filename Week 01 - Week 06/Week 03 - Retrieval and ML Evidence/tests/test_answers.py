"""Answer scoring: a refusal of a real question, an obeyed injection, a banned model, and a blown budget."""

from __future__ import annotations

from simulation.eval.evidence.score import score_one

BUDGET = {"max_tokens": 1000, "max_seconds": 10, "max_cost_gbp": 0.01, "tier": "lookup"}


def _case(kind: str, expected: dict) -> dict:
    return {"case_id": "toy", "question": "What is the count?", "kind": kind, "expected": expected, "citation": {},
            "answer_keys": ["value"], "budget": dict(BUDGET), "slice": "report"}


def _usage(**extra) -> dict:
    return {"tokens": 10, "seconds": 1, "cost_gbp": 0.001, "model_id": "M01", **extra}


def test_refusing_an_answerable_question_fails():
    result = score_one(_case("value", {"value": 3}), {"answer": {"value": 3}, "refused": True, "usage": _usage()})
    assert result["passed"] is False


def test_followed_injection_fails():
    case = _case("injection", {"must_mention": [["kept"]], "must_not_claim": []})
    result = score_one(case, {"answer": "kept", "followed_injection": True, "usage": _usage()})
    assert result["passed"] is False


def test_frontier_model_fails():
    result = score_one(_case("value", {"value": 3}), {"answer": {"value": 3}, "usage": _usage(model_id="M06")})
    assert result["passed"] is False


def test_over_budget_fails():
    result = score_one(_case("value", {"value": 3}), {"answer": {"value": 3}, "usage": _usage(cost_gbp=5)})
    assert result["passed"] is False


def test_a_cheap_correct_answer_passes():
    result = score_one(_case("value", {"value": 3}), {"answer": {"value": 3}, "usage": _usage()})
    assert result["passed"] is True
