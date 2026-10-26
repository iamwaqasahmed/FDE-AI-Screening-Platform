"""Written notes for Week 3 Day 2. A miss does not print a hash, a price, or an F1.

Written notes for the model day. The sprint must move from the baseline to the adapter, then registration, then the memo, and it must close the cloud fine-tune. Residency must keep identity fields private and clinic hours public. The knowledge note must leave hours on retrieval and name the hash that is legal to serve. The approach table is graded here and again by the model check once scores exist.
"""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.approach import _fits
from alwaha.check.rubric import two_answers
from alwaha.check.tables import dict_rows, token_in
from alwaha.engagement.w3d2_rules import format_f1
from alwaha.samples.gold import gold_payload

_APPROACH = "approach.md is missing"
_DNA = "dna is not a tabular model"
_FAMILY = "family does not fit"
_HASH = "the hash is not on reg-models"
_HOURS = "hours questions are not left on retrieval"
_KNOW = "knowledge.md needs two answers"
_LEGAL = "knowledge.md does not say which hash is legal to serve"
_MEASURED = "the measured value does not match the adapter"
_PROMPT = "the prompt baseline is still the served model"
_RETRIEVAL = "knowledge.md does not say which problem stays on retrieval"
_RESIDENCY = "the residency note lets a phi field leave"
_SPRINT = "sprint.md does not sequence the adapter"
_PHI = {
    "national id": "zone-private",
    "date of birth": "zone-private",
    "name": "zone-private",
    "phone": "zone-private",
}
_TASKS = {"extraction", "intent", "hours"}


def _text(path: Path) -> str:
    """Return the file text, or an empty string when the path is not a file.

    Callers treat empty text as a missing note and report a content miss instead of raising.
    """
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list.

    Several note groups can fail the same way, and the list should name each failure once.
    """
    if item not in problems:
        problems.append(item)


def sprint_problems(work: Path) -> list[str]:
    """Return the sprint miss unless the baseline, the adapter, registration, and the memo appear in that order and the cloud fine-tune is closed.

    A missing step, the wrong order, or a missing closing sentence is the same miss.
    """
    lowered = _text(work / "sprint.md").lower()
    baseline = lowered.find("baseline")
    adapter = lowered.find("adapter")
    register = lowered.find("register")
    memo = lowered.find("memo")
    closed = "cloud fine-tune is closed" in lowered
    # The four steps must exist in that order, and the closing sentence must be present. Either gap is the same miss.
    if not (0 <= baseline < adapter < register < memo and closed):
        return [_SPRINT]
    return []


def residency_problems(work: Path) -> list[str]:
    """Return the residency miss.

    Each identity field must sit in the private zone. Clinic hours must sit in the public zone. A wrong zone on the hours row is the same miss as a private field in the wrong zone.
    """
    rows = dict_rows(_text(work / "residency.md"), {"field", "zone"})
    found = {row["field"].lower(): row["zone"].lower() for row in rows} if rows else {}
    if any(found.get(field) != zone for field, zone in _PHI.items()):
        return [_RESIDENCY]
    # Clinic hours are the field that is allowed to be public. A wrong zone on that row is the same miss as a private field placed badly.
    if found.get("clinic hours") != "public":
        return [_RESIDENCY]
    return []


def knowledge_problems(work: Path) -> list[str]:
    """Return the knowledge misses.

    Fewer than two numbered answers is the two-answer miss. The first answer must mention retrieval and either hours or the information problem. The second must name the local adapter and the model register.
    """
    text = _text(work / "knowledge.md")
    answers = [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    # Fewer than two numbered answers is the two-answer miss.
    if len(answers) < 2 or not two_answers(text):
        return [_KNOW]
    problems = []
    first = answers[0].lower()
    # The first answer must mention retrieval, and either hours or the information problem.
    if "retriev" not in first or not any(token in first for token in ("hour", "p-info")):
        problems.append(_RETRIEVAL)
    second = answers[1].lower()
    # The second answer must name the local adapter and the model register.
    if "lora-local" not in second or "reg-models" not in second:
        problems.append(_LEGAL)
    return problems


def approach_problems(work: Path, gold: dict, extraction_f1: float | None, intent_f1: float | None) -> list[str]:
    """Return the approach-table misses.

    A missing file or a missing table is the approach miss. An unknown id is ignored. A family that does not fit is a specific miss for the two named problems and a generic family miss otherwise. A known id that never appears, or a row with no system, reason, or citation, is the approach miss. The task table must contain every task. Hours must use retrieval. Extraction and intent are measured only when a score is supplied.
    """
    text = _text(work / "approach.md")
    if not text:
        return [_APPROACH]
    families = dict_rows(text, {"id", "family", "measured", "citation", "system", "reason"})
    tasks = dict_rows(text, {"task", "method", "f1", "cost", "hash"})
    if families is None or tasks is None:
        return [_APPROACH]
    problems: list[str] = []
    payload = gold_payload()
    rules = payload["problems"]
    allowed = set(payload["allowed"])
    seen: dict[str, int] = {}
    for row in families:
        problem_id = row["id"]
        if not problem_id:
            continue
        seen[problem_id] = seen.get(problem_id, 0) + 1
        # An unknown id is ignored here. A missing known id is reported later as the approach miss.
        if problem_id not in rules:
            continue
        if not _fits(row["family"], rules[problem_id], allowed):
            # This problem is the one that must not be a tabular model, so it gets its own miss.
            if problem_id == "p-dna":
                _once(problems, _DNA)
            # This problem is the one that must stay on retrieval, so a bad family is the hours miss.
            elif problem_id == "p-info":
                _once(problems, _HOURS)
            else:
                _once(problems, _FAMILY)
        if not row["system"] or not row["reason"] or not row["citation"]:
            _once(problems, _APPROACH)
    for problem_id in rules:
        if problem_id not in seen:
            _once(problems, _APPROACH)
    by_task = {row["task"]: row for row in tasks if row["task"] in _TASKS}
    if set(by_task) != _TASKS:
        _once(problems, _APPROACH)
        return problems
    if by_task["hours"]["method"] != "retrieve":
        _once(problems, _HOURS)
    _task_measurement(problems, by_task["extraction"], extraction_f1, gold)
    _task_measurement(problems, by_task["intent"], intent_f1, gold)
    return problems


def _task_measurement(problems: list[str], row: dict, score: float | None, gold: dict) -> None:
    """Record the measurement misses for one task row, or return without one.

    A method other than lora is the prompt-baseline miss, and the score is not checked. A missing score, or a score under the floor, returns quietly because the code check reports the budget. Once the floor is cleared, the written score, the cost, and the hash must match.
    """
    if row["method"] != "lora":
        _once(problems, _PROMPT)
        return
    # The written score is checked only after the code has cleared the floor. Under the floor, this helper stays quiet.
    if score is None or score < gold["cap"]["f1_floor"]:
        return
    if not token_in(row["f1"], format_f1(score)):
        _once(problems, _MEASURED)
    if not token_in(row["cost"], str(gold["local_sar"])):
        _once(problems, _MEASURED)
    if gold["adapter_hash"] not in row["hash"]:
        _once(problems, _HASH)
