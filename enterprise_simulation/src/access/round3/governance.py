"""Desk policy rows for one letter on 19 January 2027.

The Vancouver desk and Cedar Ridge each wrote their own rows.
The list keeps every row.
"""

from __future__ import annotations

REF = "R3G-CONSENT"
PERSON = "p-r3g-1"
STREAM = "r3g-consent"
DESK = "vancouver-desk"
DESK_TZ = "America/Vancouver"
SITE = "cedar-ridge"
SITE_TZ = "America/Los_Angeles"


def commands() -> list[dict]:
    """Return the governance commands in occurred_at order."""
    return [
        _screen_consent(),
        _letter_consent(),
        _download_note(),
        _keep_years(),
        _archive_on(),
        _copy_requested(),
        _copy_completed(),
    ]


def _screen_consent() -> dict:
    return _command(
        "cmd-r3g-consent-screen",
        "channel",
        "ConsentNoted",
        "2027-01-19T17:10:00Z",
        1,
        _desk(
            {
                "consent_recorded": True,
                "scope": "screen text",
                "role": "desk-clerk",
                "policy": "Vancouver desk policy records consent for screen text.",
            }
        ),
    )


def _letter_consent() -> dict:
    return _command(
        "cmd-r3g-consent-letter",
        "hospital",
        "ConsentNoted",
        "2027-01-19T17:35:00Z",
        1,
        _hospital(
            {
                "consent_recorded": False,
                "scope": "letter file",
                "policy": (
                    "Cedar Ridge desk policy records the letter file "
                    "with consent_recorded false."
                ),
            }
        ),
    )


def _download_note() -> dict:
    return _command(
        "cmd-r3g-desk-download",
        "channel",
        "DeskNote",
        "2027-01-19T18:20:00Z",
        2,
        _desk(
            {
                "role": "desk-clerk",
                "note": "The clerk downloaded the letter anyway.",
                "policy": "Vancouver desk policy wrote this note on the letter.",
            }
        ),
    )


def _keep_years() -> dict:
    return _command(
        "cmd-r3g-keep-years",
        "channel",
        "RetentionPolicy",
        "2027-01-19T19:05:00Z",
        3,
        _desk(
            {
                "object": "letter",
                "keep_years": 7,
                "policy": "Vancouver desk policy keeps the letter for 7 years.",
            }
        ),
    )


def _archive_on() -> dict:
    return _command(
        "cmd-r3g-archive-on",
        "hospital",
        "RetentionPolicy",
        "2027-01-19T19:40:00Z",
        2,
        _hospital(
            {
                "object": "letter",
                "archive_on": "2026-12-01",
                "policy": "Cedar Ridge desk policy archives the letter on 2026-12-01.",
            }
        ),
    )


def _copy_requested() -> dict:
    return _command(
        "cmd-r3g-copy-ask",
        "channel",
        "ApprovalRequested",
        "2027-01-19T21:10:00Z",
        4,
        _desk(
            {
                "object": "letter",
                "role": "desk-clerk",
                "job": "copy",
                "destination": "ca-central-1",
                "reviewer": None,
                "policy": (
                    "Vancouver desk policy requested a letter copy to ca-central-1."
                ),
            }
        ),
    )


def _copy_completed() -> dict:
    return _command(
        "cmd-r3g-copy-done",
        "hospital",
        "CopyCompleted",
        "2027-01-19T22:15:00Z",
        3,
        _hospital(
            {
                "object": "letter",
                "destination": "ca-central-1",
                "http_status": 200,
                "reviewer": None,
                "member_desk": DESK_TZ,
                "policy": (
                    "Cedar Ridge desk policy completed the letter copy "
                    "to ca-central-1."
                ),
            }
        ),
    )


def _desk(extra: dict) -> dict:
    payload = {
        "ref": REF,
        "person_id": PERSON,
        "site": DESK,
        "desk_region": "BC",
        "timezone": DESK_TZ,
    }
    payload.update(extra)
    return payload


def _hospital(extra: dict) -> dict:
    payload = {
        "ref": REF,
        "person_id": PERSON,
        "site": SITE,
        "state": "WA",
        "timezone": SITE_TZ,
    }
    payload.update(extra)
    return payload


def _command(
    command_id: str,
    authority: str,
    event_type: str,
    occurred_at: str,
    stream_rev: int,
    payload: dict,
) -> dict:
    return {
        "command_id": command_id,
        "authority": authority,
        "type": event_type,
        "occurred_at": occurred_at,
        "stream_id": STREAM,
        "stream_rev": stream_rev,
        "payload": payload,
    }
