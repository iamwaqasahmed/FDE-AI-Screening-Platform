"""Participant pages for rel-w3d4. Held-out labels stay out."""

from __future__ import annotations

CASE_DATE = "2027-01-27"
SEATS = ("cdo", "access-mgr", "phc-lead", "dpo")


def budgets() -> dict:
    return {"citation": 0.8, "extraction": 0.8, "journey": 0.8}


def experiment() -> dict:
    return {
        "arms": ["clause", "short"],
        "counts": {
            "clause": {"contained": 30, "honest_pending": 48, "n": 80},
            "short": {"contained": 55, "honest_pending": 40, "n": 80},
        },
        "metric": "honest_pending",
    }


def dot_vote() -> dict:
    return {"method": "dot-vote", "ranked": ["p-triage", "vendor-bot", "p-status", "p-dna"]}


def hidden_test() -> str:
    return f"""# Hidden-test protocol

The benchmark labels stay on the grading service. The development slice shows outputs and does not show labels. The calibration subset is the scored set a judge may be checked on.

Case date: {CASE_DATE}.
"""


def campaign() -> str:
    return f"""# Eye-screening campaign

An eye-screening campaign is announced on {CASE_DATE}. It starts the next month. Ophthalmology demand after that date is not last year's month. A session plan that copies last year misses the campaign.

The series is demand/ophth.csv. Read the counts from that file.

Case date: {CASE_DATE}.
"""


def ab_status() -> str:
    return f"""# ab-status

ab-status is open. It is a wording experiment on status replies.

Arms: short and clause.
Pre-registered metric: honest_pending.

Record the decision in the experiment log before reading a second metric. The effect is not stated here.

Case date: {CASE_DATE}.
"""


def seats() -> str:
    return """# Workshop seats

- cdo, Layla Al-Harbi. The virtual front desk, including triage, goes live before Ramadan.
- access-mgr, Noura Al-Qahtani. No-shows dominate the cost.
- phc-lead, Dr. Hassan Al-Dosari. Hospitals return referrals arbitrarily.
- dpo, Sara Al-Mutairi. Patient data needs care.
"""
