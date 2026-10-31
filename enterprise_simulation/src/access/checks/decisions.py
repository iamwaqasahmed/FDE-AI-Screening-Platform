"""INV-02. Run decide() on letters the pack does not grade by themselves."""

from __future__ import annotations

from pathlib import Path

from access.checks.runtime import load_callable
from access.sealed_holdouts import DECISIONS
from access.sealed_release import DECISION_OWNERS, SPONSOR_FEATURE


def grade_decisions(path: Path) -> list[str]:
    fn, problems = load_callable(path, "decide")
    if fn is None:
        return problems
    for case in DECISIONS:
        got = _call(fn, case)
        if isinstance(got, str):
            problems.append(got)
            continue
        problems.extend(_judge(case, got))
    return problems


def _call(fn, case: dict) -> dict | str:
    try:
        got = fn(case)
    except Exception:
        return f"the decision function raised on {case['id']}"
    if not isinstance(got, dict):
        return f"the decision function returned no record for {case['id']}"
    return got


def _judge(case: dict, got: dict) -> list[str]:
    problems: list[str] = []
    owners = got.get("owners")
    values = got.get("values")
    if not isinstance(owners, dict) or not isinstance(values, dict):
        return ["the decision record does not name an owner for each field"]
    for field, owner in DECISION_OWNERS.items():
        if owners.get(field) != owner:
            problems.append(f"the field {field} collapses an owner")
    if values.get("dec-clinical") is not None:
        problems.append("a letter wrote the clinical decision")
    if case["coverage_answer"] == "timeout":
        if values.get("dec-slot") is not None or values.get("dec-cover") == "yes":
            problems.append("a coverage timeout confirmed a slot")
    if case["is_emergency"] and values.get("dec-route") != "person":
        problems.append("emergency wording did not reach a person")
    if case["is_return"] and got.get("return_starts_wait") is not True:
        problems.append("a return skipped the wait")
    if got.get("sponsor_feature") != SPONSOR_FEATURE:
        problems.append("the sponsor's single-field feature is still accepted")
    return problems
