"""Where a person was photographed, how the capture was stored, and on what date."""

from __future__ import annotations

from datetime import timedelta

import numpy as np
import pandas as pd

from simulation.world.clock import SNAPSHOT, iso
from simulation.world.sites import NCEC, RIVER_SITE, is_hospital

FORCED = {"false_merge", "split", "alias_source"}


def stamp_site(events: pd.DataFrame, rng: np.random.Generator) -> None:
    site = events["home_site"].to_numpy(dtype=object)
    hill = events["district"].eq("Hill Counties").to_numpy()
    river = events["district"].eq("River Districts").to_numpy()
    hill_roll = rng.random(len(events))
    river_roll = rng.random(len(events))
    site = np.where(hill & (hill_roll < 0.25), NCEC, site)
    site = np.where(river & (river_roll < 0.80), RIVER_SITE, site)
    site = np.where(river & (river_roll >= 0.80), NCEC, site)
    forced = events["scenario"].isin(FORCED).to_numpy()
    events["site"] = np.where(forced, NCEC, site)
    events["capture"] = [capture_for(value) for value in events["site"]]


def capture_for(site: str) -> str:
    if is_hospital(site):
        return "pacs"
    if site == RIVER_SITE:
        return "outreach_laptop"
    return "shared_folder"


def stamp_photos(events: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    rebook = np.where(rng.random(len(events)) < 0.2, rng.integers(7, 29, len(events)), 0)
    photos = pd.to_datetime(events["planned_date"]) + pd.to_timedelta(rebook, unit="D")
    photos = photos.clip(upper=pd.Timestamp(SNAPSHOT - timedelta(days=1)))
    events = events.copy()
    events["rebooked_days"] = rebook
    events["photo_date"] = photos.dt.strftime("%Y-%m-%d")
    keep = events["photo_date"].ge(events["cycle_start"]) & events["photo_date"].lt(iso(SNAPSHOT))
    alive = (events["flag_true_on"] == "") | (events["photo_date"] < events["flag_true_on"])
    present = (events["silent_move_on"] == "") | (events["photo_date"] < events["silent_move_on"])
    return events.loc[keep & alive & present].reset_index(drop=True)
