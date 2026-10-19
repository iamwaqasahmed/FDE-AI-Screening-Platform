"""The lost chase letters inside the bound, read one local id at a time, as at the week 5 date."""

from __future__ import annotations

from datetime import date

import pandas as pd

from simulation.eval.agent.bars import TODAY
from simulation.eval.graph.cohort import binding


def facts(linked: dict) -> tuple[dict, pd.DataFrame]:
    frame = _rows(linked["chase"])
    return {"sweep_summary": _summary(frame)}, frame


def _rows(chase: pd.DataFrame) -> pd.DataFrame:
    lost = chase[chase["in_bound"] & chase["status"].eq("lost")].sort_values(["local_pid", "request_id"])
    lost = lost.drop_duplicates("local_pid")
    rows = [_one(row) for row in lost.itertuples(index=False)]
    columns = ["local_pid", "request_id", "hospital", "clause_id", "days_over", "local_clock"]
    return pd.DataFrame(rows, columns=columns).reset_index(drop=True)


def _one(row) -> dict:
    clause = binding(str(row.hospital), str(row.referred), str(row.mrn))
    over = ""
    if clause.days is not None:
        elapsed = (TODAY - date.fromisoformat(str(row.referred)[:10])).days
        over = str(elapsed - int(clause.days))
    return {
        "local_pid": str(row.local_pid),
        "request_id": str(row.request_id),
        "hospital": str(row.hospital),
        "clause_id": clause.document_id,
        "days_over": over,
        "local_clock": clause.days is not None,
    }


def _summary(frame: pd.DataFrame) -> dict:
    clock = frame[frame["local_clock"]]
    centre = pd.to_numeric(clock["days_over"], errors="coerce").median() if len(clock) else 0
    return {
        "rows": int(len(frame)),
        "blank_hospital": int(frame["hospital"].eq("").sum()),
        "with_local_clock": int(len(clock)),
        "clause_ids": sorted(set(clock["clause_id"])),
        "median_days_over": round(float(centre or 0), 1),
    }
