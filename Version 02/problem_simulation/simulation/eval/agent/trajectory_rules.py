"""Veto, approval, and resume. A stop on the wrong task fails, and so does a pause."""

from __future__ import annotations

from simulation.eval.score.match import normalise


def holds(case: dict, answer: dict | None, notes: list[str]) -> bool:
    steps = (answer or {}).get("trajectory") if isinstance(answer, dict) else None
    if not isinstance(steps, list):
        return False
    slice_name = case.get("slice", "")
    ok = True
    if slice_name == "veto":
        ok = _veto(case, answer or {}, steps, notes)
    elif _has(steps, "veto"):
        notes.append("false stop")
        ok = False
    allowed_pause = slice_name == "resume" and case.get("resume_kind") == "approval"
    if slice_name == "approval":
        ok = _approval(case, steps, notes) and ok
    elif _has(steps, "approval") and not allowed_pause:
        notes.append("false pause")
        ok = False
    if slice_name == "resume":
        ok = _resume(case, steps, notes) and ok
    elif _runs(steps) > 1:
        notes.append("run")
        ok = False
    return ok


def _veto(case: dict, answer: dict, steps: list[dict], notes: list[str]) -> bool:
    found = [step for step in steps if step.get("node") == "veto"]
    allowed = set(case.get("veto_sources") or [])
    if len(found) != 1 or found[0] is not steps[-1] or not answer.get("refused"):
        notes.append("veto")
        return False
    if str(found[0].get("rule", "")) not in allowed:
        notes.append("veto")
        return False
    return True


def _approval(case: dict, steps: list[dict], notes: list[str]) -> bool:
    if steps[-1].get("node") != "approval" or not _pending(steps[-1], case.get("approver", "")):
        notes.append("approval")
        return False
    return True


def _resume(case: dict, steps: list[dict], notes: list[str]) -> bool:
    groups = _groups(steps)
    if len(groups) < int(case.get("runs_min") or 2):
        notes.append("resume")
        return False
    if not _resumed(groups, notes) or not _reads_once(steps, notes):
        return False
    if case.get("resume_kind") == "sweep":
        return _sweep(case, steps, notes)
    if case.get("resume_kind") == "approval":
        return _decided(case, groups, notes)
    return True


def _resumed(groups: list[list[dict]], notes: list[str]) -> bool:
    earlier = {step.get("checkpoint") for run in groups[:-1] for step in run}
    for run in groups[1:]:
        if run[0].get("node") != "resume" or run[0].get("checkpoint") not in earlier:
            notes.append("resume")
            return False
    return True


def _reads_once(steps: list[dict], notes: list[str]) -> bool:
    seen: set[tuple] = set()
    for step in steps:
        key = (str(step.get("tool", "")), tuple(str(item) for item in step.get("reads") or []))
        if key[1] and key in seen:
            notes.append("reread")
            return False
        if key[1]:
            seen.add(key)
    return True


def _sweep(case: dict, steps: list[dict], notes: list[str]) -> bool:
    tool = case.get("once_tool") or "ophthalmology.referrals"
    counts: dict[str, int] = {}
    for step in steps:
        if step.get("tool") != tool:
            continue
        for item in step.get("reads") or []:
            counts[str(item)] = counts.get(str(item), 0) + 1
    needed = [str(item) for item in case.get("once_ids") or []]
    if any(counts.get(item) != 1 for item in needed) or set(counts) != set(needed):
        notes.append("sweep")
        return False
    return True


def _decided(case: dict, groups: list[list[dict]], notes: list[str]) -> bool:
    approver = normalise(case.get("approver", ""))
    pending = [step for step in groups[0] if step.get("node") == "approval" and normalise(step.get("decision")) == "pending"]
    later = [step for run in groups[1:] for step in run if step.get("node") == "approval"]
    if not pending or len(later) != 1:
        notes.append("decision")
        return False
    decision = later[0]
    if normalise(decision.get("approver")) != approver or normalise(decision.get("decision")) not in {"approved", "rejected"}:
        notes.append("decision")
        return False
    if not str(decision.get("reason", "")).strip() or normalise(pending[0].get("approver")) != approver:
        notes.append("decision")
        return False
    return True


def _pending(step: dict, approver: str) -> bool:
    return normalise(step.get("approver")) == normalise(approver) and normalise(step.get("decision")) == "pending" and bool(
        str(step.get("reason", "")).strip())


def _groups(steps: list[dict]) -> list[list[dict]]:
    runs: dict[int, list[dict]] = {}
    for step in steps:
        runs.setdefault(int(step["run"]), []).append(step)
    return [runs[number] for number in sorted(runs)]


def _runs(steps: list[dict]) -> int:
    return len({step.get("run") for step in steps})


def _has(steps: list[dict], node: str) -> bool:
    return any(step.get("node") == node for step in steps)
