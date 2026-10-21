"""The vendor extract: the allowed captures, no date of birth, one person key per local id."""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

from simulation.eval.evidence.bars import EXTRACT_YEAR_BAR, PERSON_KEY_BAR

DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DOB = re.compile(r"dob|date_of_birth|birth_date", re.I)


def score(path: Path, gold: pd.DataFrame) -> dict:
    frame = _read(path)
    rows = _rows(frame, gold)
    dates = _dates(frame)
    keys = _keys(frame, gold)
    year = _year(frame, gold)
    ok = rows and dates and keys >= PERSON_KEY_BAR and year >= EXTRACT_YEAR_BAR
    return {"ok": ok, "rows": rows, "dates": dates, "keys": keys, "year": year}


def _read(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, dtype=str).fillna("")


def _rows(frame: pd.DataFrame, gold: pd.DataFrame) -> bool:
    if "capture_ref" not in frame.columns:
        return False
    return set(frame["capture_ref"]) == set(gold["capture_ref"].astype(str))


def _dates(frame: pd.DataFrame) -> bool:
    for column in frame.columns:
        if column == "capture_date" or "year" in column.lower():
            continue
        if DOB.search(column):
            return False
        if frame[column].astype(str).str.match(DATE).any():
            return False
    return True


def _keys(frame: pd.DataFrame, gold: pd.DataFrame) -> float:
    if "person_key" not in frame.columns or "capture_ref" not in frame.columns:
        return 0.0
    base = gold.assign(capture_ref=gold["capture_ref"].astype(str))[["capture_ref", "local_pid"]]
    merged = base.merge(frame[["capture_ref", "person_key"]], on="capture_ref", how="left")
    linked = merged[merged["local_pid"].astype(str).ne("")]
    if linked.empty:
        return 1.0
    good = 0
    for _, group in linked.groupby("local_pid"):
        keys = [str(key) for key, ref in zip(group["person_key"], group["capture_ref"]) if not _placeholder(key, ref)]
        good += int(len(set(keys)) <= 1)
    return good / linked["local_pid"].nunique()


def _placeholder(key, ref) -> bool:
    text = "" if pd.isna(key) else str(key)
    return text in ("", str(ref), f"unlinked:{ref}", f"solo:{ref}")


def _year(frame: pd.DataFrame, gold: pd.DataFrame) -> float:
    column = next((name for name in frame.columns if name.lower() == "year_of_birth"), "")
    if not column:
        return 1.0
    base = gold.assign(capture_ref=gold["capture_ref"].astype(str))[["capture_ref", "local_pid", "year_of_birth"]]
    base = base.rename(columns={"year_of_birth": "gold_year"})
    merged = base.merge(frame[["capture_ref", column]], on="capture_ref")
    linked = merged[merged["local_pid"].astype(str).ne("")]
    if linked.empty:
        return 1.0
    given = linked[column].astype(str).str.slice(0, 4)
    return float((given == linked["gold_year"].astype(str)).mean())
