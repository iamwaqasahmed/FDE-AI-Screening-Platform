"""Integration observations already on the logs."""

from __future__ import annotations

_OUTBOX = "int-outbox-17"
_REF = "INT-17"
_SMS = "Northline: visit filed for referral INT-17 at Cedar Ridge."
_FILED_AT = "2027-01-11T21:00:00Z"
_CANCELLED_AT = "2027-01-11T18:10:00Z"


def commands() -> list[dict]:
    """Return the integration commands for 7–12 January 2027."""
    return _handset() + _slot() + _partner() + _morning()


def _handset() -> list[dict]:
    return [
        _command(
            "cmd-int-outbox-recorded",
            "OutboxRecorded",
            "channel",
            "2027-01-10T16:00:00Z",
            _OUTBOX,
            1,
            {
                "ref": _REF,
                "outbox_id": _OUTBOX,
                "idempotency_key": _OUTBOX,
                "consumer_ack": "missing",
            },
        ),
        _command(
            "cmd-int-deliver-1",
            "OutboxDelivered",
            "channel",
            "2027-01-10T16:02:00Z",
            _OUTBOX,
            2,
            _delivery(1, [_SMS]),
        ),
        _command(
            "cmd-int-ack-missing",
            "ConsumerAck",
            "channel",
            "2027-01-10T16:07:00Z",
            _OUTBOX,
            3,
            {
                "ref": _REF,
                "outbox_id": _OUTBOX,
                "idempotency_key": _OUTBOX,
                "consumer_ack": "missing",
            },
        ),
        _command(
            "cmd-int-deliver-2",
            "OutboxDelivered",
            "channel",
            "2027-01-10T16:14:00Z",
            _OUTBOX,
            4,
            _delivery(2, [_SMS, _SMS]),
        ),
    ]


def _delivery(attempt: int, transcripts: list[str]) -> dict:
    return {
        "ref": _REF,
        "outbox_id": _OUTBOX,
        "idempotency_key": _OUTBOX,
        "attempt": attempt,
        "consumer_ack": "missing",
        "transcripts": transcripts,
    }


def _slot() -> list[dict]:
    return [
        _command(
            "cmd-int-slot-filed",
            "SlotFiled",
            "hospital",
            _FILED_AT,
            "int-17",
            1,
            _slot_body(),
        ),
        _command(
            "cmd-int-slot-cancelled",
            "SlotCancelled",
            "hospital",
            _CANCELLED_AT,
            "int-17",
            2,
            _slot_body(),
        ),
    ]


def _slot_body() -> dict:
    return {
        "ref": _REF,
        "site": "cedar-ridge",
        "file_id": "int-file-17",
        "clinic": "ENDO-CLN",
        "booking_date": "2027-01-11",
        "state": "WA",
        "filed_at": _FILED_AT,
        "cancelled_at": _CANCELLED_AT,
    }


def _partner() -> list[dict]:
    return [
        _command(
            "cmd-int-partner-timeout",
            "WebhookAttempt",
            "channel",
            "2027-01-08T18:05:00Z",
            "int-partner-30",
            1,
            {
                "ref": "INT-30",
                "partner": "inland-coverage",
                "attempt": 3,
                "status": "timeout",
            },
        )
    ]


def _morning() -> list[dict]:
    return [
        _command(
            "cmd-int-queue-depth",
            "QueueDepth",
            "channel",
            "2027-01-12T15:20:00Z",
            "int-queue-morning",
            1,
            {
                "visible_backlog": 40,
                "oldest_age_seconds": 960,
                "consumer_alive": True,
            },
        ),
        _command(
            "cmd-int-morning-board",
            "MorningBoard",
            "hospital",
            "2027-01-12T15:22:00Z",
            "int-board-morning",
            1,
            {
                "board": "morning",
                "shown_date": "2027-01-11",
                "read_date": "2027-01-12",
            },
        ),
    ]


def _command(
    command_id: str,
    event_type: str,
    authority: str,
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
