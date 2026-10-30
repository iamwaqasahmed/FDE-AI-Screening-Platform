"""The Lesson 3 intake stream. One letter carries the profile canary.

File order is not scenario order. The order pair is written later-sequence first, and those two events get distinct ids after they are built. The replay event is appended a second time with the same id. The watermark is appended only to the letter that is given one.
"""

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
    """Return the referral sentence for a facility, appending the watermark only when one was passed."""
    text = f"Please accept this endocrinology referral to {facility}."
    if canary:
        # The other letters stay free of the watermark.
        return f"{text} {canary}"
    return text


def _event(scenario: str, number: str, when: str, patient: str, facility: str, sequence: int = 1, canary: str = "") -> dict:
    """Return one submitted-referral event. The referral id is the part of number before the first hyphen.

    The steps fill the event id, topic, time, sequence, patient, and scenario, take the referral id from the number, and build the letter for the facility.
    """
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
    """File order. The order pair is not sorted, and one event id is repeated.

    The later order event is placed first. The earlier order event is placed near the end. The replay event is copied onto the end so a consumer sees the same id twice.
    """
    order_later = _event("order", "150", "2027-01-12T09:05:00", "pt-150", WADI, sequence=2)
    order_later["event_id"] = "evt-150-2"
    order_earlier = _event("order", "150", "2027-01-12T09:00:00", "pt-150", AIN, sequence=1)
    order_earlier["event_id"] = "evt-150-1"
    replay = _event("replay", "110", "2027-01-12T09:10:00", "pt-110", WADI)
    # order_later comes before order_earlier. The last item repeats the replay id.
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
    """Return the referral that is already open, used to mark a later event as a duplicate."""
    return [{"patient_key": "pt-160", "specialty_id": "endo", "referral_id": "ref-existing"}]


def faults() -> dict[str, str]:
    """Return the fault name for the referrals that are not a straight intake."""
    return {"ref-170": "compensate", "ref-180": "retry"}


def clinics() -> list[dict[str, str]]:
    """Return the clinic row used when a referral matches this facility and specialty."""
    return [{"facility_id": "h-wadi", "specialty_id": "endo", "clinic": "ENDO-CLN"}]
