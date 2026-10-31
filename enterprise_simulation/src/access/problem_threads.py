"""THR-17 log commands. One cross-department thread, evidence only."""

from __future__ import annotations

REF = "THR-17"
STREAM = "thr-17"
FILE_ID = "thr-cedar-2027-01-08"
PERSON = "person-thr-17"


def commands() -> list[dict]:
    """Return the THR-17 commands in the order they occurred."""
    rows = _channel() + _hospital() + _payer()
    return sorted(rows, key=lambda row: row["occurred_at"])


def _channel() -> list[dict]:
    return [
        _command(
            "cmd-thr-session-17",
            "channel",
            "DeskSession",
            "2027-01-06T15:40:00Z",
            STREAM,
            1,
            {
                "ref": REF,
                "session_id": "sess-thr-17",
                "token_subject": "member-bc-thr-17",
                "person_id": PERSON,
                "phone": "604-555-0177",
                "postal": "V6B 1A1",
                "factor": "screen-code",
                "desk_region": "BC",
                "zone": "America/Vancouver",
            },
        ),
        _command(
            "cmd-thr-accept-17",
            "channel",
            "RequestAccepted",
            "2027-01-06T15:46:00Z",
            STREAM,
            2,
            {
                "ref": REF,
                "person_id": PERSON,
                "phone": "604-555-0177",
                "utterance": "Your visit at Cedar Ridge is booked for 6 January.",
                "handset_delivered": False,
                "channel": "phone",
                "desk_region": "BC",
            },
        ),
        _command(
            "cmd-thr-handset-17",
            "channel",
            "HandsetDispatch",
            "2027-01-06T16:02:00Z",
            STREAM,
            3,
            {
                "ref": REF,
                "idempotency_key": "thr-handset-17",
                "attempt": 1,
                "status": "not-delivered",
            },
        ),
        _command(
            "cmd-thr-partner-17",
            "channel",
            "WebhookAttempt",
            "2027-01-09T16:44:00Z",
            STREAM,
            4,
            {
                "ref": REF,
                "partner": "harbor-coverage",
                "attempt": 1,
                "status": "posted",
                "eligible": True,
            },
        ),
        _command(
            "cmd-thr-clerk-17",
            "channel",
            "DeskNote",
            "2027-01-11T16:30:00Z",
            STREAM,
            5,
            {
                "ref": REF,
                "role": "clerk",
                "note": (
                    "Patient told the visit was booked. "
                    "The file night is a different date."
                ),
            },
        ),
    ]


def _hospital() -> list[dict]:
    filed = {
        "ref": REF,
        "site": "cedar-ridge",
        "file_id": FILE_ID,
        "clinic": "ENDO-CLN",
        "booking_date": "2027-01-08",
        "state": "WA",
    }
    return [
        _command(
            "cmd-thr-receipt-17",
            "hospital",
            "ReferralAccepted",
            "2027-01-07T17:05:00Z",
            STREAM,
            1,
            {
                "ref": REF,
                "person_id": PERSON,
                "site": "cedar-ridge",
                "state": "WA",
                "member_region": "BC",
            },
        ),
        _command(
            "cmd-thr-letter-17",
            "hospital",
            "LetterStored",
            "2027-01-07T18:20:00Z",
            STREAM,
            2,
            {
                "ref": REF,
                "audience": "coordinator",
                "text": (
                    "Filed desk transcript for THR-17. "
                    "Transcript says the Cedar Ridge visit was booked for 6 January."
                ),
            },
        ),
        _command(
            "cmd-thr-offer-17",
            "hospital",
            "SlotOffered",
            "2027-01-07T22:15:00Z",
            STREAM,
            3,
            {
                "ref": REF,
                "version": "slot-thr-17",
                "offer_id": "offer-thr-17",
                "site": "cedar-ridge",
            },
        ),
        _command(
            "cmd-thr-file-17",
            "hospital",
            "SlotFiled",
            "2027-01-08T21:00:00Z",
            STREAM,
            4,
            filed,
        ),
        _command(
            "cmd-thr-cache-17",
            "hospital",
            "CacheStored",
            "2027-01-09T21:12:00Z",
            STREAM,
            5,
            {
                "ref": REF,
                "eligible": True,
                "window_present": False,
                "source": "copied-from-partner-message",
            },
        ),
        _command(
            "cmd-thr-replay-17",
            "hospital",
            "SlotFiled",
            "2027-01-10T21:00:00Z",
            STREAM,
            6,
            {**filed, "replay": True},
        ),
    ]


def _payer() -> list[dict]:
    return [
        _command(
            "cmd-thr-cover-17",
            "payer",
            "CoverageDecided",
            "2027-01-09T16:40:00Z",
            STREAM,
            1,
            {
                "ref": REF,
                "answer": "yes",
                "effective_from": "2027-01-15T00:00:00Z",
                "effective_to": "2027-04-15T00:00:00Z",
                "currency": "CAD",
                "member_region": "BC",
            },
        )
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
