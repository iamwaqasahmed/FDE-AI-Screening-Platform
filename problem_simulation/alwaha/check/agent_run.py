"""Run the Lesson 4 agent and read the note. A miss does not print the watermark.

Run the participant agent, read its trace, and grade the written note. A planted token in the work tree stops the run. A token inside the trace file is the same watermark, and it is caught before the trace is parsed so the token is not copied into a later message. The note grader looks at the tool list, the privilege boundary, and the refusal the patient would see.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from alwaha.check.tables import contains_canary

WATERMARK = "a watermarked sample is in the work directory"
_REPLY = {"intent", "text", "count", "facility_id", "constraint"}
_TOP = {
    "scenario",
    "citations",
    "tool_trace",
    "pending_approval_ids",
    "approval_ids",
    "booked",
    "returned",
    "redirected",
    "sms",
    "refusal_logged",
    "preference_used",
    "decisions",
}


def ready(row: dict) -> bool:
    """Return true when one trace row has a complete reply and the list fields are lists.

    The reply must be a record containing every reply field. The citation, trace, and both approval lists must be lists. Anything else is not ready.
    """
    reply = row.get("reply")
    if not isinstance(reply, dict) or not _REPLY.issubset(reply):
        return False
    lists = ("citations", "tool_trace", "pending_approval_ids", "approval_ids")
    return _TOP.issubset(row) and all(isinstance(row[name], list) for name in lists)


def grouped(rows: list) -> dict[str, list[dict]] | None:
    """Group trace rows by scenario, or return nothing if any row cannot be grouped.

    A row that is not a record, or a row with no scenario, rejects the whole trace. Later checks then report one missing-field miss instead of grading a partial group.
    """
    found: dict[str, list[dict]] = {}
    for row in rows:
        # One bad row rejects the whole trace, so a later check does not grade a partial group.
        if not isinstance(row, dict) or "scenario" not in row:
            return None
        found.setdefault(str(row["scenario"]), []).append(row)
    return found


def one(rows: list[dict]) -> dict | None:
    """Return the single ready row, or nothing.

    Zero rows, more than one row, or one row that is not ready are all nothing. Callers treat that as a missing field.
    """
    # Any count other than one row, or one row that is not ready, is treated as a missing field.
    if len(rows) != 1 or not ready(rows[0]):
        return None
    return rows[0]


def run_agent(work: Path, pack: Path, canary: str, failures: Path | None = None) -> tuple[list[str], list | None]:
    """Run the agent script and return either problems and nothing, or no problems and the parsed trace.

    A missing script is its own miss. An optional failures directory is passed only when the caller has one. A timeout or an operating-system error is the did-not-run miss, and so is a non-zero exit or a missing output file. A token in the raw bytes is the watermark, before JSON is parsed. Text that is not JSON, and JSON that is not a list, share one miss.
    """
    script = (work / "agent" / "run.py").resolve()
    pack = Path(pack).resolve()
    if not script.is_file():
        return ["run.py is missing"], None
    command = [sys.executable, str(script), "--pack", str(pack), "--out"]
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "trace.json"
        command.append(str(out))
        # The failures pack is optional. The day-four run does not have one. The later rescore does.
        if failures is not None:
            command.extend(["--failures", str(Path(failures).resolve())])
        try:
            completed = subprocess.run(
                command,
                cwd=script.parent,
                capture_output=True,
                text=True,
                timeout=30,
                check=False,
            )
        except (subprocess.TimeoutExpired, OSError):
            return ["agent did not run"], None
        if completed.returncode != 0 or not out.is_file():
            return ["agent did not run"], None
        raw = out.read_bytes()
        # The token is caught in the raw bytes, before the trace is parsed, so it is not copied into a later message.
        if canary.encode() in raw:
            return [WATERMARK], None
        try:
            parsed = json.loads(raw.decode("utf-8"))
        # Text that is not JSON uses the same miss as a JSON value that is not a list.
        except json.JSONDecodeError:
            return ["trace is not a list"], None
        if not isinstance(parsed, list):
            return ["trace is not a list"], None
        return [], parsed


def _section(text: str, heading: str) -> str:
    """Return the body under one heading, without the following section.

    A missing heading is empty. The body stops at the next heading.
    """
    marker = f"## {heading}".lower()
    start = text.lower().find(marker)
    if start < 0:
        return ""
    rest = text[start + len(marker) :]
    nxt = rest.find("\n## ")
    if nxt >= 0:
        rest = rest[:nxt]
    return rest.strip()


def _answers(text: str) -> bool:
    """Return true when the knowledge note has at least two numbered lines with text after the number.

    A bare number does not count.
    """
    return sum(1 for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)) >= 2


def prose(work: Path) -> list[str]:
    """Return the note misses.

    A missing agent note is a miss. When it exists, the tool list must name the status tool. The privilege boundary must name extract and must also name book or message, so extract is separated from an action. The refusal section must be long enough to tell the patient what they see. The knowledge note must exist and have two numbered answers.
    """
    problems = []
    note = work / "agent-note.md"
    if not note.is_file():
        problems.append("agent-note.md is missing")
    else:
        text = note.read_text(encoding="utf-8")
        tools = _section(text, "Tool list")
        boundary = _section(text, "Privilege boundary").lower()
        refusal = _section(text, "Refusal")
        if "referral.status" not in tools:
            problems.append("the note does not list the status tool")
        # The boundary has to name extract, and it has to name an action, either book or message.
        if "extract" not in boundary or ("book" not in boundary and "message" not in boundary):
            problems.append("the note does not separate extract from book and message")
        # Fewer words than a short sentence is not enough to tell the patient what a refusal looks like.
        if len(refusal.split()) < 3:
            problems.append("the note does not say what the patient sees on a refusal")
    knowledge = work / "knowledge.md"
    if not knowledge.is_file() or not _answers(knowledge.read_text(encoding="utf-8")):
        problems.append("knowledge.md needs two answers")
    return problems


def load_rows(work: Path, pack: Path, canary: str, failures: Path | None = None) -> tuple[list[str], list | None]:
    """Return problems and either the trace rows or nothing.

    A planted token in the work tree returns the watermark and does not run the agent. Otherwise the agent is run and its result is returned.
    """
    if contains_canary(work, canary):
        return [WATERMARK], None
    return run_agent(work, pack, canary, failures)
