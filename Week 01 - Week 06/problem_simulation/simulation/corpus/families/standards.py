"""Security, cloud, classification, and EA standards, plus the five-case business case template."""

from __future__ import annotations

from datetime import date

import numpy as np

from simulation.corpus.add import Extra, add_document

FAMILY = "standards"

STANDARDS = (
    ("security-authentication-standard", "Authentication standard", date(2022, 1, 10), (
        "Staff sign in through the authority identity provider with multi-factor authentication.",
        "Service accounts are named, owned by a person, and hold only the rights the service needs.",
        "Access is removed within one working day of a leaver or role change.")),
    ("security-logging-standard", "Logging and monitoring standard", date(2022, 1, 10), (
        "Application logs must not contain names, phone numbers, addresses, or national ids.",
        "Every read of a patient record is written to the access audit log.",
        "Audit logs are kept for seven years and reviewed monthly.")),
    ("security-encryption-standard", "Encryption standard", date(2022, 1, 10), (
        "Data is encrypted in transit with current TLS and at rest with keys the authority controls.",
        "Keys for official-sensitive data are held in the authority key vault.")),
    ("security-supplier-assurance", "Supplier assurance standard", date(2023, 2, 1), (
        "Suppliers handling official-sensitive data complete the assurance questionnaire before contract award.",
        "Inbound connections from suppliers terminate in the integration zone, never in the clinical zone.",
        "Suppliers report security incidents within twenty-four hours.")),
    ("cloud-policy", "Cloud policy", date(2023, 6, 1), (
        "Official data may be processed in any approved cloud region.",
        "Official-sensitive personal data must stay in a UK region unless the DPO approves another region in writing.",
        "Large language model services follow the approved model register.")),
    ("data-classification-policy", "Data classification policy", date(2021, 9, 1), (
        "Official: routine business information.",
        "Official-sensitive: personal health data, identifiers, and photographs.",
        "Public: information approved for publication.")),
    ("ea-principles", "Enterprise architecture principles", date(2022, 5, 1), (
        "Reuse before buy, buy before build.",
        "Integrate through the integration engine; no point-to-point feeds into clinical systems.",
        "Every system names a system of record for each data item it holds.")),
)

FIVE_CASES = (
    ("Strategic case", "Why change is needed now; the problem stated with evidence from the programme's own data."),
    ("Economic case", "Options including do nothing; costs, benefits, and risks over five years; the preferred option."),
    ("Commercial case", "Procurement route and threshold; contract length; supplier market; exit."),
    ("Financial case", "Capital and revenue costs by year; funding source; affordability."),
    ("Management case", "Owner, governance, clinical safety, delivery plan, benefits realisation, and evaluation."),
)


def build(world: dict, rng: np.random.Generator) -> None:
    for doc_id, title, effective, rules in STANDARDS:
        body = "\n\n".join(["## Rules", *(f"{index}. {rule}" for index, rule in enumerate(rules, start=1))])
        add_document(world, doc_id, FAMILY, title, body, effective, extra=Extra(original="pdf"))
    body = "\n\n".join(["## How to use", "Fill every case. A case left blank fails the funding gate.",
                        *(f"## {name}\n\n{text}" for name, text in FIVE_CASES)])
    add_document(world, "business-case-template", FAMILY, "Business case template (five cases)", body, date(2024, 1, 8),
                 extra=Extra(original="docx"))
