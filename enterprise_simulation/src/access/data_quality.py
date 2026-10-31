"""Synthetic quality problems. Each payload states a business consequence."""

from __future__ import annotations

PHONE_0172 = "604-555-0172"
HOUSEHOLD_0172 = "hh-dq-0172"
POSTAL_EXAMPLE = "V6B 2W9"
ZIP_IN_POSTAL = "98101"
CALLBACK_NUMBER = "604-555-0166"


def commands() -> list[dict]:
    """Return append-only quality commands in time order."""
    return [
        *_shared_phone(),
        *_currency_rows(),
        *_kept_correction(),
        *_postal_rows(),
        *_empty_phone(),
        *_evening_file(),
    ]


def _shared_phone() -> list[dict]:
    """Two person ids, one phone, spouse on one row and patient on the other."""
    return [
        _command(
            "cmd-dq-0172-spouse",
            "channel",
            "RequestAccepted",
            "2025-06-18T16:05:00Z",
            "dq-0172-a",
            1,
            {
                "ref": "dq-0172-a",
                "person_id": "p-dq-6101",
                "phone": PHONE_0172,
                "household": HOUSEHOLD_0172,
                "relation": "spouse",
                "mrn": "MRN-610141",
                "handset_delivered": False,
                "channel": "phone",
                "desk_region": "BC",
                "utterance": "calling as the spouse",
                "consequence": (
                    "A dial of 604-555-0172 matches p-dq-6101 and p-dq-6102. "
                    "This row labels p-dq-6101 a spouse, so a consent read from "
                    "this chart is addressed to a spouse."
                ),
            },
        ),
        _command(
            "cmd-dq-0172-patient",
            "channel",
            "RequestAccepted",
            "2025-06-18T16:40:00Z",
            "dq-0172-b",
            1,
            {
                "ref": "dq-0172-b",
                "person_id": "p-dq-6102",
                "phone": PHONE_0172,
                "household": HOUSEHOLD_0172,
                "relation": "patient",
                "mrn": "MRN-610242",
                "handset_delivered": False,
                "channel": "phone",
                "desk_region": "BC",
                "utterance": "calling as the patient",
                "consequence": (
                    "A dial of 604-555-0172 matches p-dq-6102 and p-dq-6101. "
                    "This row labels p-dq-6102 the patient, so the same number "
                    "is on file as both spouse and patient."
                ),
            },
        ),
    ]


def _currency_rows() -> list[dict]:
    """BC member priced in USD, then a later CAD row on a new revision."""
    window = {
        "effective_from": "2025-09-07T00:00:00Z",
        "effective_to": "2025-12-06T00:00:00Z",
    }
    return [
        _command(
            "cmd-dq-8840-accept",
            "hospital",
            "ReferralAccepted",
            "2025-09-04T15:20:00Z",
            "dq-8840",
            1,
            {
                "ref": "dq-8840",
                "person_id": "p-dq-8840",
                "site": "fraser-burnaby",
                "state": "BC",
                "mrn": "MRN-884021",
                "consequence": (
                    "Fraser Burnaby accepted a BC referral. The price is not "
                    "on this row; the payer rows are what a bill will quote."
                ),
            },
        ),
        _command(
            "cmd-dq-8840-usd",
            "payer",
            "CoverageDecided",
            "2025-09-04T17:05:00Z",
            "dq-8840",
            1,
            {
                "ref": "dq-8840",
                "answer": "yes",
                "currency": "USD",
                "member_region": "BC",
                **window,
                "consequence": (
                    "Harbor prices this BC member in USD. A copay taken from "
                    "this row will not match a Canadian-dollar document for dq-8840."
                ),
            },
        ),
        _command(
            "cmd-dq-8840-cad",
            "payer",
            "CoverageDecided",
            "2025-09-09T14:40:00Z",
            "dq-8840",
            2,
            {
                "ref": "dq-8840",
                "answer": "yes",
                "currency": "CAD",
                "member_region": "BC",
                **window,
                "consequence": (
                    "This row was appended at stream_rev 2 and prices dq-8840 in CAD. "
                    "The USD coverage row is still on the stream at revision 1, so a "
                    "first-row reader still quotes US dollars."
                ),
            },
        ),
    ]


def _kept_correction() -> list[dict]:
    """ReferralCorrected is appended. ReferralAccepted stays in the list."""
    return [
        _command(
            "cmd-dq-2204-accept",
            "hospital",
            "ReferralAccepted",
            "2025-11-20T18:12:00Z",
            "dq-2204",
            1,
            {
                "ref": "dq-2204",
                "person_id": "p-dq-2204",
                "site": "fraser-burnaby",
                "state": "BC",
                "mrn": "MRN-220418",
                "consequence": (
                    "The hospital accepted dq-2204 at Fraser Burnaby. A reader "
                    "that stops on this row directs the patient to that BC site."
                ),
            },
        ),
        _command(
            "cmd-dq-2204-correct",
            "hospital",
            "ReferralCorrected",
            "2025-11-21T16:48:00Z",
            "dq-2204",
            2,
            {
                "ref": "dq-2204",
                "person_id": "p-dq-2204",
                "site": "cedar-ridge",
                "state": "WA",
                "mrn": "MRN-220418",
                "prior_site": "fraser-burnaby",
                "prior_state": "BC",
                "consequence": (
                    "This correction was appended and names Cedar Ridge in Washington. "
                    "The Fraser Burnaby ReferralAccepted row remains in the log, so "
                    "instructions can name both sites."
                ),
            },
        ),
    ]


