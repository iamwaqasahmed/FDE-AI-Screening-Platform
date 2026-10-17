"""One screening row per photographed person, with the sheet's messy codes."""

from __future__ import annotations

import pandas as pd


def screening_rows(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    person = tables["person"]
    photographed = person[person["cohort"] != "none"].copy()
    visit = tables["visit"][["person_uid", "photo_date", "site_name", "camera_class"]]
    image = (
        tables["image"]
        .sort_values(["person_uid", "eye"])
        .groupby("person_uid", as_index=False)
        .first()[["person_uid", "file_name", "file_path"]]
    )
    grade = tables["grade"][["person_uid", "grade", "graded_at", "grader_initials"]]
    rows = photographed.merge(visit, on="person_uid").merge(image, on="person_uid")
    rows = rows.merge(grade, on="person_uid", how="left", suffixes=("", "_graded"))
    presented = rows.apply(_present, axis=1, result_type="expand")
    rows["result"] = presented["result"]
    rows["notes"] = presented["notes"]
    rows["referral_yes"] = presented["referral_yes"]
    return rows.reset_index(drop=True)


def _present(row) -> dict:
    grade = "" if pd.isna(row["grade_graded"]) else str(row["grade_graded"])
    if grade == "" or grade == "nan":
        official = "" if pd.isna(row["grade"]) else str(row["grade"])
        grade = "" if official == "nan" else official
    slot = sum(ord(char) for char in str(row["local_pid"]))
    if grade == "R3":
        kind = slot % 3
        if kind == 0:
            return {"result": "R3", "notes": "", "referral_yes": "yes"}
        if kind == 1:
            return {"result": "", "notes": "urgent", "referral_yes": "yes"}
        return {"result": "prolif", "notes": "", "referral_yes": "yes"}
    if grade == "R2":
        return {"result": "R2", "notes": "", "referral_yes": "yes"}
    if grade == "U":
        return {"result": "U" if slot % 2 == 0 else "ungradable", "notes": "", "referral_yes": ""}
    if grade in {"R0", "R1"}:
        return {"result": grade, "notes": "", "referral_yes": ""}
    return {"result": "", "notes": "", "referral_yes": ""}
