"""chk-w2-tests. A miss does not name the interval, the delay, or a due date.

This check grades the calendar, the reply schema, the journey assertion, and the receipt clock. A sleep in the receipt test or the receipt module is a miss and does not stop the other probes. The receipt fault is a miss only when the switch is on and the result is already due. Any other clock disagreement is the clock miss. An interval, a delay, or a due date is not printed.
"""

from __future__ import annotations

import importlib
import json
import sys
from datetime import date
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.tables import contains_canary
from alwaha.serve.clock import advance
from alwaha.serve.receipt import due
from alwaha.world.calendar import add_working_days, calendar_document, holiday_dates

_NAMES = ("calendar_count", "schema", "receipt")
_TESTS = ("test_calendar.py", "test_schema.py", "test_receipt.py", "test_journey.py")
_SENT = "2027-01-19T09:00:00"
_CALENDAR = "the calendar does not match"
_SCHEMA = "the reply schema is missing"
_JOURNEY = "the journey followed the sentence"
_FAULT = "the suite accepted the receipt fault"
_CLOCK = "the receipt test does not match the clock"
_SLEEP = "the receipt test sleeps"


def load_suite(folder: Path) -> dict:
    """Import the calendar, schema, and receipt modules and return them.

    Each name is removed before import. The path is always restored. A name that was not cached is removed. A name that was cached is put back.
    """
    folder = folder.resolve()
    saved_path = list(sys.path)
    saved = {name: sys.modules.get(name) for name in _NAMES}
    sys.path.insert(0, str(folder))
    try:
        for name in _NAMES:
            sys.modules.pop(name, None)
        for name in _NAMES:
            importlib.import_module(name)
        return {name: sys.modules[name] for name in _NAMES}
    finally:
        sys.path[:] = saved_path
        for name, module in saved.items():
            # Nothing was cached under this name, so it is removed rather than restored.
            if module is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = module


def _present(work: Path) -> bool:
    """Return true when every graded module and every graded test file exists.

    Any missing file makes the caller report one missing-suite miss.
    """
    modules = all((work / "app" / f"{name}.py").is_file() for name in _NAMES)
    tests = all((work / "tests" / name).is_file() for name in _TESTS)
    return modules and tests


def _sleeps(work: Path) -> bool:
    """Return true when the receipt test or the receipt module contains a sleep.

    The calendar and the other probes still run. The sleep is an extra miss, not a reason to stop.
    """
    for relative in ("tests/test_receipt.py", "app/receipt.py"):
        path = work / relative
        if path.is_file() and "sleep" in path.read_text(encoding="utf-8"):
            return True
    return False


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list.

    Several receipt probes can fail the same way.
    """
    if item not in problems:
        problems.append(item)


def _calendar(app: dict, cases: list[dict]) -> list[str]:
    """Return the calendar miss on the first case that disagrees with the working-day helper.

    Later cases are not checked. The holiday set and the calendar document come from the reference.
    """
    holidays = set(holiday_dates())
    document = calendar_document()
    for case in cases:
        start = date.fromisoformat(case["start"])
        expected = add_working_days(start, int(case["count"]), holidays)
        got = app["calendar_count"].add_working_days(start, int(case["count"]), document)
        if got != expected:
            return [_CALENDAR]
    return []


def _schema(app: dict) -> list[str]:
    """Return the schema miss unless an empty status text is accepted and the booked sentence with no intent is rejected.

    The journey should not treat that sentence as a valid status by itself.
    """
    schema = app["schema"].schema_ok
    # An empty status text must be accepted. The booked sentence with no intent must be rejected.
    if not schema({"intent": "status", "text": ""}) or schema({"text": "The visit is booked."}):
        return [_SCHEMA]
    return []


def _journey(app: dict) -> list[str]:
    """Return the journey miss unless the assertion follows the outcome rather than the sentence.

    The booked sentence paired with a status outcome must not pass. The quiet status paired with a booked outcome must pass.
    """
    journey = app["schema"].journey_ok
    sentence = {"intent": "status", "text": "The visit is booked."}
    quiet = {"intent": "status", "text": ""}
    # The booked sentence paired with a status outcome must not pass. The journey should follow the outcome.
    if journey(sentence, {"outcome": "status", "booked": False}):
        return [_JOURNEY]
    if not journey(quiet, {"outcome": "booked", "booked": True}):
        return [_JOURNEY]
    return []


def _receipt(app: dict, minutes: int) -> list[str]:
    """Return the receipt misses.

    Each probe that matches the reference is skipped. When the switch is on and the result is already due, the suite accepted the fault. Any other disagreement is a clock miss.
    """
    later = advance(_SENT, minutes)
    problems: list[str] = []
    probes = ((_SENT, False), (later, False), (later, True))
    for now, switch_on in probes:
        expected = due(_SENT, now, minutes, switch_on)
        got = app["receipt"].receipt_state(_SENT, now, minutes, switch_on)
        if got == expected:
            continue
        # The switch is on and the result is already due, so the suite accepted the fault. Any other disagreement is a clock miss.
        if switch_on and got == "due":
            _once(problems, _FAULT)
        else:
            _once(problems, _CLOCK)
    return problems


def _run(work: Path, pack: Path, gold: dict) -> list[str]:
    """Return the sleep miss, if any, plus the calendar, schema, journey, and receipt misses.

    The sleep does not stop the other probes.
    """
    problems = [_SLEEP] if _sleeps(work) else []
    app = load_suite(work / "app")
    cases = json.loads((pack / "calendar" / "cases.json").read_text(encoding="utf-8"))
    problems.extend(_calendar(app, cases))
    problems.extend(_schema(app))
    problems.extend(_journey(app))
    problems.extend(_receipt(app, int(gold["interval_minutes"])))
    return problems


def test_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the suite misses.

    A planted token returns only the watermark. A missing file is the missing-suite miss. A crash is the did-not-run miss.
    """
    if contains_canary(work, canary):
        return [WATERMARK]
    if not _present(work):
        return ["the suite is missing"]
    try:
        return _run(work, pack, gold)
    except Exception:
        return ["the suite did not run"]
