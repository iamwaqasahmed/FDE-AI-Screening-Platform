"""The current-state enterprise architecture document, written from the component list."""

from __future__ import annotations

from datetime import date

import pandas as pd

from simulation.architecture.components import TIERS
from simulation.corpus.add import Extra, add_document
from simulation.world.staff import name

DOC_ID = "ea-current-state"
TITLE = "Screening programme current-state enterprise architecture"
EFFECTIVE = date(2026, 6, 1)
ZONE_TEXT = {
    "ministry": "Ministry data centre. The registry extract leaves here by SFTP.",
    "hospital": "Hospital networks. Image index, referral messages, lab results, and clinic letters stay on hospital premises.",
    "clinic": "Primary-care clinic file servers. No hospital identifiers.",
    "screening-service": "The screening service network: grader workbench, booking, and the camera inventory.",
    "processor": "Contracted processors: the letter bureau and the SMS gateway.",
    "authority": "The authority tenancy and on-premises estate: warehouse, identity, audit, service desk, finance, complaints.",
    "dmz": "The perimeter: API gateway and inbound webhooks.",
    "external": "Third parties outside the authority's control, including the vendor model.",
}


def add_ea_document(world: dict, components: pd.DataFrame) -> str:
    body = "\n\n".join([_intro(), _zones(components), _integration(), _identity(), _resilience(components)])
    table = [["component", "zone", "protocol", "depends_on", "dr_tier", "owner"]]
    table += components[table[0]].astype(str).values.tolist()
    return add_document(world, DOC_ID, "architecture", TITLE, body, EFFECTIVE, extra=Extra(original="docx", table=table,
                                                                                         meta={"author": name("enterprise_architect")}))


def _intro() -> str:
    return (f"## Purpose\n\nThis document records the screening estate as it runs today. It was prepared by "
            f"{name('enterprise_architect')} and is the baseline for any change. The component list in the handover is the "
            "machine-readable copy of the tables below.")


def _zones(components: pd.DataFrame) -> str:
    lines = ["## Network zones", ""]
    for zone, text in ZONE_TEXT.items():
        members = ", ".join(components.loc[components["zone"] == zone, "name"].tolist()) or "none"
        lines.append(f"- **{zone}**: {text} Components: {members}.")
    return "\n".join(lines)


def _integration() -> str:
    return (
        "## Integration\n\nThe integration engine carries HL7 v2 messages over MLLP between the hospitals, the grader workbench, "
        "and the lab. FHIR R4 is live for Patient and Appointment only, and only booking uses it. Everything else is a file drop: "
        "the registry, the letter bureau, the call-centre export, finance, and complaints. The vendor model returns scores "
        "through a callback endpoint at the perimeter, which forwards them to the integration engine and on to the grader workbench."
    )


def _identity() -> str:
    return (
        "## Identity and access\n\nStaff sign in through the authority identity provider with SAML 2.0 or OIDC. Provisioning by "
        "SCIM reaches booking only; every other role is granted and removed by a service desk request. Leavers are processed "
        "from the HR list each month. Service accounts are owned by the integration team and reviewed yearly."
    )


def _resilience(components: pd.DataFrame) -> str:
    lines = ["## Backup and recovery tiers", "", "| Tier | Target | Components |", "|---|---|---|"]
    for tier, target in TIERS.items():
        members = ", ".join(components.loc[components["dr_tier"] == tier, "component"].tolist())
        lines.append(f"| {tier} | {target} | {members} |")
    lines.append("")
    lines.append("The backup vault takes a nightly snapshot of tier 1 to 3 systems. Tier 4 systems have no backup.")
    return "\n".join(lines)
