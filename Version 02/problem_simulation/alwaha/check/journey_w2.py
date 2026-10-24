"""chk-w2-journey for webhooks and session.cancelled.

A miss does not name the extra field, the dropped field, the wait figure, or the owner.
"""

from __future__ import annotations

import importlib
import json
import sys
import tempfile
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.notes_w2 import written_problems
from alwaha.check.tables import contains_canary
from alwaha.serve.hooks import keep
from alwaha.serve.mart import read as read_mart
from alwaha.serve.sms import send

_NAMES = ("intake", "cancel", "sms", "registry", "mart", "session")


def load_worker(folder: Path) -> dict:
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
            if module is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = module


def _intake(result: dict, body: dict, gold: dict) -> list[str]:
    kept, _ignored = keep(body, set(gold["referral_fields"]))
    record = result.get("record", {})
    if result.get("mode") != "webhook":
        return ["intake still polls"]
    if gold["extra_field"] in record:
        return ["an unknown field was stored"]
    if result.get("rejected") or gold["extra_field"] not in result.get("ignored", []):
        return ["an unknown field stopped intake"]
    if result.get("referral_id") != kept.get("referral_id"):
        return ["the referral was not recorded"]
    return []


def _cancel(app: dict, events: list[dict], faults: dict, gold: dict) -> tuple[list[str], list[dict]]:
    problems = []
    rows = []
    seen: set[str] = set()
    with tempfile.TemporaryDirectory() as tmp:
        db = app["session"].connect(Path(tmp) / "sessions.db")
        for event in events:
            result = app["cancel"].apply(db, event, faults)
            rows.append(result)
            event_id = str(event["event_id"])
            if event_id in seen:
                if result.get("bookings") != 1 or result.get("sms") != 1:
                    problems.append("replay booked again")
            elif not send(str(event["booking_id"]), faults)["ok"]:
                if result.get("hold") != "released" or result.get("bookings") != 0:
                    problems.append("the hold was left open")
            elif result.get("state") != "notified" or result.get("bookings") != 1 or result.get("sms") != 1:
                problems.append("the cancellation was not notified")
            seen.add(event_id)
        left = app["cancel"].apply(db, gold["left"], faults)
        rows.append(left)
        if left.get("state") != "escalated" or left.get("bookings") != 0 or left.get("sms") != 0:
            problems.append("no-slot cancellation was booked")
        db.close()
    return problems, rows


def _run(work: Path, pack: Path, gold: dict, canary: str) -> list[str] | None:
    app = load_worker(work / "app")
    body = json.loads((pack / "webhooks" / "referral.submitted.json").read_text(encoding="utf-8"))
    registry = (pack / "registry" / "topics.md").read_text(encoding="utf-8")
    events = [
        json.loads(line)
        for line in (pack / "events" / "session.cancelled.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    faults = json.loads((pack / "channels" / "sms-faults.json").read_text(encoding="utf-8"))
    mart_text = (pack / "mart" / "waitlist.csv").read_text(encoding="utf-8")
    accepted = app["intake"].accept(body, registry)
    problems, rows = _cancel(app, events, faults, gold)
    found = app["mart"].read(mart_text)
    expected = read_mart(mart_text)
    if found.get("trusted") or found.get("clock") != expected["clock"]:
        problems.append("wait number was used as truth")
    blob = json.dumps({"intake": accepted, "rows": rows, "mart": found})
    if canary in blob or str(gold["wait"]) in json.dumps(rows):
        if canary in blob:
            return None
        problems.append("wait number was used as truth")
    return problems + _intake(accepted, body, gold)


def journey_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    if not (work / "app" / "intake.py").is_file() or not (work / "app" / "cancel.py").is_file():
        return ["the worker is missing"]
    try:
        problems = _run(work, pack, gold, canary)
    except Exception:
        return ["the worker did not run"]
    if problems is None:
        return [WATERMARK]
    return problems + written_problems(work, gold)
