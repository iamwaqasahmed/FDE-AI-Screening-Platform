"""Stakeholders: matching rules, script scores, and the full stage against its checks."""

from __future__ import annotations

import pytest

from simulation.devkit import core_world, with_stages
from simulation.stakeholders.interview import score_script
from simulation.stakeholders.matching import match
from simulation.stakeholders.model import node
from simulation.stakeholders.personas import build_personas


@pytest.fixture(scope="module")
def personas():
    return {key: persona.to_json() for key, persona in build_personas(core_world()).items()}


def test_follow_up_needs_its_topic():
    tree = (node("urgent", "urgent", "Flagged."), node("where", "where notes", "In notes.", "f1", "urgent"))
    assert match("where are the notes?", tree, set()) is None
    assert match("where are the notes?", tree, {"urgent"}).node_id == "where"


def test_reference_scripts_separate(personas):
    for key, data in personas.items():
        strong = score_script(key, list(data["strong"]), personas)["score"]
        weak = score_script(key, list(data["weak"]), personas)["score"]
        assert strong >= 0.8 and weak <= 0.4, key


def test_unknown_question_gets_opening_line(personas):
    result = score_script("cdo", ["What colour is the sky?"], personas)
    assert result["turns"][0]["answer"] == personas["cdo"]["card"]["says_first"]
    assert result["score"] == 0.0


def test_stage_passes_checks():
    from simulation.check.stakeholders import CHECKS
    from simulation.eval.stakeholders_cases import cases

    built = with_stages("simulation.corpus.stage", "simulation.stakeholders.stage")
    errors: list[str] = []
    for _, check in CHECKS:
        check(built, errors)
    assert errors == []
    found = cases(built)
    assert len(found) >= 30 and len({case["case_id"] for case in found}) == len(found)
