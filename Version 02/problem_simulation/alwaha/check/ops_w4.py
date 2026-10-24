"""chk-w4-ops. A miss does not print an owner id from gold."""

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
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _architecture(work: Path) -> list[str]:
    text = _text(work / "architecture-deploy.md")
    zones = section(text, "Zones").lower()
    flows = section(text, "Flows").lower()
    boundary = section(text, "Boundary").lower()
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
    try:
        got = module.evidence(item)
    except Exception:
        return [RUN]
    if not isinstance(got, dict):
        return [CELL, GATE]
    problems = []
    if str(got.get("cell") or "") != "med-dir":
        problems.append(CELL)
    if str(got.get("gate") or "") != "G4":
        problems.append(GATE)
    return problems


def ops_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
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
        if RUN not in problems:
            problems.append(RUN)
    return problems
