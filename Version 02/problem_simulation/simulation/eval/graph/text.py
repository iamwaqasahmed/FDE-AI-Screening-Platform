"""Key facts for the bureau contract, the graph card, and the incident note."""

from __future__ import annotations

FIELDS = [
    "feed", "system", "zone", "grain", "keys", "columns", "dates", "known_defects", "owner", "consumers",
    "fails_when", "business_key", "reconciles_against", "retention_days", "crosses_to",
]
FORBIDDEN = [
    "No letters were lost.",
    "The dispatch file is complete.",
    "The chase list is the overdue cohort.",
    "The pilot may start.",
    "Dates of birth may leave the authority zone.",
    "Every lost letter should be re-sent.",
    "M06 may read the lost-letter names.",
]
CARD_FORBIDDEN = [
    "A dispatch id is the letter.",
    "The bureau notice is the record.",
    "M06 may read patient letters.",
]


def facts(items: dict, baselines: dict) -> dict:
    return {
        "fields": list(FIELDS),
        "contract": _contract(items),
        "card": {"facts": _card(items, baselines), "forbidden": list(CARD_FORBIDDEN)},
        "note": {"facts": _note(items), "forbidden": list(FORBIDDEN)},
    }


def _contract(items: dict) -> list[dict]:
    agreement = items["bureau_agreement"]
    return [
        {"id": "key", "tokens": ["request_id"]},
        {"id": "grain", "tokens": ["dispatch"]},
        {"id": "retention", "tokens": [str(agreement["retention_days"])]},
        {"id": "dob", "tokens": ["DOB"]},
        {"id": "zone", "tokens": [agreement["zone"]]},
        {"id": "silent", "tokens": ["silent"]},
        {"id": "against", "tokens": ["request"]},
    ]


def _card(items: dict, baselines: dict) -> list[dict]:
    drop = items["drop_incident"]
    return [
        {"id": "keyword", "tokens": ["keyword"]},
        {"id": "tfidf", "tokens": ["tf-idf"]},
        {"id": "keyword-rate", "number": _percent(baselines["keyword"]["overall"]), "tolerance": 0.0},
        {"id": "tfidf-rate", "number": _percent(baselines["tfidf"]["overall"]), "tolerance": 0.0},
        {"id": "key", "tokens": ["request_id"]},
        {"id": "draft", "tokens": ["draft"]},
        {"id": "path", "tokens": ["path"]},
        {"id": "lost", "number": drop["lost"], "tolerance": 0.0},
        {"id": "duplicates", "number": drop["duplicate_rows"], "tolerance": 0.0},
        {"id": "specialist", "tokens": ["specialist"]},
    ]


def _note(items: dict) -> list[dict]:
    drop, lost, resend = items["drop_incident"], items["chase_lost_people"], items["resend_summary"]
    window, cost = items["resend_window"], items["incident_cost"]
    return [
        {"id": "start", "tokens": [drop["window"][0]]},
        {"id": "end", "tokens": [drop["window"][1]]},
        {"id": "lost", "number": drop["lost"], "tolerance": 0.0},
        {"id": "duplicates", "number": drop["duplicate_rows"], "tolerance": 0.0},
        {"id": "people-lost", "number": lost["local_ids"], "tolerance": 0.0},
        {"id": "people", "number": lost["people"], "tolerance": 0.03},
        {"id": "bound", "tokens": ["upper bound"]},
        {"id": "deceased", "tokens": ["deceased"]},
        {"id": "precedent", "tokens": ["INC-0233"]},
        {"id": "resend", "number": resend["resend"], "tolerance": 0.0},
        {"id": "window", "tokens": [window["next_window"]]},
        {"id": "cost", "number": int(round(cost["total_gbp"])), "tolerance": 0.0},
        {"id": "owner", "tokens": ["safety owner"]},
        {"id": "dob", "tokens": ["DOB"]},
        {"id": "bureau", "tokens": ["bureau"]},
    ]


def _percent(rate: float) -> int:
    return int(round(rate * 100))
