"""One row per request: how many dispatch copies came back."""

from __future__ import annotations

import pandas as pd

from simulation.drops.bureau import bureau_run

STATUS = {0: "lost", 1: "once"}


def frame(world: dict) -> pd.DataFrame:
    requests, dispatch = bureau_run(world)
    copies = dispatch.groupby("request_id").size()
    out = requests.copy()
    out["copies"] = out["request_id"].map(copies).fillna(0).astype(int)
    out["status"] = out["copies"].map(STATUS).fillna("twice")
    return out.sort_values("request_id").reset_index(drop=True)


def public_columns() -> list[str]:
    return ["request_id", "local_pid", "template", "requested_at", "copies", "status"]
