"""Grader workbench: the snapshot workbook and a 90-day event log."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from simulation.systems.common import blank, in_outage, write_jsonl
from simulation.systems.resolve import ids_on
from simulation.world.clock import SNAPSHOT, detail_start, iso

URGENT_NOTE = "urgent prolif, please prioritise"


def write_grader(events: pd.DataFrame, people: pd.DataFrame, identifiers: pd.DataFrame, folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    recent = iso(detail_start())
    queue = events[events["grade"].eq("") | events["graded_at"].ge(recent) | events["photo_date"].ge(recent)].copy()
    local_pid = ids_on(identifiers, "local_pid", iso(SNAPSHOT))
    _frame(queue, people, local_pid).to_excel(folder / "workbook.xlsx", index=False)
    detail = events[events["photo_date"] >= recent]
    write_jsonl(folder / "events_90d.jsonl", [_record(row, local_pid) for row in detail.itertuples(index=False)])


def _pid(row, local_pid: pd.Series) -> str:
    return "" if in_outage(row.site, row.photo_date) else blank(local_pid.get(row.person_uid, ""))


def _frame(events: pd.DataFrame, people: pd.DataFrame, local_pid: pd.Series) -> pd.DataFrame:
    names = people.set_index("person_uid")
    hidden = events["grade_hidden"].to_numpy()
    result = ["" if flag else grade for flag, grade in zip(hidden, events["grade"])]
    return pd.DataFrame(
        {
            "LOCAL_PID": [_pid(row, local_pid) for row in events.itertuples(index=False)],
            "PATIENT_NAME": events["person_uid"].map(names["surname"] + ", " + names["forename"]).to_numpy(),
            "DOB": events["person_uid"].map(names["dob"]).to_numpy(),
            "CLINIC": events["site"].to_numpy(),
            "PHOTO_DATE": events["photo_date"].to_numpy(),
            "GRADE_DATE": events["graded_at"].to_numpy(),
            "FILE_NAME": events["file_name"].to_numpy(),
            "RESULT": result,
            "REFERRAL": ["yes" if grade in {"R2", "R3"} else "" for grade in result],
            "NOTES": [URGENT_NOTE if flag else "" for flag in hidden],
            "GRADER": events["grader_initials"].to_numpy(),
            "QUALITY": events["quality_shown"].to_numpy(),
        }
    )


def _record(row, local_pid: pd.Series) -> dict:
    return {
        "local_pid": _pid(row, local_pid),
        "site": row.site,
        "photo_date": row.photo_date,
        "graded_at": row.graded_at,
        "grade": "" if row.grade_hidden else row.grade,
        "second_grade": row.second_grade,
        "adjudicated_grade": row.adjudicated_grade,
        "grader": row.grader_initials,
        "notes": URGENT_NOTE if row.grade_hidden else "",
        "file_name": row.file_name,
    }
