"""rel-w2d5 fixtures.
The clinic codes stay in gold and in the json fixtures.

The current clinic code and the previous code are different digests, so a file from a missed night is not the same as tonight's file. gold starts from the deployment expectations and adds the Ain documents, mentions, and readout sections.
"""

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
    """Return a hex prefix of the seed and the label so two clinic codes cannot collide."""
    return hashlib.sha256(f"{seed}:{label}".encode()).hexdigest()[:size]


def clinic_code(profile: Profile) -> str:
    """Return tonight's clinic code for this profile."""
    return "AIN-" + _digest(profile.seed, "w2d5-clinic", 6)


def previous_code(profile: Profile) -> str:
    """Return the previous clinic code, which a missed night would leave in place."""
    return "AIN-" + _digest(profile.seed, "w2d5-clinic-prev", 6)


def queued_fixture() -> dict:
    """Return a referral that is still queued, with no live slot."""
    return {"facility": "h-ain", "status": "queued"}


def live_slot(profile: Profile) -> dict:
    """Return the fault that claims a live booking. The watermark is this profile's canary."""
    return {
        "facility": "h-ain",
        "fault": "live-slot",
        "status": "booked",
        "watermark": profile.canary(),
    }


def nightly_file(profile: Profile) -> dict:
    """Return tonight's file, carrying the current clinic code."""
    return {"clinic_code": clinic_code(profile), "facility": "h-ain", "status": "file"}


def missed_file(profile: Profile) -> dict:
    """Return the file a missed night would leave behind, carrying the previous clinic code."""
    return {"clinic_code": previous_code(profile), "facility": "h-ain", "status": "previous"}


def _readout() -> dict:
    """Return the readout sections the Ain page is checked against."""
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
    """Return the Ain expectations for this profile.

    The deployment block starts from the earlier deployment gold, then adds the Ain documents and the mentions that must appear in the Ain and change sections.
    """
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
