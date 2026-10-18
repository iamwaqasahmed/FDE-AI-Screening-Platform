"""Readers for the files a team is given. Nothing here opens truth or eval."""

from __future__ import annotations

import re
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

RELEASED = re.compile(r"Released (\d{4}-\d{2}-\d{2})")
WEEKS = re.compile(r"ready (\d+) weeks|Testing takes (\d+) weeks|Mobilisation takes (\d+) weeks")


def released(data: Path, week: int) -> date:
    text = (data / f"drops/week-{week}/README.md").read_text(encoding="utf-8")
    return date.fromisoformat(RELEASED.search(text).group(1))


def durations(data: Path) -> tuple[int, int, int]:
    text = (data / "drops/week-5/delivery_assumptions.md").read_text(encoding="utf-8")
    found = [int(next(part for part in match.groups() if part)) for match in WEEKS.finditer(text)]
    return found[0], found[1], found[2]


def read_csv(data: Path, relative: str) -> pd.DataFrame:
    return pd.read_csv(data / relative, dtype=str).fillna("")


def next_monday(day: date) -> date:
    return day + timedelta(days=(7 - day.weekday()) % 7)
