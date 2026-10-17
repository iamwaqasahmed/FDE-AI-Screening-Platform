"""Normalize grader codes and attach parsed dates."""

from __future__ import annotations

from functools import lru_cache

import pandas as pd

from screening_tools.dates import parse_date
from screening_tools.load import in_window, workbook


def normalize(result: str, notes: str) -> str:
    code = "" if result is None else str(result).strip().lower()
    note = "" if notes is None else str(notes).strip().lower()
    if code in {"nan", "none"}:
        code = ""
    if note in {"nan", "none"}:
        note = ""
    if code in {"r0", "r1", "r2"}:
        return code.upper()
    if code in {"r3", "prolif"} or note == "urgent":
        return "R3"
    if code in {"u", "ungradable"}:
        return "U"
    if code == "" and note == "":
        return ""
    return "UNKNOWN"


@lru_cache(maxsize=1)
def graded_sheet() -> pd.DataFrame:
    sheet = workbook().copy()
    sheet["grade_norm"] = [
        normalize(result, notes) for result, notes in zip(sheet["RESULT"], sheet["NOTES"])
    ]
    sheet["photo"] = sheet["PHOTO_DATE"].map(parse_date)
    sheet["graded"] = sheet["GRADE_DATE"].map(parse_date)
    sheet = sheet[sheet["photo"].map(in_window)].copy()
    unknown = sheet[sheet["grade_norm"] == "UNKNOWN"]
    if not unknown.empty:
        raise ValueError(f"{len(unknown)} workbook rows have an unmapped result.")
    return sheet


def completed(sheet: pd.DataFrame | None = None) -> pd.DataFrame:
    frame = graded_sheet() if sheet is None else sheet
    return frame[frame["grade_norm"] != ""]
