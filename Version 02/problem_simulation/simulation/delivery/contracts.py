"""Workstream contracts: whose output feeds whose input, and the integrated answers that need every piece."""

from __future__ import annotations

import pandas as pd

from simulation.delivery.cohort import cohort_values
from simulation.world.staff import name

CONTRACTS = (
    ("C-01", "data_engineering", "Identity clusters: one cluster per real person across registry, image index, and shared folder",
     "ml", "Vendor evaluation cohort keyed by person, not by row", "integration.vendor_cohort_after_restriction", "week-2"),
    ("C-02", "data_engineering", "Identity clusters", "data_science",
     "Overdue referable cohort counted in people who are alive and still resident", "integration.overdue_people", "week-2"),
    ("C-03", "data_science", "Overdue referable cohort", "consultant",
     "Economics: the value of clearing the overdue backlog in the pilot scope", "integration.overdue_people_primary_care", "week-3"),
    ("C-04", "consultant", "Economics and benefits", "pm", "Business case economic and financial cases",
     "benefits.corrected_cashable_gbp", ""),
    ("C-05", "architect", "Architecture and data flows across trust zones", "software",
     "Security review by the information security officer before any vendor interface", "drops.week-3.banned_field", "week-3"),
    ("C-06", "pm", "Delivery plan with procurement route, freeze calendar, and velocity", "consultant",
     "The pilot date given to the CDO", "pilot_date.earliest_pilot", "week-5"),
    ("C-07", "software", "Letter bureau reconciliation", "data_science",
     "Overdue people whose chase letter never reached them", "integration.overdue_chase_letters_lost", "week-4"),
    ("C-08", "ml", "Vendor evaluation on the restricted cohort", "architect",
     "Which captures may cross to the vendor zone", "integration.vendor_cohort_after_restriction", "week-3"),
)
COLUMNS = ("contract_id", "producer_role", "output", "consumer_role", "consumer_use", "gold_key", "changed_by_drop")


def contracts_frame() -> pd.DataFrame:
    return pd.DataFrame([dict(zip(COLUMNS, row)) for row in CONTRACTS])


def contracts_markdown() -> str:
    lines = ["# Workstream contracts", "",
             f"Agreed by {name('delivery_manager')} with each workstream lead. A producer may not change an output's shape",
             "without telling its consumer. Each weekly drop may change an input; rerun every consumer when it does.", ""]
    for contract_id, producer, output, consumer, use, _, drop in CONTRACTS:
        lines += [f"## {contract_id}: {producer} to {consumer}", "", f"- Output: {output}.", f"- Used for: {use}."]
        if drop:
            lines.append(f"- Rerun after the {drop} drop.")
        lines.append("")
    return "\n".join(lines)


def integration_gold(world: dict, pilot: dict, benefits: dict, lost_chase: int) -> dict:
    values = cohort_values(world["events"], world["people"])
    values.update(
        earliest_pilot=pilot["earliest_pilot"],
        pilot_feasible_on_request=pilot["feasible"],
        corrected_cashable_gbp=benefits["corrected_cashable_gbp"],
        overdue_chase_letters_lost=lost_chase,
        chain=[{"contract_id": row[0], "gold_key": row[5]} for row in CONTRACTS],
    )
    return values
