"""The planted retrieval traps are visible in the small build, without opening truth."""

from __future__ import annotations

from pathlib import Path

import pytest

from reference_evidence.originals import pdf

SMALL = Path(__file__).resolve().parents[2] / "problem_simulation" / "build" / "data-small"


@pytest.mark.skipif(not (SMALL / "corpus").exists(), reason="build the small profile first")
def test_board_table_is_not_in_the_markdown_and_the_forward_exists():
    boards = sorted((SMALL / "corpus/boards").glob("board-*.md"))
    assert boards
    text = boards[0].read_text(encoding="utf-8")
    original = pdf(SMALL / "corpus/boards/originals" / f"{boards[0].stem}.pdf")
    assert "Grader backlog breaches" not in text
    assert "Grader backlog breaches" in original
    forwards = list((SMALL / "corpus").rglob("*-fwd.md"))
    assert forwards
    vendor = (SMALL / "handover/ml/vendor_retrospective.csv").read_text(encoding="utf-8")
    memo = (SMALL / "drops/week-3/dpo_restriction_memo.md").read_text(encoding="utf-8")
    assert "River Outreach" in vendor or "Riverside Outreach" in vendor
    assert "primary-care sites" in memo
    assert "DOB" in memo
