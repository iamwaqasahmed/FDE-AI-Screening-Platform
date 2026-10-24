"""Run the Day 4 agent and read the note. A miss does not print the watermark."""

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
    reply = row.get("reply")
    if not isinstance(reply, dict) or not _REPLY.issubset(reply):
        return False
    lists = ("citations", "tool_trace", "pending_approval_ids", "approval_ids")
    return _TOP.issubset(row) and all(isinstance(row[name], list) for name in lists)


def grouped(rows: list) -> dict[str, list[dict]] | None:
    found: dict[str, list[dict]] = {}
    for row in rows:
        if not isinstance(row, dict) or "scenario" not in row:
            return None
        found.setdefault(str(row["scenario"]), []).append(row)
    return found


def one(rows: list[dict]) -> dict | None:
    if len(rows) != 1 or not ready(rows[0]):
        return None
    return rows[0]


def run_agent(work: Path, pack: Path, canary: str, failures: Path | None = None) -> tuple[list[str], list | None]:
    script = (work / "agent" / "run.py").resolve()
    pack = Path(pack).resolve()
    if not script.is_file():
        return ["run.py is missing"], None
    command = [sys.executable, str(script), "--pack", str(pack), "--out"]
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "trace.json"
        command.append(str(out))
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
        if canary.encode() in raw:
            return [WATERMARK], None
        try:
            parsed = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            return ["trace is not a list"], None
        if not isinstance(parsed, list):
            return ["trace is not a list"], None
        return [], parsed


def _section(text: str, heading: str) -> str:
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
    return sum(1 for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)) >= 2


def prose(work: Path) -> list[str]:
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
        if "extract" not in boundary or ("book" not in boundary and "message" not in boundary):
            problems.append("the note does not separate extract from book and message")
        if len(refusal.split()) < 3:
            problems.append("the note does not say what the patient sees on a refusal")
    knowledge = work / "knowledge.md"
    if not knowledge.is_file() or not _answers(knowledge.read_text(encoding="utf-8")):
        problems.append("knowledge.md needs two answers")
    return problems


def load_rows(work: Path, pack: Path, canary: str, failures: Path | None = None) -> tuple[list[str], list | None]:
    if contains_canary(work, canary):
        return [WATERMARK], None
    return run_agent(work, pack, canary, failures)
