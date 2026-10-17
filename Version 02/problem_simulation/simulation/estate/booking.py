"""Appointment booking: the nightly export keeps only the last state of each slot. Truth keeps every state."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.estate.common import TRUTH, base_people, id_map, log_fault, stamp, years_back
from simulation.faults import last_state_only
from simulation.world.clock import SNAPSHOT
from simulation.world.timeline import TIMELINE

COLUMNS = ["booking_id", "appointment_id", "site", "slot_start", "status", "updated_at", "channel"]
OUTAGE = next(item for item in TIMELINE if item.ref == "INC-0281")
WINDOW_START = years_back(3)


def build_booking(world: dict, rng: np.random.Generator) -> pd.DataFrame:
    appointments = _appointments(world, rng)
    history = _history(appointments, rng)
    lost = _outage_mask(history)
    shown = history.loc[~lost]
    current, entry = last_state_only.apply(shown, rng, {"key": "appointment_id", "order": "seq"})
    log_fault(world, "booking", entry)
    log_fault(world, "booking", {"fault": "outage_lost_changes", "ref": OUTAGE.ref, "rows": int(lost.sum())})
    export = current.sort_values("appointment_id").reset_index(drop=True)
    for column in ("slot_start", "updated_at"):
        export[column] = stamp(export[column])
    world["files"]["handover/booking/appointments.csv"] = export[COLUMNS]
    truth = history.assign(lost_in_outage=lost.to_numpy())
    for column in ("slot_start", "updated_at"):
        truth[column] = stamp(truth[column])
    world["files"][f"{TRUTH}/booking_history.parquet"] = truth.reset_index(drop=True)
    return truth


def _appointments(world: dict, rng: np.random.Generator) -> pd.DataFrame:
    invitations = world["invitations"]
    window = invitations["invited"] & (invitations["planned_date"] >= WINDOW_START.isoformat()) \
        & (invitations["planned_date"] < SNAPSHOT.isoformat())
    frame = invitations.loc[window, ["person_uid", "cycle_start", "planned_date", "sms", "attended"]]
    events = world["events"][["person_uid", "cycle_start", "photo_date", "site"]].drop_duplicates(["person_uid", "cycle_start"])
    frame = frame.merge(events, on=["person_uid", "cycle_start"], how="left")
    homes = base_people(world).set_index("person_uid")["home_site"]
    frame["site"] = frame["site"].fillna(frame["person_uid"].map(homes)).fillna("")
    frame["booking_id"] = frame["person_uid"].map(id_map(world["identifiers"], "booking_id")).fillna("")
    frame = frame[frame["booking_id"] != ""].sort_values(["planned_date", "booking_id"]).reset_index(drop=True)
    frame["appointment_id"] = [f"APT{index:07d}" for index in range(1, len(frame) + 1)]
    return _outcomes(frame, rng)


def _outcomes(frame: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    count = len(frame)
    attended = frame["attended"].fillna(False).astype(bool) & frame["photo_date"].notna()
    planned = _slot(frame["planned_date"], rng)
    moved_days = rng.integers(7, 29, count)
    photo = pd.to_datetime(frame["photo_date"].fillna(frame["planned_date"]))
    final_day = np.where(attended, photo, pd.to_datetime(frame["planned_date"]) + pd.to_timedelta(moved_days, unit="D"))
    rebooked = np.where(attended, photo.dt.normalize() != planned.dt.normalize(), rng.random(count) < 0.12)
    final = np.where(rebooked, _slot(pd.Series(final_day).dt.strftime("%Y-%m-%d"), rng), planned)
    outcome = np.where(attended, "attended", np.where(rng.random(count) < 0.3, "cancelled", "dna"))
    outcome = np.where(pd.Series(final) >= pd.Timestamp(SNAPSHOT), "", outcome)
    initial = np.where(frame["sms"].to_numpy(dtype=bool), "sms", np.where(rng.random(count) < 0.12, "portal", "letter"))
    return frame.assign(
        planned_slot=planned.to_numpy(), final_slot=pd.to_datetime(final), rebooked=rebooked, outcome=outcome,
        initial_channel=initial, change_channel=np.where(rng.random(count) < 0.6, "phone", "portal"),
    )


def _slot(days: pd.Series, rng: np.random.Generator) -> pd.Series:
    base = pd.to_datetime(days.reset_index(drop=True))
    return base + pd.to_timedelta(510 + 15 * rng.integers(0, 33, len(base)), unit="min")


def _history(frame: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    count = len(frame)
    keep = ["booking_id", "appointment_id", "person_uid", "site"]
    first = frame[keep].assign(
        seq=0, status="booked", slot_start=frame["planned_slot"], channel=frame["initial_channel"],
        updated_at=frame["planned_slot"].dt.normalize() - pd.to_timedelta(rng.integers(14, 36, count), unit="D")
        + pd.to_timedelta(rng.integers(480, 1080, count), unit="min"),
    )
    moved = frame[frame["rebooked"]]
    second = moved[keep].assign(
        seq=1, status="rebooked", slot_start=moved["final_slot"], channel=moved["change_channel"],
        updated_at=moved["planned_slot"] - pd.to_timedelta(rng.integers(26, 144, len(moved)), unit="h"),
    )
    closed = frame[frame["outcome"] != ""]
    last_channel = np.where(closed["rebooked"], closed["change_channel"], closed["initial_channel"])
    third = closed[keep].assign(
        seq=2, status=closed["outcome"], slot_start=closed["final_slot"], channel=last_channel,
        updated_at=closed["final_slot"] + _close_delay(closed["outcome"], rng),
    )
    history = pd.concat([first, second, third], ignore_index=True)
    return history.sort_values(["appointment_id", "seq"]).reset_index(drop=True)


def _close_delay(outcome: pd.Series, rng: np.random.Generator) -> pd.Series:
    count = len(outcome)
    minutes = np.select(
        [outcome.eq("attended"), outcome.eq("dna")],
        [rng.integers(20, 120, count), rng.integers(1440, 2880, count)],
        default=-rng.integers(120, 1200, count),
    )
    return pd.to_timedelta(minutes, unit="min")


def _outage_mask(history: pd.DataFrame) -> pd.Series:
    start = pd.Timestamp(OUTAGE.start)
    end = pd.Timestamp(OUTAGE.end) + pd.Timedelta(days=1)
    return (history["seq"] > 0) & (history["updated_at"] >= start) & (history["updated_at"] < end)
