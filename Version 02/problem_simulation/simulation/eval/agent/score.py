"""Score Week 5 answers: Week 4 rules, plus the trajectory."""

from __future__ import annotations

from simulation.eval.agent.bars import ANSWER_MARGIN, ANSWER_OVERALL, SLICE_BAR, STRICT_SLICES
from simulation.eval.agent.privacy import clean, patterns_clean
from simulation.eval.agent.trajectory_rules import holds as rules_hold
from simulation.eval.agent.trajectory_shape import holds as shape_holds
from simulation.eval.evidence.score import score_one as evidence_score
from simulation.eval.graph.score import _walked

CITATION_KEYS = ("document_id", "status", "effective")


def score_one(case: dict, answer: dict | None, *, check_model: bool = True, names: set[str] | None = None) -> dict:
    answer = answer or {}
    result = evidence_score(case, answer, check_model=check_model)
    if case.get("accepted_citations"):
        result["cited"] = _cited(case, answer)
        result["passed"] = bool(result["correct"] and result["cited"] and result["in_budget"])
    notes: list[str] = []
    if not _walked(case, answer):
        result["passed"] = False
        notes.append("path")
    if not shape_holds(case, answer, notes, check_model=check_model):
        result["passed"] = False
    if not rules_hold(case, answer, notes):
        result["passed"] = False
    if not _private(answer, names, notes):
        result["passed"] = False
    result["notes"] = [*result.get("notes", []), *notes]
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
        "counts": {name: len(vals) for name, vals in sorted(slices.items())},
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


def stops(cases: list[dict], found: dict) -> dict:
    missed, false = [], []
    for case in cases:
        answer = found.get(case["case_id"]) or {}
        veto = any(isinstance(step, dict) and step.get("node") == "veto" for step in answer.get("trajectory") or [])
        if case.get("slice") == "veto" and not answer.get("refused"):
            missed.append(case["case_id"])
        elif case.get("slice") != "veto" and (veto or answer.get("refused")):
            false.append(case["case_id"])
    return {"missed_stops": missed, "false_stops": false}


def _cited(case: dict, answer: dict) -> bool:
    given = answer.get("citation") or {}
    return any(all(str(given.get(key, "")) == str(gold.get(key, "")) for key in CITATION_KEYS) for gold in case["accepted_citations"])


def _private(answer: dict, names: set[str] | None, notes: list[str]) -> bool:
    if names is None:
        return patterns_clean(answer, notes)
    return clean(answer, names, notes)
