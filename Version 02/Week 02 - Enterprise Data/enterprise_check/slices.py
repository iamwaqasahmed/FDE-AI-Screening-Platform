"""Slice checks. Each one is a planted defect the clusters have to get right."""

from __future__ import annotations

import pandas as pd

from simulation.eval.enterprise.naive import (
    aliases_joined,
    decoys_unlinked,
    false_merges_apart,
    reissues_joined,
    reversed_reassigned,
    splits_joined,
    twins_apart,
)

CHECKS = (
    ("aliases", aliases_joined),
    ("false_merges", false_merges_apart),
    ("splits", splits_joined),
    ("reversed", reversed_reassigned),
    ("twins", twins_apart),
    ("decoys", decoys_unlinked),
    ("reissued", reissues_joined),
)


def evaluate(records: pd.DataFrame, labels: pd.Series) -> dict[str, bool]:
    return {name: function(records, labels) for name, function in CHECKS}
