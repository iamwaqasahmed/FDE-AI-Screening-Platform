"""chk-individual-w2. A miss does not print the fixture status."""

from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.tables import contains_canary

_MISSING = "the contract test is missing"
_ACCEPTED = "the contract test accepted the live-slot fault"
_REJECTED = "the contract test rejected the queued booking"
_RUN = "the contract test did not run"


def _load(folder: Path):
    folder = folder.resolve()
    saved_path = list(sys.path)
    saved = sys.modules.get("contract")
    sys.path.insert(0, str(folder))
    try:
        sys.modules.pop("contract", None)
        return importlib.import_module("contract")
    finally:
        sys.path[:] = saved_path
        if saved is None:
            sys.modules.pop("contract", None)
        else:
            sys.modules["contract"] = saved


def individual_problems(work: Path, pack: Path, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    module_path = work / "app" / "contract.py"
    test_path = work / "tests" / "test_contract.py"
    if not module_path.is_file() or not test_path.is_file():
        return [_MISSING]
    if "holds" not in test_path.read_text(encoding="utf-8"):
        return [_MISSING]
    try:
        module = _load(work / "app")
        queued = json.loads((pack / "fixtures" / "queued.json").read_text(encoding="utf-8"))["status"]
        live = json.loads((pack / "fixtures" / "live-slot.json").read_text(encoding="utf-8"))["status"]
    except Exception:
        return [_RUN]
    problems = []
    try:
        if not module.holds(queued):
            problems.append(_REJECTED)
        if module.holds(live):
            problems.append(_ACCEPTED)
    except Exception:
        return [_RUN]
    return problems
