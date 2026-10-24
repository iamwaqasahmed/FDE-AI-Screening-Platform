"""Dev slices for rel-w3d2. Held-out rows stay in gold."""

from __future__ import annotations

DEV_LETTERS = (
    ("dev-letter-1", "Phone photo from the retina service."),
    ("dev-letter-2", "A scanned page for pediatric endocrinology."),
    ("dev-letter-3", "Kindly review the sugar clinic."),
    ("dev-letter-4", "A clinic photo for the eye clinic."),
)

HELD_LETTERS = (
    ("held-letter-1", "Phone photo from the retina service for a new visit."),
    ("held-letter-2", "A scanned pediatric referral."),
    ("held-letter-3", "Kindly review endocrinology."),
    ("held-letter-4", "A phone photo of the eye clinic page."),
    ("held-letter-5", "A scanned page for the retina service."),
    ("held-letter-6", "Pediatric follow up at the sugar clinic."),
)

DEV_MESSAGES = (
    ("dev-message-1", "What is the status of my referral?", "status"),
    ("dev-message-2", "Where is my referral? I have chest pain and I need a slot.", "emergency"),
    ("dev-message-3", "I want to book a morning slot.", "book"),
    ("dev-message-4", "Cancel this visit.", "cancel"),
    ("dev-message-5", "What documents do I bring?", "info"),
    ("dev-message-6", "Can I reschedule to Sunday?", "reschedule"),
)

HELD_MESSAGES = (
    ("held-message-1", "Please send the status.", "status"),
    ("held-message-2", "I need a person now, this cannot wait.", "emergency"),
    ("held-message-3", "I want to book a morning slot tomorrow.", "book"),
    ("held-message-4", "Cancel this visit please.", "cancel"),
    ("held-message-5", "What documents do I bring to the clinic?", "info"),
    ("held-message-6", "Can I reschedule to Sunday afternoon?", "reschedule"),
    ("held-message-7", "The clinic was closed when I arrived.", "complaint"),
    ("held-message-8", "Thank you.", "other"),
)

HOURS = (
    ("hours-1", "What are the clinic hours?"),
    ("hours-2", "When does the eye clinic open?"),
    ("hours-3", "Is the clinic open on Sunday?"),
)

DOMAIN = (
    "PHC notes say sugar clinic when they mean endocrinology.",
    "The shorthand glossary sits beside the letter, not in a coded field.",
    "A coordinator expands the shorthand before the letter is filed.",
)

DEV_PREFS = (
    ("See crit-endo-v3 at the sugar clinic on Friday.", "See crit-endo-v3 at the endocrinology"),
)

HELD_PREF = ("Book crit-ophth-v3 at the sugar clinic on 2027-03-10.", "Book crit-ophth-v3 at the endocrinology")


def letters(rows: tuple[tuple[str, str], ...]) -> list[dict]:
    return [{"item_id": item_id, "text": text} for item_id, text in rows]


def messages(rows: tuple[tuple[str, str, str], ...]) -> list[dict]:
    return [{"intent": intent, "message_id": item_id, "text": text} for item_id, text, intent in rows]


def hours() -> list[dict]:
    return [{"question_id": item_id, "text": text} for item_id, text in HOURS]


def domain() -> list[dict]:
    return [{"text": text} for text in DOMAIN]


def dev_prefs() -> list[dict]:
    return [{"draft": draft, "edited": edited} for draft, edited in DEV_PREFS]
