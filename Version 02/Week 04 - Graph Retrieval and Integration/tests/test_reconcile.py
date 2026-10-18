"""A reconciliation that dedupes on the wrong id, and a re-send that adds a name."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from graph_check.reconciliation import score as score_reconciliation
from graph_check.resend import score as score_resend


def test_wrong_copies_fail(tmp_path: Path):
    gold = pd.DataFrame([
        {"request_id": "LR-1", "local_pid": "LP1", "template": "referral-chase",
         "requested_at": "2026-10-21", "copies": 2, "status": "twice"},
    ])
    path = tmp_path / "reconciliation.csv"
    gold.assign(copies=1, status="once").to_csv(path, index=False)
    assert score_reconciliation(path, gold)["ok"] is False


def test_a_matching_reconciliation_passes(tmp_path: Path):
    gold = pd.DataFrame([
        {"request_id": "LR-1", "local_pid": "LP1", "template": "invitation",
         "requested_at": "2026-10-21", "copies": 0, "status": "lost"},
    ])
    path = tmp_path / "reconciliation.csv"
    gold.to_csv(path, index=False)
    assert score_reconciliation(path, gold)["ok"] is True


def test_a_name_column_fails_the_resend(tmp_path: Path):
    path = tmp_path / "resend.csv"
    path.write_text("request_id,local_pid,action,reason,surname\nLR-1,LP1,resend,,Nguyen\n", encoding="utf-8")
    gold = {"resend": [{"request_id": "LR-1", "local_pid": "LP1", "action": "resend", "reason": ""}]}
    assert score_resend(path, gold)["ok"] is False


def test_the_hold_reason_has_to_match(tmp_path: Path):
    path = tmp_path / "resend.csv"
    path.write_text("request_id,local_pid,action,reason\nLR-1,LP1,resend,\n", encoding="utf-8")
    gold = {"resend": [{"request_id": "LR-1", "local_pid": "LP1", "action": "hold", "reason": "deceased"}]}
    assert score_resend(path, gold)["ok"] is False
