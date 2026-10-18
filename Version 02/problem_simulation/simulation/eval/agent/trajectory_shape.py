"""Trajectory shape: ordered steps, no writes, a register model, and a budget the steps add up to."""

from __future__ import annotations

import re

from simulation.architecture.model_register import MODELS
from simulation.eval.agent.bars import BANNED_MODEL, COST_TOLERANCE, PERSONAL_MODELS

REGISTER = {row[0] for row in MODELS}
NODES = {"plan", "tool", "check", "veto", "approval", "resume", "answer"}
ENDS = {"answer", "veto", "approval"}
LOCAL = re.compile(r"\bL[PX]\d+\b")
PERSON_TOOLS = {"ophthalmology.referrals", "registry.person", "booking.contact"}


def holds(case: dict, answer: dict | None, notes: list[str], *, check_model: bool) -> bool:
    steps = (answer or {}).get("trajectory") if isinstance(answer, dict) else None
    if not isinstance(steps, list) or not steps:
        notes.append("trajectory")
        return False
    ok = _ordered(steps, notes) and _closed(steps, notes) and _writes(steps, notes)
    ok = _budget(case, answer, steps, notes) and ok
    if check_model:
        ok = _models(steps, notes) and ok
    return ok


def _ordered(steps: list[dict], notes: list[str]) -> bool:
    seen: dict[int, int] = {}
    for step in steps:
        if not isinstance(step, dict) or step.get("node") not in NODES:
            notes.append("node")
            return False
        run, number = step.get("run"), step.get("step")
        if not isinstance(run, int) or not isinstance(number, int):
            notes.append("step")
            return False
        if number <= seen.get(run, 0):
            notes.append("step")
            return False
        seen[run] = number
    if sorted(seen) != list(range(1, len(seen) + 1)):
        notes.append("run")
        return False
    return True


def _closed(steps: list[dict], notes: list[str]) -> bool:
    if steps[-1].get("node") not in ENDS:
        notes.append("end")
        return False
    return True


def _writes(steps: list[dict], notes: list[str]) -> bool:
    for step in steps:
        if step.get("writes"):
            notes.append("write")
            return False
    return True


def _models(steps: list[dict], notes: list[str]) -> bool:
    for step in steps:
        model = str(step.get("model_id", ""))
        if model not in REGISTER or model == BANNED_MODEL:
            notes.append("model")
            return False
        if _personal(step) and model not in PERSONAL_MODELS:
            notes.append("model")
            return False
    return True


def _personal(step: dict) -> bool:
    if str(step.get("tool", "")) in PERSON_TOOLS:
        return True
    return any(_person_read(item) for item in step.get("reads") or [])


def _person_read(item) -> bool:
    text = str(item)
    return bool(LOCAL.search(text) or text.startswith(("CMP-", "patient-letter")))


def _budget(case: dict, answer: dict, steps: list[dict], notes: list[str]) -> bool:
    if len(steps) > int(case.get("max_steps") or 0):
        notes.append("steps")
        return False
    spent = round(sum(float(step.get("cost_gbp") or 0) for step in steps), 4)
    usage = float((answer.get("usage") or {}).get("cost_gbp") or 0)
    if abs(spent - usage) > COST_TOLERANCE:
        notes.append("cost")
        return False
    return True
