"""Public rows for rel-w4d2. The override rate stays out of the pack."""

from __future__ import annotations

import hashlib

from alwaha.config.profile import Profile
from alwaha.engagement.w2d4 import approved_hash

CASE_AT = "2027-02-01T08:00:00+03:00"
CASE_DATE = "2027-02-01"
FIRST_ERROR = "2027-02-01T09:12:00+03:00"
ALERT_AT = "2027-02-01T09:15:00+03:00"
SLO_MINUTES = 5
CIRCULAR = "circ-ramadan-hours"
CLINIC = "ophth-screen"
TOOL = "referral.status"
TOKENS = 128
DETAIL = "status tool returned an error"
OLD_HOURS = "Code hrs-ramadan closes the evening clinics at 21:00."
NEW_HOURS = "Evening clinics close at 01:00. Daytime slots are not offered."
REGISTERED = "Your referral is still pending."
SHADOW_TEXT = "Your referral was accepted by the shadow adapter."
TRACE = "tr-replay"


def shadow_hash(profile: Profile) -> str:
    digest = hashlib.sha256(f"{profile.seed}:w4d2-shadow".encode()).hexdigest()[:16]
    return "sha256:" + digest


def spans(profile: Profile) -> list[dict]:
    digest = approved_hash(profile)
    base = {"cpu": 0.2, "hospital": "h-wadi", "trace_id": TRACE}
    return [
        {
            **base,
            "at": "2027-02-01T09:00:00+03:00",
            "detail": "",
            "hash": digest,
            "latency_ms": 180,
            "name": "model",
            "span_id": "sp-1",
            "status": "ok",
            "tokens": TOKENS,
            "tool": TOOL,
        },
        {
            **base,
            "at": "2027-02-01T09:05:00+03:00",
            "detail": "",
            "hash": "",
            "latency_ms": 220,
            "name": "tool",
            "span_id": "sp-2",
            "status": "ok",
            "tokens": 0,
            "tool": TOOL,
        },
        {
            **base,
            "at": FIRST_ERROR,
            "detail": DETAIL,
            "hash": "",
            "latency_ms": 2400,
            "name": "tool",
            "span_id": "sp-3",
            "status": "error",
            "tokens": 0,
            "tool": TOOL,
        },
        {
            **base,
            "at": "2027-02-01T09:13:00+03:00",
            "detail": DETAIL,
            "hash": "",
            "latency_ms": 2600,
            "name": "tool",
            "span_id": "sp-4",
            "status": "error",
            "tokens": 0,
            "tool": TOOL,
        },
        {
            **base,
            "at": "2027-02-01T09:14:00+03:00",
            "detail": DETAIL,
            "hash": "",
            "latency_ms": 2800,
            "name": "tool",
            "span_id": "sp-5",
            "status": "error",
            "tokens": 0,
            "tool": TOOL,
        },
        {
            **base,
            "at": ALERT_AT,
            "detail": "",
            "hash": "",
            "latency_ms": 0,
            "name": "alert",
            "span_id": "sp-6",
            "status": "error",
            "tokens": 0,
            "tool": "",
        },
    ]


def changed() -> dict:
    return {
        "body": NEW_HOURS,
        "doc_id": CIRCULAR,
        "status": "in_force",
        "supersedes": "circ-ramadan",
        "topic": "document.changed",
    }


def gateway(seed: int) -> list[dict]:
    extra = 1 + (seed % 3)
    return [
        {"hospital": "h-wadi", "sar": 10 + extra, "tokens": 400},
        {"hospital": "h-wadi", "sar": 4, "tokens": 100},
        {"hospital": "h-nakhl", "sar": 7, "tokens": 200},
        {"hospital": "h-safra", "sar": 3 + extra, "tokens": 90},
    ]


def overrides(seed: int) -> list[dict]:
    stamped = 2 + (seed % 5)
    rows = [{"id": f"stamp-{index}", "stamped": True} for index in range(stamped)]
    rows.extend({"id": f"plain-{index}", "stamped": False} for index in range(6))
    return rows


def signals() -> list[dict]:
    return [
        {"current": CIRCULAR, "id": "drift-hours", "kind": "hours", "seen": "circ-ramadan"},
        {"current": "crit-endo-v4", "id": "drift-criteria", "kind": "criteria", "seen": "crit-endo-v3"},
        {"current": CLINIC, "id": "drift-clinic", "kind": "clinic", "seen": "ophth-clinic"},
    ]


def experiment(profile: Profile) -> dict:
    return {
        "candidate_hash": shadow_hash(profile),
        "id": "shadow-extract",
        "note": "The patient must not see the shadow text.",
        "registered_hash": approved_hash(profile),
        "registered_reply": REGISTERED,
        "shadow_reply": SHADOW_TEXT,
    }
