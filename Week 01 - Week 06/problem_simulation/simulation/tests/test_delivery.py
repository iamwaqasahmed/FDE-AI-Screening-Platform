"""Delivery and drops stages on the cached core world: checks pass, plants hold, and a rerun matches."""

from __future__ import annotations

import copy

import numpy as np
import pytest

from simulation.check.delivery import CHECKS
from simulation.delivery import stage as delivery_stage
from simulation.delivery.accessibility import contrast
from simulation.delivery.plan import pilot_path, release_windows
from simulation.devkit import with_stages
from simulation.eval.delivery_cases import cases
from simulation.world.engagement import PILOT_DATE_REQUESTED


@pytest.fixture(scope="module")
def world() -> dict:
    return with_stages("simulation.corpus.stage", "simulation.delivery.stage", "simulation.drops.stage")


def test_checks_pass(world):
    errors: list[str] = []
    for _, check in CHECKS:
        check(world, errors)
    assert errors == []


def test_pilot_date_needs_procurement_and_freeze():
    from datetime import date

    path = pilot_path(date.min)
    assert path["earliest_pilot"] > PILOT_DATE_REQUESTED.isoformat()
    assert path["registry_window"] > path["registry_freeze_end"]
    assert all(not ("2026-10-19" <= day.isoformat() <= "2027-01-29") for day in release_windows("registry"))


def test_contrast_matches_wcag_examples():
    assert contrast("#000000", "#FFFFFF") == 21.0
    assert contrast("#777777", "#FFFFFF") < 4.5


def test_tracker_and_velocity_agree(world):
    tickets = world["files"]["handover/delivery/tracker.csv"]
    velocity = world["files"]["handover/delivery/velocity.csv"]
    done = tickets[(tickets["status"] == "Done") & (tickets["type"] != "epic")]
    in_sprints = sum(
        int(done[(done["team"] == row.team) & (done["resolved"] >= row.start) & (done["resolved"] <= row.end)]["story_points"].sum())
        for row in velocity.itertuples(index=False)
    )
    assert in_sprints == int(velocity["completed_points"].sum())


def test_cases_have_unique_ids_and_cover_outcomes(world):
    found = cases(world)
    assert len(found) >= 50
    assert len({case["case_id"] for case in found}) == len(found)
    assert {case["tags"]["outcome"] for case in found} == {"delivery", "fde", "consulting"}
    press = next(case for case in found if case["case_id"] == "delivery-press-answer")
    assert press["expected"]["must_not_claim"] and press["expected"]["must_mention"]


def test_rerun_matches():
    base = with_stages("simulation.corpus.stage")
    first, second = copy.deepcopy(base), copy.deepcopy(base)
    delivery_stage.build(first, np.random.default_rng(7))
    delivery_stage.build(second, np.random.default_rng(7))
    assert first["gold"]["backlog"] == second["gold"]["backlog"]
    assert first["files"]["handover/delivery/tracker.csv"].equals(second["files"]["handover/delivery/tracker.csv"])
