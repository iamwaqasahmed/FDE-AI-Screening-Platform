"""Key facts for the eleven feed contracts, the warehouse model, and the data note."""

from __future__ import annotations

FIELDS = [
    "feed", "system", "zone", "grain", "keys", "columns", "dates",
    "known_defects", "owner", "consumers", "fails_when",
]
FEEDS = (
    "registry_file", "registry_api", "pacs", "shared_folder", "grader",
    "ophthalmology", "epr_letters", "lab", "booking", "sms", "vendor_retrospective",
)
FORBIDDEN = [
    "Each registry number belongs to one person.",
    "Records with the same name and date of birth are the same person.",
    "A blank seen date means the patient was not seen.",
    "Deceased people are eligible.",
    "The MRN identifies one person.",
]


def text_facts(gold: dict) -> dict:
    drop, counts, cohorts, release = gold["drop"], gold["counts"], gold["cohorts"], gold["release"]
    return {
        "fields": FIELDS,
        "feeds": list(FEEDS),
        "contracts": {feed: _contract(feed) for feed in FEEDS},
        "model": {"facts": _model(), "forbidden": list(FORBIDDEN)},
        "note": {"facts": _note(drop, counts, cohorts, release), "forbidden": list(FORBIDDEN)},
    }


def _contract(feed: str) -> list[dict]:
    shared = [{"id": "fails-loudly", "tokens": ["silent"]}]
    extra = {
        "registry_file": [
            {"id": "rename", "tokens": ["REGISTERED_SITE", "HOME_CLINIC"]},
            {"id": "added", "tokens": ["DISTRICT_CODE", "FLAG_DATE", "SCHEMA_VERSION"]},
            {"id": "dob", "tokens": ["ISO"]},
            {"id": "reissue", "tokens": ["reissued"]},
        ],
        "registry_api": [
            {"id": "keeps", "tokens": ["home_clinic"]},
            {"id": "version", "tokens": ["Accept-Version"]},
            {"id": "missing", "tokens": ["DISTRICT_CODE"]},
            {"id": "old", "tokens": ["reissued"]},
        ],
        "pacs": [{"id": "mrn", "tokens": ["MRN"]}, {"id": "split", "tokens": ["split"]}, {"id": "merge", "tokens": ["merge"]}],
        "shared_folder": [{"id": "decoy", "tokens": ["decoy"]}, {"id": "name", "tokens": ["FILE_NAME"]}],
        "grader": [{"id": "pid", "tokens": ["LOCAL_PID"]}, {"id": "signed", "tokens": ["signed"]}],
        "ophthalmology": [{"id": "seen", "tokens": ["seen"]}, {"id": "blank", "tokens": ["blank"]}, {"id": "pid", "tokens": ["local_pid"]}],
        "epr_letters": [{"id": "seen", "tokens": ["seen"]}, {"id": "mrn", "tokens": ["MRN"]}],
        "lab": [{"id": "pid", "tokens": ["lab_pid"]}, {"id": "units", "tokens": ["mmol/mol"]}],
        "booking": [{"id": "history", "tokens": ["last state"]}, {"id": "key", "tokens": ["booking_id"]}],
        "sms": [{"id": "duplicate", "tokens": ["duplicate"]}, {"id": "order", "tokens": ["order"]}, {"id": "key", "tokens": ["booking_id"]}],
        "vendor_retrospective": [{"id": "ref", "tokens": ["capture_ref"]}, {"id": "file", "tokens": ["file_name"]}],
    }
    return extra[feed] + shared


def _model() -> list[dict]:
    return [
        {"id": "person", "tokens": ["person"]},
        {"id": "bridge", "tokens": ["identifier", "valid"]},
        {"id": "schema", "tokens": ["schema"]},
        {"id": "seen", "tokens": ["seen"]},
        {"id": "rule", "tokens": ["sop-national-v3"]},
        {"id": "window", "tokens": ["730"]},
        {"id": "deceased", "tokens": ["deceased"]},
        {"id": "zone", "tokens": ["authority"]},
        {"id": "sql", "tokens": ["build.sql"]},
    ]


def _note(drop: dict, counts: dict, cohorts: dict, release: dict) -> list[dict]:
    overdue = cohorts["overdue"]
    return [
        {"id": "rename", "tokens": ["REGISTERED_SITE"]},
        {"id": "reissued", "number": drop["reissued"], "tolerance": 0.0},
        {"id": "eligible", "number": counts["eligible"], "tolerance": counts["eligible_tolerance"]},
        {"id": "coverage", "number": counts["coverage"], "tolerance": counts["coverage_tolerance"]},
        {"id": "bound", "tokens": ["upper bound"]},
        {"id": "blank", "number": overdue["blank_rows"], "tolerance": 0.0},
        {"id": "freeze", "tokens": [release["freeze_start"]]},
        {"id": "release", "tokens": [release["registry_release"]]},
        {"id": "identity", "tokens": ["identity resolution"]},
        {"id": "threshold", "tokens": ["threshold"]},
        {"id": "eligibility", "tokens": ["eligibility"]},
        {"id": "stopped", "tokens": ["pilot", "stopped"]},
    ]
