"""Questions for rel-w3d3. Held-out text stays out of the pack."""

from __future__ import annotations

from alwaha.engagement.w3d3_docs import CASE_DATE

DEV = (
    {
        "asker": "patient",
        "case_date": CASE_DATE,
        "question_id": "dev-hours",
        "site": "cluster",
        "text": "When do the public evening clinics close?",
    },
    {
        "asker": "staff",
        "case_date": CASE_DATE,
        "question_id": "dev-endo",
        "site": "cluster",
        "specialty": "endo",
        "started": CASE_DATE,
        "text": "Which endocrinology criteria does a new referral use?",
    },
    {
        "asker": "staff",
        "case_date": CASE_DATE,
        "question_id": "dev-flight",
        "site": "cluster",
        "specialty": "endo",
        "started": "2027-01-20",
        "text": "Which endocrinology criteria does a referral opened last week keep?",
    },
)

HELD = (
    {
        "asker": "patient",
        "case_date": CASE_DATE,
        "question_id": "held-hours",
        "site": "cluster",
        "text": "Which evening clinic hours apply under code hrs-ramadan in the fasting month?",
    },
    {
        "asker": "staff",
        "case_date": CASE_DATE,
        "question_id": "held-endo",
        "site": "cluster",
        "specialty": "endo",
        "started": CASE_DATE,
        "text": "Which criteria bind endocrinology on this case date under code endo-v4?",
    },
    {
        "asker": "staff",
        "case_date": CASE_DATE,
        "inflight": True,
        "question_id": "held-flight",
        "site": "cluster",
        "specialty": "endo",
        "started": "2027-01-20",
        "text": "Which criteria bind an in-flight endocrinology referral that already started, under code endo-v4?",
    },
    {
        "asker": "staff",
        "case_date": CASE_DATE,
        "question_id": "held-neuro",
        "site": "cluster",
        "specialty": "neuro",
        "started": CASE_DATE,
        "text": "Which criteria bind neurology under code neuro-v4?",
    },
    {
        "asker": "patient",
        "case_date": CASE_DATE,
        "question_id": "held-leaflet",
        "site": "cluster",
        "text": "What should a patient bring to endocrinology preparation under code prep-endo?",
    },
    {
        "asker": "patient",
        "case_date": CASE_DATE,
        "question_id": "held-none",
        "site": "cluster",
        "text": "What is the aeromedical transfer rule under code aero-x9?",
    },
)


def dev_questions() -> list[dict]:
    return [dict(row) for row in DEV]


def held_questions() -> list[dict]:
    return [dict(row) for row in HELD]
