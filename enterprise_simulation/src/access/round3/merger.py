"""Referral R3A-MERGE after Inlet Medical joins Cedar Ridge.

Each row stays in the list. The list does not rank the rows.
"""

from __future__ import annotations

REF = "R3A-MERGE"
PERSON = "p-r3a-1"
OLD_SITE = "inlet-medical"
NEW_SITE = "cedar-ridge"
MERGED_ON = "2026-09-01"
BOOKING_DATE = "2026-11-02"
INLET_FILE = "inlet-2026-11-02"
CEDAR_FILE = "cedar-r3a-2026-11-02"
STATE = "WA"
DESK = "vancouver-desk"
DESK_CITY = "Vancouver"
DESK_REGION = "BC"
DESK_TZ = "America/Vancouver"
SITE_TZ = "America/Los_Angeles"
PAYER = "harbor-coverage"
CLINIC_STREAM = "r3a-clinic"
CASE_STREAM = "r3a-merge"
DESK_STREAM = "r3a-desk"
PAYER_STREAM = "r3a-payer"


def commands() -> list[dict]:
    """Return the merger commands in occurred_at order."""
    rows = [
        _clinic_listed(),
        _chart(),
        _merged(),
        _inlet_file(),
        _cedar_file(),
        _historical_note(),
        _retired_note(),
        _obligation(),
        _payer_queues(),
    ]
    return sorted(rows, key=lambda row: row["occurred_at"])


def _clinic_listed() -> dict:
    return _command(
        "cmd-r3a-clinic-list",
        "hospital",
        "ClinicListed",
        "2025-06-02T16:00:00Z",
        CLINIC_STREAM,
        1,
        {
            "ref": REF,
            "site": OLD_SITE,
            "region": STATE,
            "state": STATE,
            "timezone": SITE_TZ,
            "statement": "inlet-medical is a clinic in WA.",
        },
    )


def _chart() -> dict:
    return _command(
        "cmd-r3a-chart",
        "hospital",
        "ReferralAccepted",
        "2026-08-12T17:30:00Z",
        CASE_STREAM,
        1,
        {
            "ref": REF,
            "person_id": PERSON,
            "site": OLD_SITE,
            "state": STATE,
            "member_region": DESK_REGION,
            "timezone": SITE_TZ,
            "statement": "Person p-r3a-1 is on the inlet-medical record in WA.",
        },
    )


def _merged() -> dict:
    return _command(
        "cmd-r3a-merged",
        "hospital",
        "ClinicMerged",
        "2026-09-01T16:00:00Z",
        CLINIC_STREAM,
        2,
        {
            "ref": REF,
            "person_id": PERSON,
            "old_site": OLD_SITE,
            "new_site": NEW_SITE,
            "merged_on": MERGED_ON,
            "old_state": STATE,
            "new_state": STATE,
            "new_site_slot_api": False,
            "new_site_timezone": SITE_TZ,
            "statement": "Clinic inlet-medical in WA is merged into cedar-ridge.",
        },
    )


def _inlet_file() -> dict:
    return _slot(
        "cmd-r3a-file-inlet",
        "2026-11-02T21:00:00Z",
        2,
        INLET_FILE,
        OLD_SITE,
    )


def _cedar_file() -> dict:
    return _slot(
        "cmd-r3a-file-cedar",
        "2026-11-02T22:10:00Z",
        3,
        CEDAR_FILE,
        NEW_SITE,
        slot_api=False,
    )


def _historical_note() -> dict:
    return _desk_note(
        "cmd-r3a-desk-historical",
        "2026-11-03T16:20:00Z",
        1,
        "desk-supervisor",
        "Desk supervisor",
        DESK,
        "The old site id inlet-medical must keep working for historical files.",
    )


def _retired_note() -> dict:
    return _desk_note(
        "cmd-r3a-desk-retired",
        "2026-11-03T17:05:00Z",
        2,
        "cedar-records",
        "Clinic records clerk",
        NEW_SITE,
        "The old site id inlet-medical was retired on the merger date 2026-09-01.",
    )


def _obligation() -> dict:
    return _command(
        "cmd-r3a-obligation",
        "channel",
        "ObligationNoted",
        "2026-11-03T18:15:00Z",
        DESK_STREAM,
        3,
        {
            "ref": REF,
            "person_id": PERSON,
            "site": DESK,
            "desk_city": DESK_CITY,
            "desk_region": DESK_REGION,
            "timezone": DESK_TZ,
            "file_ids": [INLET_FILE, CEDAR_FILE],
            "operations_role_id": "ops-director",
            "operations_title": "Operations director",
            "operations_site": DESK,
            "operations_statement": "Operations wants one wait number.",
            "clerk_role_id": "cedar-clerk",
            "clerk_title": "Nightly file clerk",
            "clerk_site": NEW_SITE,
            "clerk_slot_api": False,
            "clerk_statement": (
                "Inlet files are not on the cedar nightly extract yet."
            ),
        },
    )


def _payer_queues() -> dict:
    return _command(
        "cmd-r3a-payer-queues",
        "payer",
        "AccountListed",
        "2026-11-04T17:00:00Z",
        PAYER_STREAM,
        1,
        {
            "ref": REF,
            "person_id": PERSON,
            "payer": PAYER,
            "site": PAYER,
            "currencies": ["CAD", "USD"],
            "member_region": DESK_REGION,
            "clinic_state": STATE,
            "statement": (
                "Harbor Coverage lists CAD for the BC member and USD for the WA clinic."
            ),
        },
    )


def _slot(
    command_id: str,
    occurred_at: str,
    stream_rev: int,
    file_id: str,
    site: str,
    slot_api: bool | None = None,
) -> dict:
    payload = {
        "ref": REF,
        "person_id": PERSON,
        "booking_date": BOOKING_DATE,
        "file_id": file_id,
        "site": site,
        "state": STATE,
        "timezone": SITE_TZ,
    }
    if slot_api is not None:
        payload["slot_api"] = slot_api
    return _command(
        command_id,
        "hospital",
        "SlotFiled",
        occurred_at,
        CASE_STREAM,
        stream_rev,
        payload,
    )


def _desk_note(
    command_id: str,
    occurred_at: str,
    stream_rev: int,
    role_id: str,
    title: str,
    site: str,
    note: str,
) -> dict:
    return _command(
        command_id,
        "channel",
        "DeskNote",
        occurred_at,
        DESK_STREAM,
        stream_rev,
        {
            "ref": REF,
            "person_id": PERSON,
            "role_id": role_id,
            "title": title,
            "site": site,
            "desk_city": DESK_CITY,
            "desk_region": DESK_REGION,
            "timezone": DESK_TZ,
            "old_site": OLD_SITE,
            "new_site": NEW_SITE,
            "merged_on": MERGED_ON,
            "booking_date": BOOKING_DATE,
            "file_ids": [INLET_FILE, CEDAR_FILE],
            "note": note,
        },
    )


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
