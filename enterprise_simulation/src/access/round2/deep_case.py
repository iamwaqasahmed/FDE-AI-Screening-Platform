"""R2E-9 evidence. Every row is visible. None is marked as the conclusion."""

from __future__ import annotations

REF = "R2E-9"
PERSON = "p-r2e-9"
OLD_MEMBER = "MBR-OLD-9"
CURRENT_MEMBER = "MBR-R2E-9"
SITE = "cedar-ridge"
STATE = "WA"
REGION = "BC"
CURRENCY = "CAD"
CLOSED_ON = "2027-02-15"
FILE_ID = "cedar-r2e-2027-02-15"
CASE_STREAM = "r2e-9"
OFFICE_STREAM = "r2e-office"


def commands() -> list[dict]:
    """Return the R2E-9 commands in the order they occurred."""
    return sorted(_rows(), key=lambda row: row["occurred_at"])


def _rows() -> list[dict]:
    return [
        _chart(),
        _migration(),
        _closure(),
        _accepted(),
        _filed(),
        _coverage(),
        _cache(),
        _operations_note(),
        _supervisor_note(),
    ]


def _chart() -> dict:
    return _command(
        "cmd-r2e-chart",
        "hospital",
        "ReferralAccepted",
        "2027-01-11T16:20:00Z",
        CASE_STREAM,
        1,
        {
            "ref": REF,
            "person_id": PERSON,
            "member_id": OLD_MEMBER,
            "member_region": REGION,
            "site": SITE,
            "state": STATE,
        },
    )


def _migration() -> dict:
    return _command(
        "cmd-r2e-migrate",
        "hospital",
        "MigrationNote",
        "2027-01-27T19:05:00Z",
        CASE_STREAM,
        2,
        {
            "ref": REF,
            "person_id": PERSON,
            "previous_member_id": OLD_MEMBER,
            "current_member_id": CURRENT_MEMBER,
        },
    )


def _closure() -> dict:
    return _command(
        "cmd-r2e-closure",
        "hospital",
        "ClosureListed",
        "2027-02-01T16:30:00Z",
        OFFICE_STREAM,
        1,
        {
            "ref": REF,
            "site": SITE,
            "state": STATE,
            "closed_office_days": [CLOSED_ON],
        },
    )


def _accepted() -> dict:
    return _command(
        "cmd-r2e-accept",
        "channel",
        "RequestAccepted",
        "2027-02-12T16:12:00Z",
        CASE_STREAM,
        1,
        {
            "ref": REF,
            "person_id": PERSON,
            "member_id": CURRENT_MEMBER,
            "member_region": REGION,
            "desk_region": REGION,
            "site": SITE,
            "utterance": "The Cedar Ridge visit is booked for 2027-02-15.",
            "handset_delivered": False,
            "channel": "phone",
        },
    )


def _filed() -> dict:
    return _command(
        "cmd-r2e-file",
        "hospital",
        "SlotFiled",
        "2027-02-15T21:00:00Z",
        CASE_STREAM,
        3,
        {
            "ref": REF,
            "booking_date": CLOSED_ON,
            "file_id": FILE_ID,
            "site": SITE,
            "state": STATE,
            "trailer_ok": True,
            "trailer_count": 9,
            "body_count": 9,
        },
    )


def _coverage() -> dict:
    return _command(
        "cmd-r2e-cover",
        "payer",
        "CoverageDecided",
        "2027-02-16T17:25:00Z",
        CASE_STREAM,
        1,
        {
            "ref": REF,
            "answer": "yes",
            "effective_from": "2027-02-20",
            "effective_to": "2027-05-20",
            "currency": CURRENCY,
            "member_region": REGION,
        },
    )


def _cache() -> dict:
    return _command(
        "cmd-r2e-cache",
        "hospital",
        "CacheStored",
        "2027-02-16T23:40:00Z",
        CASE_STREAM,
        4,
        {
            "ref": REF,
            "eligible": True,
            "window_present": False,
        },
    )


def _operations_note() -> dict:
    return _command(
        "cmd-r2e-ops-note",
        "channel",
        "DeskNote",
        "2027-02-17T15:05:00Z",
        CASE_STREAM,
        2,
        {
            "ref": REF,
            "role": "operations",
            "on_date": CLOSED_ON,
            "note": (
                "Count 2027-02-15 as a working day so the weekend number "
                "still looks small."
            ),
        },
    )


def _supervisor_note() -> dict:
    return _command(
        "cmd-r2e-supervisor-note",
        "channel",
        "DeskNote",
        "2027-02-17T15:48:00Z",
        CASE_STREAM,
        3,
        {
            "ref": REF,
            "role": "desk-supervisor",
            "on_date": CLOSED_ON,
            "note": "The office list does not include that date.",
        },
    )


def _command(
    command_id: str,
    authority: str,
    event_type: str,
    occurred_at: str,
    stream_id: str,
    rev: int,
    payload: dict,
) -> dict:
    return {
        "command_id": command_id,
        "authority": authority,
        "type": event_type,
        "occurred_at": occurred_at,
        "stream_id": stream_id,
        "stream_rev": rev,
        "payload": payload,
    }
