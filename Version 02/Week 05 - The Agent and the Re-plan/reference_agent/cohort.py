"""The chase list from Week 4's files, read again on the week 5 date."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pandas as pd

from reference_agent.load import released
from reference_graph.measure import _pilot_ids, build as week4
from simulation.eval.evidence.drop import restriction
from simulation.eval.graph.cohort import binding


def load(data: Path) -> tuple[pd.DataFrame, list[dict], set[str]]:
    _items, _reconciled, chase, resend = week4(data)
    memo = (data / "drops/week-3/dpo_restriction_memo.md").read_text(encoding="utf-8")
    scope = _pilot_ids(data, restriction(memo, [])["allowed_sites"])
    return chase, resend, scope


def sweep(data: Path, chase: pd.DataFrame) -> pd.DataFrame:
    today = released(data, 5)
    lost = chase[chase["in_bound"] & chase["status"].eq("lost")].sort_values(["local_pid", "request_id"])
    lost = lost.drop_duplicates("local_pid")
    return pd.DataFrame([_row(row, today) for row in lost.itertuples(index=False)])


def summary(frame: pd.DataFrame) -> dict:
    clock = frame[frame["local_clock"]]
    centre = pd.to_numeric(clock["days_over"], errors="coerce").median() if len(clock) else 0
    return {
        "rows": int(len(frame)),
        "blank_hospital": int(frame["hospital"].eq("").sum()),
        "with_local_clock": int(frame["local_clock"].sum()),
        "clause_ids": sorted(set(clock["clause_id"])),
        "median_days_over": round(float(centre or 0), 1),
    }


def person(row, scope: set[str], local_id: str) -> dict:
    clause = binding(str(row.hospital), str(row.referred), str(row.mrn))
    action, reason = _action(row)
    visit = [str(row.request_id), clause.document_id]
    if str(row.mrn):
        visit.append(str(row.mrn))
    return {
        "answer": {"in_pilot_scope": local_id in scope, "copies": int(row.copies), "action": action,
                   "reason": reason, "clause_id": clause.document_id},
        "path": visit,
    }


def _row(row, today: date) -> dict:
    clause = binding(str(row.hospital), str(row.referred), str(row.mrn))
    over = ""
    if clause.days is not None:
        over = str((today - date.fromisoformat(str(row.referred)[:10])).days - int(clause.days))
    return {
        "local_pid": str(row.local_pid), "request_id": str(row.request_id), "hospital": str(row.hospital),
        "clause_id": clause.document_id, "days_over": over, "local_clock": clause.days is not None,
    }


def _action(row) -> tuple[str, str]:
    if row.status != "lost":
        return "none", ""
    if bool(row.seen_flag):
        return "hold", "seen"
    if bool(row.deceased):
        return "hold", "deceased"
    if bool(row.moved):
        return "hold", "moved"
    return "resend", ""
