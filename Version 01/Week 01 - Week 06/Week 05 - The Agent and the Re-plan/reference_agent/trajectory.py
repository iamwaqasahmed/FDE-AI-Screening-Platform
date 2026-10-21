"""One step of a trajectory. Checkpoints are names, not patient records."""

from __future__ import annotations

STEP = 0.001
READ = 0.0001


def step(run: int, number: int, node: str, checkpoint: str, tool: str = "", reads: list | None = None, cost: float = STEP) -> dict:
    row = {"run": run, "step": number, "node": node, "checkpoint": checkpoint, "model_id": "M02", "cost_gbp": cost, "reads": list(reads or [])}
    if tool:
        row["tool"] = tool
    return row


def walk(path: list[str]) -> list[dict]:
    return [step(1, 1, "plan", "c1"), step(1, 2, "tool", "c2", "lookup", path), step(1, 3, "answer", "c3")]


def veto(rule: str) -> list[dict]:
    return [step(1, 1, "plan", "c1"), step(1, 2, "check", "c2"), {**step(1, 3, "veto", "c3"), "rule": rule}]


def approval(approver: str, path: list[str]) -> list[dict]:
    last = step(1, 3, "approval", "c3")
    last.update(approver=approver, decision="pending", reason="Waiting for the accountable person")
    return [step(1, 1, "plan", "c1"), step(1, 2, "tool", "c2", "draft", path), last]


def line(approver: str, path: list[str]) -> list[dict]:
    pending = step(1, 2, "approval", "c2")
    pending.update(approver=approver, decision="pending", reason="The line leaves the office")
    decided = step(2, 2, "approval", "c4")
    decided.update(approver=approver, decision="approved", reason="The line names no person and no date")
    return [step(1, 1, "plan", "c1"), pending, {**step(2, 1, "resume", "c2"), "checkpoint": "c2"}, decided, step(2, 3, "answer", "c5")]


def sweep(ids: list[str], tool: str) -> list[dict]:
    cut = max(len(ids) // 2, 1) if ids else 0
    steps = [step(1, 1, "plan", "c1")]
    for index, local_id in enumerate(ids[:cut], start=2):
        steps.append(step(1, index, "tool", f"c1-{index}", tool, [local_id], READ))
    resume_at = steps[-1]["checkpoint"]
    steps.append({**step(2, 1, "resume", "r1"), "checkpoint": resume_at})
    for index, local_id in enumerate(ids[cut:], start=2):
        steps.append(step(2, index, "tool", f"c2-{index}", tool, [local_id], READ))
    steps.append(step(2, len(ids[cut:]) + 2, "answer", "done"))
    return steps


def finish(case_id: str, answer, citation: dict, path: list, refused: bool, steps: list[dict]) -> dict:
    return {
        "case_id": case_id, "answer": answer, "citation": citation or {}, "path": list(path), "refused": refused,
        "followed_injection": False, "trajectory": steps,
        "usage": {"tokens": 800, "seconds": 2, "cost_gbp": round(sum(row["cost_gbp"] for row in steps), 4), "model_id": "M02"},
    }
