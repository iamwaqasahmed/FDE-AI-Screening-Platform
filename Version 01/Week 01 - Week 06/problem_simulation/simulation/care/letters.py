"""Letter bureau: a short normal lag, a slow migration window, and the duplicate week."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.world.clock import (
    BUREAU_MIGRATION_END,
    BUREAU_MIGRATION_START,
    INCIDENT_END,
    INCIDENT_START,
    SNAPSHOT,
    iso,
)


def stamp_letters(events: pd.DataFrame, rng: np.random.Generator) -> None:
    graded = events["graded_at"].ne("").to_numpy()
    lag = 1 + rng.poisson(1.6, len(events))
    migrating = events["graded_at"].between(iso(BUREAU_MIGRATION_START), iso(BUREAU_MIGRATION_END)).to_numpy()
    lag = np.where(migrating, lag + rng.integers(6, 27, len(events)), lag)
    graded_ts = pd.to_datetime(events["graded_at"].replace("", pd.NA))
    letter_at = graded_ts + pd.to_timedelta(lag, unit="D")
    letter_day = letter_at.dt.strftime("%Y-%m-%d").fillna("")
    died = (events["flag_true_on"] != "") & (events["flag_true_on"] <= letter_day)
    sent = graded & (letter_at <= pd.Timestamp(SNAPSHOT)).fillna(False).to_numpy() & ~died.to_numpy()
    events["letter_lag"] = np.where(sent, lag, 0)
    events["letter_at"] = np.where(sent, letter_day, "")
    events["letter_suppressed"] = died.to_numpy() & graded
    events["letter_in_migration"] = sent & migrating
    events["letter_duplicate"] = sent & events["letter_at"].ge(iso(INCIDENT_START)) & events["letter_at"].lt(iso(INCIDENT_END))
