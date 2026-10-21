"""Hidden attendance terms. The reminder uplift differs by district and is never written to the drop."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.world.clock import REMINDER_CHANGE

REMINDER_UPLIFT = {"North City": 0.10, "East City": 0.22, "Hill Counties": 0.45, "River Districts": 0.04}
SEASON = {12: -0.35, 1: -0.35, 2: -0.25, 7: -0.15, 8: -0.20, 9: 0.10, 10: 0.15, 11: 0.10}
SMS_FROM = "2021-01-01"
COVID_HARD = ("2020-03-16", "2020-08-31")
COVID_SOFT = ("2020-09-01", "2021-06-30")
OUTREACH_FROM = pd.Timestamp("2021-07-01")
DNA_PENALTY = -0.8


def static_terms(frame: pd.DataFrame, age: np.ndarray, hba1c: np.ndarray) -> np.ndarray:
    return -0.35 * (frame["travel_burden"].to_numpy() - 3) + 0.01 * (np.minimum(age, 80) - 60) - 0.012 * (hba1c - 55)


def time_terms(planned: pd.Series, has_phone: np.ndarray, district: pd.Series) -> dict[str, np.ndarray]:
    day = planned.dt.strftime("%Y-%m-%d").to_numpy()
    month = planned.dt.month.to_numpy()
    season = np.array([SEASON.get(int(value), 0.0) for value in month])
    covid = np.where((day >= COVID_HARD[0]) & (day <= COVID_HARD[1]), -1.8, 0.0)
    covid = np.where((day >= COVID_SOFT[0]) & (day <= COVID_SOFT[1]), -0.6, covid)
    years = np.clip((planned - OUTREACH_FROM).dt.days.to_numpy() / 365.25, 0, 3)
    sms = (day >= SMS_FROM) & has_phone
    reminder = (day >= REMINDER_CHANGE.isoformat()) & has_phone
    uplift = district.map(REMINDER_UPLIFT).to_numpy()
    return {
        "season": season,
        "covid": covid,
        "trend": 0.12 * years,
        "sms": sms,
        "reminder": reminder,
        "reminder_term": np.where(reminder, uplift, 0.0),
    }


def calibrate_base(static: np.ndarray, target: float) -> float:
    low, high = -6.0, 6.0
    for _ in range(40):
        middle = (low + high) / 2
        if sigmoid(middle + static).mean() < target:
            low = middle
        else:
            high = middle
    return (low + high) / 2


def sigmoid(value: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-value))
