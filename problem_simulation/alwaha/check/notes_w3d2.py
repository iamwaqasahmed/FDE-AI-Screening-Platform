"""Written notes for Week 3 Day 2. A miss does not print a hash, a price, or an F1."""

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
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)


def sprint_problems(work: Path) -> list[str]:
    lowered = _text(work / "sprint.md").lower()
    baseline = lowered.find("baseline")
    adapter = lowered.find("adapter")
    register = lowered.find("register")
    memo = lowered.find("memo")
    closed = "cloud fine-tune is closed" in lowered
    if not (0 <= baseline < adapter < register < memo and closed):
        return [_SPRINT]
    return []


def residency_problems(work: Path) -> list[str]:
    rows = dict_rows(_text(work / "residency.md"), {"field", "zone"})
    found = {row["field"].lower(): row["zone"].lower() for row in rows} if rows else {}
    if any(found.get(field) != zone for field, zone in _PHI.items()):
        return [_RESIDENCY]
    if found.get("clinic hours") != "public":
        return [_RESIDENCY]
    return []


def knowledge_problems(work: Path) -> list[str]:
    text = _text(work / "knowledge.md")
    answers = [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2 or not two_answers(text):
        return [_KNOW]
    problems = []
    first = answers[0].lower()
    if "retriev" not in first or not any(token in first for token in ("hour", "p-info")):
        problems.append(_RETRIEVAL)
    second = answers[1].lower()
    if "lora-local" not in second or "reg-models" not in second:
        problems.append(_LEGAL)
    return problems


def approach_problems(work: Path, gold: dict, extraction_f1: float | None, intent_f1: float | None) -> list[str]:
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
        if problem_id not in rules:
            continue
        if not _fits(row["family"], rules[problem_id], allowed):
            if problem_id == "p-dna":
                _once(problems, _DNA)
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
    if row["method"] != "lora":
        _once(problems, _PROMPT)
        return
    if score is None or score < gold["cap"]["f1_floor"]:
        return
    if not token_in(row["f1"], format_f1(score)):
        _once(problems, _MEASURED)
    if not token_in(row["cost"], str(gold["local_sar"])):
        _once(problems, _MEASURED)
    if gold["adapter_hash"] not in row["hash"]:
        _once(problems, _HASH)
