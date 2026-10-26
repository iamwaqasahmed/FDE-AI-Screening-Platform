"""chk-w4-integrate. A miss does not print a lag or a count.

This check grades staff sign-in, the bus, the handoff, late leave, and the warehouse clock. A staff role must be accepted and a service token must not. An unknown bus field must be kept. A cancellation must be kept. A handoff with a summary must copy it, and a handoff without one must be refused. Late leave must cancel the session and emit the cancellation event. The warehouse clock is the referral time. Notes are graded last. A lag or a count is not printed. Gold is unused because the rows come from the pack.
"""

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
    """Append the miss when that sentence is not already in the list.

    Several probes can fail the same way, and the list should name each failure once.
    """
    if item not in problems:
        problems.append(item)


def _rows(path: Path) -> list[dict]:
    """Return the non-blank lines of a JSON-lines file as records.

    A blank line is skipped so a trailing newline is not parsed as a row.
    """
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _signin(module, sheet: dict) -> list[str]:
    """Return the sign-in misses.

    A crash, or a result that is not a record, fails both the staff acceptance and the service rejection. A staff actor that is not accepted is the staff miss. A service actor that is accepted is the service miss.
    """
    problems = []
    for actor in sheet["actors"]:
        try:
            got = module.accept(actor)
        except Exception:
            return [RUN]
        # A result that is not a record fails both sign-in rules, so the caller does not have to guess which one.
        if not isinstance(got, dict):
            return [STAFF, SERVICE]
        staff = bool(got.get("staff"))
        if actor.get("kind") == "staff" and not staff:
            _once(problems, STAFF)
        if actor.get("kind") == "service" and staff:
            _once(problems, SERVICE)
    return problems


def _bus(module, rows: list[dict]) -> list[str]:
    """Return the bus misses.

    A crash, or a result that is not a record, fails both the unknown-field rule and the cancellation rule. An event with a field outside the known set must still be kept, and its id must survive. A cancellation must be kept under that same topic.
    """
    problems = []
    for event in rows:
        try:
            got = module.consume(event)
        except Exception:
            return [RUN]
        if not isinstance(got, dict):
            return [UNKNOWN, MISSED]
        # Fields outside the known set are the unknown-field case. They must still be kept.
        extra = set(event) - _KNOWN
        if extra and (not got.get("kept") or got.get("id") != event.get("id")):
            _once(problems, UNKNOWN)
        if event.get("topic") == "session.cancelled" and (got.get("topic") != "session.cancelled" or not got.get("kept")):
            _once(problems, MISSED)
    return problems


def _handoff(module, rows: list[dict]) -> list[str]:
    """Return the summary miss, or nothing when every call is right.

    A crash or a non-record is the summary miss. A call that already has a summary must copy it and must not refuse. A call with no summary must be refused, and must not name an agent or invent a summary.
    """
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
        # A call with no summary must be refused, and must not name an agent or invent a summary.
        elif not got.get("refused") or got.get("agent") or got.get("summary"):
            return [SUMMARY]
    return []


def _leave(module, row: dict) -> list[str]:
    """Return the late-leave misses.

    A crash or a non-record fails both the status and the event. The status must be cancelled. The event must be the cancellation topic. Those are separate misses.
    """
    # The session and the leave are the records the module applies.
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
        # A crash fails both the status and the event.
        return [RUN]
    # A result that is not a record fails both checks together.
    if not isinstance(got, dict):
        return [LATE, EVENT]
    problems = []
    # The status must be cancelled. That check is separate from the event.
    if got.get("status") != "cancelled":
        problems.append(LATE)
    # The emitted event must be the cancellation topic.
    if got.get("event") != "session.cancelled":
        problems.append(EVENT)
    return problems


def _clock(module, rows: list[dict]) -> list[str]:
    """Return the clock miss when any row's clock is not the referral time.

    A crash is the harness miss. The referral time is the warehouse clock. A booking time is not.
    """
    for row in rows:
        try:
            got = module.clock(row)
        except Exception:
            return [RUN]
        # The warehouse clock has to be the referral time on the row, not a later booking time.
        if got != row.get("referred_at"):
            return [CLOCK]
    return []


def integrate_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the integration misses and then the note misses.

    Gold is discarded because every row comes from the pack. A planted token returns only the watermark. The five modules run under one import. Leave uses the first leave row. A crash of the import is the harness miss. Notes are graded afterward.
    """
    # Gold is unused. The rows come from the pack. The caller still loads the release so a missing pack fails first.
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
