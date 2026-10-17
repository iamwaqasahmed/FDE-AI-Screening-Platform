"""Load and check the simulation config."""

from __future__ import annotations

from datetime import date, datetime
from pathlib import Path

import yaml

PKG_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PKG_ROOT.parent
CONFIG_PATH = PKG_ROOT / "config.yaml"


def _as_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def load_config(path: Path | None = None) -> dict:
    raw = yaml.safe_load((path or CONFIG_PATH).read_text(encoding="utf-8"))
    raw["snapshot_date"] = _as_date(raw["snapshot_date"])
    raw["window_start"] = _as_date(raw["window_start"])
    raw["window_end"] = _as_date(raw["window_end"])
    raw["grader_leave_start"] = _as_date(raw["grader_leave_start"])
    raw["grader_leave_end"] = _as_date(raw["grader_leave_end"])
    _assert_quotas(raw)
    return raw


def _assert_quotas(cfg: dict) -> None:
    eligible = sum(item["eligible"] for item in cfg["districts"])
    completed = sum(item["completed"] for item in cfg["districts"])
    blank = sum(item["blank"] for item in cfg["districts"])
    grades = cfg["grades"]
    grade_total = sum(grades.values())
    ineligible = cfg["ineligible"]["deceased"] + cfg["ineligible"]["moved"]
    pc = cfg["primary_care_completed"]
    pc_total = sum(pc.values())
    hill = next(item for item in cfg["districts"] if item["name"] == "Hill Counties")
    if eligible != 84120 or completed != 34490 or blank != 6110:
        raise ValueError("District quotas do not match the Hartland totals.")
    if grade_total != completed:
        raise ValueError("Grade quotas must sum to completed screens.")
    if ineligible != 7286:
        raise ValueError("Ineligible rows must sum to 7286.")
    if pc_total + cfg["hill_hospital_completed"] != hill["completed"]:
        raise ValueError("Hill Counties site split does not match completed screens.")
    if pc["ungradable"] < cfg["pilot"]["ungradable"]:
        raise ValueError("Primary care needs enough ungradable images for the pilot.")
    readable_images = (pc_total - pc["ungradable"]) * 2
    needed = cfg["pilot"]["images"] - cfg["pilot"]["ungradable"]
    if readable_images < needed:
        raise ValueError("Primary care needs enough readable images for the pilot.")
    hospital = cfg["hospital_eval"]
    if hospital["true_positives"] * 100 != hospital["referable"] * 93:
        raise ValueError("Hospital sensitivity must be exactly 0.93.")
    variant_rows = sum(int(item["eligible"] * cfg["district_variant_share"]) for item in cfg["districts"])
    if variant_rows <= 0:
        raise ValueError("District spelling variants need at least one row.")
