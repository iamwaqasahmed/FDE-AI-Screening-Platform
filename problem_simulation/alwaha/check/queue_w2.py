"""chk-journey for the Ain file. A miss does not print the clinic code.

This check grades the Ain booking path: the live-slot promise, the nightly file, and a failed notice. Each helper stays quiet when its file is absent, and only a file that exists is called. A planted token stops the check. A crash is the run miss. The clinic code is not printed.
"""

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
    """Import one module from a folder and return it.

    A cached module of the same name is set aside so the import reads the participant file. The path is always restored. If nothing was cached, the name is removed. If something was cached, that object is put back.
    """
    folder = folder.resolve()
    saved_path = list(sys.path)
    saved = sys.modules.get(name)
    sys.path.insert(0, str(folder))
    try:
        sys.modules.pop(name, None)
        return importlib.import_module(name)
    finally:
        sys.path[:] = saved_path
        # Nothing was imported under this name before, so the name is removed rather than restored.
        if saved is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = saved


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list.

    Several facility probes can fail the same way, and the list should name the live-slot miss once.
    """
    if item not in problems:
        problems.append(item)


def _queue(folder: Path) -> list[str]:
    """Return the live-slot misses for the booking helper, or nothing when that file is absent.

    Each facility and fault pair must agree with the reference booker. One disagreement is the live-slot miss. A crash is the run miss.
    """
    path = folder / "queue.py"
    # A missing booking module is not graded here. Only a file that exists is called.
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
    """Return the nightly-file misses, or nothing when that file is absent.

    A night with no arriving file must agree with the reference, which is the missed-night case. An arriving file must replace the previous day. A crash is the run miss.
    """
    path = folder / "file_ain.py"
    # A missing nightly-file module is not graded here. Only a file that exists is called.
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
    """Return the notice miss, or nothing when that file is absent.

    A queued booking with a failed send must agree with the reference. A disagreement means a failed notice confirmed a slot. A crash is the run miss.
    """
    path = folder / "notify.py"
    # A missing notice module is not graded here. Only a file that exists is called.
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
    """Return the booking misses from the three helpers.

    A planted token returns only the watermark. The helpers are concatenated, so a missing file in one of them does not hide a miss in another.
    """
    if contains_canary(work, canary):
        return [WATERMARK]
    folder = work / "app"
    return _queue(folder) + _file(folder, gold) + _notice(folder)