def _postal_rows() -> list[dict]:
    """A ZIP sits in the BC postal field. A later note says the clerk rejected it."""
    return [
        _command(
            "cmd-dq-post-address",
            "hospital",
            "AddressRecorded",
            "2026-02-11T19:06:00Z",
            "dq-post",
            1,
            {
                "ref": "dq-post",
                "person_id": "p-dq-7730",
                "mrn": "MRN-773014",
                "site": "fraser-burnaby",
                "region": "BC",
                "city": "Vancouver",
                "line1": "18 Northline Way",
                "bc_postal": ZIP_IN_POSTAL,
                "bc_postal_example": POSTAL_EXAMPLE,
                "consequence": (
                    "The BC postal field holds ZIP 98101, so a carrier sorts this "
                    "Vancouver packet toward Seattle. A BC postal code has the shape "
                    "of V6B 2W9, and the referral letter would leave British Columbia."
                ),
            },
        ),
        _command(
            "cmd-dq-post-note",
            "hospital",
            "ClerkNote",
            "2026-02-11T20:22:00Z",
            "dq-post",
            2,
            {
                "ref": "dq-post",
                "clerk_action": "rejected",
                "packet": "held",
                "bc_postal": ZIP_IN_POSTAL,
                "bc_postal_example": POSTAL_EXAMPLE,
                "note": (
                    "Registration rejected this address before the letter went out. "
                    "The postal field contains 98101. A BC postal code has the shape "
                    "of V6B 2W9."
                ),
                "consequence": (
                    "The clerk rejected the address and held the letter. The address "
                    "row at revision 1 still stores 98101, and this note was added beside it."
                ),
            },
        ),
    ]


def _empty_phone() -> list[dict]:
    """An empty phone on the request, then a callback number on a later event."""
    return [
        _command(
            "cmd-dq-4408-request",
            "channel",
            "RequestAccepted",
            "2026-04-02T17:14:00Z",
            "dq-4408",
            1,
            {
                "ref": "dq-4408",
                "person_id": "p-dq-4408",
                "phone": "",
                "mrn": "MRN-440811",
                "handset_delivered": False,
                "channel": "web",
                "desk_region": "BC",
                "utterance": "please have the desk call me",
                "consequence": (
                    "The request stored an empty phone string, so the desk has no "
                    "number to dial and a text cannot be sent from this row."
                ),
            },
        ),
        _command(
            "cmd-dq-4408-callback",
            "channel",
            "CallbackRecorded",
            "2026-04-03T15:02:00Z",
            "dq-4408",
            2,
            {
                "ref": "dq-4408",
                "person_id": "p-dq-4408",
                "callback_number": CALLBACK_NUMBER,
                "channel": "phone",
                "consequence": (
                    "Callback number 604-555-0166 arrived on a later channel event. "
                    "The request still has an empty phone, and this event leaves that row as it was."
                ),
            },
        ),
    ]


def _evening_file() -> list[dict]:
    """booking_date is the UTC date. The clinic evening is the previous local day."""
    return [
        _command(
            "cmd-dq-6612-file",
            "hospital",
            "SlotFiled",
            "2026-06-13T21:00:00Z",
            "dq-6612",
            1,
            {
                "ref": "dq-6612",
                "site": "cedar-ridge",
                "file_id": "cedar-2026-06-13-dq6612",
                "clinic": "ENDO-CLN",
                "booking_date": "2026-06-13",
                "clinic_local": "2026-06-12T21:40:00-07:00",
                "zone": "America/Los_Angeles",
                "state": "WA",
                "consequence": (
                    "The file's booking_date is Saturday 2026-06-13, the UTC date of "
                    "a Friday 21:40 visit in America/Los_Angeles. A wait figure that "
                    "reads booking_date alone counts that Friday evening clinic on "
                    "Saturday, outside the Monday-Friday office week."
                ),
            },
        )
    ]


def _command(
    command_id: str,
    authority: str,
    event_type: str,
    occurred_at: str,
    stream_id: str,
    stream_rev: int,
    payload: dict,
) -> dict:
    return {
        "command_id": command_id,
        "authority": authority,
        "type": event_type,
        "occurred_at": occurred_at,
        "stream_id": stream_id,
        "stream_rev": stream_rev,
        "payload": payload,
    }
