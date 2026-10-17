"""Load the client drop. Does not read truth, eval, or the generator config."""

from __future__ import annotations

from datetime import date, datetime
from functools import lru_cache
from pathlib import Path

import pandas as pd

from screening_tools.dates import parse_date

REPO_ROOT = Path(__file__).resolve().parents[1]
HANDOVER = REPO_ROOT / "data" / "handover"
CORPUS = REPO_ROOT / "data" / "corpus"

DISTRICT_ALIASES = {
    "north city": "North City",
    "n. city": "North City",
    "northcity": "North City",
    "east city": "East City",
    "east-city": "East City",
    "e. city": "East City",
    "hill counties": "Hill Counties",
    "hill county": "Hill Counties",
    "river districts": "River Districts",
    "river district": "River Districts",
    "rivers": "River Districts",
}


def canonical_district(value: str) -> str:
    key = str(value).strip().lower()
    if key not in DISTRICT_ALIASES:
        raise ValueError(f"Unmapped district: {value!r}")
    return DISTRICT_ALIASES[key]


@lru_cache(maxsize=1)
def snapshot() -> date:
    text = (HANDOVER / "README.txt").read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.lower().startswith("snapshot:"):
            raw = line.split(":", 1)[1].strip()
            return datetime.strptime(raw, "%d %B %Y").date()
    raise ValueError("Cover note has no snapshot date.")


def window() -> tuple[date, date]:
    end = snapshot()
    start = end.replace(year=end.year - 2)
    return start, end


def in_window(value: date | None) -> bool:
    if value is None:
        return False
    start, end = window()
    return start <= value < end


@lru_cache(maxsize=1)
def registry() -> pd.DataFrame:
    frame = pd.read_csv(HANDOVER / "diabetes_registry.csv", dtype=str).fillna("")
    frame["district_name"] = frame["DISTRICT"].map(canonical_district)
    return frame


@lru_cache(maxsize=1)
def workbook() -> pd.DataFrame:
    book = pd.read_excel(HANDOVER / "grader_workbook.xlsx", sheet_name=None, dtype=str)
    frames = [frame.fillna("") for name, frame in book.items() if name != "OLD"]
    sheet = pd.concat(frames, ignore_index=True)
    sheet = sheet[~sheet["LOCAL_PID"].str.startswith("TEST")].copy()
    return sheet


@lru_cache(maxsize=1)
def letters() -> pd.DataFrame:
    return pd.read_csv(HANDOVER / "letter_dispatch.csv", dtype=str).fillna("")


@lru_cache(maxsize=1)
def referrals() -> pd.DataFrame:
    return pd.read_csv(HANDOVER / "ophthalmology_referrals.csv", dtype=str).fillna("")


@lru_cache(maxsize=1)
def vendor_scores() -> pd.DataFrame:
    return pd.read_csv(HANDOVER / "vendor_scores.csv", dtype=str).fillna("")


@lru_cache(maxsize=1)
def corpus_status() -> dict[str, str]:
    manifest = pd.read_csv(CORPUS / "manifest.csv", dtype=str)
    return dict(zip(manifest["document_id"], manifest["status"]))


def require_status(document_id: str, expected: str) -> None:
    actual = corpus_status().get(document_id)
    if actual != expected:
        raise ValueError(f"{document_id} is {actual}, expected {expected}.")
