"""Score Week 4 answers: Week 3 rules, plus the path the answer had to walk."""

from __future__ import annotations

from simulation.eval.evidence.score import score_one as evidence_score
from simulation.eval.evidence.score import summarise
from simulation.eval.graph.bars import ANSWER_MARGIN, ANSWER_OVERALL, SLICE_BAR, STRICT_SLICES


def score_one(case: dict, answer: dict | None, *, check_model: bool = True) -> dict:
    result = evidence_score(case, answer, check_model=check_model)
    if not _walked(case, answer):
        result["passed"] = False
        result["notes"] = [*result.get("notes", []), "path"]
    return result


def answers_ok(summary: dict, baselines: dict) -> bool:
    overall = summary["overall"]
    if overall < ANSWER_OVERALL or overall < baselines["best"] + ANSWER_MARGIN:
        return False
    for name, rate in summary["slices"].items():
        if rate < (1.0 if name in STRICT_SLICES else SLICE_BAR):
            return False
    return True


def _walked(case: dict, answer: dict | None) -> bool:
    needed = [str(item) for item in case.get("must_visit") or [] if str(item)]
    if not needed:
        return True
    path = (answer or {}).get("path") if isinstance(answer, dict) else None
    have = {str(item) for item in path} if isinstance(path, list) else set()
    return set(needed) <= have


__all__ = ["answers_ok", "score_one", "summarise"]
