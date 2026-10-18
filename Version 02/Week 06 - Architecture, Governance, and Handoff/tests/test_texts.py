"""Pages that disagree, and a banned sentence."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from simulation.eval.handoff.oracle import pack
from simulation.eval.handoff.score_pages import pages_agree, score_document

SMALL = Path(__file__).resolve().parents[2] / "problem_simulation" / "build" / "data-small"
pytestmark = pytest.mark.skipif(not (SMALL / "truth/gold/handoff.json").exists(), reason="small handoff gold is not present")


def _gold() -> dict:
    return json.loads((SMALL / "truth/gold/handoff.json").read_text(encoding="utf-8"))


def test_pages_that_disagree_on_the_date_fail():
    gold = _gold()
    texts = pack(gold)["texts"]
    clinical = texts["clinical"].replace(gold["text"]["pages"]["date"], "1999-01-01")
    assert pages_agree(texts["executive"], clinical, gold["text"]["pages"]) is False


def test_a_banned_sentence_fails_the_page():
    gold = _gold()
    text = pack(gold)["texts"]["executive"] + "The pilot may start.\n"
    assert score_document(text, gold["text"]["executive"])["ok"] is False
