"""Pairwise precision, recall, and F0.5 for a cluster file. A false merge costs more than a missed link."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from enterprise_check.slices import evaluate
from simulation.eval.enterprise.bars import F05_MIN, PRECISION_MIN, RECALL_MIN
from simulation.eval.enterprise.naive import scores


def load(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame(columns=["kind", "record_id", "cluster_id"])
    frame = pd.read_csv(path, dtype=str).fillna("")
    return frame


def score(submitted: pd.DataFrame, records: pd.DataFrame) -> dict:
    labels = _labels(submitted, records)
    row = scores(records, labels)
    slices = evaluate(records, labels)
    row["slices"] = slices
    row["ok"] = (
        row["f05"] >= F05_MIN
        and row["precision"] >= PRECISION_MIN
        and row["recall"] >= RECALL_MIN
        and all(slices.values())
    )
    return row


def _labels(submitted: pd.DataFrame, records: pd.DataFrame) -> pd.Series:
    if submitted.empty:
        return pd.Series([f"missing-{index}" for index in range(len(records))])
    keys = submitted["kind"].astype(str) + "|" + submitted["record_id"].astype(str)
    mapping = dict(zip(keys, submitted["cluster_id"].astype(str)))
    gold_keys = records["kind"].astype(str) + "|" + records["record_id"].astype(str)
    return pd.Series([mapping.get(key, f"missing-{index}") for index, key in enumerate(gold_keys)], index=records.index)
