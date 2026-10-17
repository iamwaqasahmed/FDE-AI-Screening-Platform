"""Weeks of delay beyond each clock, and harm points from the true disease level during the delay."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.economics.costs import HARM_UNIT_GBP, HARM_WEIGHTS, PROGRESSION_POINTS
from simulation.world.clock import SNAPSHOT

MAX_WEEKS = 26.0
CAUSES = ("grader_backlog", "letter_bureau", "booking")


def _days(later: pd.Series, earlier: pd.Series) -> np.ndarray:
    late = pd.to_datetime(later.replace("", pd.NA))
    early = pd.to_datetime(earlier.replace("", pd.NA))
    return (late - early).dt.days.to_numpy(dtype=float)


def delay_weeks(events: pd.DataFrame) -> np.ndarray:
    """Weeks past the limit of the clock that overran, zero for encounters with no breach."""
    snapshot = pd.Series([SNAPSHOT.isoformat()] * len(events), index=events.index)
    to_snapshot_photo = _days(snapshot, events["photo_date"])
    to_snapshot_graded = _days(snapshot, events["graded_at"])
    graded = events["grade"].ne("").to_numpy()
    grade_over = np.where(graded, events["grade_lag"].to_numpy(float), to_snapshot_photo) - events["grade_limit"].to_numpy(float)
    sent = events["letter_at"].ne("").to_numpy()
    letter_over = np.where(sent, events["letter_lag"].to_numpy(float), to_snapshot_graded) - events["letter_limit"].to_numpy(float)
    spec = pd.to_numeric(events["specialist_days"], errors="coerce").to_numpy(float)
    seen = events["seen_at"].ne("").to_numpy()
    wait = np.where(seen, _days(events["seen_at"], events["graded_at"]), to_snapshot_graded)
    booking_over = wait - spec
    breach = events["breach"].to_numpy()
    over = np.select(
        [breach == "grader_backlog", breach == "letter_bureau", breach == "booking"],
        [grade_over, letter_over, booking_over],
        default=0.0,
    )
    return np.clip(np.nan_to_num(over / 7.0, nan=0.0), 0.0, MAX_WEEKS)


def harm_points(events: pd.DataFrame) -> np.ndarray:
    weight = events["true_level"].map(HARM_WEIGHTS).fillna(0.0).to_numpy(float)
    progressed = events["progressed_in_delay"].to_numpy(bool) & events["breach"].ne("").to_numpy()
    return delay_weeks(events) * weight + np.where(progressed, PROGRESSION_POINTS, 0.0)


def cause_masks(events: pd.DataFrame) -> dict[str, np.ndarray]:
    """Graded-late and never-graded encounters share the grader_backlog label but have different causes."""
    never = events["cohort"].eq("photo_no_result").to_numpy()
    masks = {cause: events["breach"].eq(cause).to_numpy() for cause in CAUSES}
    masks["never_graded"] = masks["grader_backlog"] & never
    masks["grader_backlog"] = masks["grader_backlog"] & ~never
    return masks


def harm_by_cause(events: pd.DataFrame) -> dict[str, dict]:
    points = harm_points(events)
    weeks = delay_weeks(events)
    out = {}
    for cause, mask in cause_masks(events).items():
        out[cause] = {
            "encounters": int(mask.sum()),
            "delay_weeks": round(float(weeks[mask].sum()), 1),
            "harm_points": round(float(points[mask].sum()), 1),
            "harm_gbp": round(float(points[mask].sum()) * HARM_UNIT_GBP, 0),
            "progressed_in_delay": int((events["progressed_in_delay"].to_numpy(bool) & mask).sum()),
        }
    return out
