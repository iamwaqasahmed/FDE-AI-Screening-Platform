"""Letter delay and urgent-specialist delay."""

from __future__ import annotations

from screening_tools.dates import median_days, parse_date
from screening_tools.grades import completed
from screening_tools.load import letters, referrals, require_status


def letter_timing() -> dict:
    require_status("letter-result", "in_force")
    paired = completed().merge(letters(), on="LOCAL_PID", how="inner")
    delays = []
    for photo, sent in zip(paired["photo"], paired["SENT_DATE"]):
        sent_on = parse_date(sent)
        if sent_on is None:
            continue
        delays.append((sent_on - photo).days)
    return {
        "tool": "letter_timing",
        "document_id": "letter-result",
        "pairs": len(delays),
        "median_days": median_days(delays),
    }


def urgent_wait() -> dict:
    require_status("sop-urgent-draft", "draft")
    urgent = completed()
    urgent = urgent[urgent["grade_norm"] == "R3"]
    paired = urgent.merge(referrals(), on="LOCAL_PID", how="inner")
    waits = []
    for graded_on, seen in zip(paired["graded"], paired["SEEN_DATE"]):
        seen_on = parse_date(seen)
        if graded_on is None or seen_on is None:
            continue
        waits.append((seen_on - graded_on).days)
    return {
        "tool": "urgent_wait",
        "document_id": "sop-urgent-draft",
        "draft_in_force": False,
        "cases": len(waits),
        "median_days": median_days(waits),
    }
