"""What the incumbent vendor claims, and on which subgroups the claim is actually true."""

from __future__ import annotations

import math

import pandas as pd

from simulation.ml.operating import CUTS, lookup
from simulation.world.staff import VENDORS

CLAIM = {
    "vendor": VENDORS["retinalytics"],
    "metric": "sensitivity",
    "claimed": 0.95,
    "claimed_specificity": 0.90,
    "cut": CUTS[1],
    "label": "R2 or above is referable",
}
MIN_SUBGROUP = 30


def claim_gold(points: pd.DataFrame) -> dict:
    at_cut = points[(points["reference"] == "true_referable") & (points["cut"] == CLAIM["cut"]) & (points["positives"] >= MIN_SUBGROUP)]
    holds = sorted(at_cut.loc[at_cut["sensitivity"] >= CLAIM["claimed"], "subgroup"])
    fails = sorted(at_cut.loc[at_cut["sensitivity"] < CLAIM["claimed"], "subgroup"])
    return dict(
        CLAIM,
        true_sensitivity_all=lookup(points, "all"),
        true_specificity_all=lookup(points, "all", metric="specificity"),
        grader_sensitivity_all=lookup(points, "all", reference="grader_label"),
        favourable_sensitivity=lookup(points, "favourable"),
        holds_on=holds,
        fails_on=fails,
        holds_overall=bool(lookup(points, "all") >= CLAIM["claimed"]),
    )


def material_gap(points: pd.DataFrame, subgroup: str, baseline: str = "all", threshold: float = 0.08) -> bool:
    left, right = lookup(points, subgroup), lookup(points, baseline)
    return not math.isnan(left) and not math.isnan(right) and right - left >= threshold
