"""rel-w2d2 fixtures.
The extra field and the dropped field stay in the gold.

These builders make the referral webhook, the cancellation cases, the out-of-order messages, and the mart row the checker compares. gold collects the values that must survive in a submission, including the field that arrived extra and the field the mapping drops.
"""

from __future__ import annotations

from alwaha.config.profile import Profile

EXTRA = "priorityHint"
DROPPED = "sub_specialty"
CLOCK = "booking_date"
WAIT = "wait_days"
REFERRAL_FIELDS = (
    "event_id",
    "topic",
    "occurred_at",
    "sequence",
    "referral_id",
    "patient_key",
    "letter",
)


def wait_days(seed: int) -> int:
    """Return the wait for this seed.

    It moves with the seed and stays fixed for a profile, so the mart row and the gold use the same value.
    """
    return 10 + (seed % 9)


def webhook(profile: Profile) -> dict:
    """Return a referral submission, including the field the listed contract does not name.

    The letter is this profile's canary. The extra field is set after the known fields so it is present without being one of them.
    """
    body = {
        "event_id": "evt-ref-200",
        "topic": "referral.submitted",
        "occurred_at": "2027-01-18T09:00:00",
        "sequence": 1,
        "referral_id": "ref-200",
        "patient_key": "pt-200",
        "letter": profile.canary(),
    }
    body[EXTRA] = "soon"
    return body


def _cancel(event_id: str, booking_id: str, when: str, scenario: str, slot: bool = True) -> dict:
    """Return one cancellation.

    The session id is derived from the booking id. The slot flag defaults to present. The left scenario passes it unset because that cancellation does not free a slot.
    """
    return {
        "event_id": event_id,
        "topic": "session.cancelled",
        "occurred_at": when,
        "sequence": 1,
        "booking_id": booking_id,
        "session_id": booking_id.replace("bkg", "ses"),
        "facility_id": "h-wadi",
        "slot": slot,
        "scenario": scenario,
    }


def cancellations() -> list[dict]:
    """Return the happy event, a replay of that same event, and a different event the compensator rejects.

    The replay keeps the happy event's identity and changes only the scenario, so a duplicate is not a new cancellation.
    """
    happy = _cancel("evt-can-1", "bkg-1", "2027-01-18T10:00:00", "happy")
    replay = dict(happy)
    # Same event as the happy path, retagged so a duplicate can be recognized.
    replay["scenario"] = "replay"
    rejected = _cancel("evt-can-2", "bkg-2", "2027-01-18T11:00:00", "compensate")
    return [happy, replay, rejected]


def left_event() -> dict:
    """Return the cancellation that does not carry a slot."""
    # This scenario records no slot, unlike the happy and rejected cancellations.
    return _cancel("evt-can-3", "bkg-3", "2027-01-18T12:00:00", "left", slot=False)


def faults() -> dict:
    """Return the booking the compensator must reject."""
    return {"bkg-2": "reject"}


def hl7_rows() -> list[dict]:
    """Return two schedule messages out of order, then a mapping that drops the sub-specialty.

    The later sequence is listed first, so a handler that trusts arrival order keeps the stale message. The raw row names a sub-specialty the mapped row does not keep.
    """
    return [
        {"kind": "siu", "facility_id": "h-safra", "sequence": 2},
        {"kind": "siu", "facility_id": "h-safra", "sequence": 1},
        {
            "kind": "mapping",
            "facility_id": "h-nakhl",
            "raw": {"SCH": "endo", "ZSS": "thyroid"},
            "mapped": {"facility_id": "h-nakhl", "specialty": "endo"},
        },
    ]


def mart_csv(profile: Profile) -> str:
    """Return a mart extract whose wait comes from this profile's seed."""
    return f"person_key,{WAIT},{CLOCK}\npt-200,{wait_days(profile.seed)},2026-06-01\n"


def gold(profile: Profile) -> dict:
    """Return the values a correct submission for this profile must contain.

    That includes the extra field, the dropped field, the clock column, the seeded wait, and the cancellation that carries no slot.
    """
    return {
        "extra_field": EXTRA,
        "dropped_field": DROPPED,
        "clock": CLOCK,
        "wait_column": WAIT,
        "wait": wait_days(profile.seed),
        "owner": "eref",
        "referral_id": "ref-200",
        "referral_fields": list(REFERRAL_FIELDS),
        "left": left_event(),
        "reject_booking": "bkg-2",
    }
