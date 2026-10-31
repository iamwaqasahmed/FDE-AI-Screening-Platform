"""Fraser Burnaby onboarding, one quotation, and a Saturday file tally.

These rows record what the desk, the hospital, and the payer wrote.
They do not close the packet.
"""

from __future__ import annotations

import hashlib

ONBOARD = "r2a-onboard-fb"
QUOTE = "r2a-quote-18420"
SATURDAY = "r2a-sat-file"
QUOTE_ID = "QUO-18420"
QUOTE_DOC = "r2a-quo-18420"
SUPPLIER_ON_QUOTE = "SUP-14"
SUPPLIER_ON_INVOICE = "SUP-14B"
AMOUNT = 9600
CURRENCY = "CAD"
FILE_SAT = "cedar-r2a-2027-01-16"
BOOKING_SAT = "2027-01-16"


def commands() -> list[dict]:
    """Return the operations commands in occurred_at order."""
    rows = [*_onboarding(), *_quotation(), *_saturday()]
    return sorted(rows, key=lambda row: row["occurred_at"])


def _onboarding() -> list[dict]:
    """Clinic packet for fraser-burnaby, from lodge through a coverage row."""
    return [
        _lodged_at_desk(),
        _lodged_at_hospital(),
        _finance_ask(),
        _privacy_note(),
        _coverage(),
    ]


def _lodged_at_desk() -> dict:
    return _command(
        "cmd-r2a-lodge",
        "channel",
        "RequestAccepted",
        "2027-01-12T16:20:00Z",
        ONBOARD,
        1,
        {
            "ref": ONBOARD,
            "site": "fraser-burnaby",
            "region": "BC",
            "packet": "clinic-onboarding",
            "application_status": "lodged",
            "utterance": "Fraser Burnaby clinic onboarding application lodged.",
            "channel": "web",
            "desk_region": "BC",
            "handset_delivered": False,
        },
    )


def _lodged_at_hospital() -> dict:
    return _command(
        "cmd-r2a-hospital-lodge",
        "hospital",
        "OnboardingNoted",
        "2027-01-12T17:05:00Z",
        ONBOARD,
        2,
        {
            "ref": ONBOARD,
            "site": "fraser-burnaby",
            "region": "BC",
            "packet": "clinic-onboarding",
            "application_status": "lodged",
            "note": (
                "Fraser Burnaby recorded the lodged clinic application "
                "on the hospital record."
            ),
        },
    )


def _finance_ask() -> dict:
    return _command(
        "cmd-r2a-finance-quote",
        "channel",
        "DeskNote",
        "2027-01-12T18:10:00Z",
        ONBOARD,
        3,
        {
            "ref": ONBOARD,
            "role_id": "finance-partner",
            "title": "Finance partner",
            "site": "vancouver-desk",
            "quote_id": QUOTE_ID,
            "note": (
                "Finance asked for supplier quotation id QUO-18420 "
                "on the Fraser Burnaby clinic onboarding packet."
            ),
        },
    )


def _privacy_note() -> dict:
    return _command(
        "cmd-r2a-privacy-letter",
        "hospital",
        "OnboardingNoted",
        "2027-01-12T20:15:00Z",
        ONBOARD,
        4,
        {
            "ref": ONBOARD,
            "role_id": "privacy-officer",
            "title": "Privacy officer",
            "site": "cascade-seattle",
            "packet_site": "fraser-burnaby",
            "note": "The referral letter stays on the hospital side.",
        },
    )


def _coverage() -> dict:
    return _command(
        "cmd-r2a-cover",
        "payer",
        "CoverageDecided",
        "2027-01-13T17:30:00Z",
        ONBOARD,
        5,
        {
            "ref": ONBOARD,
            "answer": "yes",
            "currency": CURRENCY,
            "member_region": "BC",
            "site": "fraser-burnaby",
            "effective_from": "2027-01-20T00:00:00Z",
            "effective_to": "2027-04-20T00:00:00Z",
        },
    )


def _quotation() -> list[dict]:
    """Quotation document and the invoice note that names another supplier."""
    return [_quote_document(), _invoice_note()]


def _quote_body() -> str:
    return (
        f"Fraser Burnaby clinic onboarding quotation {QUOTE_ID}. "
        f"Supplier id {SUPPLIER_ON_QUOTE}. Amount {AMOUNT} {CURRENCY}."
    )


