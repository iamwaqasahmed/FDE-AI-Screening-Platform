"""Reference adapter for rel-w3d2. Participant copies do not import this module."""

from __future__ import annotations

from alwaha.engagement.w3d1_rules import relabel

EMERGENCY = ("chest pain", "cannot wait", "person now")
HOLIDAY = "2027-03-10"
QLORA_RANK = 32
RANK_PER_GPU = 32


def extract(row: dict) -> dict:
    labeled = relabel(row)
    return {
        "item_id": row["item_id"],
        "source_type": labeled["source_type"],
        "sub_specialty": labeled["sub_specialty"],
    }


def classify(row: dict) -> str:
    text = row["text"].lower()
    if any(phrase in text for phrase in EMERGENCY):
        return "emergency"
    if "reschedule" in text:
        return "reschedule"
    if "cancel" in text:
        return "cancel"
    if "book" in text:
        return "book"
    if "document" in text or "bring" in text:
        return "info"
    if "closed" in text or "complaint" in text:
        return "complaint"
    if "status" in text or "referral" in text:
        return "status"
    return "other"


def extraction_f1(rows: list[dict], predictions: list[dict]) -> float:
    pairs = []
    for row, pred in zip(rows, predictions):
        pairs.append((row["source_type"], pred.get("source_type", "")))
        pairs.append((row["sub_specialty"], pred.get("sub_specialty", "")))
    return _ratio(pairs)


def intent_f1(rows: list[dict], predictions: list[str]) -> float:
    pairs = [(row["intent"], pred) for row, pred in zip(rows, predictions)]
    return _ratio(pairs)


def format_f1(value: float) -> str:
    return f"{value:.4f}"


def qlora(rank: int, gpus: int) -> dict:
    need = max(1, (rank + RANK_PER_GPU - 1) // RANK_PER_GPU)
    return {"gpus": min(need, gpus), "method": "qlora", "rank": rank}


def keep_domain(rows: list[dict]) -> list[dict]:
    return [row for row in rows if "item_id" not in row]


def revise(draft: str) -> str:
    text = draft.replace("sugar clinic", "endocrinology").replace("Friday", " ").replace(HOLIDAY, " ")
    return " ".join(word for word in text.split() if word not in {"on", "."})


def _ratio(pairs: list[tuple[str, str]]) -> float:
    if not pairs:
        return 0.0
    return sum(left == right for left, right in pairs) / len(pairs)
