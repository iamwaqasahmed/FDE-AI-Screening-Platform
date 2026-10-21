"""SMS gateway delivery receipts: late, written in arrival order, and some twice."""

from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

from simulation.estate.common import TRUTH, id_map, log_fault, stamp
from simulation.faults import duplicate, late_arrival, out_of_order
from simulation.world.clock import REMINDER_CHANGE, SNAPSHOT

SMS_START = date(2021, 1, 4)
KEYS = ["message_id", "booking_id", "kind", "sent_at", "receipt_at", "status", "attempt"]
STATUS = ("delivered", "failed", "pending")
STATUS_P = (0.93, 0.05, 0.02)


def build_sms(world: dict, rng: np.random.Generator) -> pd.DataFrame:
    messages = _messages(world, rng)
    receipts = _receipts(messages, rng)
    receipts, late = late_arrival.apply(receipts, rng, {"column": "receipt_at", "share": 0.08, "hours": (2, 96), "key": "message_id"})
    receipts["_arrival"] = receipts["receipt_at"]
    clean = receipts.sort_values(["sent_at", "message_id", "attempt"]).reset_index(drop=True)
    shown, dup = duplicate.apply(receipts, rng, {"share": 0.02, "key": "message_id", "shift": "_arrival", "minutes": (1, 720)})
    shown, order = out_of_order.apply(shown, rng, {"arrival": "_arrival", "event": "sent_at", "drop": True})
    for entry in (late, dup, order):
        log_fault(world, "sms", entry)
    world["files"]["handover/sms/receipts.jsonl"] = _records(shown)
    truth = clean.drop(columns=["_arrival"]).assign(person_uid=lambda frame: frame["booking_id"].map(_owners(world)))
    for column in ("sent_at", "receipt_at"):
        truth[column] = stamp(truth[column])
    world["files"][f"{TRUTH}/sms_receipts.parquet"] = truth
    return truth


def _messages(world: dict, rng: np.random.Generator) -> pd.DataFrame:
    invitations = world["invitations"]
    contactable = invitations["invited"] & invitations["has_phone"] & (invitations["planned_date"] < SNAPSHOT.isoformat())
    booking = id_map(world["identifiers"], "booking_id")
    frame = invitations.loc[contactable, ["person_uid", "planned_date", "sms", "reminder"]].copy()
    frame["booking_id"] = frame["person_uid"].map(booking).fillna("")
    frame = frame[frame["booking_id"] != ""]
    planned = pd.to_datetime(frame["planned_date"])
    invites = frame[frame["sms"].to_numpy(dtype=bool)].assign(kind="invite", sent_day=planned - pd.Timedelta(days=21))
    reminders = frame[frame["reminder"].to_numpy(dtype=bool)].assign(kind="reminder", sent_day=planned - pd.Timedelta(days=3))
    both = pd.concat([invites, reminders], ignore_index=True)
    start = np.where(both["kind"] == "invite", pd.Timestamp(SMS_START), pd.Timestamp(REMINDER_CHANGE))
    both = both[(both["sent_day"] >= start) & (both["sent_day"] < pd.Timestamp(SNAPSHOT))]
    both = both.sort_values(["sent_day", "booking_id", "kind"]).reset_index(drop=True)
    both["sent_at"] = both["sent_day"].dt.normalize() + pd.to_timedelta(rng.integers(540, 1020, len(both)), unit="min")
    both["message_id"] = [f"SMS{index:09d}" for index in range(1, len(both) + 1)]
    return both[["message_id", "booking_id", "kind", "sent_at"]]


def _receipts(messages: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    first = _attempt(messages, rng, 1)
    failed = first[first["status"] == "failed"]
    retry = failed[["message_id", "booking_id", "kind"]].assign(sent_at=failed["sent_at"] + pd.Timedelta(minutes=30))
    second = _attempt(retry, rng, 2)
    return pd.concat([first, second], ignore_index=True)


def _attempt(messages: pd.DataFrame, rng: np.random.Generator, attempt: int) -> pd.DataFrame:
    count = len(messages)
    delay = pd.to_timedelta(np.round(rng.lognormal(1.0, 0.9, count), 0) + 1, unit="min")
    return messages.assign(
        receipt_at=messages["sent_at"] + delay,
        status=rng.choice(STATUS, size=count, p=STATUS_P),
        attempt=attempt,
    )


def _records(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame[KEYS].copy()
    out["sent_at"] = stamp(out["sent_at"])
    out["receipt_at"] = stamp(out["receipt_at"])
    out["attempt"] = out["attempt"].astype(int)
    return out


def _owners(world: dict) -> pd.Series:
    booking = id_map(world["identifiers"], "booking_id")
    return pd.Series(booking.index.to_numpy(), index=booking.to_numpy())
