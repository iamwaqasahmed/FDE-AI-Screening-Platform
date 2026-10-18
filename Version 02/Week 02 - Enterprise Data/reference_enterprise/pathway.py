"""Pathway rules read from the signed headers and the sentences, not from the register."""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

from reference_enterprise.load import documents

COLUMNS = ["site", "topic", "grade", "clause_id", "document_id", "days", "effective", "sunset"]


def rules(data: Path) -> pd.DataFrame:
    rows = []
    for document in documents(data):
        if document.get("status") == "draft":
            continue
        rows.extend(_rows(document))
    frame = pd.DataFrame(rows, columns=COLUMNS)
    return _inherit_coverage(frame)


def _rows(document: dict) -> list[dict]:
    sites = document.get("applies_to") or [""]
    found = []
    for topic, grade, days in _phrases(document.get("body", "")):
        for site in sites:
            found.append(_rule(document, site, topic, grade, days))
    if _eligibility(document.get("body", "")) and not any(row["topic"] == "eligibility" for row in found):
        for site in sites:
            found.append(_rule(document, site, "eligibility", "", ""))
    return found


def _rule(document: dict, site: str, topic: str, grade: str, days: str) -> dict:
    return {
        "site": site,
        "topic": topic,
        "grade": grade,
        "clause_id": document.get("document_id", ""),
        "document_id": document.get("document_id", ""),
        "days": days,
        "effective": document.get("effective", ""),
        "sunset": document.get("sunset", ""),
    }


def _phrases(body: str) -> list[tuple[str, str, str]]:
    found = []
    for sentence in re.split(r"[.\n]", body):
        found.extend(_sentence(sentence.lower()))
    return found


def _sentence(low: str) -> list[tuple[str, str, str]]:
    found = []
    if "ten weekdays" in low:
        found.append(("grade_turnaround", "", "10"))
    if "three weeks" in low and "grade" in low:
        found.append(("grade_turnaround", "", "21"))
    if "two weeks" in low and "grade" in low:
        found.append(("grade_turnaround", "", "14"))
    if "five weekdays" in low:
        found.append(("letter_turnaround", "", "5"))
    if "one week" in low and "letter" in low:
        found.append(("letter_turnaround", "", "7"))
    if "two weeks" in low and "letter" in low:
        found.append(("letter_turnaround", "", "14"))
    if "fortnight" in low:
        found.append(("specialist_review", "", "14"))
    if any(phrase in low for phrase in ("no national deadline", "no national clock", "not on a national clock", "not given a national")):
        found.append(("specialist_review", "", ""))
    if "two years" in low:
        found.append(("coverage_window", "", "730"))
    if "three months" in low and "ungradable" in low:
        found.append(("recall", "U", "90"))
    if "two months" in low:
        found.append(("recall", "U", "60"))
    if "one year" in low and "non-referable" in low:
        found.extend([("recall", "R0", "365"), ("recall", "R1", "365")])
    return found


def _eligibility(body: str) -> bool:
    lowered = body.lower()
    return ("flag" in lowered and "empty" in lowered) or ("deceased" in lowered and "coverage count" in lowered) or "eligible" in lowered


def _inherit_coverage(frame: pd.DataFrame) -> pd.DataFrame:
    """Version 3 supersedes version 2 and does not restate the two-year window."""
    stated = frame[(frame["document_id"] == "sop-national-v3") & (frame["topic"] == "coverage_window")]
    if not stated.empty:
        return frame
    earlier = frame[(frame["document_id"] == "sop-national-v2") & (frame["topic"] == "coverage_window")]
    if earlier.empty:
        return frame
    copied = earlier.iloc[0].to_dict()
    current = frame[frame["document_id"].eq("sop-national-v3")]
    copied["document_id"] = "sop-national-v3"
    copied["clause_id"] = "sop-national-v3"
    if not current.empty:
        copied["effective"] = current.iloc[0]["effective"]
        copied["sunset"] = current.iloc[0]["sunset"]
    return pd.concat([frame, pd.DataFrame([copied])], ignore_index=True)
