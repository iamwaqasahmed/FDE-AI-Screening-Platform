"""Shortcuts that look finished and are wrong."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from graph_check.gold import load
from graph_check.items.cohort import chase_lost_people
from graph_check.items.drop import drop_incident
from graph_check.resend import score as score_resend

SMALL = Path(__file__).resolve().parents[2] / "problem_simulation" / "build" / "data-small"


def test_trusting_the_notice_fails():
    answer = {
        "window": ["2026-10-19", "2026-10-25"],
        "loop_days": ["2026-10-21"],
        "requests": 1,
        "dispatch_rows": 1,
        "unique_dispatched": 1,
        "duplicate_rows": 0,
        "lost": 0,
        "notice_claims_hold": True,
    }
    gold = {"items": {"drop_incident": dict(answer, notice_claims_hold=False, lost=3)}}
    assert drop_incident(answer, gold) is False


def test_counting_every_lost_chase_as_the_cohort_fails():
    gold = {"items": {"chase_lost_people": {"local_ids": 10, "people": 10, "is_upper_bound": True}}}
    assert chase_lost_people({"local_ids": 40, "people": 40, "is_upper_bound": True}, gold) is False


def test_resending_every_lost_request_is_not_enough(tmp_path: Path):
    path = tmp_path / "resend.csv"
    pd.DataFrame([
        {"request_id": "LR-1", "local_pid": "LP1", "action": "resend", "reason": ""},
    ]).to_csv(path, index=False)
    gold = {"resend": [{"request_id": "LR-1", "local_pid": "LP1", "action": "hold", "reason": "seen"}]}
    assert score_resend(path, gold)["ok"] is False


@pytest.mark.skipif(not (SMALL / "truth/gold/graph.json").exists(), reason="build the small profile first")
def test_dispatch_rows_are_not_the_letters_sent():
    gold = load(SMALL)
    row = dict(gold["items"]["drop_incident"])
    row["unique_dispatched"] = row["dispatch_rows"]
    row["duplicate_rows"] = 0
    assert drop_incident(row, gold) is False
