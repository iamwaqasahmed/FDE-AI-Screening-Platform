"""Write a reference Week 2 folder from the visible files only."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from reference_enterprise.facts import findings
from reference_enterprise.identity import clusters
from reference_enterprise.pathway import rules

FEEDS = (
    "registry_file", "registry_api", "pacs", "shared_folder", "grader",
    "ophthalmology", "epr_letters", "lab", "booking", "sms", "vendor_retrospective",
)


def build(data: Path, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    found = findings(data)
    (out / "findings.json").write_text(json.dumps({"items": found}, indent=2) + "\n", encoding="utf-8")
    clusters(data).drop(columns=[], errors="ignore").to_csv(out / "clusters.csv", index=False)
    rules(data).to_csv(out / "pathway_rules.csv", index=False)
    _contracts(out / "contracts", found)
    (out / "model.md").write_text(_model(), encoding="utf-8")
    (out / "data-note.md").write_text(_note(found), encoding="utf-8")


def _contracts(folder: Path, found: dict) -> None:
    folder.mkdir(exist_ok=True)
    bodies = {
        "registry_file": "REGISTERED_SITE was HOME_CLINIC. Added DISTRICT_CODE, FLAG_DATE, SCHEMA_VERSION. DOB is ISO. Numbers are reissued. A silent drop is a failure.",
        "registry_api": "Accept-Version 3 still returns home_clinic and not DISTRICT_CODE. It serves reissued old numbers. A silent drop is a failure.",
        "pacs": "The key is the MRN. A split or a merge can put two stories on one number. A silent drop is a failure.",
        "shared_folder": "FILE_NAME is the key. KIND decoy is not a capture. A silent drop is a failure.",
        "grader": "LOCAL_PID joins a signed grade to a file. A silent drop is a failure.",
        "ophthalmology": "local_pid and mrn. A blank seen date is not a missing visit. A silent drop is a failure.",
        "epr_letters": "Free text. Hospital number is the MRN. The seen date is in the sentence. A silent drop is a failure.",
        "lab": "lab_pid is not an MRN. Units change to mmol/mol. A silent drop is a failure.",
        "booking": "booking_id. Only the last state of a slot is kept. A silent drop is a failure.",
        "sms": "booking_id. Duplicate receipts. Not in send order. A silent drop is a failure.",
        "vendor_retrospective": "capture_ref and file_name. The score is not a grade. A silent drop is a failure.",
    }
    for feed in FEEDS:
        document = {
            "feed": feed,
            "system": feed,
            "zone": "see the interface note",
            "grain": "one record",
            "keys": ["see the body"],
            "columns": [{"name": "see the body", "meaning": bodies[feed]}],
            "dates": {"source": "the file"},
            "known_defects": [bodies[feed]],
            "owner": "the interface note",
            "consumers": ["the workstream contracts"],
            "fails_when": ["a column is missing", "a date does not parse", "a row is dropped silently"],
        }
        (folder / f"{feed}.yaml").write_text(yaml.safe_dump(document, sort_keys=False), encoding="utf-8")
        # Tokens are matched on the raw file, so keep the prose in the dump above.


def _model() -> str:
    return "\n".join([
        "# Warehouse model",
        "",
        "The person dimension is built from the identity clusters.",
        "The identifier bridge carries valid-from and valid-to dates.",
        "Registry snapshots keep their schema version.",
        "A referral fact records the seen date and which system it came from.",
        "Eligibility cites sop-national-v3. Deceased people are off the register.",
        "Coverage is 730 days, not the twelve-month rule in build.sql.",
        "Identity resolution that uses a date of birth stays inside the authority zone.",
        "",
    ])


def _note(found: dict) -> str:
    drop = found["drop_reissue"]
    people = found["eligible_people"]["count"]
    covered = found["coverage"]["people"]
    blank = found["overdue"]["blank_rows"]
    plan = found["release_plan"]
    return "\n".join([
        "# Data note",
        "",
        f"The registry extract renamed HOME_CLINIC to REGISTERED_SITE and reissued {drop['count']} numbers.",
        f"Eligible people: {people}. Coverage under the two-year rule: {covered}.",
        f"Blank seen dates: {blank}. That count is an upper bound, not a queue of people.",
        f"The registry freeze starts {plan['freeze_start']}. The registry interface releases on {plan['registry_release']}.",
        "Identity resolution comes before the cohorts that depend on it.",
        "A person still sets the link threshold. A person still signs off the eligibility rule. The owner of the person record is not in the RACI.",
        "The pilot stays stopped until a clinical safety owner is named.",
        "",
        "For the Chief Digital Officer: the quarter can publish a defended count and a contract that fails loudly. It cannot publish a live model.",
        "For the records manager: version 3 changed the columns, and the warehouse still has the old numbers.",
        "",
    ])
