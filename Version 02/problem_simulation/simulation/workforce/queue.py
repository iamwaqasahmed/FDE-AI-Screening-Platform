"""First-in, first-out service against daily capacity. Delay is an outcome, not a planted number."""

from __future__ import annotations

from datetime import date

import numpy as np

from simulation.world.clock import HISTORY_START


def serve(arrival_days: np.ndarray, capacity: np.ndarray, min_lag: int = 1) -> np.ndarray:
    """Return the service day index for each arrival. Unserved items get -1."""
    order = np.argsort(arrival_days, kind="stable")
    sorted_arrivals = arrival_days[order]
    served = np.full(len(arrival_days), -1, dtype=int)
    pointer = 0
    total = len(sorted_arrivals)
    for day, slots in enumerate(capacity):
        ready_until = np.searchsorted(sorted_arrivals, day - min_lag, side="right")
        take = min(int(slots), ready_until - pointer)
        if take > 0:
            served[order[pointer : pointer + take]] = day
            pointer += take
        if pointer >= total:
            break
    return served


def day_index(values) -> np.ndarray:
    base = np.datetime64(HISTORY_START.isoformat())
    return (np.array(values, dtype="datetime64[D]") - base).astype(int)


def index_day(indices: np.ndarray) -> np.ndarray:
    base = np.datetime64(HISTORY_START.isoformat())
    out = (base + indices.astype("timedelta64[D]")).astype(str)
    return np.where(indices < 0, "", out)


def to_date(index: int) -> date:
    return date.fromordinal(HISTORY_START.toordinal() + index)
