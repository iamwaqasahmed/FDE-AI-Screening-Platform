"""Every request's copies and status."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

COLUMNS = ["request_id", "local_pid", "template", "requested_at", "copies", "status"]


def score(path: Path, gold: pd.DataFrame) -> dict:
    if not path.exists():
        return {"ok": False, "rows": 0}
    frame = pd.read_csv(path, dtype=str).fillna("")
    expected = gold.copy()
    expected["copies"] = expected["copies"].astype(int).astype(str)
    expected["requested_at"] = expected["requested_at"].astype(str).str.slice(0, 10)
    frame["requested_at"] = frame["requested_at"].astype(str).str.slice(0, 10)
    if any(column not in frame.columns for column in COLUMNS):
        return {"ok": False, "rows": len(frame)}
    got = frame[COLUMNS].drop_duplicates("request_id").set_index("request_id").sort_index()
    want = expected[COLUMNS].drop_duplicates("request_id").set_index("request_id").sort_index()
    ok = got.index.equals(want.index) and got.astype(str).equals(want.astype(str))
    return {"ok": bool(ok), "rows": int(len(got))}
