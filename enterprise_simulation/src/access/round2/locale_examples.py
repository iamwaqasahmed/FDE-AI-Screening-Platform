"""Locale comparison rows for students. Not a legal memo."""

from __future__ import annotations

_BC_REF = "R2H-BC"
_WA_REF = "R2H-WA"
_WINDOW_FROM = "2027-02-01T00:00:00Z"
_WINDOW_TO = "2027-05-01T00:00:00Z"


def commands() -> list[dict]:
    """Return locale examples a student can compare, in time order."""
    rows = _bc_postal() + _wa_site() + _coverage() + _local_pair()
    return sorted(rows, key=lambda row: (row["occurred_at"], row["command_id"]))


def _bc_postal() -> list[dict]:
    """BC desk kept V6B 2W9 and did not store the ZIP the clerk typed."""
    return [
        _command(
            "cmd-r2h-bc-postal",
            "channel",
            "DeskNote",
            "2027-01-11T16:15:00Z",
            "r2h-bc-postal",
            1,
            {
                "ref": _BC_REF,
                "region": "BC",
                "city": "Vancouver",
                "line1": "22 Northline Place",
                "postal": "V6B 2W9",
                "rejected_zip": "98101",
                "outcome": "not-stored",
                "note": (
                    "The clerk typed 98101 on this British Columbia address. "
                    "The desk kept postal V6B 2W9."
                ),
            },
        )
    ]


def _wa_site() -> list[dict]:
    """Washington site row stores a ZIP and has no postal field."""
    return [
        _command(
            "cmd-r2h-wa-zip",
            "hospital",
            "AddressRecorded",
            "2027-01-11T17:05:00Z",
            "r2h-wa-site",
            1,
            {
                "ref": _WA_REF,
                "site": "cascade-seattle",
                "region": "WA",
                "city": "Seattle",
                "line1": "90 Northline Avenue",
                "zip": "98101",
                "note": "Cascade Seattle site address for this Washington row.",
            },
        )
    ]


def _coverage() -> list[dict]:
    """CAD for the BC member and USD for the WA member."""
    return [
        _yes_row(
            "cmd-r2h-bc-cad",
            "2027-01-11T20:00:00Z",
            "r2h-bc",
            _BC_REF,
            "CAD",
            "BC",
        ),
        _yes_row(
            "cmd-r2h-wa-usd",
            "2027-01-11T20:10:00Z",
            "r2h-wa",
            _WA_REF,
            "USD",
            "WA",
        ),
    ]


def _yes_row(
    command_id: str,
    occurred_at: str,
    stream_id: str,
    ref: str,
    currency: str,
    member_region: str,
) -> dict:
    return _command(
        command_id,
        "payer",
        "CoverageDecided",
        occurred_at,
        stream_id,
        1,
        {
            "ref": ref,
            "answer": "yes",
            "currency": currency,
            "member_region": member_region,
            "effective_from": _WINDOW_FROM,
            "effective_to": _WINDOW_TO,
        },
    )


def _local_pair() -> list[dict]:
    """17:00 Pacific standard time on 11 January 2027, plus the spreadsheet stamp."""
    return [
        _command(
            "cmd-r2h-local-1700",
            "channel",
            "DeskNote",
            "2027-01-12T01:00:00Z",
            "r2h-local",
            1,
            {
                "local_vancouver": "2027-01-11T17:00:00-08:00",
                "local_los_angeles": "2027-01-11T17:00:00-08:00",
                "zone_vancouver": "America/Vancouver",
                "zone_los_angeles": "America/Los_Angeles",
                "spreadsheet_utc": "2027-01-11T17:00:00Z",
                "note": "The spreadsheet omitted the offset.",
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
