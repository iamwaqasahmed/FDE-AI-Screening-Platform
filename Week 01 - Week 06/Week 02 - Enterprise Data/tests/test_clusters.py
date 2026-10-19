"""Toy clusters: a false merge costs more than a missed link, and the slices notice."""

from __future__ import annotations

import pandas as pd

from simulation.eval.enterprise.naive import false_merges_apart, labels_for, scores


def _records() -> pd.DataFrame:
    return pd.DataFrame({
        "kind": ["registry", "registry", "pacs", "pacs"],
        "record_id": ["a", "b", "s1", "s2"],
        "person": ["P1", "P2", "P1", "P1"],
        "link_name": ["ada|north|2000-01-01", "ada|north|2000-01-01", "", ""],
        "false_pair": ["fm-0", "fm-0", "", ""],
        "false_side": ["a", "b", "", ""],
    })


def test_perfect_clusters_score_higher_than_a_false_merge():
    records = _records()
    perfect = pd.Series(["P1", "P2", "P1", "P1"])
    merged = pd.Series(["same", "same", "P1", "P1"])
    good = scores(records, perfect)
    bad = scores(records, merged)
    assert good["f05"] > bad["f05"]
    assert false_merges_apart(records, perfect)
    assert not false_merges_apart(records, merged)


def test_an_empty_link_does_not_collapse_every_row():
    records = _records()
    labels = labels_for(records, "link_name")
    assert labels.nunique() == 3
