"""chk-events. A miss does not print the due date, the clause, or the fitting state.

This check runs the participant worker and grades the scenario log. A poison scenario must not be applied. A live scenario must stop for one person, keep the calendar due date, the criteria in force, and the booking, suggestion, clinic, duplicate, and hold flags. The intake note must show a human step and must keep the criteria version. A due date, a clause, or a fitting state is not printed.
"""

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
    """Return true when a log row has every required field and its approval list is a list.

    A missing field or an approval value that is not a list is not ready.
    """
    return all(key in row for key in _FIELDS) and isinstance(row.get("approval_ids"), list)


def _merged(rows: list[dict]) -> dict | None:
    """Merge several rows for one scenario into one row, or return nothing.

    An empty group, or any row that is not ready, cannot be merged. Approval ids are concatenated so a split log still carries every approval. The other fields come from the first row.
    """
    if not rows or any(not isinstance(row, dict) or not _ready(row) for row in rows):
        return None
    merged = dict(rows[0])
    approvals: list[str] = []
    for row in rows:
        approvals.extend(row["approval_ids"])
    merged["approval_ids"] = approvals
    return merged


def _grouped(rows: list) -> dict[str, list[dict]] | None:
    """Group log rows by scenario, or return nothing if any row cannot be grouped.

    A row that is not a record, or a row with no scenario, rejects the whole log.
    """
    grouped: dict[str, list[dict]] = {}
    for row in rows:
        if not isinstance(row, dict) or "scenario" not in row:
            return None
        grouped.setdefault(str(row["scenario"]), []).append(row)
    return grouped


def _live(name: str, gold: dict, row: dict) -> list[str]:
    """Return the misses for a scenario that should have been applied.

    Stopping for a person means one approval, the expected state, and not a dead letter. A second approval is its own miss. A case that did not stop is a different miss. The due date, the criteria, the suggestion, the clinic, and the hold must match. Booking and the duplicate flag have messages that say which way they disagree.
    """
    problems = []
    approvals = row["approval_ids"]
    # Stopping for a person means one approval, the expected state, and not a dead letter.
    stopped = len(approvals) == 1 and row["state"] == gold["state"] and not row["dead_letter"]
    if len(approvals) > 1:
        problems.append(f"{name} opened a second approval")
    # A second approval was already reported. This branch is the case that never stopped for a person.
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
        # The message says which way the duplicate flag is wrong.
        word = "was not flagged" if gold["duplicate"] else "was flagged"
        problems.append(f"{name} referral {word}")
    if row["hold"] != gold["hold"]:
        problems.append(f"{name} hold does not match")
    return problems


def _scenario(name: str, gold: dict, rows: list[dict]) -> list[str]:
    """Return the misses for one scenario.

    No rows means the scenario is missing. Rows that cannot be merged are a missing field. A poison scenario fails if it was applied at all: it is not dead-lettered, or it opened an approval, booked, or left a hold open. Any other scenario is graded as live.
    """
    if not rows:
        return [f"{name} is missing"]
    row = _merged(rows)
    if row is None:
        return [f"{name} log is missing a field"]
    if gold["dead_letter"]:
        # Any of these means the poison event was applied: it was not dead-lettered, or it opened an approval, booked, or left a hold open.
        applied = not row["dead_letter"] or row["approval_ids"] or row["booked"] or row["hold"] == "open"
        return [f"{name} applied the poison event"] if applied else []
    return _live(name, gold, row)


def _scenarios(rows: list, gold: dict) -> list[str]:
    """Return the misses for every gold scenario.

    A log that cannot be grouped is one missing-field miss. Otherwise each gold scenario is graded, including one that has no rows.
    """
    grouped = _grouped(rows)
    if grouped is None:
        return ["scenario log is missing a field"]
    problems = []
    for item in gold["scenarios"]:
        problems.extend(_scenario(item["scenario"], item, grouped.get(item["scenario"], [])))
    return problems


def _answers(text: str) -> bool:
    """Return true when the knowledge note has at least two numbered lines with text after the number."""
    return sum(1 for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)) >= 2


def _prose(work: Path) -> list[str]:
    """Return the note misses.

    A missing intake note is a miss. When it exists, it must show a human step, named as a coordinator or a human. It must also keep the criteria version by mentioning in-flight, criteria, and version together. The knowledge note must exist and have two numbered answers.
    """
    problems = []
    intake = work / "intake.md"
    # A missing intake note is its own miss. The human step is not guessed.
    if not intake.is_file():
        problems.append("intake.md is missing")
    else:
        text = intake.read_text(encoding="utf-8").lower()
        # The human step may be named as a coordinator or as a human.
        if "coordinator" not in text and "human" not in text:
            problems.append("the diagram does not show the human step")
        # The criteria version is kept only when in-flight, criteria, and version all appear.
        if not ("in-flight" in text and "criteria" in text and "version" in text):
            problems.append("the note does not keep the criteria version")
    knowledge = work / "knowledge.md"
    # The knowledge note must exist and have two numbered answers.
    if not knowledge.is_file() or not _answers(knowledge.read_text(encoding="utf-8")):
        problems.append("knowledge.md needs two answers")
    return problems


def _run(worker: Path, pack: Path, canary: str) -> tuple[list[str], list | None]:
    """Run the worker and return either problems and nothing, or no problems and the parsed log.

    A missing worker is its own miss. A timeout, an operating-system error, a non-zero exit, or a missing output file is the did-not-run miss. A token in the raw bytes is the watermark, before JSON is parsed. Text that is not JSON, and JSON that is not a list, share one miss.
    """
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
        # Text that is not JSON uses the same miss as a JSON value that is not a list.
        except json.JSONDecodeError:
            return ["scenario log is not a list"], None
        if not isinstance(parsed, list):
            return ["scenario log is not a list"], None
        return [], parsed


def events_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the worker misses and the note misses.

    A planted token in the work tree returns only the watermark and does not run the worker. When the log parsed, the scenarios are graded. The notes are graded even when the worker failed.
    """
    if contains_canary(work, canary):
        return [_WATERMARK]
    problems, rows = _run(work / "workflow" / "worker.py", pack, canary)
    if rows is not None:
        problems.extend(_scenarios(rows, gold))
    problems.extend(_prose(work))
    return problems
