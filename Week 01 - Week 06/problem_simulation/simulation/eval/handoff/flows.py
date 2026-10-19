"""Flows the design needs, and flows a rule denies. Pending waits on a named decision."""

from __future__ import annotations

from simulation.drops.rules import BANNED_FIELD, PRIMARY_CARE_SITES, REPLACEMENT_FIELD
from simulation.systems.catalog import SCORE_SYSTEM, SIGNED_GRADE_SYSTEM
from simulation.world.staff import name

# source, target, data, allowed, accepted document ids
ROWS = (
    ("shared-folder", "integration-engine", "photograph", "yes", ("ea-principles", "dpo-rule-2018")),
    ("vendor", "vendor-callback", "vendor_score", "yes", ("ea-current-state", "ea-principles")),
    ("vendor-callback", "integration-engine", "vendor_score", "yes", ("security-supplier-assurance", "ea-principles", "ea-current-state")),
    ("integration-engine", "grader", "vendor_score", "yes", ("ea-current-state", "ea-principles")),
    ("grader", "letters", "signed_grade", "yes", ("dpo-rule-2018", "ai-human-oversight-standard")),
    ("screening-agent", "M02", "local_id", "yes", ("cloud-policy", "data-classification-policy")),
    ("screening-agent", "audit", "record_reference", "yes", ("security-logging-standard",)),
    ("integration-engine", "vendor", "photograph", "pending", ("cloud-policy",)),
    ("integration-engine", "vendor", "year_of_birth", "pending", ("cloud-policy",)),
    ("pacs", "vendor", "hospital_study", "no", ("dpia-vendor-2024", "dpo-restriction-memo", "dsa-retinalytics-2025")),
    ("integration-engine", "vendor", "date_of_birth", "no", ("dpo-restriction-memo", "dpo-rule-2018")),
    ("vendor-callback", "grader", "vendor_score", "no", ("security-supplier-assurance", "ea-principles")),
    ("integration-engine", "letters", "vendor_score", "no", ("dpo-rule-2018", "ai-human-oversight-standard")),
    ("shared-folder", "screening-agent", "photograph", "no", ("dpo-rule-2018",)),
    ("screening-agent", "M06", "local_id", "no", ("cloud-policy", "data-classification-policy")),
)


def rules(world: dict) -> dict:
    return {"flow_rules": {
        "allowed_sites": list(PRIMARY_CARE_SITES),
        "banned_field": BANNED_FIELD,
        "replacement_field": REPLACEMENT_FIELD,
        "inbound_terminates": "integration-engine",
        "result_system": SIGNED_GRADE_SYSTEM,
        "score_system": SCORE_SYSTEM,
        "region_decided_by": name("dpo"),
    }}


def rows(world: dict) -> list[dict]:
    del world
    return [
        {"flow_id": f"F-{index:02d}", "source": source, "target": target, "data": data, "allowed": allowed, "rules": list(accepted)}
        for index, (source, target, data, allowed, accepted) in enumerate(ROWS, start=1)
    ]
