"""Judge items for rel-w3d4.
The held-out item stays out of the pack.

subset is the calibration the pack can show: a fluent answer that fails, a terse answer that passes, and a fluent answer that passes. held is the item only the checker sees. full_set is both, in that order.
"""

from __future__ import annotations

HELD_DOC = "held-doc"
HELD_SPAN = "held-span-9"
FLUENT_WRONG = "cal-fluent-wrong"


def subset() -> list[dict]:
    """Return the calibration items the pack can show.

    One is fluent and wrong, one is terse and right, and one is fluent and right, so fluency and correctness are not the same thing.
    """
    return [
        {
            "answer": "The clinic is open every night and the citation reads as settled.",
            "fluent": True,
            "item_id": FLUENT_WRONG,
            "pass": False,
        },
        {"answer": "In force.", "fluent": False, "item_id": "cal-terse-right", "pass": True},
        {
            "answer": "The in-force document is the cluster circular, and the hours match that document.",
            "fluent": True,
            "item_id": "cal-fluent-right",
            "pass": True,
        },
    ]


def held() -> list[dict]:
    """Return the held-out judge item. It is fluent, it fails, and it names a document the pack does not include."""
    return [
        {
            "answer": f"Held night hours cite {HELD_SPAN} on {HELD_DOC}.",
            "doc_id": HELD_DOC,
            "fluent": True,
            "item_id": "cal-held-wrong",
            "pass": False,
            "span": HELD_SPAN,
        }
    ]


def full_set() -> list[dict]:
    """Return the pack items followed by the held-out item."""
    return subset() + held()
