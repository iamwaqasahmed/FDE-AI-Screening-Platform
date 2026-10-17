"""Daily grading capacity from the rota. Calibrated against demand so that only vacancies make backlog."""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd

from simulation.workforce.graders import ROSTER, active_on
from simulation.world.clock import HISTORY_START, ROTA_CHANGE, SNAPSHOT

HEADROOM = 1.37
ROTA_SLOWDOWN = 0.55
BASE_YEAR = 2019


def days() -> list[date]:
    count = (SNAPSHOT - HISTORY_START).days + 120
    return [HISTORY_START + timedelta(days=offset) for offset in range(count)]


def grader_hours(rng: np.random.Generator) -> pd.DataFrame:
    """Hours each grader worked each day, after leave and the December dip."""
    calendar = days()
    weekday = np.array([day.weekday() < 5 for day in calendar])
    december = np.array([day.month == 12 and day.day > 20 for day in calendar])
    table = {}
    for grader in ROSTER:
        active = np.array([active_on(grader, day) for day in calendar])
        leave = _leave_days(len(calendar), rng)
        hours = np.where(active & weekday & ~leave, grader.weekly_hours / 5.0, 0.0)
        hours = np.where(december, hours * 0.4, hours)
        if grader.worse_after_rota:
            after = np.array([day >= ROTA_CHANGE for day in calendar])
            hours = np.where(after, hours * ROTA_SLOWDOWN, hours)
        table[grader.grader_id] = hours
    frame = pd.DataFrame(table)
    frame.insert(0, "day", [day.isoformat() for day in calendar])
    return frame


def _leave_days(count: int, rng: np.random.Generator) -> np.ndarray:
    leave = np.zeros(count, dtype=bool)
    for year_start in range(0, count, 365):
        for _ in range(3):
            start = year_start + int(rng.integers(0, 340))
            leave[start : start + int(rng.integers(5, 12))] = True
    return leave


def reads_per_hour(hours: pd.DataFrame, demand_per_day: float) -> float:
    """One rate for everyone, set so the full pre-vacancy team has HEADROOM over demand."""
    graders = [column for column in hours.columns if column != "day"]
    window = hours[(hours["day"] >= "2019-01-01") & (hours["day"] < "2020-01-01")]
    staffed = window[graders].sum(axis=1).mean()
    return HEADROOM * demand_per_day / max(staffed, 1e-6)


def plan_factors(hours: pd.DataFrame, photo_dates: pd.Series) -> np.ndarray:
    """Sessions are set each January from last year's volume, so a growth year starts short."""
    volume = photo_dates.str[:4].astype(int).value_counts()
    base = max(volume.get(BASE_YEAR, 1), 1)
    years = hours["day"].str[:4].astype(int).to_numpy()
    factors = {year: max(1.0, volume.get(year - 1, base) / base) if year > BASE_YEAR else 1.0 for year in set(years)}
    return np.array([factors[year] for year in years])


def daily_capacity(hours: pd.DataFrame, rate: float, factors: np.ndarray) -> np.ndarray:
    graders = [column for column in hours.columns if column != "day"]
    raw = hours[graders].sum(axis=1).to_numpy() * rate * factors
    cumulative = np.floor(np.cumsum(raw))
    return np.diff(np.concatenate([[0.0], cumulative])).astype(int)
