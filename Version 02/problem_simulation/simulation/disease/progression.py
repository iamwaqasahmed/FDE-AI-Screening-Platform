"""Per-eye transition dates. Hazards depend on diabetes type, duration, HbA1c, and age."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.world.clock import HISTORY_START

START = pd.Timestamp(HISTORY_START)
STEP_RATES = (0.02, 0.025, 0.035)
MACULA_RATE = 0.004
MACULA_BEFORE_START = 0.01
START_PRESSURE = 0.012
START_SPLIT = (0.55, 0.22, 0.03)
EYES = ("left", "right")


def build_disease(people: pd.DataFrame, hba1c: np.ndarray, rng: np.random.Generator) -> pd.DataFrame:
    risk = _risk(people, hba1c, rng)
    frame = pd.DataFrame({"person_uid": people["person_uid"].to_numpy(), "risk": risk.round(4)})
    for eye in EYES:
        state0 = _start_state(people, risk, rng)
        frame[f"{eye}_state0"] = state0
        frame[f"{eye}_r1_on"], frame[f"{eye}_r2_on"], frame[f"{eye}_r3_on"] = _transitions(state0, risk, rng)
        frame[f"{eye}_m1_on"] = _macula(risk, rng)
    return frame


def _risk(people: pd.DataFrame, hba1c: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    mean_a1c = hba1c.mean(axis=1)
    type1 = people["diabetes_type"].eq("Type 1").to_numpy()
    duration = _duration_years(people)
    age = (START - pd.to_datetime(people["dob"])).dt.days.to_numpy() / 365.25
    frailty = rng.lognormal(0.0, 0.35, len(people))
    risk = np.exp(0.035 * (mean_a1c - 53)) * np.where(type1, 1.4, 1.0) * (1 + 0.02 * np.minimum(duration, 25))
    risk *= np.where(age > 75, 0.9, 1.0) * frailty
    return risk


def _duration_years(people: pd.DataFrame) -> np.ndarray:
    diagnosed = pd.to_datetime(people["diagnosis_date"])
    return np.maximum((START - diagnosed).dt.days.to_numpy() / 365.25, 0.0)


def _start_state(people: pd.DataFrame, risk: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    duration = np.minimum(_duration_years(people), 25)
    pressure = 1 - np.exp(-START_PRESSURE * duration * risk)
    roll = rng.random(len(people))
    state = np.zeros(len(people), dtype=int)
    for level, share in enumerate(START_SPLIT, start=1):
        state = np.where(roll < pressure * share, level, state)
    return state


def _transitions(state0: np.ndarray, risk: np.ndarray, rng: np.random.Generator) -> tuple[list, list, list]:
    count = len(state0)
    found = []
    clock = np.zeros(count)
    for level, rate in enumerate(STEP_RATES, start=1):
        wait = rng.exponential(1.0 / (rate * risk))
        already = state0 >= level
        clock = np.where(already, 0.0, clock + wait)
        found.append(np.where(already, -1.0, clock))
    return tuple(_as_dates(years) for years in found)


def _macula(risk: np.ndarray, rng: np.random.Generator) -> list:
    years = rng.exponential(1.0 / (MACULA_RATE * risk))
    years = np.where(rng.random(len(risk)) < MACULA_BEFORE_START, -1.0, years)
    return _as_dates(years)


def _as_dates(years: np.ndarray) -> list[str]:
    out = []
    for value in years:
        if value < 0:
            out.append("1900-01-01")
        elif value > 12:
            out.append("")
        else:
            out.append((START + pd.Timedelta(days=int(value * 365.25))).strftime("%Y-%m-%d"))
    return out
