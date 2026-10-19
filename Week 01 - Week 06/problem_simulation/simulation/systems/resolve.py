"""Which identifier a system would have shown on a given day."""

from __future__ import annotations

import pandas as pd

_RANK = {
    "assigned": 0,
    "reuse": 0,
    "split": 1,
    "false_merge": 1,
    "merge": 1,
    "provisional": 2,
    "wrong": 2,
    "typo": 2,
    "merge_reversed": 1,
    "household": 0,
    "missing": 3,
}


def ids_on(identifiers: pd.DataFrame, id_type: str, on: str, site: str = "") -> pd.Series:
    frame = identifiers[identifiers["id_type"] == id_type]
    open_now = (frame["valid_from"] <= on) & ((frame["valid_to"] == "") | (frame["valid_to"] > on))
    frame = frame.loc[open_now]
    if site:
        frame = frame[frame["site"] == site]
    if frame.empty:
        return pd.Series(dtype=object)
    frame = frame.copy()
    frame["_rank"] = frame["relation"].map(_RANK).fillna(9)
    frame = frame.sort_values(["person_uid", "_rank"])
    return frame.groupby("person_uid", as_index=True)["id_value"].first()
