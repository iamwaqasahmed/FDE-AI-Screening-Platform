"""Judge items for rel-w3d4. The held-out item stays out of the pack."""

from __future__ import annotations

HELD_DOC = "held-doc"
HELD_SPAN = "held-span-9"
FLUENT_WRONG = "cal-fluent-wrong"


def subset() -> list[dict]:
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
    return subset() + held()
