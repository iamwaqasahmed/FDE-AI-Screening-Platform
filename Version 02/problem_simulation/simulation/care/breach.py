"""One label per overdue encounter. The first clock that overruns wins."""

from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

from simulation.world.clock import SNAPSHOT


def apply_breach(events: pd.DataFrame) -> pd.DataFrame:
    frame = events.copy()
    frame["breach"] = _labels(frame)
    return frame


def _labels(frame: pd.DataFrame) -> np.ndarray:
    photo = pd.to_datetime(frame["photo_date"])
    graded_at = pd.to_datetime(frame["graded_at"].replace("", pd.NA))
    letter_at = pd.to_datetime(frame["letter_at"].replace("", pd.NA))
    seen_at = pd.to_datetime(frame["seen_at"].replace("", pd.NA))
    graded = frame["grade"].ne("")
    grade_limit = frame["grade_limit"].to_numpy()
    letter_limit = frame["letter_limit"].to_numpy()
    grade_lag = frame["grade_lag"].fillna(0).to_numpy()
    letter_lag = frame["letter_lag"].fillna(0).to_numpy()
    elapsed = (pd.Timestamp(SNAPSHOT) - photo).dt.days.to_numpy()
    grade_over = np.where(graded, grade_lag > grade_limit, elapsed > grade_limit)

    suppressed = frame["letter_suppressed"].to_numpy()
    letter_elapsed = (pd.Timestamp(SNAPSHOT) - graded_at).dt.days.to_numpy()
    letter_elapsed = np.nan_to_num(letter_elapsed, nan=0)
    sent = letter_at.notna().to_numpy()
    letter_over = graded & ~suppressed & np.where(sent, letter_lag > letter_limit, letter_elapsed > letter_limit)

    spec = pd.to_numeric(frame["specialist_days"], errors="coerce").to_numpy()
    has_spec = ~np.isnan(spec)
    wait = (seen_at - graded_at).dt.days.to_numpy()
    unseen_elapsed = (pd.Timestamp(SNAPSHOT) - graded_at).dt.days.to_numpy()
    booking_over = (
        frame["grade"].eq("R3").to_numpy()
        & graded.to_numpy()
        & has_spec
        & np.where(seen_at.notna().to_numpy(), wait > spec, unseen_elapsed > spec)
    )

    label = np.full(len(frame), "", dtype=object)
    label = np.where(booking_over, "booking", label)
    label = np.where(letter_over, "letter_bureau", label)
    label = np.where(grade_over, "grader_backlog", label)
    return label


def within_snapshot(value: date) -> bool:
    return value <= SNAPSHOT
