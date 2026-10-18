"""Score Week 3 answers: the shared scorer, plus a pound budget and the model register."""

from __future__ import annotations

from simulation.architecture.model_register import MODELS
from simulation.eval.evidence.bars import ANSWER_MARGIN, ANSWER_OVERALL, BANNED_MODEL, SLICE_BAR, STRICT_SLICES
from simulation.eval.score.case import score_case

REGISTER = {row[0] for row in MODELS}


def score_one(case: dict, answer: dict | None, *, check_model: bool = True) -> dict:
    answer = answer or {}
    usage = dict(answer.get("usage") or {})
    if "cost_gbp" in usage:
        usage["cost_usd"] = usage["cost_gbp"]
    elif check_model:
        usage["cost_usd"] = 1e9
    adapted = dict(answer, usage=usage)
    budget = dict(case["budget"])
    budget["max_cost_usd"] = budget.get("max_cost_gbp", budget.get("max_cost_usd", 0))
    result = score_case({**case, "budget": budget}, adapted)
    model = str(usage.get("model_id", ""))
    if check_model and (model not in REGISTER or model == BANNED_MODEL):
        result["in_budget"] = False
        result["passed"] = False
        result["notes"] = [*result.get("notes", []), "model"]
    result["slice"] = case.get("slice", "")
    return result


def summarise(cases: list[dict], results: list[dict]) -> dict:
    by_id = {row["case_id"]: row for row in results}
    overall, slices = [], {}
    for case in cases:
        passed = bool(by_id.get(case["case_id"], {}).get("passed"))
        overall.append(passed)
        slices.setdefault(case["slice"], []).append(passed)
    return {
        "overall": round(sum(overall) / len(overall), 4) if overall else 0.0,
        "slices": {name: round(sum(vals) / len(vals), 4) for name, vals in sorted(slices.items())},
        "failed": [case["case_id"] for case in cases if not by_id.get(case["case_id"], {}).get("passed")],
    }


def answers_ok(summary: dict, baselines: dict) -> bool:
    overall = summary["overall"]
    if overall < ANSWER_OVERALL or overall < baselines["best"] + ANSWER_MARGIN:
        return False
    for name, rate in summary["slices"].items():
        if rate < (1.0 if name in STRICT_SLICES else SLICE_BAR):
            return False
    return True
