"""Reference rules for rel-w3d1. The participant copies do not import this module."""

from __future__ import annotations

CHANGE = "2024-06-01"
ENDO = {"END-01", "ENDO-CLN"}
RARE = "retina"
INVITE_ON = "2026-03-01"
PIT_ROWS = (
    {"as_of": "2026-01-01", "district": "d-rim", "insurance": "class-a"},
    {"as_of": "2026-06-01", "district": "d-wadi", "insurance": "class-b"},
)
SPEND_ITEMS = (
    {"item_id": "low", "uncertainty": 0.1},
    {"item_id": "mid", "uncertainty": 0.5},
    {"item_id": "high", "uncertainty": 0.9},
    {"item_id": "higher", "uncertainty": 0.95},
)


def clinic(code: str, as_of: str, facility: str) -> str:
    if facility == "h-wadi" and as_of >= CHANGE and code in ENDO:
        return "ENDO-CLN"
    return code


def partition(rows: list[dict]) -> list[list[str]]:
    parent = {row["row_id"]: row["row_id"] for row in rows}
    by_national_id: dict[str, str] = {}
    for row in rows:
        if row["relation"] in {"newborn", "twin"}:
            continue
        national_id = row["national_id"]
        if not national_id:
            continue
        if national_id in by_national_id:
            _union(parent, row["row_id"], by_national_id[national_id])
        else:
            by_national_id[national_id] = row["row_id"]
    for row in rows:
        if not row["replaces"]:
            continue
        for other in rows:
            if other["national_id"] == row["replaces"]:
                _union(parent, row["row_id"], other["row_id"])
    groups: dict[str, list[str]] = {}
    for row in rows:
        groups.setdefault(_find(parent, row["row_id"]), []).append(row["row_id"])
    return sorted(sorted(group) for group in groups.values())


def patient_count(rows: list[dict]) -> int:
    return len(partition(rows))


def removals(waitlist: list[dict]) -> list[str]:
    flags = {"death-late", "seen-elsewhere"}
    return sorted(row["row_id"] for row in waitlist if row["flag"] in flags)


def relabel(row: dict) -> dict:
    text = row["text"].lower()
    if "retina" in text:
        sub_specialty = RARE
    elif "pediatric" in text:
        sub_specialty = "pediatric"
    else:
        sub_specialty = ""
    if "phone" in text or "photo" in text:
        source_type = "photo"
    elif "scan" in text:
        source_type = "scan"
    else:
        source_type = "typed"
    return {
        "guideline": "ann-v2",
        "item_id": row["item_id"],
        "source_type": source_type,
        "sub_specialty": sub_specialty,
    }


def sample(card: dict) -> list[dict]:
    rare = card["rare_sub_specialty"]
    return [
        {"source_type": "typed", "specialty": "endo", "sub_specialty": rare, "text": "Kindly review endocrinology."},
        {"source_type": "typed", "specialty": "endo", "sub_specialty": "", "text": "Kindly review the sugar clinic."},
        {"source_type": "photo", "specialty": "ophth", "sub_specialty": rare, "text": "A clinic photo for the eye clinic."},
        {"source_type": "scan", "specialty": "ophth", "sub_specialty": "", "text": "A scanned page for the eye clinic."},
    ]


def features_at(rows: list[dict], invite_on: str) -> dict:
    chosen = None
    for row in rows:
        if row["as_of"] <= invite_on and (chosen is None or row["as_of"] > chosen["as_of"]):
            chosen = row
    if chosen is None:
        return {}
    return {"district": chosen["district"], "insurance": chosen["insurance"]}


def spend(items: list[dict], price: float, budget_sar: float) -> list[str]:
    ordered = sorted(items, key=lambda item: (-item["uncertainty"], item["item_id"]))
    chosen = []
    spent = 0.0
    for item in ordered:
        if spent + price > budget_sar:
            break
        chosen.append(item["item_id"])
        spent += price
    return chosen


def fidelity_card() -> dict:
    return {
        "label_margin": {RARE: [0.3, 0.7]},
        "phrase": {"kindly": [0.2, 0.6]},
        "rare_sub_specialty": RARE,
        "sample_size": [4, 8],
        "specialty_mix": {"endo": [0.4, 0.6], "ophth": [0.4, 0.6]},
    }


def _find(parent: dict[str, str], item: str) -> str:
    while parent[item] != item:
        parent[item] = parent[parent[item]]
        item = parent[item]
    return item


def _union(parent: dict[str, str], left: str, right: str) -> None:
    parent[_find(parent, left)] = _find(parent, right)
