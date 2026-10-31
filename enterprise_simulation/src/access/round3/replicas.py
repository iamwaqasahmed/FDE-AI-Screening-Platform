"""Replica copies of one hospital file. Observations only."""

from __future__ import annotations

REF = "R3E-SYNC"
SOURCE = "r3e-sync"
FILE_ID = "cedar-r3e-2027-01-18"
SITE = "cedar-ridge"
SMS_KEY = "r3e-sms-1"
CEDAR = "cedar-copy"
CASCADE = "cascade-copy"
_FILED_TEXT = "Northline visit filed at Cedar Ridge."
_BOOKED_TEXT = "Northline visit booked at Cedar Ridge."


def commands() -> list[dict]:
    """Return 9 commands for 18–19 January 2027."""
    return _slot() + _cursors() + _exports() + _handset() + _morning()


def _slot() -> list[dict]:
    return [
        _command(
            "cmd-r3e-slot-filed",
            "hospital",
            "SlotFiled",
            "2027-01-18T21:00:00Z",
            SOURCE,
            1,
            {
                "ref": REF,
                "booking_date": "2027-01-18",
                "file_id": FILE_ID,
                "site": SITE,
                "clinic": "ENDO-CLN",
                "state": "WA",
                "trailer_ok": True,
                "trailer_count": 8,
                "body_count": 8,
            },
        )
    ]


def _cursors() -> list[dict]:
    return [
        _cursor("cmd-r3e-cursor-cedar", CEDAR, 14, "2027-01-18T22:10:00Z"),
        _cursor("cmd-r3e-cursor-cascade", CASCADE, 10, "2027-01-18T22:16:00Z"),
    ]


def _cursor(command_id: str, replica: str, seq_caught: int, occurred_at: str) -> dict:
    return _command(
        command_id,
        "hospital",
        "ReplicaCursor",
        occurred_at,
        f"r3e-{replica}",
        1,
        {
            "ref": REF,
            "replica": replica,
            "source_stream": SOURCE,
            "seq_caught": seq_caught,
            "file_id": FILE_ID,
        },
    )


def _exports() -> list[dict]:
    return [
        _export("cmd-r3e-export-cedar", CEDAR, "USD", "2027-01-19T14:40:00Z"),
        _export("cmd-r3e-export-cascade", CASCADE, "CAD", "2027-01-19T14:46:00Z"),
    ]


def _export(command_id: str, replica: str, currency: str, occurred_at: str) -> dict:
    return _command(
        command_id,
        "hospital",
        "ReplicaExport",
        occurred_at,
        f"r3e-{replica}",
        2,
        {
            "ref": REF,
            "replica": replica,
            "source_stream": SOURCE,
            "file_id": FILE_ID,
            "amount": 90,
            "currency": currency,
        },
    )


def _handset() -> list[dict]:
    return [
        _dispatch("cmd-r3e-handset-1", 1, "sent", _FILED_TEXT, "2027-01-19T15:02:00Z"),
        _dispatch(
            "cmd-r3e-handset-2",
            2,
            "redelivered",
            _BOOKED_TEXT,
            "2027-01-19T15:08:00Z",
        ),
    ]


def _dispatch(
    command_id: str,
    attempt: int,
    status: str,
    transcript: str,
    occurred_at: str,
) -> dict:
    return _command(
        command_id,
        "channel",
        "HandsetDispatch",
        occurred_at,
        "r3e-handset",
        attempt,
        {
            "ref": REF,
            "file_id": FILE_ID,
            "idempotency_key": SMS_KEY,
            "attempt": attempt,
            "status": status,
            "transcripts": [transcript],
        },
    )


def _morning() -> list[dict]:
    return [
        _command(
            "cmd-r3e-queue-depth",
            "channel",
            "QueueDepth",
            "2027-01-19T15:20:00Z",
            "r3e-queue",
            1,
            {
                "ref": REF,
                "visible_backlog": 120,
                "oldest_age_seconds": 5400,
                "consumer_alive": True,
            },
        ),
        _command(
            "cmd-r3e-desk-note",
            "channel",
            "DeskNote",
            "2027-01-19T15:26:00Z",
            "r3e-desk",
            1,
            {
                "ref": REF,
                "file_id": FILE_ID,
                "note": "The morning board was printed from cascade-copy.",
            },
        ),
    ]


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
