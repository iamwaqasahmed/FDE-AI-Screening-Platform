"""Naive clusterings, used to prove the bars still reject the shortcuts."""

from __future__ import annotations

import pandas as pd


def f_beta(records: pd.DataFrame, labels: pd.Series, beta: float = 0.5) -> float:
    return scores(records, labels, beta)["f05"]


def scores(records: pd.DataFrame, labels: pd.Series, beta: float = 0.5) -> dict:
    """Pairwise precision, recall, and F-beta. Gold pairs share a person. Predicted pairs share a label."""
    frame = pd.DataFrame({"person": records["person"].to_numpy(), "label": pd.Series(labels).to_numpy()})
    frame = frame[frame["person"].ne("")]
    if frame.empty:
        return {"precision": 0.0, "recall": 0.0, "f05": 0.0}
    true_pairs = _pairs(frame.groupby("person").size())
    predicted = _pairs(frame.groupby("label").size())
    hits = _pairs(frame.groupby(["person", "label"]).size())
    if predicted == 0 or true_pairs == 0:
        return {"precision": 0.0, "recall": 0.0, "f05": 0.0}
    precision, recall = hits / predicted, hits / true_pairs
    weight = beta * beta
    value = (1 + weight) * precision * recall / (weight * precision + recall)
    return {"precision": precision, "recall": recall, "f05": value}


def labels_for(records: pd.DataFrame, column: str) -> pd.Series:
    raw = records[column].astype(str)
    solo = "solo-" + records.index.astype(str)
    return raw.where(raw.ne(""), solo)


def false_merges_apart(records: pd.DataFrame, labels: pd.Series) -> bool:
    return _sides_apart(records, labels, "false_pair", "false_side")


def twins_apart(records: pd.DataFrame, labels: pd.Series) -> bool:
    return _sides_apart(records, labels, "twin_pair", "twin_side")


def splits_joined(records: pd.DataFrame, labels: pd.Series) -> bool:
    return _one_label(records, labels, "split_pair")


def reissues_joined(records: pd.DataFrame, labels: pd.Series) -> bool:
    return _one_label(records, labels, "reissue_pair")


def aliases_joined(records: pd.DataFrame, labels: pd.Series) -> bool:
    return _one_label(records, labels, "alias_pair")


def reversed_reassigned(records: pd.DataFrame, labels: pd.Series) -> bool:
    studies = _roles(records, labels, "study")
    people = _roles(records, labels, "person")
    owners = _roles(records, labels, "owner")
    if studies.empty:
        return False
    same = studies.eq(people.reindex(studies.index))
    different = ~studies.eq(owners.reindex(studies.index))
    return bool(same.all() and different.all())


def decoys_unlinked(records: pd.DataFrame, labels: pd.Series) -> bool:
    decoy = records["decoy"].eq("1")
    if not decoy.any():
        return False
    used = set(labels[~decoy])
    return not any(label in used for label in labels[decoy])


def _sides_apart(records: pd.DataFrame, labels: pd.Series, pair: str, side: str) -> bool:
    frame = records[records[pair].ne("")]
    if frame.empty:
        return False
    grouped = frame.assign(_label=labels.loc[frame.index]).groupby(pair)
    for _, rows in grouped:
        left = set(rows.loc[rows[side].eq("a"), "_label"])
        right = set(rows.loc[rows[side].eq("b"), "_label"])
        if not left or not right or left & right:
            return False
    return True


def _one_label(records: pd.DataFrame, labels: pd.Series, pair: str) -> bool:
    frame = records[records[pair].ne("")]
    if frame.empty:
        return False
    counts = frame.assign(_label=labels.loc[frame.index]).groupby(pair)["_label"].nunique()
    return bool(counts.eq(1).all())


def _roles(records: pd.DataFrame, labels: pd.Series, role: str) -> pd.Series:
    rows = records[records["rev_role"].eq(role)]
    return labels.loc[rows.index].groupby(rows["rev_pair"]).first()


def _pairs(sizes: pd.Series) -> float:
    return float((sizes * (sizes - 1) / 2).sum())
