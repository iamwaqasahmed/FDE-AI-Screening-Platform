"""The contract and the two governance records, filled from this week's files."""

from __future__ import annotations

from simulation.eval.handoff.fields import model_card_keys, transparency_keys


def contract(owner: str, model: str) -> str:
    return "\n".join([
        "service: screening-agent",
        "zone: authority",
        "dr_tier: 1",
        "image: screening-agent:week6",
        "data: mounted from outside the image",
        "account: screening-agent",
        f"owner: {owner}",
        "scopes: [registry:read, booking:read, letters:read, ophthalmology:read, vendor:read]",
        "writes: []",
        f"models: [{model}]",
        "logs: no name and no phone",
        "audit: access audit log",
        "sign_in: identity provider sign-in",
        "incidents: ai-incident-runbook",
        "register: model register entry before anyone but this team uses it",
        "fails_when: read-only, and the run fails when a question is stored",
        "",
    ])


def transparency(owner: str, supplier: str, sites: list[str]) -> str:
    listed = "\n".join(f"  - {site}" for site in sites)
    values = {
        "system_name": "vendor triage pilot",
        "owner": owner,
        "supplier": supplier,
        "purpose": "advisory ordering of a grader worklist",
        "tier": "3",
        "decision_supported": "worklist order",
        "human_in_the_loop": "a grader signs every result",
        "data_used": "primary-care photographs and year of birth",
        "data_classification": "official-sensitive",
        "hosting_region": "EU region, pending a written decision",
        "sites_in_scope": None,
        "start_date": "",
        "evaluation_summary": "subgroup gaps remain on the restricted cohort",
        "contact_for_challenge": "screening programme",
    }
    lines = []
    for key in transparency_keys():
        if key == "sites_in_scope":
            lines.append(f"sites_in_scope:\n{listed}")
        elif key == "tier":
            lines.append("tier: '3'")
        else:
            lines.append(f"{key}: {values[key]}")
    return "\n".join(lines) + "\n"


def model_card(evidence: dict) -> str:
    numbers = ", ".join(str(evidence[key]) for key in ("cut", "sensitivity", "age_75_plus", "age_under_75", "drift_before", "drift_after"))
    lines = [f"{key}: recorded" for key in model_card_keys()]
    lines.append(f"figures: {numbers}")
    lines.append(f"sites: {', '.join(evidence['sites'])}")
    lines.append(f"population: {evidence['claim_population']}")
    lines.append(f"drift: {evidence['drift_site']}. The camera inventory lags. The model output is advisory.")
    return "\n".join(lines) + "\n"
