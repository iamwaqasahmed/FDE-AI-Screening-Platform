"""Optional incident overlays.

The base history already contains the opening defects. ``reset`` rebuilds
that history and leaves these lists unused. A caller appends one named
list when that extra incident is wanted. Command ids and stream revisions
are unused by the base log, so the append does not collide.
"""

from __future__ import annotations

from access.doc_hash import content_hash

_FRASER_DRAFT = "Fraser Burnaby evening clinic closes at 9:00 p.m. Pacific."
_FRASER_FORCE = "Fraser Burnaby clinic closes at 4:00 p.m. Pacific."


def names() -> list[str]:
    """Return the overlay names in registry order."""
    return ["partner-outage", "hours-served-stale"]


def overlay(name: str) -> list[dict]:
    """Return a fresh command list for one overlay."""
    builders = {
        "partner-outage": _partner_outage,
        "hours-served-stale": _hours_served_stale,
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


def _partner_outage() -> list[dict]:
    """Harbor times out, while the morning board still shows the last yes."""
    ref = "SCN-OUT-1"
    return [
        _command(
            "cmd-scn-out-ask",
            "channel",
            "RequestAccepted",
            "2027-01-15T15:00:00Z",
            "scn-out-ask",
            1,
            {
                "ref": ref,
                "utterance": "waiting on harbor coverage this morning",
                "handset_delivered": False,
                "channel": "web",
                "desk_region": "WA",
            },
        ),
        _command(
            "cmd-scn-out-cover",
            "payer",
            "CoverageDecided",
            "2027-01-15T15:10:00Z",
            "scn-out-cover",
            1,
            {
                "ref": ref,
                "answer": "timeout",
                "currency": "USD",
                "member_region": "WA",
            },
        ),
        _command(
            "cmd-scn-out-hook",
            "channel",
            "WebhookAttempt",
            "2027-01-15T15:11:00Z",
            "scn-out-hook",
            1,
            {
                "ref": ref,
                "partner": "harbor-coverage",
                "attempt": 4,
                "status": "timeout",
            },
        ),
        _command(
            "cmd-scn-out-board",
            "hospital",
            "CacheStored",
            "2027-01-15T15:12:00Z",
            "scn-out-board",
            1,
            {
                "ref": ref,
                "eligible": True,
                "window_present": False,
                "source": "morning-board-last-yes",
            },
        ),
        _command(
            "cmd-scn-out-note",
            "channel",
            "DeskNote",
            "2027-01-15T15:20:00Z",
            "scn-out-note",
            1,
            {
                "ref": ref,
                "note": "the morning board still shows the last yes",
            },
        ),
    ]


def _hours_served_stale() -> list[dict]:
    """Fraser hours move to 16:00, and a patient in Burnaby is still told 21:00."""
    return [
        _command(
            "cmd-scn-hrs-draft",
            "hospital",
            "DocumentChanged",
            "2027-01-15T16:00:00Z",
            "scn-hrs-fraser",
            1,
            {
                "doc_id": "hours-fraser",
                "version": "draft-close-21",
                "status": "superseded",
                "audience": "public",
                "close_local": "21:00",
                "timezone": "America/Vancouver",
                "language": "en",
                "body": _FRASER_DRAFT,
                "content_hash": content_hash(_FRASER_DRAFT),
            },
        ),
        _command(
            "cmd-scn-hrs-force",
            "hospital",
            "DocumentChanged",
            "2027-01-15T20:00:00Z",
            "scn-hrs-fraser",
            2,
            {
                "doc_id": "hours-fraser",
                "version": "close-16",
                "status": "in_force",
                "audience": "public",
                "close_local": "16:00",
                "timezone": "America/Vancouver",
                "language": "en",
                "body": _FRASER_FORCE,
                "content_hash": content_hash(_FRASER_FORCE),
            },
        ),
        _command(
            "cmd-scn-hrs-served",
            "channel",
            "ServedDocument",
            "2027-01-15T22:10:00Z",
            "scn-hrs-served",
            1,
            {
                "doc_id": "hours-fraser",
                "version": "draft-close-21",
                "served_version": "draft-close-21",
                "site": "fraser-burnaby",
                "city": "Burnaby",
                "region": "BC",
                "told_close_local": "21:00",
            },
        ),
        _command(
            "cmd-scn-hrs-told",
            "channel",
            "DeskNote",
            "2027-01-15T22:15:00Z",
            "scn-hrs-told",
            1,
            {
                "doc_id": "hours-fraser",
                "site": "fraser-burnaby",
                "city": "Burnaby",
                "region": "BC",
                "told_close_local": "21:00",
                "note": "a patient in Burnaby is told 21:00",
            },
        ),
    ]
