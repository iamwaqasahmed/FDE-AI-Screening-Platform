"""Grading: the queue sets the date, the grader and the image set the code."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.devices.quality import UNGRADABLE_BELOW
from simulation.workforce.assign import assign_graders, initials_for
from simulation.workforce.capacity import daily_capacity, grader_hours, plan_factors, reads_per_hour
from simulation.workforce.graders import LEAD, ROSTER, sigma_on
from simulation.workforce.queue import day_index, index_day, serve, to_date
from simulation.world.clock import SNAPSHOT
from simulation.world.quotas import UNCODED

CODES = np.array(["R0", "R1", "R2", "R3"])
SECOND_SHARE = 0.08


def stamp_grading(events: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    """Return the daily hours table so the workforce surface can be written from the same draw."""
    uncoded = rng.random(len(events)) < events["district"].map(UNCODED).to_numpy()
    arrivals = day_index(events["photo_date"])
    hours = grader_hours(rng)
    window = (events["photo_date"] >= "2019-01-01") & (events["photo_date"] < "2020-01-01") & ~uncoded
    rate = reads_per_hour(hours, window.sum() / 365.0)
    capacity = daily_capacity(hours, rate, plan_factors(hours, events.loc[~uncoded, "photo_date"]))
    queued = np.where(uncoded, 10**7, arrivals)
    served = serve(queued, capacity)
    snapshot_index = (SNAPSHOT - to_date(0)).days
    served = np.where(served >= snapshot_index, -1, served)
    graded = served >= 0
    events["cohort"] = np.where(graded, "completed", "photo_no_result")
    events["graded_at"] = index_day(served)
    events["grade_lag"] = np.where(graded, served - arrivals, 0)
    grader, position = assign_graders(served, hours, rng)
    events["grader_id"] = np.where(graded, grader, "")
    events["grader_initials"] = initials_for(events["grader_id"])
    events["session_position"] = position
    events["grade"] = np.where(graded, _read(events, events["grader_id"], position, rng), "")
    _second(events, hours, rng)
    hours.attrs["reads_per_hour"] = rate
    return hours


def latent_severity(events: pd.DataFrame) -> np.ndarray:
    level = events["true_level"].to_numpy().astype(float)
    return np.where(events["true_macula"].to_numpy(), np.maximum(level, 2.0), level)


def _read(events: pd.DataFrame, graders: pd.Series, position: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    severity = latent_severity(events)
    quality = events["quality"].to_numpy()
    days = events["graded_at"].to_numpy()
    out = np.full(len(events), "", dtype=object)
    lookup = {grader.grader_id: grader for grader in ROSTER}
    for grader_id in pd.unique(graders):
        if not grader_id:
            continue
        grader = lookup[grader_id]
        rows = np.flatnonzero(graders.to_numpy() == grader_id)
        sigma = np.array([sigma_on(grader, to_date_str(days[i]), position[i]) for i in rows])
        blur = 1 + 1.5 * np.clip(0.6 - quality[rows], 0, None)
        reading = severity[rows] + grader.bias + rng.normal(0, 1, len(rows)) * sigma * blur
        codes = CODES[np.clip(np.rint(reading), 0, 3).astype(int)]
        threshold = UNGRADABLE_BELOW + (0.04 if grader.bias > 0.3 else 0.0)
        out[rows] = np.where(quality[rows] < threshold, "U", codes)
    return out


def _second(events: pd.DataFrame, hours: pd.DataFrame, rng: np.random.Generator) -> None:
    graded = events["grade"].ne("").to_numpy()
    take = graded & (rng.random(len(events)) < SECOND_SHARE)
    lag = rng.integers(1, 5, len(events))
    second_day = np.where(take, day_index(np.where(graded, events["graded_at"], "2018-10-01")) + lag, -1)
    snapshot_index = (SNAPSHOT - to_date(0)).days
    take &= second_day < snapshot_index
    second_day = np.where(take, second_day, -1)
    grader, position = assign_graders(second_day, hours, rng)
    same = grader == events["grader_id"].to_numpy()
    grader = np.where(same, LEAD.grader_id, grader)
    second_frame = events[["true_level", "true_macula", "quality"]].copy()
    second_frame["graded_at"] = index_day(second_day)
    reads = _read(second_frame, pd.Series(np.where(take, grader, "")), position, rng)
    events["second_grade"] = np.where(take, reads, "")
    events["second_grader"] = np.where(take, grader, "")
    events["second_graded_at"] = np.where(take, index_day(second_day), "")
    disagree = take & (_referable(events["grade"]) != _referable(events["second_grade"]))
    adjudicator = pd.Series(np.where(disagree, LEAD.grader_id, ""))
    adjudication = _read(second_frame, adjudicator, np.zeros(len(events)), rng)
    events["adjudicated_grade"] = np.where(disagree, adjudication, "")


def _referable(codes: pd.Series) -> np.ndarray:
    return codes.isin(["R2", "R3", "U"]).to_numpy()


def to_date_str(value: str):
    from datetime import date

    return date.fromisoformat(value) if value else SNAPSHOT
