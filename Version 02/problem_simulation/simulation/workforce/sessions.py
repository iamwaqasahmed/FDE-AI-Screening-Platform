"""Clinic sessions, camera slots, outreach van days, and ophthalmology fast-track slots by week."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.care.referrals import CONSULTANT_GAP
from simulation.world.sites import RIVER_SITE

SLOTS_PER_SESSION = 12


def build_sessions(events: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    frame = events[["site", "district", "photo_date"]].copy()
    frame["week"] = _week(frame["photo_date"])
    used = frame.groupby(["site", "district", "week"]).size().rename("captures").reset_index()
    spare = rng.uniform(1.05, 1.35, len(used))
    used["sessions"] = np.ceil(used["captures"] * spare / SLOTS_PER_SESSION).astype(int)
    used["camera_slots"] = used["sessions"] * SLOTS_PER_SESSION
    used["unused_slots"] = used["camera_slots"] - used["captures"]
    used["van_days"] = np.where(used["site"] == RIVER_SITE, np.ceil(used["sessions"] / 2).astype(int), 0)
    return used.sort_values(["week", "site"]).reset_index(drop=True)


def build_ophthalmology_slots(events: pd.DataFrame) -> pd.DataFrame:
    fast = events[events["fast_track"]].copy()
    fast["week"] = _week(fast["graded_at"])
    demand = fast.groupby("week").size().rename("fast_referrals").reset_index()
    weekly = max(demand["fast_referrals"].mean(), 1.0) * 1.35
    in_gap = demand["week"].between(CONSULTANT_GAP[0], CONSULTANT_GAP[1])
    demand["fast_slots"] = np.where(in_gap, np.floor(weekly * 0.55), np.ceil(weekly)).astype(int)
    demand["consultant_vacancy"] = in_gap
    return demand


def _week(dates: pd.Series) -> pd.Series:
    return pd.to_datetime(dates).dt.to_period("W-SUN").dt.start_time.dt.strftime("%Y-%m-%d")
