"""chk-w4-integrate. A miss does not print a lag or a count."""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.notes_w4d5 import note_problems
from alwaha.check.tables import contains_canary

CLOCK = "the warehouse clock starts at booking"
EVENT = "leave does not emit session.cancelled"
LATE = "late leave leaves the session published"
MISSED = "the bus misses session.cancelled"
RUN = "the harness did not run"
SERVICE = "a service token is accepted as staff"
STAFF = "staff sign-in rejects a staff role"
SUMMARY = "the handoff has no summary"
UNKNOWN = "the bus drops an event with an unknown field"
_KNOWN = {"id", "session", "topic"}
_MODULES = ("signin", "bus", "handoff", "leave", "warehouse")


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)


def _rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _signin(module, sheet: dict) -> list[str]:
    problems = []
    for actor in sheet["actors"]:
        try:
            got = module.accept(actor)
        except Exception:
            return [RUN]
        if not isinstance(got, dict):
            return [STAFF, SERVICE]
        staff = bool(got.get("staff"))
        if actor.get("kind") == "staff" and not staff:
            _once(problems, STAFF)
        if actor.get("kind") == "service" and staff:
            _once(problems, SERVICE)
    return problems


def _bus(module, rows: list[dict]) -> list[str]:
    problems = []
    for event in rows:
        try:
            got = module.consume(event)
        except Exception:
            return [RUN]
        if not isinstance(got, dict):
            return [UNKNOWN, MISSED]
        extra = set(event) - _KNOWN
        if extra and (not got.get("kept") or got.get("id") != event.get("id")):
            _once(problems, UNKNOWN)
        if event.get("topic") == "session.cancelled" and (got.get("topic") != "session.cancelled" or not got.get("kept")):
            _once(problems, MISSED)
    return problems


def _handoff(module, rows: list[dict]) -> list[str]:
    for call in rows:
        try:
            got = module.handoff(call)
        except Exception:
            return [RUN]
        if not isinstance(got, dict):
            return [SUMMARY]
        summary = str(call.get("summary") or "").strip()
        if summary:
            if got.get("summary") != summary or got.get("refused"):
                return [SUMMARY]
        elif not got.get("refused") or got.get("agent") or got.get("summary"):
            return [SUMMARY]
    return []


def _leave(module, row: dict) -> list[str]:
    session = {
        "consultant": row["consultant"],
        "id": row["session"],
        "published_at": row["published_at"],
        "status": row["status"],
    }
    leave = {"consultant": row["consultant"], "entered_at": row["entered_at"], "id": row["id"]}
    try:
        got = module.apply(session, leave)
    except Exception:
        return [RUN]
    if not isinstance(got, dict):
        return [LATE, EVENT]
    problems = []
    if got.get("status") != "cancelled":
        problems.append(LATE)
    if got.get("event") != "session.cancelled":
        problems.append(EVENT)
    return problems


def _clock(module, rows: list[dict]) -> list[str]:
    for row in rows:
        try:
            got = module.clock(row)
        except Exception:
            return [RUN]
        if got != row.get("referred_at"):
            return [CLOCK]
    return []


def integrate_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    del gold
    if contains_canary(work, canary):
        return [WATERMARK]
    sheet = json.loads((pack / "iam" / "staff.json").read_text(encoding="utf-8"))
    bus_rows = _rows(pack / "bus" / "events.jsonl")
    calls = _rows(pack / "cc" / "handoff.jsonl")
    leave_rows = _rows(pack / "hr" / "leave.jsonl")
    feed = _rows(pack / "warehouse" / "feed.jsonl")
    problems: list[str] = []
    try:
        with modules(work / "app", _MODULES) as loaded:
            for item in _signin(loaded["signin"], sheet):
                _once(problems, item)
            for item in _bus(loaded["bus"], bus_rows):
                _once(problems, item)
            for item in _handoff(loaded["handoff"], calls):
                _once(problems, item)
            for item in _leave(loaded["leave"], leave_rows[0]):
                _once(problems, item)
            for item in _clock(loaded["warehouse"], feed):
                _once(problems, item)
    except Exception:
        _once(problems, RUN)
    for item in note_problems(work):
        _once(problems, item)
    return problems
