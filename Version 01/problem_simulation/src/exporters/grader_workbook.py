"""Grader workbook with one tab per year and a junk OLD tab."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pandas as pd

from problem_simulation.src.exporters.dates import format_mixed


def write_grader_workbook(rows, handover_dir: Path) -> None:
    sheet = pd.DataFrame(
        {
            "LOCAL_PID": rows["local_pid"],
            "PATIENT_NAME": rows["surname"] + ", " + rows["forename"],
            "DOB": [_as_mixed(value, index) for index, value in enumerate(rows["dob"])],
            "CLINIC": rows["site_name"],
            "PHOTO_DATE": [_as_mixed(value, index) for index, value in enumerate(rows["photo_date"])],
            "GRADE_DATE": [_as_mixed(value, index + 1) for index, value in enumerate(rows["graded_at"])],
            "FILE_NAME": rows["file_name"],
            "RESULT": rows["result"],
            "REFERRAL": rows["referral_yes"],
            "NOTES": rows["notes"],
            "GRADER": rows["grader_initials"].fillna(""),
        }
    )
    years = pd.to_datetime(rows["photo_date"]).dt.year
    path = handover_dir / "grader_workbook.xlsx"
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        for year in (2024, 2025, 2026):
            sheet.loc[years == year].to_excel(writer, sheet_name=str(year), index=False)
        _old_tab().to_excel(writer, sheet_name="OLD", index=False)


def _as_mixed(value, slot: int):
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return ""
    if hasattr(value, "date") and not isinstance(value, date):
        value = value.date()
    if isinstance(value, pd.Timestamp):
        if pd.isna(value):
            return ""
        value = value.date()
    return format_mixed(value, slot)


def _old_tab() -> pd.DataFrame:
    rows = []
    for offset in range(15):
        rows.append(
            {
                "LOCAL_PID": f"TEST{offset + 1:03d}",
                "PATIENT_NAME": "TEST PATIENT",
                "DOB": "01/01/1970",
                "CLINIC": "Training",
                "PHOTO_DATE": "15/03/2019",
                "GRADE_DATE": "20/03/2019",
                "FILE_NAME": f"TEST_{offset + 1}.jpg",
                "RESULT": "R2",
                "REFERRAL": "yes",
                "NOTES": "imported practice row",
                "GRADER": "XX",
            }
        )
    return pd.DataFrame(rows)
