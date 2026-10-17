"""Unfinished photos and the four-pile grader queue."""

from __future__ import annotations

from screening_tools.grades import graded_sheet
from screening_tools.load import require_status


def unfinished_photos() -> dict:
    require_status("grade-codes", "in_force")
    sheet = graded_sheet()
    return {
        "tool": "unfinished_photos",
        "document_id": "grade-codes",
        "count": int((sheet["grade_norm"] == "").sum()),
    }


def grader_queue() -> dict:
    require_status("clinic-note", "in_force")
    sheet = graded_sheet()
    counts = sheet["grade_norm"].value_counts().to_dict()
    return {
        "tool": "grader_queue",
        "document_id": "clinic-note",
        "order": ["unfinished", "unreadable", "mild_referable", "sight_threatening"],
        "counts": {
            "unfinished": int(counts.get("", 0)),
            "unreadable": int(counts.get("U", 0)),
            "mild_referable": int(counts.get("R2", 0)),
            "sight_threatening": int(counts.get("R3", 0)),
        },
        "readable_not_referable": int(counts.get("R0", 0) + counts.get("R1", 0)),
    }
