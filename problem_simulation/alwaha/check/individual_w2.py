"""chk-individual-m02. A miss does not print the fixture status.

This personal check grades the booking contract. The queued fixture must be held and the live-slot fault must not. A planted token stops the check. A missing module, a missing test, or a test that never calls the contract is the missing miss. A crash while loading or while calling is the run miss.
"""

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
    """Import the contract module from a folder and return it.

    A cached module of the same name is set aside so the import reads the participant file. The path is always restored. If nothing was cached, the name is removed. If something was cached, that object is put back.
    """
    folder = folder.resolve()
    saved_path = list(sys.path)
    saved = sys.modules.get("contract")
    sys.path.insert(0, str(folder))
    try:
        sys.modules.pop("contract", None)
        return importlib.import_module("contract")
    finally:
        sys.path[:] = saved_path
        # Nothing was imported under this name before, so the name is removed rather than restored.
        if saved is None:
            sys.modules.pop("contract", None)
        else:
            sys.modules["contract"] = saved


def individual_problems(work: Path, pack: Path, canary: str) -> list[str]:
    """Return the contract misses.

    A planted token wins. Both the module and the test file must exist, and the test source must mention the contract call. The queued status must be held. The live-slot status must not. A crash while reading fixtures is the run miss, and so is a crash inside the calls. Those two crashes are separate so a bad fixture and a bad call are not confused with a wrong answer.
    """
    if contains_canary(work, canary):
        return [WATERMARK]
    module_path = work / "app" / "contract.py"
    test_path = work / "tests" / "test_contract.py"
    if not module_path.is_file() or not test_path.is_file():
        return [_MISSING]
    # A test file that never calls the contract is the same miss as a missing file.
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
        # The queued booking has to be held. Rejecting it is a miss.
        if not module.holds(queued):
            problems.append(_REJECTED)
        # The live-slot fault must not be held. Accepting it is a miss.
        if module.holds(live):
            problems.append(_ACCEPTED)
    except Exception:
        return [_RUN]
    return problems
