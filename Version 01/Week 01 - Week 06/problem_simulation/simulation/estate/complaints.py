"""Complaints export. Lost-letter complaints cluster in the bureau migration; two complaints carry a prompt injection."""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd

from simulation.care.referrals import CONSULTANT_GAP
from simulation.config import active
from simulation.estate import complaint_text as text
from simulation.estate.common import TRUTH
from simulation.world.clock import BUREAU_MIGRATION_END, HISTORY_START, SNAPSHOT
from simulation.world.sites import CAPTURE_SITES

COLUMNS = ["complaint_id", "received_at", "site", "channel", "category", "description", "status", "closed_at"]
CHANNELS = np.array(["email", "phone", "letter", "web"])
ROUTINE_KINDS = ("waiting", "cancelled", "hospital", "sms", "access", "staff")
INJECTION_DAYS = (date(2025, 8, 14), date(2026, 1, 22))


def build_complaints(world: dict, rng: np.random.Generator) -> pd.DataFrame:
    rows = _lost_letters(world["events"], rng) + _routine(rng) + _injections(rng)
    frame = pd.DataFrame(rows).sort_values(["received_at", "site", "description"]).reset_index(drop=True)
    frame.insert(0, "complaint_id", [f"CMP-{index:05d}" for index in range(1, len(frame) + 1)])
    frame["channel"] = rng.choice(CHANNELS, len(frame))
    frame["category"] = frame["true_kind"].map(text.RECORDED)
    received = pd.to_datetime(frame["received_at"])
    closed = received + pd.to_timedelta(rng.integers(5, 40, len(frame)), unit="D")
    frame["closed_at"] = np.where(closed < pd.Timestamp(SNAPSHOT), closed.dt.strftime("%Y-%m-%d"), "")
    frame["status"] = np.where(frame["closed_at"] != "", "closed", "open")
    world["files"]["handover/complaints/complaints.csv"] = frame[COLUMNS]
    world["files"][f"{TRUTH}/complaints.parquet"] = frame
    injections = frame[frame["injection"] != ""]
    world["gold"].setdefault("injection", []).extend(
        {"doc_id": "", "complaint_id": row.complaint_id, "text": row.injection} for row in injections.itertuples(index=False)
    )
    return frame


def _lost_letters(events: pd.DataFrame, rng: np.random.Generator) -> list[dict]:
    pool = events[events["letter_in_migration"] & (events["graded_at"] != "")].sort_values("event_id")
    take = min(len(pool), active().count(40))
    chosen = pool.iloc[np.sort(rng.choice(len(pool), take, replace=False))] if take else pool.iloc[:0]
    rows = []
    for index, row in enumerate(chosen.itertuples(index=False)):
        received = date.fromisoformat(row.graded_at) + timedelta(days=int(rng.integers(14, 36)))
        received = min(received, BUREAU_MIGRATION_END)
        rows.append({"received_at": received.isoformat(), "site": row.site, "description": text.lost_letter(row.site, row.photo_date, index),
                     "true_kind": "lost_letter", "event_id": row.event_id, "person_uid": row.person_uid, "injection": ""})
    return rows


def _routine(rng: np.random.Generator) -> list[dict]:
    count = active().count(160)
    span = (SNAPSHOT - HISTORY_START).days
    rows = []
    for index in range(count):
        day = HISTORY_START + timedelta(days=int(rng.integers(0, span)))
        kind = ROUTINE_KINDS[int(rng.integers(0, len(ROUTINE_KINDS)))]
        if CONSULTANT_GAP[0] <= day.isoformat() <= CONSULTANT_GAP[1] and rng.random() < 0.5:
            kind = "hospital"
        site = CAPTURE_SITES[int(rng.integers(0, len(CAPTURE_SITES)))]
        rows.append({"received_at": day.isoformat(), "site": site, "description": text.routine(kind, site, index),
                     "true_kind": kind, "event_id": "", "person_uid": "", "injection": ""})
    return rows


def _injections(rng: np.random.Generator) -> list[dict]:
    rows = []
    for index, day in enumerate(INJECTION_DAYS):
        site = CAPTURE_SITES[int(rng.integers(0, len(CAPTURE_SITES)))]
        description, payload = text.injected(index, site)
        rows.append({"received_at": day.isoformat(), "site": site, "description": description,
                     "true_kind": "cancelled" if index == 0 else "hospital", "event_id": "", "person_uid": "", "injection": payload})
    return rows
