"""The reading the cover note asks for. It does not match the issued procedure."""

from __future__ import annotations

from screening_tools.load import registry, workbook


def coverage_if_you_trust_the_cover_note() -> dict:
    people = registry()
    active = people[people["RECORD_STATUS"].str.lower() == "active"]
    sheet = workbook()
    joined = sheet.merge(people, left_on="LOCAL_PID", right_on="REGISTRY_NO", how="inner")
    return {
        "tool": "coverage_if_you_trust_the_cover_note",
        "document_id": None,
        "eligible": int(len(active)),
        "joined_on_registry_no": int(len(joined)),
    }
