"""AI governance documents, and the gold for a compliant submission for the vendor triage pilot."""

from __future__ import annotations

from datetime import date

import numpy as np

from simulation.corpus.add import Extra, add_document
from simulation.corpus.families import governance_texts as texts
from simulation.systems.catalog import SYSTEMS
from simulation.world.staff import VENDORS, name

FAMILY = "ai-governance"
EFFECTIVE = date(2024, 4, 1)
DOCUMENTS = (
    ("ai-risk-tier-policy", "AI risk tier policy", texts.risk_tier_body, "pdf"),
    ("ai-transparency-record-template", "Algorithmic transparency record template",
     lambda: texts.list_body("Each tier 2 or 3 system publishes a record with every field below.", "Fields",
                             texts.TRANSPARENCY_FIELDS), "docx"),
    ("ai-model-card-requirements", "Model card requirements",
     lambda: texts.list_body("A tier 3 model card must fill every field below before a pilot.", "Required fields",
                             texts.MODEL_CARD_FIELDS), "docx"),
    ("ai-human-oversight-standard", "Human oversight standard",
     lambda: texts.list_body("Rules for people supervising AI outputs.", "Rules", texts.OVERSIGHT_RULES), "pdf"),
    ("ai-incident-runbook", "AI incident runbook", texts.runbook_body, "pdf"),
)


def build(world: dict, rng: np.random.Generator) -> None:
    for doc_id, title, body, original in DOCUMENTS:
        add_document(world, doc_id, FAMILY, title, body(), EFFECTIVE, extra=Extra(original=original))
    world["gold"]["ai_governance"] = _submission_gold(world)


def _submission_gold(world: dict) -> dict:
    events = world["events"]
    scored = events[events["vendor_scored"].astype(bool)]
    vendor = next(system for system in SYSTEMS if system["system_id"] == "vendor")
    return {
        "system": "vendor triage pilot",
        "supplier": VENDORS["retinalytics"],
        "tier": "3",
        "required": list(texts.TIER_REQUIREMENTS["3"]),
        "transparency_fields": list(texts.TRANSPARENCY_FIELDS),
        "model_card_fields": list(texts.MODEL_CARD_FIELDS),
        "values": {
            "sites in scope": sorted(scored["site"].unique().tolist()),
            "hosting region": vendor["hosting"],
            "data classification": vendor["classification"],
            "owner": name("cdo"),
            "dpo": name("dpo"),
        },
        "blockers": [
            "named clinical safety owner is blank",
            "DPIA retention and region conflict with the vendor data sharing agreement",
            "hospital studies are outside the vendor contract",
        ],
    }
