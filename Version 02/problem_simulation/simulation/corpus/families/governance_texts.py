"""The authority's AI governance documents as structured sections. Field lists here feed the gold."""

from __future__ import annotations

TIERS = (
    ("1", "minimal", "Internal productivity tools that never touch personal data or decisions about people."),
    ("2", "limited", "Tools that summarise or search official information for staff, with a person reading every output."),
    ("3", "high", "Systems that rank, triage, or prioritise people for a public service, or that inform a clinical decision."),
    ("4", "unacceptable", "Systems that make a clinical or eligibility decision about a person with no human review."),
)

TIER_REQUIREMENTS = {
    "1": ("register entry",),
    "2": ("register entry", "transparency record"),
    "3": ("register entry", "transparency record", "model card", "DPIA signed by the DPO", "named clinical safety owner",
          "human oversight plan", "subgroup evaluation", "incident runbook entry"),
    "4": ("not permitted",),
}

TRANSPARENCY_FIELDS = (
    "system name", "owner", "supplier", "purpose", "tier", "decision supported", "human in the loop", "data used",
    "data classification", "hosting region", "sites in scope", "start date", "evaluation summary", "contact for challenge",
)

MODEL_CARD_FIELDS = (
    "intended use", "out-of-scope use", "training data provenance", "evaluation population", "operating point",
    "sensitivity and specificity by age band", "performance by site", "performance by camera and firmware",
    "image quality limits", "known failure modes", "monitoring plan", "drift trigger", "version and change log",
)

OVERSIGHT_RULES = (
    "A tier 3 system may reorder a worklist but may not remove an item from human review.",
    "Every override of a model output is logged with the reviewer and a reason.",
    "A model output must never be sent to a patient without a signed human decision.",
    "The clinical safety owner may suspend the system at any time without a change request.",
)

INCIDENT_LEVELS = (
    ("SEV1", "possible patient harm or a personal data breach", "four hours", "clinical safety owner, DPO, security officer"),
    ("SEV2", "wrong output reaching staff at scale, or the system unavailable for a day", "one working day",
     "service owner, clinical safety owner"),
    ("SEV3", "isolated wrong output caught by a reviewer", "five working days", "service owner"),
)


def risk_tier_body() -> str:
    lines = ["## Purpose", "Every AI system the authority runs or buys is placed in one tier before work starts.", "## Tiers"]
    lines += [f"- Tier {number} ({label}): {text}" for number, label, text in TIERS]
    lines.append("## Requirements by tier")
    lines += [f"- Tier {number}: {', '.join(items)}." for number, items in TIER_REQUIREMENTS.items()]
    lines += ["## Rule", "A system that cannot meet every requirement of its tier does not go live, including in a pilot."]
    return "\n\n".join(lines)


def list_body(intro: str, heading: str, items: tuple[str, ...]) -> str:
    return "\n\n".join(["## Purpose", intro, f"## {heading}", "\n".join(f"- {item}" for item in items)])


def runbook_body() -> str:
    lines = ["## Purpose", "How staff report and handle an AI incident.", "## Severity levels"]
    lines += [f"- {code}: {what}. Report within {limit} to: {who}." for code, what, limit, who in INCIDENT_LEVELS]
    lines += ["## First steps", "Stop new outputs from reaching staff. Keep the inputs and outputs. Open a service desk incident."]
    return "\n\n".join(lines)
