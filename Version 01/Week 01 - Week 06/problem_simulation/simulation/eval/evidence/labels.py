"""How often each grader's referable call disagrees with the lead grader's, on the restricted sample."""

from __future__ import annotations

import pandas as pd

from simulation.eval.evidence.bars import MIN_GRADER_ROWS
from simulation.eval.evidence.rates import GRADED, REFER


def noise(frame: pd.DataFrame, joined: pd.DataFrame) -> dict:
    graded = joined[joined["routine_label"].isin(GRADED) & joined["adjudicated_label"].isin(GRADED)]
    rows = [_row(initials, group) for initials, group in graded.groupby("routine_grader", sort=True)]
    ranked = [row for row in rows if row["n"] >= MIN_GRADER_ROWS] or rows
    missing = float(frame["grader_label"].eq("").mean()) if len(frame) else 0.0
    return {
        "routine_missing_share": round(missing, 4),
        "most_over_call": _top(ranked, "over_call"),
        "most_miss": _top(ranked, "miss"),
        "graders": rows,
    }


def _row(initials: str, group: pd.DataFrame) -> dict:
    routine, lead = group["routine_label"].isin(REFER), group["adjudicated_label"].isin(REFER)
    return {
        "grader": str(initials),
        "n": int(len(group)),
        "disagree": round(float((routine != lead).mean()), 3),
        "over_call": round(float((routine & ~lead).mean()), 3),
        "miss": round(float((~routine & lead).mean()), 3),
    }


def _top(rows: list[dict], key: str) -> str:
    if not rows:
        return ""
    return sorted(rows, key=lambda row: (-row[key], row["grader"]))[0]["grader"]
