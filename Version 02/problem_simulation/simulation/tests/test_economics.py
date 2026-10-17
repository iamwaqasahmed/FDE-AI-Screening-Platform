"""Economics: the reminder trap, the flashy opportunity, the dependency graph, and the stage's checks."""

from __future__ import annotations

import pytest

from simulation.devkit import core_world, with_stages
from simulation.economics.dependencies import unlocks
from simulation.economics.reminder import naive_before_after, true_uplift
from simulation.economics.summary import economic_summary


@pytest.fixture(scope="module")
def world():
    return core_world()


def test_naive_overstates_in_two_districts(world):
    true, naive = true_uplift(world["invitations"]), naive_before_after(world["invitations"])
    assert sum(naive[d] > true[d] for d in true) >= 2


def test_flashy_claims_most_and_nets_least(world):
    rows = economic_summary(world)["opportunities"]
    assert max(rows, key=lambda r: r["claimed_annual_gbp"])["key"] == "vendor_model_expansion"
    assert min(rows, key=lambda r: r["net_annual_gbp"])["key"] == "vendor_model_expansion"


def test_identity_unlocks_most():
    assert {"dna_prediction", "reminder_targeting", "vendor_model_expansion"} <= set(unlocks("identity_resolution"))


def test_stage_passes_checks():
    from simulation.check.economics import CHECKS
    from simulation.eval.economics_cases import cases

    built = with_stages("simulation.economics.stage")
    errors: list[str] = []
    for _, check in CHECKS:
        check(built, errors)
    assert errors == []
    found = cases(built)
    assert len(found) >= 25 and len({case["case_id"] for case in found}) == len(found)
