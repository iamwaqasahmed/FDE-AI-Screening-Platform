"""Letter-not-received calls around the two bureau windows. The estimate is the true count."""

from __future__ import annotations

from datetime import date, timedelta

import pandas as pd

from simulation.eval.graph.bars import BASELINE_DAYS, CALL_TAIL_DAYS
from simulation.world.clock import BUREAU_MIGRATION_END, BUREAU_MIGRATION_START, INCIDENT_END, INCIDENT_START, iso


def facts(world: dict) -> dict:
    calls = world["files"]["truth/estate/call_reasons.parquet"]
    windows = [
        ("CHG-0158", BUREAU_MIGRATION_START, BUREAU_MIGRATION_END),
        ("INC-0233", INCIDENT_START, INCIDENT_END + timedelta(days=CALL_TAIL_DAYS)),
    ]
    rows = [_window(calls, ref, start, end) for ref, start, end in windows]
    true = sum(row["estimate"] for row in rows)
    coded = sum(row["coded"] for row in rows)
    return {"call_signal": {"windows": rows, "coded_share": round(coded / true, 4) if true else 0.0}}


def _window(calls: pd.DataFrame, ref: str, start: date, end: date) -> dict:
    inside = _between(calls, start, end)
    before = _between(calls, start - timedelta(days=BASELINE_DAYS), start - timedelta(days=1))
    true = int((inside["true_reason"] == "LNR").sum())
    coded = int((inside["reason_code"] == "LNR").sum())
    baseline_true = int((before["true_reason"] == "LNR").sum())
    return {
        "ref": ref,
        "start": iso(start),
        "end": iso(end),
        "coded": coded,
        "estimate": true,
        "baseline_per_day": round(baseline_true / BASELINE_DAYS, 4),
    }


def _between(calls: pd.DataFrame, start: date, end: date) -> pd.DataFrame:
    return calls[calls["call_date"].between(iso(start), iso(end))]
