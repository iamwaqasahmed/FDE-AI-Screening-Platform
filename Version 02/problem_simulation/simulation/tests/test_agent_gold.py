"""Agent gold: the traps stay traps, and a second computation matches."""

from __future__ import annotations

from simulation.check.agent import check
from simulation.devkit import with_stages
from simulation.eval.agent import build

STAGES = (
    "simulation.workforce.stage",
    "simulation.corpus.stage",
    "simulation.estate.stage",
    "simulation.economics.stage",
    "simulation.stakeholders.stage",
    "simulation.ml.stage",
    "simulation.delivery.stage",
    "simulation.drops.stage",
)


def test_recompute_matches_and_the_traps_hold():
    world = with_stages(*STAGES)
    payload, backlog, sweep = build(world)
    world["gold"]["agent"] = payload
    errors: list[str] = []
    check(world, errors)
    assert errors == [], errors
    items = payload["items"]
    assert items["critical_path"]["requested_feasible"] is False
    assert items["second_site"]["allowed"] is False
    assert items["service_account"]["read_only"] is True
    assert payload["baselines"]["best"] < 0.5
    assert len(payload["questions"]) >= 40
    assert items["backlog_triage"]["open_pilot_points_with_duplicates"] >= items["backlog_triage"]["open_pilot_points"]
    assert len(backlog) >= 1
    assert len(sweep) == items["sweep_summary"]["rows"]
