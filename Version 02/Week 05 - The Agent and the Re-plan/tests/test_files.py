"""Backlog and sweep files, and the public line."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from agent_check.files import score_backlog
from agent_check.texts import score_file
from simulation.eval.agent.bars import BACKLOG_COLUMNS


def test_a_reordered_backlog_still_matches(tmp_path):
    frame = pd.DataFrame([{"ticket_id": "DLV-2", "duplicate_of": "", "missing_criteria": "false", "blocked_by": ""},
                          {"ticket_id": "DLV-1", "duplicate_of": "DLV-9", "missing_criteria": "true", "blocked_by": "FRZ-0301"}])
    path = tmp_path / "backlog.csv"
    frame.to_csv(path, index=False)
    gold = frame.iloc[::-1].reset_index(drop=True)
    assert score_backlog(path, gold)["ok"]


def test_an_extra_column_fails(tmp_path):
    frame = pd.DataFrame([{column: "" for column in BACKLOG_COLUMNS} | {"ticket_id": "DLV-1", "note": "x"}])
    path = tmp_path / "backlog.csv"
    frame.to_csv(path, index=False)
    assert score_backlog(path, frame[list(BACKLOG_COLUMNS)])["ok"] is False


def test_a_line_that_names_the_date_fails(tmp_path):
    path = tmp_path / "press-line.md"
    path.write_text("Graders decide.\n\nThe pilot starts on 2027-02-01.\n", encoding="utf-8")
    gold = {"text": {"line": {"facts": [{"id": "graders", "tokens": ["grader"]}], "forbidden": [],
                              "forbidden_terms": ["2027-02-01"]}}}
    assert score_file(path, gold, "line")["ok"] is False


def test_a_date_does_not_count_as_the_lost_letters(tmp_path):
    path = tmp_path / "press-line.md"
    path.write_text("Graders decide. The bureau problem ran from 2026-10-19 to 2026-10-25.\n\nContact the screening programme.\n", encoding="utf-8")
    gold = {"text": {"line": {"facts": [{"id": "graders", "tokens": ["grader"]}, {"id": "contact", "tokens": ["screening programme"]}],
                              "forbidden": [], "forbidden_terms": ["10", "19", "25"]}}}
    assert score_file(path, gold, "line")["ok"]


def test_two_paragraphs_pass(tmp_path):
    path = tmp_path / "press-line.md"
    path.write_text("Trained graders decide every result.\n\nContact the screening programme.\n", encoding="utf-8")
    gold = {"text": {"line": {"facts": [{"id": "graders", "tokens": ["grader"]}, {"id": "contact", "tokens": ["screening programme"]}],
                              "forbidden": ["The AI system is approved."], "forbidden_terms": []}}}
    assert score_file(path, gold, "line")["ok"]
