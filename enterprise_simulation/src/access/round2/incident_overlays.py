"""Incident overlays for a replay storm and a partial write.

The base history already contains the opening defects. ``scenarios.names()``
stays on the earlier overlays. A caller appends one of these lists when that
extra incident is wanted. Command ids and stream revisions here are unused
by the base log and by those earlier overlays.
"""

from __future__ import annotations

_STORM_REF = "R2G-STORM"
_STORM_STREAM = "r2g-storm"
_STORM_FILE = "cedar-storm-2027-03-01"
_PART_REF = "R2G-PART"
_PART_STREAM = "r2g-part"
_PART_SENTENCE = "the visit was booked"


def names() -> list[str]:
    """Return the overlay names in registry order."""
    return ["replay-storm", "partial-write"]


def overlay(name: str) -> list[dict]:
    """Return a fresh command list for one overlay."""
    builders = {
        "replay-storm": _replay_storm,
        "partial-write": _partial_write,
    }
    builder = builders.get(name)
    if builder is None:
        raise ValueError(f"unknown overlay: {name}")
    return builder()


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


def _replay_storm() -> list[dict]:
    """One night file is stored three times; the last trailer does not match."""
    return [
        _storm_file("cmd-r2g-storm-file-1", "2027-03-01T21:00:00Z", 1, _storm_body()),
        _storm_file("cmd-r2g-storm-file-2", "2027-03-01T21:06:00Z", 2, _storm_body()),
        _storm_file("cmd-r2g-storm-file-3", "2027-03-02T21:00:00Z", 3, _storm_bad_body()),
        _storm_note(),
    ]


def _storm_file(command_id: str, occurred_at: str, rev: int, payload: dict) -> dict:
    return _command(
        command_id,
        "hospital",
        "SlotFiled",
        occurred_at,
        _STORM_STREAM,
        rev,
        payload,
    )


def _storm_body() -> dict:
    return {
        "ref": _STORM_REF,
        "booking_date": "2027-03-01",
        "file_id": _STORM_FILE,
        "site": "cedar-ridge",
        "clinic": "ENDO-CLN",
        "state": "WA",
    }


def _storm_bad_body() -> dict:
    body = _storm_body()
    body["trailer_ok"] = False
    body["trailer_count"] = 9
    body["body_count"] = 8
    return body


def _storm_note() -> dict:
    return _command(
        "cmd-r2g-storm-note",
        "channel",
        "DeskNote",
        "2027-03-02T21:25:00Z",
        _STORM_STREAM,
        1,
        {
            "ref": _STORM_REF,
            "file_id": _STORM_FILE,
            "site": "cedar-ridge",
            "note": (
                "three night files, the last trailer does not match. "
                "The third copy has trailer_ok false, trailer_count 9, body_count 8."
            ),
        },
    )


def _partial_write() -> list[dict]:
    """The hospital file landed. The handset and the coverage window did not."""
    return [
        _part_request(),
        _part_coverage(),
        _part_handset(),
        _part_file(),
        _part_note(),
    ]


def _part_request() -> dict:
    return _command(
        "cmd-r2g-part-asked",
        "channel",
        "RequestAccepted",
        "2027-03-04T16:00:00Z",
        _PART_STREAM,
        1,
        {
            "ref": _PART_REF,
            "utterance": _PART_SENTENCE,
            "handset_delivered": False,
            "channel": "phone",
            "desk_region": "WA",
        },
    )


def _part_coverage() -> dict:
    return _command(
        "cmd-r2g-part-timeout",
        "payer",
        "CoverageDecided",
        "2027-03-04T16:10:00Z",
        _PART_STREAM,
        1,
        {
            "ref": _PART_REF,
            "answer": "timeout",
            "currency": "USD",
            "member_region": "WA",
        },
    )


def _part_handset() -> dict:
    return _command(
        "cmd-r2g-part-handset",
        "channel",
        "HandsetDispatch",
        "2027-03-04T16:20:00Z",
        _PART_STREAM,
        2,
        {
            "ref": _PART_REF,
            "idempotency_key": "r2g-part-handset",
            "attempt": 1,
            "status": "not-sent",
        },
    )


def _part_file() -> dict:
    return _command(
        "cmd-r2g-part-filed",
        "hospital",
        "SlotFiled",
        "2027-03-04T21:00:00Z",
        _PART_STREAM,
        1,
        {
            "ref": _PART_REF,
            "site": "cascade-seattle",
            "file_id": "cascade-part-2027-03-04",
            "clinic": "ENDO-CLN",
            "booking_date": "2027-03-04",
            "state": "WA",
            "trailer_ok": True,
            "trailer_count": 8,
            "body_count": 8,
        },
    )


def _part_note() -> dict:
    return _command(
        "cmd-r2g-part-note",
        "channel",
        "DeskNote",
        "2027-03-04T21:30:00Z",
        _PART_STREAM,
        3,
        {
            "ref": _PART_REF,
            "site": "cascade-seattle",
            "note": "the screen still shows the caller's sentence that the visit was booked",
        },
    )
