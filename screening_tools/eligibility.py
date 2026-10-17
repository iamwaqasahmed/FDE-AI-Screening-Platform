"""Eligibility and coverage from the issued screening procedure."""

from __future__ import annotations

from screening_tools.grades import completed, graded_sheet
from screening_tools.load import registry, require_status

DOCUMENT_ID = "sop-issued"


def coverage(district: str | None = None) -> dict:
    require_status(DOCUMENT_ID, "in_force")
    people = registry()
    eligible = people[people["FLAG"] == ""].copy()
    screened = completed(graded_sheet())
    joined = screened.merge(
        eligible[["LOCAL_PID", "district_name"]],
        on="LOCAL_PID",
        how="left",
    )
    if joined["district_name"].isna().any():
        raise ValueError("A completed screen did not join an eligible registry row.")
    by_district = []
    for name, group in eligible.groupby("district_name", sort=True):
        done = int((joined["district_name"] == name).sum())
        by_district.append({"district": name, "eligible": int(len(group)), "completed": done})
    result = {
        "tool": "coverage",
        "document_id": DOCUMENT_ID,
        "eligible": int(len(eligible)),
        "completed": int(len(screened)),
        "by_district": by_district,
    }
    if district is None:
        return result
    match = [row for row in by_district if row["district"] == district]
    if not match:
        raise ValueError(f"Unknown district: {district}")
    return {
        "tool": "coverage",
        "document_id": DOCUMENT_ID,
        "district": district,
        "eligible": match[0]["eligible"],
        "completed": match[0]["completed"],
    }
