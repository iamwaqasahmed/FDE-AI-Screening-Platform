"""The bureau window, counted from the request and dispatch files."""

from __future__ import annotations

import pandas as pd

from simulation.drops.bureau import bureau_gold


def facts(world: dict, reconciled: pd.DataFrame) -> dict:
    requests = reconciled.drop(columns=["copies", "status"])
    dispatch = _dispatch(reconciled)
    gold = bureau_gold(world, requests, dispatch)
    return {
        "drop_incident": {
            "window": list(gold["window"]),
            "loop_days": list(gold["retry_loop_days"]),
            "requests": gold["requests"],
            "dispatch_rows": gold["dispatch_rows"],
            "unique_dispatched": gold["unique_dispatched"],
            "duplicate_rows": gold["duplicate_rows"],
            "lost": gold["lost_count"],
            "notice_claims_hold": False,
        },
        "outputs_changed": _outputs(world),
        "dedupe_keys": {
            "transport_key": "dispatch_id",
            "business_key": "request_id",
            "transport_rows_removed": 0,
            "business_rows_removed": gold["duplicate_rows"],
        },
    }


def _outputs(world: dict) -> dict:
    frame = world["files"]["engagement/workstreams/contracts.csv"]
    changed = sorted(frame.loc[frame["changed_by_drop"].astype(str).eq("week-4"), "contract_id"].astype(str))
    return {"contracts": changed, "week2_rule": "feed_dedupe", "unchanged": ["overdue", "overdue_pilot_scope"]}


def _dispatch(reconciled: pd.DataFrame) -> pd.DataFrame:
    """One synthetic row per copy, so bureau_gold can count rows against request ids."""
    rows = []
    for request in reconciled.itertuples(index=False):
        rows.extend({"request_id": request.request_id} for _ in range(int(request.copies)))
    return pd.DataFrame(rows, columns=["request_id"])
