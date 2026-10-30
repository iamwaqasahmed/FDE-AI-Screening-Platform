"""chk-m04-l05-ops. A miss does not print an owner id from gold.

This check grades the deployment architecture, the operations plan, and the gate evidence helper. The architecture must name the three zones, the four flows, and a boundary that leaves urgency with a clinician. The plan must name owners, an incident section, the clinical safety cell, and the gate. The helper must return that same cell and gate. Gold is unused because the evidence row comes from the pack. An owner id is not printed.
"""

from __future__ import annotations

import json
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.rubric import section
from alwaha.check.tables import contains_canary

ARCH = "the deployment architecture misses a required section"
CELL = "the operations plan leaves the clinical safety cell empty"
GATE = "the operations plan skips G4"
OWNER = "the operations plan misses an owner"
RUN = "the harness did not run"
_MODULES = ("gates",)
_ZONES = ("zone-private", "zone-hospital", "zone-public")


def _text(path: Path) -> str:
    """Return the file text, or an empty string when the path is not a file.

    A missing note becomes empty sections, so the content misses still fire.
    """
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _architecture(work: Path) -> list[str]:
    """Return the architecture miss unless zones, flows, and the boundary are all filled.

    Every zone name must appear. The flows must name the contact center, business intelligence, human resources, and the bus. The boundary must mention a clinician and urgency.
    """
    text = _text(work / "architecture-deploy.md")
    # Zones, flows, and the boundary are read as separate sections.
    zones = section(text, "Zones").lower()
    flows = section(text, "Flows").lower()
    boundary = section(text, "Boundary").lower()
    # Every zone name must appear. The flows must name each connected system.
    # The boundary must mention a clinician and urgency.
    filled = (
        all(name in zones for name in _ZONES)
        and all(name in flows for name in ("cc", "bi", "hr", "bus"))
        and "clinician" in boundary
        and "urgency" in boundary
    )
    if not filled:
        return [ARCH]
    return []


def _operations(work: Path) -> list[str]:
    """Return the plan misses.

    Owners and the incident section must both be non-empty. The responsibility section must name the clinical safety cell. The gate section must name the gate and the checklist. These can all appear.
    """
    text = _text(work / "operations.md")
    problems = []
    if not section(text, "Owners").strip() or not section(text, "Incident").strip():
        problems.append(OWNER)
    if "med-dir" not in section(text, "RACI").lower():
        problems.append(CELL)
    gate = section(text, "Gate").lower()
    if "g4" not in gate or "checklist" not in gate:
        problems.append(GATE)
    return problems


def _evidence(module, item: dict) -> list[str]:
    """Return the evidence misses.

    A crash is the harness miss. A result that is not a record fails both the cell and the gate. The cell must be the clinical director. The gate must be the gate token in the condition.
    """
    try:
        got = module.evidence(item)
    except Exception:
        return [RUN]
    # A result that is not a record fails both the safety cell and the gate.
    if not isinstance(got, dict):
        return [CELL, GATE]
    problems = []
    if str(got.get("cell") or "") != "med-dir":
        problems.append(CELL)
    if str(got.get("gate") or "") != "G4":
        problems.append(GATE)
    return problems


def ops_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the operations misses.

    Gold is discarded because the evidence row comes from the pack. A planted token returns only the watermark. The notes are graded first. Evidence misses are added only when that sentence is not already present. A crash of the import adds the harness miss the same way.
    """
    # Gold is unused. The evidence row comes from the pack. The caller still loads the release so a missing pack fails first.
    del gold
    if contains_canary(work, canary):
        return [WATERMARK]
    item = json.loads((pack / "raci" / "assistant.json").read_text(encoding="utf-8"))
    problems = _architecture(work) + _operations(work)
    try:
        with modules(work / "app", _MODULES) as loaded:
            for name in _evidence(loaded["gates"], item):
                if name not in problems:
                    problems.append(name)
    except Exception:
        # The harness miss is added once. A note miss with the same sentence is not duplicated.
        if RUN not in problems:
            problems.append(RUN)
    return problems
