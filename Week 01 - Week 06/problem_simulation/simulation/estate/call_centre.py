"""Call-centre log: daily exports bundled by month. The reason mix moves with the bureau migration and the consultant gap."""

from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

from simulation.care.referrals import CONSULTANT_GAP
from simulation.config import active
from simulation.estate.call_notes import caller_pool, notes, with_pii
from simulation.estate.common import TRUTH, base_people, id_map, log_fault, stamp
from simulation.estate.sms import SMS_START
from simulation.faults import schema_drift
from simulation.world.clock import BUREAU_MIGRATION_END, BUREAU_MIGRATION_START, HISTORY_START, INCIDENT_END, INCIDENT_START, SNAPSHOT

REASONS = {"LNR": 0.10, "CGA": 0.08, "RBK": 0.26, "RES": 0.15, "TRN": 0.08, "SMS": 0.07, "MOV": 0.10, "CMP": 0.05, "OTH": 0.11}
LABELS = {"LNR": "letter not received", "CGA": "cannot get appointment", "RBK": "rebook appointment", "RES": "results query",
          "TRN": "transport", "SMS": "text message query", "MOV": "change of address", "CMP": "complaint", "OTH": "other"}
EXPORT_V2 = date(2024, 7, 1)
CODED_SHARE = 0.55
PII_SHARE = 0.12
V1 = ["call_id", "call_date", "started_at", "duration_s", "agent_id", "reason_code", "note"]


def build_call_centre(world: dict, rng: np.random.Generator) -> pd.DataFrame:
    calls = _calls(rng)
    calls["note"] = notes(calls["true_reason"].to_numpy(), rng)
    calls = _add_pii(world, calls, rng)
    for month, part in calls.groupby("month", sort=True):
        world["files"][f"handover/call_centre/export/calls-{month}.csv"] = _export(world, part, month, rng)
    truth = calls.drop(columns=["month"])
    truth["started_at"] = stamp(truth["started_at"])
    world["files"][f"{TRUTH}/call_reasons.parquet"] = truth
    return truth


def reason_weights(days: pd.DatetimeIndex) -> np.ndarray:
    codes = list(REASONS)
    weights = np.tile(np.array([REASONS[code] for code in codes]), (len(days), 1))
    migration = (days >= pd.Timestamp(BUREAU_MIGRATION_START)) & (days <= pd.Timestamp(BUREAU_MIGRATION_END))
    incident = (days >= pd.Timestamp(INCIDENT_START)) & (days <= pd.Timestamp(INCIDENT_END) + pd.Timedelta(days=14))
    gap = (days >= pd.Timestamp(CONSULTANT_GAP[0])) & (days <= pd.Timestamp(CONSULTANT_GAP[1]))
    weights[:, codes.index("LNR")] *= np.where(migration, 5.0, np.where(incident, 4.0, 1.0))
    weights[:, codes.index("CGA")] *= np.where(gap, 4.0, 1.0)
    weights[:, codes.index("SMS")] *= np.where(days >= pd.Timestamp(SMS_START), 1.0, 0.0)
    return weights / weights.sum(axis=1, keepdims=True)


def _calls(rng: np.random.Generator) -> pd.DataFrame:
    days = pd.date_range(pd.Timestamp(HISTORY_START), pd.Timestamp(SNAPSHOT) - pd.Timedelta(days=1), freq="D")
    weekday = np.select([days.dayofweek == 6, days.dayofweek == 5], [0.0, 0.4], default=1.0)
    counts = rng.poisson(active().count(16) * weekday)
    weights = reason_weights(days)
    codes = np.array(list(REASONS))
    reasons = np.concatenate([rng.choice(codes, size=count, p=row) for count, row in zip(counts, weights) if count])
    call_days = np.repeat(days.to_numpy(), counts)
    started = pd.Series(call_days) + pd.to_timedelta(rng.integers(480, 1110, len(call_days)), unit="min")
    frame = pd.DataFrame({"started_at": started, "true_reason": reasons}).sort_values("started_at", kind="stable").reset_index(drop=True)
    frame.insert(0, "call_id", [f"CALL{index:08d}" for index in range(1, len(frame) + 1)])
    frame["call_date"] = frame["started_at"].dt.strftime("%Y-%m-%d")
    frame["month"] = frame["call_date"].str[:7]
    frame["duration_s"] = np.round(rng.gamma(2.2, 120, len(frame))).astype(int) + 20
    frame["agent_id"] = np.char.add("CC", np.char.zfill(rng.integers(1, 13, len(frame)).astype(str), 2))
    coded = rng.random(len(frame)) < CODED_SHARE
    frame["reason_code"] = np.where(coded, frame["true_reason"], "GEN")
    frame["person_uid"] = ""
    return frame


def _add_pii(world: dict, calls: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    identifiers = world["identifiers"]
    pool = caller_pool(base_people(world), id_map(identifiers, "phone", ("assigned", "household")), id_map(identifiers, "national_id"))
    chosen = np.flatnonzero(rng.random(len(calls)) < PII_SHARE)
    callers = pool.iloc[rng.integers(0, len(pool), len(chosen))].reset_index(drop=True)
    texts, spans = with_pii(calls["call_id"].iloc[chosen].tolist(), calls["note"].iloc[chosen].tolist(), callers, rng)
    out = calls.copy()
    out.loc[out.index[chosen], "note"] = texts
    out.loc[out.index[chosen], "person_uid"] = callers["person_uid"].to_numpy()
    world["gold"].setdefault("pii_calls", []).extend(spans)
    return out


def _export(world: dict, part: pd.DataFrame, month: str, rng: np.random.Generator) -> pd.DataFrame:
    frame = part[V1].copy()
    frame["started_at"] = stamp(frame["started_at"])
    if month < EXPORT_V2.isoformat()[:7]:
        return frame
    drifted, entry = schema_drift.apply(frame, rng, {
        "renames": {"reason_code": "disposition_code", "note": "agent_notes"}, "added": {"queue": "screening"},
        "version": "v2", "partition": month,
    })
    if month == EXPORT_V2.isoformat()[:7]:
        log_fault(world, "call-centre", entry)
    return drifted
