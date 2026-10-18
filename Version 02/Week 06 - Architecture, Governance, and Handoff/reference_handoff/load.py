"""Readers for the files a team is given. Nothing here opens truth or eval."""

from __future__ import annotations

import re
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

FROM = re.compile(r"From: ([^,]+), ([^\n]+)")
DAY = re.compile(r"Date: (\d{4}-\d{2}-\d{2})")
CONDITION = re.compile(r"^(CSO-\d+)\.", re.MULTILINE)
SITES = re.compile(r"primary-care captures at (.+)\.")
SECOND = re.compile(r"Add (.+) as a second")
REQUESTED = re.compile(r"(\d{4}-\d{2}-\d{2})")


def read_csv(data: Path, relative: str) -> pd.DataFrame:
    return pd.read_csv(data / relative, dtype=str).fillna("")


def memo(data: Path, relative: str) -> str:
    return (data / relative).read_text(encoding="utf-8")


def sender(text: str) -> tuple[str, str]:
    found = FROM.search(text)
    return found.group(1).strip(), found.group(2).strip()


def dated(text: str) -> date:
    return date.fromisoformat(DAY.search(text).group(1))


def friday(day: date) -> str:
    return (day + timedelta(days=4)).isoformat()


def condition_ids(text: str) -> list[str]:
    return CONDITION.findall(text)


def pilot_sites(text: str) -> list[str]:
    raw = SITES.search(text).group(1)
    return sorted(part.strip() for part in raw.split(" and ") if part.strip())


def second_site(text: str) -> str:
    return SECOND.search(text).group(1).strip()


def requested(text: str) -> str:
    return REQUESTED.findall(text)[-1]
