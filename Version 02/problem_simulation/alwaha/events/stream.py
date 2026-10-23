"""The Day 3 intake stream. One letter carries the profile canary."""

from __future__ import annotations

WADI = "Wadi Specialist Hospital"
AIN = "Ain Diabetes and Eye Center"
ORDER_REF = "ref-150"

SCENARIO_ORDER = (
    "happy",
    "replay",
    "friday",
    "holiday",
    "ain",
    "order",
    "duplicate",
    "compensation",
    "dead-letter",
)


def letter(facility: str, canary: str = "") -> str:
    text = f"Please accept this endocrinology referral to {facility}."
    if canary:
        return f"{text} {canary}"
    return text


def _event(scenario: str, number: str, when: str, patient: str, facility: str, sequence: int = 1, canary: str = "") -> dict:
    return {
        "event_id": f"evt-{number}",
        "topic": "referral.submitted",
        "occurred_at": when,
        "sequence": sequence,
        "referral_id": f"ref-{number.split('-')[0]}",
        "patient_key": patient,
        "scenario": scenario,
        "letter": letter(facility, canary),
    }


def events(canary: str) -> list[dict]:
    """File order. The order pair is not sorted, and one event id is repeated."""
    order_later = _event("order", "150", "2027-01-12T09:05:00", "pt-150", WADI, sequence=2)
    order_later["event_id"] = "evt-150-2"
    order_earlier = _event("order", "150", "2027-01-12T09:00:00", "pt-150", AIN, sequence=1)
    order_earlier["event_id"] = "evt-150-1"
    replay = _event("replay", "110", "2027-01-12T09:10:00", "pt-110", WADI)
    return [
        order_later,
        _event("happy", "100", "2027-01-12T09:00:00", "pt-100", WADI, canary=canary),
        _event("friday", "120", "2027-01-14T09:00:00", "pt-120", WADI),
        _event("holiday", "130", "2027-03-09T09:00:00", "pt-130", WADI),
        _event("ain", "140", "2027-01-13T09:00:00", "pt-140", AIN),
        replay,
        _event("duplicate", "160", "2027-01-12T11:00:00", "pt-160", WADI),
        _event("compensation", "170", "2027-01-12T12:00:00", "pt-170", WADI),
        _event("dead-letter", "180", "2027-01-12T13:00:00", "pt-180", WADI),
        order_earlier,
        dict(replay),
    ]


def open_referrals() -> list[dict[str, str]]:
    return [{"patient_key": "pt-160", "specialty_id": "endo", "referral_id": "ref-existing"}]


def faults() -> dict[str, str]:
    return {"ref-170": "compensate", "ref-180": "retry"}


def clinics() -> list[dict[str, str]]:
    return [{"facility_id": "h-wadi", "specialty_id": "endo", "clinic": "ENDO-CLN"}]
