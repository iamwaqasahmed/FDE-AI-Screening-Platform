"""Shortcuts that look finished and are not."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from handoff_check.items.conditions import conditions, register_state
from handoff_check.items.security import threat_summary
from simulation.eval.handoff.bars import FLOW_COLUMNS
from simulation.eval.handoff.oracle import pack
from simulation.eval.handoff.score_files import score_flows, score_hazards
from simulation.eval.handoff.score_pages import score_document
from simulation.eval.handoff.score_records import score_contract, score_dockerfile, score_model_card, score_transparency

SMALL = Path(__file__).resolve().parents[2] / "problem_simulation" / "build" / "data-small"
pytestmark = pytest.mark.skipif(not (SMALL / "truth/gold/handoff.json").exists(), reason="small handoff gold is not present")


def _gold() -> dict:
    import json

    return json.loads((SMALL / "truth/gold/handoff.json").read_text(encoding="utf-8"))


def _copy(gold: dict, item: str) -> dict:
    import copy

    return copy.deepcopy(gold["items"][item])


def test_marking_cso2_met_fails():
    gold = _gold()
    answer = _copy(gold, "conditions")
    answer["CSO-2"]["met"] = True
    assert conditions(answer, gold) is False


def test_closing_r02_fails():
    gold = _gold()
    answer = _copy(gold, "register_state")
    answer["keep_open"] = [item for item in answer["keep_open"] if item != "R-02"]
    assert register_state(answer, gold) is False


def test_calling_t3_live_fails():
    gold = _gold()
    answer = _copy(gold, "threat_summary")
    answer["live"] = ["T1", "T2", "T3", "T4"]
    assert threat_summary(answer, gold) is False


def test_a_hospital_study_marked_yes_fails():
    gold = _gold()
    frame = pack(gold)["flows"]
    frame.loc[frame["data"].eq("hospital_study"), "allowed"] = "yes"
    assert score_flows(frame, gold)["ok"] is False


def test_river_outreach_in_the_record_fails():
    gold = _gold()
    text = pack(gold)["transparency"] + "sites_note: River Outreach\n"
    assert score_transparency(text, gold)["ok"] is False


def test_quoting_the_claim_as_the_operating_point_fails():
    gold = _gold()
    text = pack(gold)["model_card"] + "The model meets the claimed sensitivity of 0.95.\n"
    assert score_model_card(text, gold)["ok"] is False


def test_an_accepted_decision_fails():
    gold = _gold()
    text = pack(gold)["texts"]["adr-01"].replace("Status: Proposed.", "Status: Accepted.")
    assert score_document(text, gold["text"]["adr-01"])["ok"] is False


def test_the_discovery_token_fails_the_contract():
    gold = _gold()
    text = pack(gold)["contract"].replace("account: screening-agent", "account: discovery-team")
    assert score_contract(text, gold)["ok"] is False


def test_a_dockerfile_that_copies_the_handover_fails():
    gold = _gold()
    assert score_dockerfile("COPY data/handover /data\n", gold)["ok"] is False


def test_flow_columns_stay_available():
    assert "allowed" in FLOW_COLUMNS
    assert isinstance(pack(_gold())["flows"], pd.DataFrame)
