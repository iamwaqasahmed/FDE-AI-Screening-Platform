"""Observations for lesson worlds that are thin.

These commands are evidence. They are not a repair, and `history()` does not
append them.
"""

from __future__ import annotations

_AUTHORITIES = ("hospital", "channel", "payer")
_LETTER_SENTENCE = "Patient reports urgent chest pain."


def commands() -> list[dict]:
    """Return the curriculum observations in lesson order."""
    return [
        *_delivery(),
        *_score(),
        *_signal(),
        *_bytes(),
    ]


def _delivery() -> list[dict]:
    """INV-04. A cancelled nightly row, the text that followed it, and closure dates."""
    file_id = "cedar-cur-2027-01-13"
    return [
        _command(
            "cmd-cur-visit-cancelled",
            "hospital",
            "VisitCancelled",
            "2027-01-13T21:00:00Z",
            "cur-cancel",
            {
                "ref": "CUR-4",
                "site": "cedar-ridge",
                "file_id": file_id,
                "visit_state": "cancelled",
            },
        ),
        _command(
            "cmd-cur-text-after-cancel",
            "channel",
            "HandsetDispatch",
            "2027-01-13T21:10:00Z",
            "cur-text",
            {
                "ref": "CUR-4",
                "file_id": file_id,
                "status": "dispatched",
                "text_sent": True,
            },
        ),
        _command(
            "cmd-cur-closures",
            "channel",
            "ClosuresAnnounced",
            "2026-12-15T16:00:00Z",
            "cur-closures",
            {
                "list_id": "office-closures-2027",
                "dates": ["2027-01-01", "2027-02-15"],
                "note": "announced office closure dates",
            },
        ),
    ]


def _score() -> list[dict]:
    """INV-06. A small channel comparison. The note carries the figures."""
    return [
        _command(
            "cmd-cur-tiny-delta",
            "channel",
            "ComparisonNoted",
            "2027-01-14T16:00:00Z",
            "cur-score",
            {
                "ref": "CUR-6",
                "tiny_delta": "scores 0.5002 vs 0.5000, n 9",
                "score_a": 0.5002,
                "score_b": 0.5000,
                "n": 9,
            },
        )
    ]


def _signal() -> list[dict]:
    """INV-07. Shadow traffic wrote a slot. A green host is serving an old id."""
    return [
        _command(
            "cmd-cur-shadow-wrote",
            "channel",
            "ShadowRequest",
            "2027-01-14T17:00:00Z",
            "cur-shadow",
            {
                "ref": "CUR-7",
                "shadow_wrote": True,
                "wrote_slot": True,
                "replay": True,
            },
        ),
        _command(
            "cmd-cur-host-green",
            "channel",
            "HostObserved",
            "2027-01-14T17:01:00Z",
            "cur-host",
            {
                "ref": "CUR-7",
                "host": "desk-app-9",
                "cpu_percent": 11,
                "status": "green",
                "served_version": "old-hours",
                "from_cache": True,
            },
        ),
    ]


def _bytes() -> list[dict]:
    """INV-08. One FAQ body quotes one sentence from the referral letter."""
    return [
        _command(
            "cmd-cur-faq-quote",
            "hospital",
            "FaqBodyStored",
            "2027-01-14T18:00:00Z",
            "cur-faq",
            {
                "faq_id": "faq-mixed-cur",
                "body": _LETTER_SENTENCE,
            },
        )
    ]


def _command(
    command_id: str,
    authority: str,
    event_type: str,
    occurred_at: str,
    stream_id: str,
    payload: dict,
) -> dict:
    if not command_id.startswith("cmd-cur-"):
        raise ValueError(command_id)
    if authority not in _AUTHORITIES:
        raise ValueError(authority)
    if not stream_id.startswith("cur-"):
        raise ValueError(stream_id)
    return {
        "command_id": command_id,
        "authority": authority,
        "type": event_type,
        "occurred_at": occurred_at,
        "stream_id": stream_id,
        "stream_rev": 1,
        "payload": payload,
    }
