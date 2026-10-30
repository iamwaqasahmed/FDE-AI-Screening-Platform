"""Reference adapter for rel-m03-l02.
Participant copies do not import this module.

extract and classify are the reference behaviors the scores compare against. The score helpers return a match ratio. qlora turns a rank into a GPU request that cannot exceed the quota. revise shows the preference edit the domain notes imply.
"""

from __future__ import annotations

from alwaha.engagement.m03_l01_rules import relabel

EMERGENCY = ("chest pain", "cannot wait", "person now")
HOLIDAY = "2027-03-10"
QLORA_RANK = 32
RANK_PER_GPU = 32


def extract(row: dict) -> dict:
    """Return the source and sub-specialty the letter rules assign, plus the item id.

    The earlier relabel decides the fields. This function keeps only the ones this day scores.
    """
    labeled = relabel(row)
    return {
        "item_id": row["item_id"],
        "source_type": labeled["source_type"],
        "sub_specialty": labeled["sub_specialty"],
    }


def classify(row: dict) -> str:
    """Return the intent of one message.

    The tests run from the most specific cue to the broadest. A message that also mentions a referral is not a status ask when an earlier cue already matched. Anything left is other.
    """
    text = row["text"].lower()
    # An emergency cue wins even when the message also asks to book or asks for a status.
    if any(phrase in text for phrase in EMERGENCY):
        return "emergency"
    if "reschedule" in text:
        return "reschedule"
    # Cancel is tested before book so a cancellation is not read as a booking.
    if "cancel" in text:
        return "cancel"
    if "book" in text:
        return "book"
    if "document" in text or "bring" in text:
        return "info"
    if "closed" in text or "complaint" in text:
        return "complaint"
    # Status is broad because it matches the word referral, so it stays after the narrower intents.
    if "status" in text or "referral" in text:
        return "status"
    return "other"


def extraction_f1(rows: list[dict], predictions: list[dict]) -> float:
    """Return the share of source and sub-specialty fields that match, walking the rows in order.

    The steps walk the rows in order, pair each predicted source and sub-specialty with the row's values, and return the share of pairs that match.
    """
    pairs = []
    for row, pred in zip(rows, predictions):
        pairs.append((row["source_type"], pred.get("source_type", "")))
        pairs.append((row["sub_specialty"], pred.get("sub_specialty", "")))
    return _ratio(pairs)


def intent_f1(rows: list[dict], predictions: list[str]) -> float:
    """Return the share of intents that match, walking the rows in order."""
    pairs = [(row["intent"], pred) for row, pred in zip(rows, predictions)]
    return _ratio(pairs)


def format_f1(value: float) -> str:
    """Return the score as text with a fixed number of decimal places, so a table can show it."""
    return f"{value:.4f}"


def qlora(rank: int, gpus: int) -> dict:
    """Return the adapter request: the method, the rank, and how many GPUs it may use.

    The rank needs at least one GPU. The request is then capped by the quota so it never asks for more than the release allows.
    """
    need = max(1, (rank + RANK_PER_GPU - 1) // RANK_PER_GPU)
    # The quota wins when the rank would ask for more GPUs than the release has.
    return {"gpus": min(need, gpus), "method": "qlora", "rank": rank}


def keep_domain(rows: list[dict]) -> list[dict]:
    """Return only the domain notes.

    Letters carry an item id. Domain notes do not, so this drops the letters.
    """
    return [row for row in rows if "item_id" not in row]


def revise(draft: str) -> str:
    """Return the draft with the shorthand expanded and the day words removed.

    The clinic nickname becomes the specialty name. The weekday and the holiday are blanked, then the leftover filler words are dropped.
    """
    text = draft.replace("sugar clinic", "endocrinology").replace("Friday", " ").replace(HOLIDAY, " ")
    return " ".join(word for word in text.split() if word not in {"on", "."})


def _ratio(pairs: list[tuple[str, str]]) -> float:
    """Return the share of pairs that match. No pairs scores as nothing, so an empty comparison does not divide by zero."""
    # Nothing to score.
    if not pairs:
        return 0.0
    return sum(left == right for left, right in pairs) / len(pairs)
