"""Tag the gold intent. An emergency phrase wins over a status question."""

from __future__ import annotations

_EMERGENCY = ("chest pain", "cannot wait", "person now")


def classify(row: dict) -> str:
    text = row["text"].lower()
    if any(phrase in text for phrase in _EMERGENCY):
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
