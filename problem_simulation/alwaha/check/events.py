"""chk-w1-events. A miss does not print the due date, the clause, or the fitting state."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from alwaha.check.tables import contains_canary

_FIELDS = (
    "state",
    "due",
    "approval_ids",
    "booked",
    "criteria_id",
    "suggested_facility",
    "clinic",
    "duplicate",
    "hold",
    "dead_letter",
)
_WATERMARK = "a watermarked sample is in the work directory"


def _ready(row: dict) -> bool:
    return all(key in row for key in _FIELDS) and isinstance(row.get("approval_ids"), list)


def _merged(rows: list[dict]) -> dict | None:
    if not rows or any(not isinstance(row, dict) or not _ready(row) for row in rows):
        return None
    merged = dict(rows[0])
    approvals: list[str] = []
    for row in rows:
        approvals.extend(row["approval_ids"])
    merged["approval_ids"] = approvals
    return merged


def _grouped(rows: list) -> dict[str, list[dict]] | None:
    grouped: dict[str, list[dict]] = {}
    for row in rows:
        if not isinstance(row, dict) or "scenario" not in row:
            return None
        grouped.setdefault(str(row["scenario"]), []).append(row)
    return grouped


def _live(name: str, gold: dict, row: dict) -> list[str]:
    problems = []
    approvals = row["approval_ids"]
    stopped = len(approvals) == 1 and row["state"] == gold["state"] and not row["dead_letter"]
    if len(approvals) > 1:
        problems.append(f"{name} opened a second approval")
    elif not stopped:
        problems.append(f"{name} did not stop for a person")
    if row["due"] != gold["due"]:
        problems.append(f"{name} due date does not match the calendar")
    if row["criteria_id"] != gold["criteria_id"]:
        problems.append(f"{name} criteria is not the one in force")
    if row["booked"] != gold["booked"]:
        problems.append(f"{name} booked a slot" if row["booked"] else f"{name} booking does not match")
    if row["suggested_facility"] != gold["suggested_facility"]:
        problems.append(f"{name} suggestion does not match")
    if row["clinic"] != gold["clinic"]:
        problems.append(f"{name} clinic does not match")
    if bool(row["duplicate"]) != bool(gold["duplicate"]):
        word = "was not flagged" if gold["duplicate"] else "was flagged"
        problems.append(f"{name} referral {word}")
    if row["hold"] != gold["hold"]:
        problems.append(f"{name} hold does not match")
    return problems


def _scenario(name: str, gold: dict, rows: list[dict]) -> list[str]:
    if not rows:
        return [f"{name} is missing"]
    row = _merged(rows)
    if row is None:
        return [f"{name} log is missing a field"]
    if gold["dead_letter"]:
        applied = not row["dead_letter"] or row["approval_ids"] or row["booked"] or row["hold"] == "open"
        return [f"{name} applied the poison event"] if applied else []
    return _live(name, gold, row)


def _scenarios(rows: list, gold: dict) -> list[str]:
    grouped = _grouped(rows)
    if grouped is None:
        return ["scenario log is missing a field"]
    problems = []
    for item in gold["scenarios"]:
        problems.extend(_scenario(item["scenario"], item, grouped.get(item["scenario"], [])))
    return problems


def _answers(text: str) -> bool:
    return sum(1 for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)) >= 2


def _prose(work: Path) -> list[str]:
    problems = []
    intake = work / "intake.md"
    if not intake.is_file():
        problems.append("intake.md is missing")
    else:
        text = intake.read_text(encoding="utf-8").lower()
        if "coordinator" not in text and "human" not in text:
            problems.append("the diagram does not show the human step")
        if not ("in-flight" in text and "criteria" in text and "version" in text):
            problems.append("the note does not keep the criteria version")
    knowledge = work / "knowledge.md"
    if not knowledge.is_file() or not _answers(knowledge.read_text(encoding="utf-8")):
        problems.append("knowledge.md needs two answers")
    return problems


def _run(worker: Path, pack: Path, canary: str) -> tuple[list[str], list | None]:
    worker = worker.resolve()
    pack = Path(pack).resolve()
    if not worker.is_file():
        return ["worker.py is missing"], None
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "scenario-log.json"
        try:
            completed = subprocess.run(
                [sys.executable, str(worker), "--pack", str(pack), "--out", str(out)],
                cwd=worker.parent,
                capture_output=True,
                text=True,
                timeout=30,
                check=False,
            )
        except (subprocess.TimeoutExpired, OSError):
            return ["worker did not run"], None
        if completed.returncode != 0 or not out.is_file():
            return ["worker did not run"], None
        raw = out.read_bytes()
        if canary.encode() in raw:
            return [_WATERMARK], None
        try:
            parsed = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            return ["scenario log is not a list"], None
        if not isinstance(parsed, list):
            return ["scenario log is not a list"], None
        return [], parsed


def events_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [_WATERMARK]
    problems, rows = _run(work / "workflow" / "worker.py", pack, canary)
    if rows is not None:
        problems.extend(_scenarios(rows, gold))
    problems.extend(_prose(work))
    return problems
