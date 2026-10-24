"""rel-w2d5 fixtures. The clinic codes stay in gold and in the json fixtures."""

from __future__ import annotations

import hashlib

from alwaha.config.profile import Profile
from alwaha.engagement.w2d4 import gold as deploy_gold

CARD = "Change request cr-ain: include h-ain."
QUESTIONS = (
    "What does the deployed assistant still not do?",
    "Will you include Ain, and where in the sequence?",
    "How does a patient at Ain get a confirmed slot?",
    "What does the starter dashboard show?",
    "What will this proof not build?",
)
AIN_DOCS = (
    "cr-ain",
    "notices/cr-ain.md",
    "sched-ain",
    "systems/sched-ain.md",
)


def _digest(seed: int, label: str, size: int) -> str:
    return hashlib.sha256(f"{seed}:{label}".encode()).hexdigest()[:size]


def clinic_code(profile: Profile) -> str:
    return "AIN-" + _digest(profile.seed, "w2d5-clinic", 6)


def previous_code(profile: Profile) -> str:
    return "AIN-" + _digest(profile.seed, "w2d5-clinic-prev", 6)


def queued_fixture() -> dict:
    return {"facility": "h-ain", "status": "queued"}


def live_slot(profile: Profile) -> dict:
    return {
        "facility": "h-ain",
        "fault": "live-slot",
        "status": "booked",
        "watermark": profile.canary(),
    }


def nightly_file(profile: Profile) -> dict:
    return {"clinic_code": clinic_code(profile), "facility": "h-ain", "status": "file"}


def missed_file(profile: Profile) -> dict:
    return {"clinic_code": previous_code(profile), "facility": "h-ain", "status": "previous"}


def _readout() -> dict:
    return {
        "asks": "Asks",
        "boundary": ["clinician", "urgency", "ext-large"],
        "sections": [
            {"all": ["health", "hash"], "heading": "Smoke", "id": "smoke"},
            {"all": ["cr-ain", "sequenc"], "heading": "Change", "id": "change"},
            {"all": ["nightly", "sched-ain", "zone-hospital"], "heading": "File", "id": "file"},
            {"all": ["queued"], "heading": "Patients", "id": "patients"},
            {"all": ["latency"], "any": ["stage 2", "week 4"], "heading": "Monitoring", "id": "monitoring"},
            {"all": ["local-small", "quota"], "heading": "Model", "id": "model"},
        ],
    }


def gold(profile: Profile) -> dict:
    base = deploy_gold(profile)["deployment"]
    mentions = list(base["mentions"]) + [
        {"any": ["h-ain"], "id": "ain", "section": "Ain"},
        {"any": ["sched-ain"], "id": "sched", "section": "Ain"},
        {"any": ["nightly"], "id": "nightly", "section": "Ain"},
        {"any": ["zone-hospital"], "id": "hospital", "section": "Ain"},
        {"any": ["cr-ain"], "id": "change", "section": "Change"},
        {"any": ["sequenc"], "id": "sequence", "section": "Change"},
    ]
    return {
        "clinic_code": clinic_code(profile),
        "deployment": {
            "doc_ids": list(base["doc_ids"]) + list(AIN_DOCS),
            "mentions": mentions,
            "share": 0.8,
        },
        "previous_code": previous_code(profile),
        "readout": _readout(),
    }
