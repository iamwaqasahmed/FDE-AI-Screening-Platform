"""Reference rules for rel-w3d1.
The participant copies do not import this module.

These functions are the checker's copy of the identity, clinic, label, and spend decisions. They read the rows from the sibling module and return the groups, labels, and purchases a correct submission must match.
"""

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
    """Return the clinic code after the rename, or the original code when the rename does not apply.

    Only one facility, on or after the change, rewrites an endocrinology code. Every other row keeps the code it arrived with.
    """
    # The rename is local to that facility and does not reach back before the change.
    if facility == "h-wadi" and as_of >= CHANGE and code in ENDO:
        return "ENDO-CLN"
    return code


def partition(rows: list[dict]) -> list[list[str]]:
    """Return row ids grouped into one patient each.

    Rows that share a national id are the same person, except a newborn or a twin, who stays separate even when an identifier is shared. A row that names a superseded national id is joined to the row that still carries it. Groups come back sorted, and the ids inside each group are sorted.
    """
    parent = {row["row_id"]: row["row_id"] for row in rows}
    by_national_id: dict[str, str] = {}
    for row in rows:
        # A newborn or a twin is its own patient even when the national id or phone is shared.
        if row["relation"] in {"newborn", "twin"}:
            continue
        national_id = row["national_id"]
        # A blank national id cannot join two rows.
        if not national_id:
            continue
        # The same national id is one person.
        if national_id in by_national_id:
            _union(parent, row["row_id"], by_national_id[national_id])
        else:
            by_national_id[national_id] = row["row_id"]
    for row in rows:
        # No superseded id means there is nothing further to link.
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
    """Return how many distinct patients the rows contain, after the identity rules."""
    return len(partition(rows))


def removals(waitlist: list[dict]) -> list[str]:
    """Return the waitlist ids that leave the list, in sorted order.

    Death discovered late and a patient already seen elsewhere are removals. A bounce and a resubmission stay.
    """
    flags = {"death-late", "seen-elsewhere"}
    return sorted(row["row_id"] for row in waitlist if row["flag"] in flags)


def relabel(row: dict) -> dict:
    """Return the corrected sub-specialty and source for one letter.

    The clerk's own fields are not trusted. The words in the text decide both labels, and the rare sub-specialty is tested before the broader pediatric cue.
    """
    text = row["text"].lower()
    # Retina is tested first so a note that also says pediatric keeps the rare sub-specialty.
    if "retina" in text:
        sub_specialty = RARE
    elif "pediatric" in text:
        sub_specialty = "pediatric"
    else:
        sub_specialty = ""
    # A phone photo is a photo even when the clerk called it a scan.
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
    """Return the small labeled sample the fidelity card describes.

    The rare sub-specialty comes from the card so the sample and the card name the same value.
    """
    rare = card["rare_sub_specialty"]
    return [
        {"source_type": "typed", "specialty": "endo", "sub_specialty": rare, "text": "Kindly review endocrinology."},
        {"source_type": "typed", "specialty": "endo", "sub_specialty": "", "text": "Kindly review the sugar clinic."},
        {"source_type": "photo", "specialty": "ophth", "sub_specialty": rare, "text": "A clinic photo for the eye clinic."},
        {"source_type": "scan", "specialty": "ophth", "sub_specialty": "", "text": "A scanned page for the eye clinic."},
    ]


def features_at(rows: list[dict], invite_on: str) -> dict:
    """Return the district and insurance that were already true on the invite date.

    Later rows are ignored. An empty result means no row had started by that date.
    """
    chosen = None
    for row in rows:
        # Keep the latest row that was already true on the invite date.
        if row["as_of"] <= invite_on and (chosen is None or row["as_of"] > chosen["as_of"]):
            chosen = row
    # No row had started by the invite date.
    if chosen is None:
        return {}
    return {"district": chosen["district"], "insurance": chosen["insurance"]}


def spend(items: list[dict], price: float, budget_sar: float) -> list[str]:
    """Return the item ids bought, most uncertain first, until the next one would pass the budget.

    The price is the same for every item, so the first item that does not fit ends the selection. Ties in uncertainty are broken by item id.
    """
    ordered = sorted(items, key=lambda item: (-item["uncertainty"], item["item_id"]))
    chosen = []
    spent = 0.0
    for item in ordered:
        # The price does not fall later in the list, so there is no point continuing.
        if spent + price > budget_sar:
            break
        chosen.append(item["item_id"])
        spent += price
    return chosen


def fidelity_card() -> dict:
    """Return the ranges and the rare sub-specialty the sample is judged against."""
    return {
        "label_margin": {RARE: [0.3, 0.7]},
        "phrase": {"kindly": [0.2, 0.6]},
        "rare_sub_specialty": RARE,
        "sample_size": [4, 8],
        "specialty_mix": {"endo": [0.4, 0.6], "ophth": [0.4, 0.6]},
    }


def _find(parent: dict[str, str], item: str) -> str:
    """Return the representative of this row, and compress the path on the way."""
    while parent[item] != item:
        parent[item] = parent[parent[item]]
        item = parent[item]
    return item


def _union(parent: dict[str, str], left: str, right: str) -> None:
    """Join the two rows into one patient by attaching one representative to the other."""
    parent[_find(parent, left)] = _find(parent, right)
