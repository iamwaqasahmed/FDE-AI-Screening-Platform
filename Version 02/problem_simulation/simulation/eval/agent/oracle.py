"""A trajectory built from the gold task, used to prove the scorer accepts a complete answer."""

from __future__ import annotations

STEP_COST = 0.001
READ_COST = 0.0001


def answers(cases: list[dict]) -> list[dict]:
    return [_one(case) for case in cases]


def _one(case: dict) -> dict:
    if case["slice"] == "veto":
        return _veto(case)
    if case["slice"] == "approval":
        return _approval(case)
    if case.get("resume_kind") == "sweep":
        return _sweep(case)
    if case.get("resume_kind") == "approval":
        return _paused(case)
    if case["kind"] in ("written", "injection"):
        return _written(case)
    return _value(case)


def _value(case: dict) -> dict:
    visit = list(case.get("must_visit") or [])
    steps = [_step(1, 1, "plan", "c1"), _step(1, 2, "tool", "c2", tool="lookup", reads=visit), _step(1, 3, "answer", "c3")]
    return _row(case, case["expected"], steps, visit, False)


def _written(case: dict) -> dict:
    visit = list(case.get("must_visit") or [])
    steps = [_step(1, 1, "plan", "c1"), _step(1, 2, "tool", "c2", tool="lookup", reads=visit), _step(1, 3, "answer", "c3")]
    return _row(case, _text(case), steps, visit, False)


def _veto(case: dict) -> dict:
    rule = case["veto_sources"][0]
    steps = [_step(1, 1, "plan", "c1"), _step(1, 2, "check", "c2"), {**_step(1, 3, "veto", "c3"), "rule": rule}]
    row = _row(case, {}, steps, [rule], True)
    row["citation"] = dict(case["accepted_citations"][0])
    return row


def _approval(case: dict) -> dict:
    last = _step(1, 3, "approval", "c3")
    last.update(approver=case["approver"], decision="pending", reason="Waiting for the accountable person")
    steps = [_step(1, 1, "plan", "c1"), _step(1, 2, "tool", "c2", tool="draft", reads=list(case.get("must_visit") or [])), last]
    return _row(case, _text(case), steps, list(case.get("must_visit") or []), False)


def _sweep(case: dict) -> dict:
    ids = [str(item) for item in case.get("once_ids") or []]
    cut = max(len(ids) // 2, 1) if ids else 0
    steps = [_step(1, 1, "plan", "c1")]
    for index, local_id in enumerate(ids[:cut], start=2):
        steps.append(_read(1, index, local_id, case["once_tool"]))
    resume_at = steps[-1]["checkpoint"]
    steps.append({**_step(2, 1, "resume", "r1"), "checkpoint": resume_at})
    for index, local_id in enumerate(ids[cut:], start=2):
        steps.append(_read(2, index, local_id, case["once_tool"]))
    steps.append(_step(2, len(ids[cut:]) + 2, "answer", "done"))
    visit = list(case.get("must_visit") or [])
    return _row(case, case["expected"], steps, visit, False)


def _paused(case: dict) -> dict:
    pending = _step(1, 2, "approval", "c2")
    pending.update(approver=case["approver"], decision="pending", reason="The line leaves the office")
    decided = _step(2, 2, "approval", "c4")
    decided.update(approver=case["approver"], decision="approved", reason="The line names no person and no date")
    steps = [
        _step(1, 1, "plan", "c1"), pending,
        {**_step(2, 1, "resume", "c2"), "checkpoint": "c2"},
        decided, _step(2, 3, "answer", "c5"),
    ]
    return _row(case, _text(case), steps, list(case.get("must_visit") or []), False)


def _row(case: dict, answer, steps: list[dict], path: list, refused: bool) -> dict:
    cost = round(sum(float(step.get("cost_gbp") or 0) for step in steps), 4)
    return {
        "case_id": case["case_id"],
        "answer": answer,
        "citation": dict(case.get("citation") or {}),
        "path": list(path),
        "refused": refused,
        "followed_injection": False,
        "trajectory": steps,
        "usage": {"tokens": 800, "seconds": 2, "cost_gbp": cost, "model_id": "M02"},
    }


def _text(case: dict) -> str:
    groups = (case.get("expected") or {}).get("must_mention") or []
    return " ".join(group if isinstance(group, str) else group[0] for group in groups)


def _step(run: int, number: int, node: str, checkpoint: str, tool: str = "", reads: list | None = None) -> dict:
    row = {
        "run": run, "step": number, "node": node, "checkpoint": checkpoint, "model_id": "M02",
        "cost_gbp": STEP_COST, "reads": list(reads or []),
    }
    if tool:
        row["tool"] = tool
    return row


def _read(run: int, number: int, local_id: str, tool: str) -> dict:
    return {**_step(run, number, "tool", f"c{run}-{number}"), "tool": tool, "reads": [local_id], "cost_gbp": READ_COST}
