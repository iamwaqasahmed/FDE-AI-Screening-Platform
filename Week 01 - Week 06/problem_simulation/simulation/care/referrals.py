"""Referrals to ophthalmology. Fast-track waits come from clinic slots; disease can progress meanwhile."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.disease.state import DiseaseIndex
from simulation.workforce.queue import day_index, serve
from simulation.world.clock import SNAPSHOT, iso

CONSULTANT_GAP = ("2025-07-01", "2026-02-28")


def stamp_referrals(events: pd.DataFrame, disease: DiseaseIndex, rng: np.random.Generator) -> None:
    referable = events["cohort"].eq("completed").to_numpy() & events["grade"].isin(["R2", "R3"]).to_numpy()
    fast = referable & events["specialist_days"].ne("").to_numpy() & events["grade"].eq("R3").to_numpy()
    graded_index = day_index(np.where(referable, events["graded_at"], "2018-10-01"))
    fast_wait = _fast_waits(graded_index, fast)
    routine = np.where(events["grade"].eq("R3"), rng.integers(20, 61, len(events)), rng.integers(30, 121, len(events)))
    wait = np.where(fast, fast_wait, routine)
    graded_ts = pd.to_datetime(events["graded_at"].replace("", pd.NA))
    seen_ts = graded_ts + pd.to_timedelta(wait, unit="D")
    dna_chance = np.clip(0.18 + 0.08 * (events["travel_burden"].to_numpy() - 3), 0.05, 0.6)
    dna = referable & (rng.random(len(events)) < dna_chance)
    seen_ok = referable & ~dna & (seen_ts <= pd.Timestamp(SNAPSHOT)).fillna(False).to_numpy()
    booked_ts = np.maximum(seen_ts - pd.Timedelta(days=7), graded_ts + pd.Timedelta(days=1))
    events["referred_at"] = np.where(referable, events["graded_at"], "")
    events["booked_at"] = np.where(seen_ok, pd.Series(booked_ts).dt.strftime("%Y-%m-%d").fillna(""), "")
    events["seen_at"] = np.where(seen_ok, seen_ts.dt.strftime("%Y-%m-%d").fillna(""), "")
    events["dna"] = dna
    events["fast_track"] = fast
    reached = np.where(seen_ok, events["seen_at"], np.where(referable, iso(SNAPSHOT), ""))
    level, macula = disease.level(events["person_uid"], pd.Series(reached))
    events["true_level_at_seen"] = np.where(referable, level, -1)
    events["progressed_in_delay"] = referable & (level > events["true_level"].to_numpy())


def _fast_waits(graded_index: np.ndarray, fast: np.ndarray) -> np.ndarray:
    arrivals = np.where(fast, graded_index, 10**7)
    horizon = int(day_index([iso(SNAPSHOT)])[0]) + 400
    per_day = max(fast.sum() / max(np.ptp(graded_index[fast]) if fast.any() else 1, 1), 0.05)
    capacity = np.zeros(horizon, dtype=float)
    weekdays = (np.arange(horizon) + 0) % 7 < 5
    capacity[weekdays] = per_day * 7 / 5 * 1.35
    gap = (np.arange(horizon) >= day_index([CONSULTANT_GAP[0]])[0]) & (np.arange(horizon) <= day_index([CONSULTANT_GAP[1]])[0])
    capacity[gap] *= 0.55
    slots = _integerise(capacity)
    served = serve(arrivals, slots, min_lag=2)
    wait = np.where(served >= 0, served - graded_index, 400)
    return np.where(fast, wait, 0)


def _integerise(capacity: np.ndarray) -> np.ndarray:
    cumulative = np.floor(np.cumsum(capacity))
    return np.diff(np.concatenate([[0.0], cumulative])).astype(int)


def stamp_truth(events: pd.DataFrame, disease: DiseaseIndex) -> None:
    level, macula = disease.level(events["person_uid"], events["photo_date"])
    events["true_level"] = level
    events["true_macula"] = macula
    events["true_referable"] = (level >= 2) | macula
