"""Small helpers shared by the system writers."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from simulation.world.clock import OUTAGE_END, OUTAGE_START
from simulation.world.sites import RIVER_SITE


def display_name(person: pd.Series) -> str:
    return f"{person['surname']}, {person['forename']}"


def in_outage(site: str, photo_date: str) -> bool:
    return site == RIVER_SITE and OUTAGE_START.isoformat() <= photo_date < OUTAGE_END.isoformat()


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=True) + "\n" for row in rows), encoding="utf-8")


def blank(value) -> str:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return ""
    return str(value)
