"""Patient messages. The intent stays out of the participant file."""

from __future__ import annotations

BASE: tuple[tuple[str, str, str], ...] = (
    ("m01", "What is the status of my referral?", "status"),
    ("m02", "Please send the status.", "status"),
    ("m03", "I need a status before Thursday.", "status"),
    ("m04", "Status update on the booking.", "status"),
    ("m05", "Where is my referral?", "status"),
    ("m06", "Has the hospital received the letter?", "status"),
    ("m07", "Any news on the appointment request?", "status"),
    ("m08", "I want to book a morning slot.", "book"),
    ("m09", "Can I reschedule to Sunday?", "reschedule"),
    ("m10", "Cancel this visit.", "cancel"),
    ("m11", "What documents do I bring?", "info"),
    ("m12", "What are the clinic hours?", "info"),
    ("m13", "The clinic was closed when I arrived.", "complaint"),
    ("m14", "I need a person now, this cannot wait.", "emergency"),
    ("m15", "Thank you.", "other"),
)


def message_rows(seed: int) -> list[dict[str, str]]:
    extra = ("m16", "What is the status of my file?", "status")
    if seed % 2:
        extra = ("m16", "Where did my referral go?", "status")
    rows = []
    for message_id, text, intent in (*BASE, extra):
        rows.append({"message_id": message_id, "text": text, "intent": intent})
    return rows
