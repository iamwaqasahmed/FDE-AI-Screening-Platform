"""Access audit log: one JSON line per record read, keyed by booking id. One stale account reads records without a care relationship."""

from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

from simulation.estate.common import TRUTH, id_map, stamp
from simulation.estate.identity_roles import EXCESS_SERVICE
from simulation.world.timeline import TIMELINE

AUDIT_START = date(2024, 1, 1)
INAPPROPRIATE_READS = 36
NO_CARE_DAYS = 120
INCIDENT = next(item for item in TIMELINE if item.ref == "INC-0262")
COLUMNS = ["audit_id", "read_at", "account_id", "booking_id", "action", "client"]


def build_audit(world: dict, identity: dict, rng: np.random.Generator) -> pd.DataFrame:
    accounts = identity["accounts"].set_index("source")["account_id"]
    booking = id_map(world["identifiers"], "booking_id")
    events = world["events"]
    events = events[(events["photo_date"] >= AUDIT_START.isoformat()) & events["person_uid"].isin(booking.index)]
    legit = pd.concat([_grader_reads(events, accounts, rng), _clinic_reads(events, accounts, rng)], ignore_index=True)
    bad = _inappropriate(world["events"], booking, identity["audit_account"], rng)
    reads = pd.concat([legit.assign(appropriate=True), bad.assign(appropriate=False)], ignore_index=True)
    reads = reads[reads["read_at"] >= pd.Timestamp(AUDIT_START)].copy()
    reads["booking_id"] = reads["person_uid"].map(booking)
    reads = reads.sort_values(["read_at", "account_id", "booking_id"], kind="stable").reset_index(drop=True)
    reads.insert(0, "audit_id", [f"AUD{index:09d}" for index in range(1, len(reads) + 1)])
    reads["read_at"] = stamp(reads["read_at"])
    world["files"]["handover/audit/record_reads.jsonl"] = reads[COLUMNS]
    world["files"][f"{TRUTH}/audit_reads.parquet"] = reads
    flagged = reads[~reads["appropriate"]]
    world["gold"]["inappropriate_access"] = flagged[["audit_id", "account_id", "booking_id", "read_at"]].to_dict(orient="records")
    return reads


def _grader_reads(events: pd.DataFrame, accounts: pd.Series, rng: np.random.Generator) -> pd.DataFrame:
    graded = events[(events["grader_id"] != "") & (events["graded_at"] != "")]
    when = pd.to_datetime(graded["graded_at"]) + pd.to_timedelta(rng.integers(480, 1050, len(graded)), unit="min")
    return pd.DataFrame({"person_uid": graded["person_uid"].to_numpy(), "account_id": graded["grader_id"].map(accounts).to_numpy(),
                         "read_at": when.to_numpy(), "action": "view", "client": "grader-workbench"})


def _clinic_reads(events: pd.DataFrame, accounts: pd.Series, rng: np.random.Generator) -> pd.DataFrame:
    staff = np.array([accounts["booking_admin"], accounts["outreach_coordinator"], accounts["call_centre_lead"]])
    who = staff[rng.choice(3, len(events), p=[0.6, 0.15, 0.25])]
    when = pd.to_datetime(events["photo_date"]) - pd.to_timedelta(rng.integers(1, 11, len(events)), unit="D") \
        + pd.to_timedelta(rng.integers(480, 1050, len(events)), unit="min")
    clinic = pd.DataFrame({"person_uid": events["person_uid"].to_numpy(), "account_id": who, "read_at": when.to_numpy(),
                           "action": rng.choice(np.array(["view", "search", "update"]), len(events), p=[0.6, 0.25, 0.15]),
                           "client": "booking-portal"})
    sync = pd.DataFrame({"person_uid": events["person_uid"].to_numpy(), "account_id": accounts[EXCESS_SERVICE[0]],
                         "read_at": (pd.to_datetime(events["photo_date"]) + pd.Timedelta(hours=23, minutes=30)).to_numpy(),
                         "action": "view", "client": "integration-engine"})
    return pd.concat([clinic, sync], ignore_index=True)


def _inappropriate(events: pd.DataFrame, booking: pd.Series, account: str, rng: np.random.Generator) -> pd.DataFrame:
    start, end = pd.Timestamp(INCIDENT.start), pd.Timestamp(INCIDENT.end) + pd.Timedelta(hours=23)
    seconds = np.sort(rng.integers(0, int((end - start).total_seconds()), INAPPROPRIATE_READS))
    when = start + pd.to_timedelta(seconds, unit="s")
    near = _in_care(events, start - pd.Timedelta(days=NO_CARE_DAYS), end + pd.Timedelta(days=NO_CARE_DAYS))
    pool = np.array(sorted(set(booking.index) - near))
    chosen = rng.choice(pool, INAPPROPRIATE_READS, replace=False)
    return pd.DataFrame({"person_uid": chosen, "account_id": account, "read_at": when.round("min").to_numpy(),
                         "action": rng.choice(np.array(["view", "export"]), INAPPROPRIATE_READS, p=[0.8, 0.2]), "client": "vpn-remote"})


def _in_care(events: pd.DataFrame, start: pd.Timestamp, end: pd.Timestamp) -> set[str]:
    dates = events[["photo_date", "graded_at", "referred_at", "seen_at"]]
    inside = np.zeros(len(events), dtype=bool)
    for column in dates.columns:
        inside |= dates[column].between(start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")).to_numpy()
    return set(events.loc[inside, "person_uid"])


def care_people(world: dict) -> set[str]:
    start, end = pd.Timestamp(INCIDENT.start), pd.Timestamp(INCIDENT.end)
    return _in_care(world["events"], start - pd.Timedelta(days=NO_CARE_DAYS), end + pd.Timedelta(days=NO_CARE_DAYS))
