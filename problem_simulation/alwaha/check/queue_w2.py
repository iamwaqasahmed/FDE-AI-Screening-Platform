"""chk-w2-journey for the Ain file. A miss does not print the clinic code."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.tables import contains_canary
from alwaha.serve.ain import apply_file, book, notify

_LIVE = "a live slot was promised"
_MISSED = "a missed night cleared the slots"
_REPLACED = "the nightly file did not replace yesterday"
_NOTICE = "a failed notice confirmed a slot"
_RUN = "the booking did not run"


def _load(folder: Path, name: str):
    folder = folder.resolve()
    saved_path = list(sys.path)
    saved = sys.modules.get(name)
    sys.path.insert(0, str(folder))
    try:
        sys.modules.pop(name, None)
        return importlib.import_module(name)
    finally:
        sys.path[:] = saved_path
        if saved is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = saved


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)


def _queue(folder: Path) -> list[str]:
    path = folder / "queue.py"
    if not path.is_file():
        return []
    try:
        module = _load(folder, "queue")
        probes = (("h-ain", ""), ("h-ain", "live-slot"), ("h-wadi", ""))
        problems = []
        for facility, fault in probes:
            if module.book(facility, fault) != book(facility, fault):
                _once(problems, _LIVE)
        return problems
    except Exception:
        return [_RUN]


def _file(folder: Path, gold: dict) -> list[str]:
    path = folder / "file_ain.py"
    if not path.is_file():
        return []
    previous = {"clinic_code": gold["previous_code"], "day": "yesterday"}
    arrived = {"clinic_code": gold["clinic_code"], "day": "today"}
    try:
        module = _load(folder, "file_ain")
        problems = []
        if module.apply_file(previous, None) != apply_file(previous, None):
            problems.append(_MISSED)
        if module.apply_file(previous, arrived) != apply_file(previous, arrived):
            problems.append(_REPLACED)
        return problems
    except Exception:
        return [_RUN]


def _notice(folder: Path) -> list[str]:
    path = folder / "notify.py"
    if not path.is_file():
        return []
    try:
        module = _load(folder, "notify")
        if module.notify("queued", False) != notify("queued", False):
            return [_NOTICE]
        return []
    except Exception:
        return [_RUN]


def queue_problems(work: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    folder = work / "app"
    return _queue(folder) + _file(folder, gold) + _notice(folder)
