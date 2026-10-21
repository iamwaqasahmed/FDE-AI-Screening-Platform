"""Key facts for the vendor-extract contract, the retrieval card, and the evidence note."""

from __future__ import annotations

FIELDS = [
    "feed", "system", "zone", "grain", "keys", "columns", "dates", "known_defects", "owner", "consumers",
    "fails_when", "allowed_sites", "banned_fields", "crosses_to",
]
FORBIDDEN = [
    "The claimed sensitivity holds for every patient.",
    "The routine grade is the ground truth.",
    "A random split is an honest split.",
    "The pilot may start.",
    "Dates of birth may leave the authority zone.",
    "ClearSight was deployed successfully.",
    "M06 may read patient letters.",
]
CARD_FORBIDDEN = [
    "The register status is the status in force.",
    "A forwarded copy is the record to cite.",
    "M06 may read patient letters.",
]


def facts(items: dict, baselines: dict) -> dict:
    drop, scope = items["drop_restriction"], items["vendor_scope"]
    dna, overdue = items["dna_leak"], items["overdue_pilot_scope"]
    return {
        "fields": list(FIELDS),
        "contract": _contract(drop),
        "card": {"facts": _card(items, baselines), "forbidden": list(CARD_FORBIDDEN)},
        "note": {"facts": _note(drop, scope, items, dna, overdue), "forbidden": list(FORBIDDEN)},
    }


def _contract(drop: dict) -> list[dict]:
    return [
        {"id": "silent", "tokens": ["silent"]},
        {"id": "dob", "tokens": [drop["banned_field"]]},
        {"id": "year", "tokens": [drop["replacement_field"]]},
        {"id": "sites", "tokens": list(drop["allowed_sites"])},
        {"id": "ref", "tokens": ["capture_ref"]},
        {"id": "person", "tokens": ["person_key"]},
        {"id": "file", "tokens": ["file name"]},
    ]


def _card(items: dict, baselines: dict) -> list[dict]:
    originals, duplicates = items["originals"], items["near_duplicates"]
    return [
        {"id": "keyword", "tokens": ["keyword"]},
        {"id": "tfidf", "tokens": ["tf-idf"]},
        {"id": "keyword-rate", "number": _percent(baselines["keyword"]["overall"]), "tolerance": 0.0},
        {"id": "tfidf-rate", "number": _percent(baselines["tfidf"]["overall"]), "tolerance": 0.0},
        {"id": "draft", "tokens": ["draft"]},
        {"id": "status", "tokens": ["status", "effective"]},
        {"id": "forwarded", "tokens": ["forwarded"]},
        {"id": "table", "tokens": ["table"]},
        {"id": "pdf", "number": originals["pdf"], "tolerance": 0.0},
        {"id": "forwards", "number": duplicates["count"], "tolerance": 0.0},
    ]


def _note(drop: dict, scope: dict, items: dict, dna: dict, overdue: dict) -> list[dict]:
    return [
        {"id": "effective", "tokens": [drop["effective"]]},
        {"id": "removed", "tokens": list(drop["removed_sites"]) or ["none"]},
        {"id": "captures", "number": scope["captures"], "tolerance": 0.0},
        {"id": "adjudicated", "number": scope["adjudicated"], "tolerance": 0.0},
        {"id": "claim", "tokens": ["0.95", "adjudicated"]},
        {"id": "dob", "tokens": ["DOB", "YEAR_OF_BIRTH"]},
        {"id": "leak", "tokens": [dna["leaky_feature"]]},
        {"id": "honest", "tokens": ["honest", f"{dna['honest_auc']:.2f}"]},
        {"id": "random", "tokens": ["random", f"{dna['random_auc']:.2f}"]},
        {"id": "stopped", "tokens": ["pilot", "stopped"]},
        {"id": "owner", "tokens": ["safety owner"]},
        {"id": "region", "tokens": ["EU"]},
        {"id": "filename", "tokens": ["file name"]},
        {"id": "bound-words", "tokens": ["upper bound"]},
        {"id": "bound", "number": overdue["upper_bound"], "tolerance": 0.02},
    ]


def _percent(rate: float) -> int:
    return int(round(rate * 100))
