"""chk-w2-journey for a status question. A miss does not name the field or the count."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.shell import exercise


def _knowledge(work: Path) -> list[str]:
    path = work / "knowledge.md"
    if not path.is_file():
        return ["knowledge.md needs two answers"]
    answers = [line for line in path.read_text(encoding="utf-8").splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2:
        return ["knowledge.md needs two answers"]
    problems = []
    if "loa-2" not in answers[0]:
        problems.append("knowledge.md does not name the booking assurance level")
    if "database" not in answers[1].lower():
        problems.append("knowledge.md does not say where the session row lives")
    return problems


def journey_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    problems, found = exercise(work, pack, gold, canary)
    if found is None:
        return problems
    answer = found["answer"]
    probe = found["probe"]
    status = gold["status"]
    trace = answer.get("tool_trace", [])
    if not found["fhir_ok"]:
        problems.append("his-wadi read failed")
    if "status" not in trace:
        problems.append("status tool is missing")
    if answer.get("booked") or "book" in trace or probe.get("booked") or "book" in probe.get("tool_trace", []):
        problems.append("a book call was made")
    if answer.get("count") != status["count"]:
        problems.append("status count does not match")
    if answer.get("state") != status["state"]:
        problems.append("status state does not match")
    if answer.get("facility_id") != status["facility_id"]:
        problems.append("facility does not match")
    if answer.get("pending_approval_ids"):
        problems.append("an approval was left open")
    if status["tool"] == "status" and "his-wadi" not in answer.get("citations", []):
        problems.append("the status reply has no citation")
    health = found["health"]
    if not health.get("model_hash") or not health.get("prompt_version") or "dependencies" not in health:
        problems.append("health does not report the model")
    if found["approval"].get("status") != "later":
        problems.append("approval is not held for a later day")
    return problems + _knowledge(work)
