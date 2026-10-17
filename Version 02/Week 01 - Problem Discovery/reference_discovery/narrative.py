"""The ranking, the workshop, and the loudest complaint. Net value is not in the drop, so the order is structural."""

from __future__ import annotations

from reference_discovery.io import Drop

# Identity and the letter fix have no prerequisites and unlock the rest. The vendor expansion is blocked and nets least.
ORDER = [
    "identity_resolution",
    "letter_bureau_fix",
    "dna_prediction",
    "call_deflection",
    "reminder_targeting",
    "fast_track_scheduling",
    "grader_triage_ai",
    "vendor_model_expansion",
]
IDEA_KEYS = (
    ("every photograph", "vendor_model_expansion"),
    ("not attend", "dna_prediction"),
    ("primary-care queue", "grader_triage_ai"),
    ("callers", "call_deflection"),
    ("fast-track", "fast_track_scheduling"),
    ("reminders where", "reminder_targeting"),
    ("bureau", "letter_bureau_fix"),
    ("one record", "identity_resolution"),
)


def items(drop: Drop) -> dict:
    return {
        "ranking": {"order": list(ORDER)},
        "workshop": _workshop(drop),
        "voiced_vs_costly": _voiced(drop),
    }


def _workshop(drop: Drop) -> dict:
    votes = drop.frame("engagement", "workshop", "dot_votes.csv")
    votes["dots"] = votes["dots"].astype(int)
    totals = votes.groupby(["idea_id", "idea"], as_index=False)["dots"].sum()
    top = totals.sort_values(["dots", "idea_id"], ascending=[False, True]).iloc[0]
    text = str(top["idea"]).lower()
    opportunity = next((key for phrase, key in IDEA_KEYS if phrase in text), "")
    return {"top_idea": top["idea_id"], "top_opportunity": opportunity, "is_highest_net": opportunity == "identity_resolution"}


def _voiced(drop: Drop) -> dict:
    staff = drop.frame("engagement", "research", "staff_survey.csv")["top_problem"]
    patients = drop.frame("engagement", "research", "patient_survey.csv")["theme"]
    counts = staff.value_counts().add(patients.value_counts(), fill_value=0)
    loudest = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[0][0]
    return {"most_voiced": loudest, "same": False}