def _quote_document() -> dict:
    body = _quote_body()
    return _command(
        "cmd-r2a-quote-doc",
        "hospital",
        "DocumentChanged",
        "2027-01-13T19:00:00Z",
        QUOTE,
        1,
        {
            "ref": QUOTE,
            "packet_ref": ONBOARD,
            "doc_id": QUOTE_DOC,
            "version": "2027-01-13",
            "status": "in_force",
            "audience": "procurement",
            "language": "en",
            "body": body,
            "content_hash": _content_hash(body),
            "quote_id": QUOTE_ID,
            "supplier_id": SUPPLIER_ON_QUOTE,
            "amount": AMOUNT,
            "currency": CURRENCY,
            "site": "fraser-burnaby",
        },
    )


def _invoice_note() -> dict:
    return _command(
        "cmd-r2a-invoice-note",
        "channel",
        "DeskNote",
        "2027-01-14T16:45:00Z",
        QUOTE,
        2,
        {
            "ref": QUOTE,
            "packet_ref": ONBOARD,
            "role_id": "finance-partner",
            "title": "Finance partner",
            "site": "vancouver-desk",
            "quote_id": QUOTE_ID,
            "supplier_id": SUPPLIER_ON_INVOICE,
            "amount": AMOUNT,
            "currency": CURRENCY,
            "note": (
                f"Invoice note for quotation {QUOTE_ID} names supplier id "
                f"{SUPPLIER_ON_INVOICE}. Amount {AMOUNT} {CURRENCY}."
            ),
        },
    )


def _saturday() -> list[dict]:
    """Cedar Ridge nightly file and three notes about that Saturday."""
    return [
        _saturday_file(),
        _clerk_tally(),
        _supervisor_tally(),
        _cedar_tally(),
    ]


def _saturday_file() -> dict:
    return _command(
        "cmd-r2a-sat-file",
        "hospital",
        "SlotFiled",
        "2027-01-16T21:00:00Z",
        SATURDAY,
        1,
        {
            "ref": SATURDAY,
            "booking_date": BOOKING_SAT,
            "file_id": FILE_SAT,
            "site": "cedar-ridge",
            "clinic": "ENDO-CLN",
            "state": "WA",
            "slot_api": False,
        },
    )


def _clerk_tally() -> dict:
    return _tally(
        "cmd-r2a-sat-clerk",
        "2027-01-18T16:00:00Z",
        2,
        "desk-clerk",
        "Desk clerk",
        "vancouver-desk",
        (
            f"I counted the Saturday cedar-ridge file {FILE_SAT} as an office day. "
            f"Booking date {BOOKING_SAT} is on my Vancouver tally."
        ),
        "counted",
        None,
    )


def _supervisor_tally() -> dict:
    return _tally(
        "cmd-r2a-sat-supervisor",
        "2027-01-18T17:15:00Z",
        3,
        "desk-supervisor",
        "Desk supervisor",
        "vancouver-desk",
        (
            "The organization calendar is Monday through Friday. "
            f"I left Saturday {BOOKING_SAT} off my office-day tally for file {FILE_SAT}. "
            "I have not signed the clerk tally."
        ),
        "left-off",
        "cmd-r2a-sat-clerk",
    )


def _cedar_tally() -> dict:
    return _tally(
        "cmd-r2a-sat-cedar",
        "2027-01-18T18:40:00Z",
        4,
        "cedar-clerk",
        "Nightly file clerk",
        "cedar-ridge",
        (
            f"I counted Saturday {BOOKING_SAT} on the cedar-ridge file tally "
            f"for {FILE_SAT}. I did not add that Saturday to the Vancouver "
            "office-day tally."
        ),
        "file-tally-only",
        "cmd-r2a-sat-supervisor",
    )


def _tally(
    command_id: str,
    occurred_at: str,
    stream_rev: int,
    role_id: str,
    title: str,
    site: str,
    note: str,
    tally: str,
    prior_command_id: str | None,
) -> dict:
    payload = {
        "ref": SATURDAY,
        "role_id": role_id,
        "title": title,
        "site": site,
        "file_id": FILE_SAT,
        "booking_date": BOOKING_SAT,
        "tally": tally,
        "note": note,
    }
    if prior_command_id:
        payload["prior_command_id"] = prior_command_id
    return _command(
        command_id,
        "channel",
        "DeskNote",
        occurred_at,
        SATURDAY,
        stream_rev,
        payload,
    )


def _content_hash(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


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
