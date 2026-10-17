"""The failed 2021 AI pilot. The minutes hold the real reasons; the post-mortem blames accuracy."""

from __future__ import annotations

from datetime import date

from simulation.world.sites import HARBOUR
from simulation.world.staff import VENDORS

VENDOR = VENDORS["clearsight"]
START = date(2021, 2, 1)
STOPPED = date(2021, 6, 30)
POSTMORTEM = date(2021, 9, 14)

REASONS = {
    "2021-02": ("no_safety_owner", f"The triage pilot with {VENDOR} started at {HARBOUR}. Nobody has signed the hazard log as clinical "
                                   "safety owner; the chair accepted the risk for the pilot period."),
    "2021-03": ("laterality_lost", "Graders report that images exported from the hospital image index lose the eye laterality, "
                                   "so model results cannot be matched to the right or left eye."),
    "2021-04": ("dpia_unsigned", "The data protection impact assessment for the pilot is still a draft with the data protection officer."),
    "2021-05": ("graders_ignore", "The lead grader reports that graders stopped looking at model output after repeated false alarms on "
                                  "ungradable images."),
    "2021-06": ("stopped", "The board stopped the triage pilot. The supplier is asked for a written explanation of performance."),
}

PHRASES = {
    "no_safety_owner": ["safety owner", "hazard log"],
    "laterality_lost": ["laterality", "left eye", "right eye"],
    "dpia_unsigned": ["impact assessment", "dpia"],
    "graders_ignore": ["false alarm", "stopped looking", "ignored", "lost trust"],
}

POSTMORTEM_FINDING = (
    f"The pilot was stopped because the model from {VENDOR} did not reach the accuracy described in its proposal. "
    "The recommendation is to select a more accurate product before trying again."
)


def minute_line(month: str) -> tuple[str, str] | None:
    return REASONS.get(month)


def gold() -> dict:
    return {
        "vendor": VENDOR,
        "site": HARBOUR,
        "start": START.isoformat(),
        "stopped": STOPPED.isoformat(),
        "true_reasons": [{"month": month, "reason": key} for month, (key, _) in REASONS.items() if key != "stopped"],
        "postmortem_reason": "accuracy",
        "postmortem_doc": "postmortem-ai-pilot-2021",
    }
