"""Patient messages. The intent stays out of the participant file.

BASE is the fixed message list, each row an id, a text, and an intent. One extra row is appended. An odd seed replaces that extra text with the other sentence. Both extras are labeled status, but only one of the two sentences contains the word the keyword baseline counts.
"""

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
    """Return the message rows, including the seed-dependent extra status row."""
    extra = ("m16", "What is the status of my file?", "status")
    if seed % 2:
        # Odd seeds use the other sentence. The intent label is still status.
        extra = ("m16", "Where did my referral go?", "status")
    rows = []
    for message_id, text, intent in (*BASE, extra):
        rows.append({"message_id": message_id, "text": text, "intent": intent})
    return rows
