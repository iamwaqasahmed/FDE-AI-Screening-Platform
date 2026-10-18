"""Estimate letter-not-received calls from the notes, trained on the coded rows."""

from __future__ import annotations

import re
from datetime import date, timedelta

import pandas as pd

WORD = re.compile(r"[a-z0-9']+")
BASELINE_DAYS = 56
TAIL = 14


def signal(frame: pd.DataFrame, migration: tuple[date, date], incident: tuple[date, date]) -> dict:
    prototypes = _prototypes(frame)
    windows = [
        _window(frame, prototypes, "CHG-0158", migration[0], migration[1]),
        _window(frame, prototypes, "INC-0233", incident[0], incident[1] + timedelta(days=TAIL)),
    ]
    coded = sum(row["coded"] for row in windows)
    estimate = sum(row["estimate"] for row in windows)
    return {"windows": windows, "coded_share": round(coded / estimate, 4) if estimate else 0.0}


def _window(frame: pd.DataFrame, prototypes: list[set[str]], ref: str, start: date, end: date) -> dict:
    inside = _between(frame, start, end)
    before = _between(frame, start - timedelta(days=BASELINE_DAYS), start - timedelta(days=1))
    return {
        "ref": ref,
        "start": start.isoformat(),
        "end": end.isoformat(),
        "coded": int((inside["reason_code"] == "LNR").sum()),
        "estimate": int(inside["note"].map(lambda note: _similar(note, prototypes)).sum()),
        "baseline_per_day": round(float(before["note"].map(lambda note: _similar(note, prototypes)).sum()) / BASELINE_DAYS, 4),
    }


def _prototypes(frame: pd.DataFrame) -> list[set[str]]:
    coded = frame[frame["reason_code"].eq("LNR")]["note"]
    return [_words(text) for text in coded if _words(text)]


def _similar(note: str, prototypes: list[set[str]]) -> bool:
    words = _words(note)
    return any(proto and len(words & proto) / len(proto) >= 0.7 for proto in prototypes)


def _words(text: str) -> set[str]:
    return set(WORD.findall(str(text).lower()))


def _between(frame: pd.DataFrame, start: date, end: date) -> pd.DataFrame:
    return frame[frame["call_date"].between(start.isoformat(), end.isoformat())]
