"""Historical rows whose append order and authority time differ.

``seq`` on a log is the order of append. ``occurred_at`` is the time that
authority wrote on the row. This list is the append order.
"""

from __future__ import annotations

_PERSON = "p-r2f-2701"
_DIGITS = "6045552701"
_DASHED = "604-555-2701"
_SOURCE = "desk-spreadsheet-2024"


def commands() -> list[dict]:
    """Return the historical commands in append order."""
    return (
        _digits_epoch()
        + _digits_on_file()
        + _dashed_epoch()
        + _dashed_on_file()
        + _clinic_order()
        + _migrated_rows()
        + _late_request()
    )


def _digits_epoch() -> list[dict]:
    return [
        _epoch(
            "cmd-r2f-schema-1",
            1,
            "2025-01-15",
            "digits",
            _DIGITS,
        )
    ]


def _dashed_epoch() -> list[dict]:
    return [
        _epoch(
            "cmd-r2f-schema-2",
            2,
            "2026-06-01",
            "dashed",
            _DASHED,
        )
    ]


def _epoch(
    command_id: str,
    stream_rev: int,
    occurred_at: str,
    form: str,
    example: str,
) -> dict:
    return _command(
        command_id,
        "channel",
        "SchemaEpoch",
        occurred_at,
        "r2f-schema",
        stream_rev,
        {
            "person_id": _PERSON,
            "field": "phone",
            "form": form,
            "example": example,
        },
    )


def _digits_on_file() -> list[dict]:
    """Channel digits, then the payer copy of that number."""
    phone = {
        "person_id": _PERSON,
        "field": "phone",
        "form": "digits",
        "phone": _DIGITS,
    }
    return [
        _command(
            "cmd-r2f-phone-digits",
            "channel",
            "PhoneRecorded",
            "2025-04-11T17:20:00Z",
            "r2f-phone",
            1,
            phone,
        ),
        _command(
            "cmd-r2f-payer-digits",
            "payer",
            "PhoneFiled",
            "2025-04-11T19:05:00Z",
            "r2f-member",
            1,
            {"ref": "R2F-2701", **phone},
        ),
    ]


def _dashed_on_file() -> list[dict]:
    return [
        _command(
            "cmd-r2f-phone-dashed",
            "channel",
            "PhoneRecorded",
            "2026-06-02T16:40:00Z",
            "r2f-phone",
            2,
            {
                "person_id": _PERSON,
                "field": "phone",
                "form": "dashed",
                "phone": _DASHED,
            },
        )
    ]


def _clinic_order() -> list[dict]:
    """Revision 2 is an earlier clinic day and a later append."""
    return [
        _command(
            "cmd-r2f-order-1",
            "hospital",
            "ClinicNoted",
            "2026-08-02",
            "r2f-order",
            1,
            {
                "ref": "R2F-ORD",
                "person_id": "p-r2f-ord",
                "site": "cedar-ridge",
            },
        ),
        _command(
            "cmd-r2f-order-2",
            "hospital",
            "ClinicNoted",
            "2026-08-01",
            "r2f-order",
            2,
            {
                "ref": "R2F-ORD",
                "person_id": "p-r2f-ord",
                "site": "cedar-ridge",
            },
        ),
    ]


def _migrated_rows() -> list[dict]:
    """One spreadsheet key on two hospital refs, and a neighboring row."""
    return [
        _migrated(
            "cmd-r2f-mig-14",
            "r2f-sheet-14",
            "2024-03-14T16:10:00Z",
            "S-14",
            "R2F-14",
            "p-r2f-14",
        ),
        _migrated(
            "cmd-r2f-mig-15",
            "r2f-sheet-15",
            "2024-03-18T16:10:00Z",
            "S-15",
            "R2F-15",
            "p-r2f-15",
        ),
        _migrated(
            "cmd-r2f-mig-99",
            "r2f-sheet-99",
            "2024-10-02T16:10:00Z",
            "S-14",
            "R2F-99",
            "p-r2f-99",
        ),
    ]


def _migrated(
    command_id: str,
    stream_id: str,
    occurred_at: str,
    source_row: str,
    ref: str,
    person_id: str,
) -> dict:
    return _command(
        command_id,
        "hospital",
        "SourceRowMigrated",
        occurred_at,
        stream_id,
        1,
        {
            "source": _SOURCE,
            "source_row": source_row,
            "ref": ref,
            "person_id": person_id,
        },
    )


def _late_request() -> list[dict]:
    """Authority time in March, recorded date in November."""
    return [
        _command(
            "cmd-r2f-late",
            "channel",
            "RequestAccepted",
            "2026-03-04T15:00:00Z",
            "r2f-late",
            1,
            {
                "ref": "R2F-LATE",
                "person_id": "p-r2f-late",
                "recorded_on": "2026-11-02",
                "reason": "spreadsheet row found in November",
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
