"""Naive readings fail: the warehouse count, a twelve-month window, and a name-and-date merge."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from enterprise_check.clusters import score as score_clusters
from enterprise_check.gold import load, records
from enterprise_check.items.counts import coverage, eligible_people
from simulation.eval.enterprise.naive import labels_for

SMALL = Path(__file__).resolve().parents[2] / "problem_simulation" / "build" / "data-small"


@pytest.mark.skipif(not (SMALL / "truth/gold/enterprise.json").exists(), reason="build the small profile first")
def test_warehouse_count_and_name_clusters_fail():
    gold = load(SMALL)
    frame = records(SMALL)
    assert not eligible_people({"count": gold["counts"]["warehouse_eligible"]}, gold)
    assert not eligible_people({"count": gold["counts"]["rows"]}, gold)
    assert not coverage({"people": gold["counts"]["warehouse_covered"], "days": 365, "warehouse_months": 12}, gold)
    labels = labels_for(frame, "link_name")
    submitted = pd.DataFrame({"kind": frame["kind"], "record_id": frame["record_id"], "cluster_id": labels})
    assert score_clusters(submitted, frame)["ok"] is False
