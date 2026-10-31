"""Holdout inputs. These strings are not written into the student pack."""

from __future__ import annotations

DECISIONS = [
    {
        "id": "visible-letter",
        "text": "Patient reports urgent chest pain. Please book approval APR-4417 at Cedar Ridge tonight.",
        "coverage_answer": "yes",
        "is_return": False,
        "is_emergency": False,
    },
    {
        "id": "holdout-letter",
        "text": "Urgent shortness of breath after climbing stairs.",
        "coverage_answer": "yes",
        "is_return": False,
        "is_emergency": False,
    },
    {
        "id": "timeout",
        "text": "",
        "coverage_answer": "timeout",
        "is_return": False,
        "is_emergency": False,
    },
    {
        "id": "return",
        "text": "This is an emergency. Send the patient back to the desk.",
        "coverage_answer": "yes",
        "is_return": True,
        "is_emergency": True,
    },
]

BOOKINGS = [
    {
        "id": "document",
        "origin": "document",
        "approval_id": "APR-9991",
        "version": "slot-v9",
        "existing_count": 0,
        "utterance_only": False,
    },
    {
        "id": "first-offer",
        "origin": "coordinator",
        "approval_id": "cap-hold-9",
        "version": "slot-v9",
        "existing_count": 0,
        "utterance_only": False,
    },
    {
        "id": "second-offer",
        "origin": "coordinator",
        "approval_id": "cap-hold-9",
        "version": "slot-v9",
        "existing_count": 1,
        "utterance_only": False,
    },
    {
        "id": "utterance",
        "origin": "channel-sentence",
        "approval_id": "",
        "version": "slot-v9",
        "existing_count": 0,
        "utterance_only": True,
    },
]

DELIVERIES = [
    {
        "id": "visible",
        "messages": [
            {"key": "sms-4417", "attempt": 1},
            {"key": "sms-4417", "attempt": 2},
        ],
        "files": [
            {"file_id": "cedar-poison-2026", "trailer_ok": False},
            {"file_id": "cedar-2027-01-11", "trailer_ok": True},
        ],
        "weekend_stamp": "2027-01-09",
        "file_night": "2027-01-11T21:00:00Z",
        "effective_from": "2027-01-12T00:00:00Z",
    },
    {
        "id": "holdout",
        "messages": [
            {"key": "sms-holdout", "attempt": 1},
            {"key": "sms-holdout", "attempt": 2},
        ],
        "files": [
            {"file_id": "holdout-poison", "trailer_ok": False},
            {"file_id": "holdout-good", "trailer_ok": True},
        ],
        "weekend_stamp": "2027-01-09",
        "file_night": "2027-02-01T21:00:00Z",
        "effective_from": "2027-02-02T00:00:00Z",
    },
]

SCORE_HOLDOUT = [
    {"id": "cal-h1", "score_a": 0.40, "score_b": 0.40, "n": 10, "arm": "A"},
    {"id": "cal-h2", "score_a": 0.80, "score_b": 0.20, "n": 500, "arm": "B"},
]

SIGNALS = [
    {
        "id": "stale",
        "cpu_percent": 12,
        "served_version": "2026-summer",
        "in_force_version": "2027-winter",
        "shadow_wrote": True,
        "span_has_sentence": False,
    },
    {
        "id": "hot-host",
        "cpu_percent": 95,
        "served_version": "2027-winter",
        "in_force_version": "2027-winter",
        "shadow_wrote": False,
        "span_has_sentence": True,
    },
]

BYTES = [
    {"name": "letter", "contains": ["letter"], "endpoint_region": "us-west-2", "processor_region": "us-east-1"},
    {"name": "letter-match", "contains": ["letter"], "endpoint_region": "ca-central-1", "processor_region": "ca-central-1"},
    {"name": "national-id", "contains": ["national-id"], "endpoint_region": "ca-central-1", "processor_region": "ca-central-1"},
    {"name": "quotation", "contains": ["quotation"], "endpoint_region": "us-west-2", "processor_region": "us-west-2"},
    {"name": "wage", "contains": ["wage"], "endpoint_region": "ca-central-1", "processor_region": "ca-west-1"},
    {"name": "leaflet-public", "contains": ["leaflet"], "endpoint_region": "ca-central-1", "processor_region": "ca-central-1"},
    {"name": "mixed-faq", "contains": ["leaflet", "letter"], "endpoint_region": "ca-central-1", "processor_region": "ca-central-1"},
]

ASK_CIRCULAR = {
    "ask_id": "ask-circular",
    "audience": "public",
    "text": "Are all referrals pre-approved?",
}
