"""Vendor pilot labels. The hospital sensitivity slide is not in this file."""

from __future__ import annotations

from screening_tools.load import require_status, vendor_scores


def vendor_pilot() -> dict:
    require_status("grade-codes", "in_force")
    scores = vendor_scores()
    empty = scores["MODEL_LABEL"] == ""
    disagree = ~empty & (scores["MODEL_LABEL"] != scores["GRADER_LABEL"])
    return {
        "tool": "vendor_pilot",
        "document_id": "grade-codes",
        "images": int(len(scores)),
        "empty_model_labels": int(empty.sum()),
        "disagreements": int(disagree.sum()),
    }
