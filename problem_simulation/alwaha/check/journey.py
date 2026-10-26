"""chk-w2-journey for a status question. A miss does not name the field or the count.

This check grades a status question against the shell exercise. It fails a book call, a wrong count, a wrong state, a wrong facility, an open approval, a missing citation, a thin health report, and an approval that is not held. The knowledge note must answer where assurance sits and where the session row lives. A miss does not name the field or the count.
"""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.shell import exercise


def _knowledge(work: Path) -> list[str]:
    """Return the knowledge-note misses.

    A missing file, or fewer than two numbered answers, is the two-answer miss. The first answer must name the booking assurance level. The second must say the session row lives in the database.
    """
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
    """Return the status-question misses plus the knowledge misses.

    If the shell returns no record, its misses are the whole result and the knowledge note is not graded. Otherwise a failed direct read, a missing status tool, and any book call are misses. The book call can show up on the answer, in its trace, on the probe, or in the probe trace. The count, state, and facility must match gold. A non-empty pending-approval list means an approval was left open. The status citation is required only when gold says the tool is status. Health must report a model hash, a prompt version, and a dependencies entry. The approval must be held for a later day.
    """
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
    # A book call counts wherever it appears: on the answer, in the answer trace, on the probe, or in the probe trace.
    if answer.get("booked") or "book" in trace or probe.get("booked") or "book" in probe.get("tool_trace", []):
        problems.append("a book call was made")
    if answer.get("count") != status["count"]:
        problems.append("status count does not match")
    if answer.get("state") != status["state"]:
        problems.append("status state does not match")
    if answer.get("facility_id") != status["facility_id"]:
        problems.append("facility does not match")
    # An empty list is fine. Any pending id means an approval was left open.
    if answer.get("pending_approval_ids"):
        problems.append("an approval was left open")
    # The citation is required only when gold says this scenario's tool is status.
    if status["tool"] == "status" and "his-wadi" not in answer.get("citations", []):
        problems.append("the status reply has no citation")
    health = found["health"]
    # Health has to name the model, the prompt, and the dependency list. Any one missing is the same miss.
    if not health.get("model_hash") or not health.get("prompt_version") or "dependencies" not in health:
        problems.append("health does not report the model")
    if found["approval"].get("status") != "later":
        problems.append("approval is not held for a later day")
    return problems + _knowledge(work)
