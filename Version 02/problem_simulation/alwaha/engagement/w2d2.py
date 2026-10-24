"""rel-w2d2 fixtures. The extra field and the dropped field stay in the gold."""

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
    return 10 + (seed % 9)


def webhook(profile: Profile) -> dict:
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
    happy = _cancel("evt-can-1", "bkg-1", "2027-01-18T10:00:00", "happy")
    replay = dict(happy)
    replay["scenario"] = "replay"
    rejected = _cancel("evt-can-2", "bkg-2", "2027-01-18T11:00:00", "compensate")
    return [happy, replay, rejected]


def left_event() -> dict:
    return _cancel("evt-can-3", "bkg-3", "2027-01-18T12:00:00", "left", slot=False)


def faults() -> dict:
    return {"bkg-2": "reject"}


def hl7_rows() -> list[dict]:
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
    return f"person_key,{WAIT},{CLOCK}\npt-200,{wait_days(profile.seed)},2026-06-01\n"


def gold(profile: Profile) -> dict:
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
