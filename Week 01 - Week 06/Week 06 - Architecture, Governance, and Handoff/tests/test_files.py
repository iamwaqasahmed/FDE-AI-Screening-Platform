"""CSV files: order does not matter, an extra column does, a signature does."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import pytest

from simulation.eval.handoff.bars import FLOW_COLUMNS, HAZARD_COLUMNS
from simulation.eval.handoff.oracle import pack
from simulation.eval.handoff.score_files import score_flows, score_hazards

SMALL = Path(__file__).resolve().parents[2] / "problem_simulation" / "build" / "data-small"
pytestmark = pytest.mark.skipif(not (SMALL / "truth/gold/handoff.json").exists(), reason="small handoff gold is not present")


def _gold() -> dict:
    return json.loads((SMALL / "truth/gold/handoff.json").read_text(encoding="utf-8"))


def test_a_reordered_flow_file_passes():
    gold = _gold()
    frame = pack(gold)["flows"].iloc[::-1].reset_index(drop=True)
    assert score_flows(frame, gold)["ok"]


def test_an_extra_benign_row_passes():
    gold = _gold()
    frame = pack(gold)["flows"]
    extra = pd.DataFrame([{column: "" for column in FLOW_COLUMNS} |
                          {"flow_id": "F-99", "source": "finance", "target": "audit", "data": "record_reference",
                           "allowed": "no", "rule": "security-logging-standard"}])
    assert score_flows(pd.concat([frame, extra], ignore_index=True), gold)["ok"]


def test_an_extra_column_fails():
    gold = _gold()
    frame = pack(gold)["flows"]
    frame["note"] = ""
    assert score_flows(frame, gold)["ok"] is False


def test_a_signed_hazard_row_fails():
    gold = _gold()
    frame = pack(gold)["hazards"]
    frame.loc[0, "signed_by"] = "signed"
    assert score_hazards(frame, gold)["ok"] is False
    assert list(HAZARD_COLUMNS)[-1] == "signed_by"
