"""The volume knob: multi-million-row SMS and audit streams, partitioned by year. Off unless the profile sets volume."""

from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

from simulation.faults import duplicate, out_of_order
from simulation.world.clock import SNAPSHOT

VOLUME_ROWS = 5_000_000
PART_ROWS = 500_000


def sms_stream(booking_ids: np.ndarray, rng: np.random.Generator, start: date, rows: int = VOLUME_ROWS) -> tuple[dict, list]:
    messages = rows // 2
    sent = _times(rng, start, messages)
    frame = pd.DataFrame({
        "message_seq": np.arange(1, messages + 1, dtype=np.int64),
        "booking_id": rng.choice(booking_ids, messages),
        "kind": rng.choice(np.array(["invite", "reminder"]), messages, p=[0.55, 0.45]),
    })
    submitted = frame.assign(event_type="submitted", event_at=sent, status="accepted", attempt=1)
    retried = rng.random(messages) < 0.06
    retry = frame.loc[retried].assign(event_type="retry", event_at=sent[retried] + pd.Timedelta(minutes=30), status="accepted", attempt=2)
    delay = pd.to_timedelta(np.round(rng.lognormal(1.0, 1.4, messages)) + 1, unit="min")
    receipt = frame.assign(event_type="receipt", event_at=sent + delay,
                           status=rng.choice(np.array(["delivered", "failed", "pending"]), messages, p=[0.93, 0.05, 0.02]), attempt=1)
    stream = pd.concat([submitted, retry, receipt], ignore_index=True)
    return _faulted(stream, rng, "handover/sms/stream", "message_seq")


def audit_stream(accounts: np.ndarray, booking_ids: np.ndarray, rng: np.random.Generator, start: date,
                 rows: int = VOLUME_ROWS) -> tuple[dict, list]:
    stream = pd.DataFrame({
        "event_seq": np.arange(1, rows + 1, dtype=np.int64),
        "account_id": rng.choice(accounts, rows),
        "booking_id": rng.choice(booking_ids, rows),
        "action": rng.choice(np.array(["view", "search", "update", "export"]), rows, p=[0.78, 0.15, 0.06, 0.01]),
        "event_at": _times(rng, start, rows),
    })
    return _faulted(stream, rng, "handover/audit/stream", "event_seq")


def _times(rng: np.random.Generator, start: date, count: int) -> pd.Series:
    first = np.datetime64(start.isoformat(), "s").astype(np.int64)
    last = np.datetime64(SNAPSHOT.isoformat(), "s").astype(np.int64)
    seconds = np.sort(rng.integers(first, last, count))
    return pd.Series(seconds.astype("datetime64[s]"))


def _faulted(stream: pd.DataFrame, rng: np.random.Generator, prefix: str, key: str) -> tuple[dict, list]:
    stream = stream.assign(_arrival=stream["event_at"] + pd.to_timedelta(rng.exponential(90, len(stream)).round(), unit="s"))
    stream, dup = duplicate.apply(stream, rng, {"share": 0.01, "shift": "_arrival", "minutes": (1, 240)})
    stream, order = out_of_order.apply(stream, rng, {"arrival": "_arrival", "event": "event_at", "drop": False})
    return _partitions(stream, prefix), [dup, order]


def _partitions(stream: pd.DataFrame, prefix: str) -> dict:
    files = {}
    years = stream["_arrival"].dt.year.to_numpy()
    for year in np.unique(years):
        part = stream.loc[years == year].drop(columns=["_arrival"]).reset_index(drop=True)
        for index, begin in enumerate(range(0, len(part), PART_ROWS)):
            files[f"{prefix}/year={int(year)}/part-{index:04d}.parquet"] = part.iloc[begin:begin + PART_ROWS].reset_index(drop=True)
    return files
