"""Discovery gold: the traps stay traps, and a second computation matches."""

from __future__ import annotations

from simulation.check.discovery import check
from simulation.devkit import core_world
from simulation.eval.discovery_gold import build


def test_traps_hold_on_the_core_world():
    world = core_world()
    gold = build(world)
    assert gold["ranking"]["highest"] == "identity_resolution"
    assert gold["ranking"]["lowest"] == "vendor_model_expansion"
    eligible = gold["eligible"]
    assert eligible["registry_rows"] > eligible["warehouse"] > eligible["count"] > 0
    assert gold["profiling"]["duplicate_month"]
    assert gold["profiling"]["firmware"]
    assert gold["backlog"]["true"] < gold["backlog"]["board"] < gold["backlog"]["lead"]


def test_recompute_matches_and_needs_the_call_file():
    world = core_world()
    world["gold"]["discovery"] = build(world)
    errors: list[str] = []
    check(world, errors)
    assert errors == ["Letter-call peak month is missing; the research stage did not run"]
