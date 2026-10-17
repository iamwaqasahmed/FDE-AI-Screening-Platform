"""Shared helpers for document families: monthly aggregates, phrasing variety, and date labels."""

from __future__ import annotations

import random
from datetime import date

import pandas as pd

from simulation.world.clock import HISTORY_START, SNAPSHOT

WORDS = ("no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")


def months() -> list[date]:
    out, day = [], date(HISTORY_START.year, HISTORY_START.month, 1)
    while day < date(SNAPSHOT.year, SNAPSHOT.month, 1):
        out.append(day)
        day = date(day.year + (day.month == 12), day.month % 12 + 1, 1)
    return out


def quarters() -> list[tuple[int, int, date]]:
    return [(day.year, (day.month - 1) // 3 + 1, day) for day in months() if day.month in (1, 4, 7, 10)]


def month_label(day: date) -> str:
    return f"{day:%B %Y}"


def quarter_of(column: pd.Series) -> pd.Series:
    stamp = pd.to_datetime(column, errors="coerce")
    return stamp.dt.year.astype("Int64").astype(str) + "q" + stamp.dt.quarter.astype("Int64").astype(str)


def site_month_stats(events: pd.DataFrame) -> pd.DataFrame:
    """Per capture site and photo month: captures, grades, referrals, breaches, and lag."""
    frame = events[events["photo_date"] != ""].copy()
    frame["month"] = frame["photo_date"].str.slice(0, 7)
    frame["lag"] = pd.to_numeric(frame["grade_lag"], errors="coerce")
    grouped = frame.groupby(["site", "month"])
    stats = pd.DataFrame(
        {
            "captures": grouped.size(),
            "ungradable": grouped["grade"].apply(lambda grades: int((grades == "U").sum())),
            "referable": grouped["grade"].apply(lambda grades: int(grades.isin(["R2", "R3"]).sum())),
            "backlog": grouped["breach"].apply(lambda breach: int((breach == "grader_backlog").sum())),
            "letters": grouped["breach"].apply(lambda breach: int((breach == "letter_bureau").sum())),
            "booking": grouped["breach"].apply(lambda breach: int((breach == "booking").sum())),
            "median_lag": grouped["lag"].median().round(0),
        }
    )
    return stats.reset_index()


def pick(rng: random.Random, *options: str) -> str:
    return options[rng.randrange(len(options))]


def percent(part: int, whole: int) -> str:
    return f"{100 * part / whole:.1f}" if whole else "0.0"
