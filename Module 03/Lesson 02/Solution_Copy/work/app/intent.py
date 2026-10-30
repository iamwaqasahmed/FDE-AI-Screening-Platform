"""Tag the gold intent. An emergency phrase wins over a status question.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell calls every message a status question. While that shell
is the file that runs, the model check says intent F1 is outside
the budget. The check does not print an F1 or a gold label.
"""

from __future__ import annotations

# An emergency phrase is checked before status, referral, or book.
_EMERGENCY = ("chest pain", "cannot wait", "person now")


def classify(row: dict) -> str:
    """Return one intent for the message text.

    row carries text. The first matching rule wins. An emergency
    phrase wins even when the same sentence also asks for status
    or a slot. A message that matches nothing is other.
    """
    text = row["text"].lower()
    if any(phrase in text for phrase in _EMERGENCY):
        return "emergency"
    # Later rules are ordinary requests. Order is the priority.
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
