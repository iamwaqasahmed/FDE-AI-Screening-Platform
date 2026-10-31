"""Legacy desk feed. These commands are the behavior already on the desk."""

from __future__ import annotations

import hashlib


DRAFT_BODY = "Cedar Ridge draft hours close at 5:00 p.m. Pacific."
SCREEN_CODE = "4417"
REF = "LEG-2201"
FILE_ID = "cedar-legacy-2027-01-11"


def commands() -> list[dict]:
    """Return the legacy desk, channel, and hospital commands."""
    return (
        _desk_id()
        + _desk_channel()
        + _handoff_queue()
        +         _referral_feed()
        + _documents()
        + _schedule()
    )


def symptoms(commands: list[dict]) -> dict:
    """Return a JSON view of the defects visible on these commands."""
    return {
        "reused_screen_code": _reused_screen_code(commands),
        "stuck_caller": _stuck_caller(commands),
        "hidden_pending": _hidden_pending(commands),
        "no_slot_api": _no_slot_api(commands),
    }


def _desk_id() -> list[dict]:
    return [
        _command(
            "cmd-leg-desk-7710",
            "DeskSession",
            "channel",
            "2027-01-09T08:22:00Z",
            "leg-desk-7710",
            1,
            {
                "session_id": "sess-7710",
                "token_subject": "member-bc-4417",
                "factor": "screen-code-then-sms",
                "screen_code": SCREEN_CODE,
                "desk_region": "BC",
            },
        ),
        _command(
            "cmd-leg-desk-9920",
            "DeskSession",
            "channel",
            "2027-01-09T11:05:00Z",
            "leg-desk-9920",
            1,
            {
                "session_id": "sess-9920",
                "token_subject": "member-wa-2201",
                "factor": "screen-code-then-sms",
                "screen_code": SCREEN_CODE,
                "desk_region": "WA",
                "ref": REF,
            },
        ),
    ]


def _desk_channel() -> list[dict]:
    stream = "leg-channel-2201"
    return [
        _command(
            "cmd-leg-window-open",
            "WindowOpened",
            "channel",
            "2027-01-09T16:00:00Z",
            stream,
            1,
            {"ref": REF, "channel": "phone", "desk_region": "WA", "state": "open"},
        ),
        _command(
            "cmd-leg-provider-accept",
            "ProviderAccepted",
            "channel",
            "2027-01-09T16:04:00Z",
            stream,
            2,
            {"ref": REF, "channel": "phone", "desk_region": "WA"},
        ),
        _command(
            "cmd-leg-handset",
            "HandsetDelivered",
            "channel",
            "2027-01-09T16:11:00Z",
            stream,
            3,
            {"ref": REF, "channel": "sms", "status": "delivered"},
        ),
        _command(
            "cmd-leg-window-close",
            "WindowClosed",
            "channel",
            "2027-01-09T16:40:00Z",
            stream,
            4,
            {"ref": REF, "channel": "phone", "desk_region": "WA", "state": "closed"},
        ),
    ]


def _handoff_queue() -> list[dict]:
    stream = "leg-cc"
    return [
        _command(
            "cmd-leg-handoff-1",
            "HandoffQueued",
            "channel",
            "2027-01-09T17:15:00Z",
            stream,
            1,
            {
                "queue": "handoff",
                "call_id": "p-legacy-1",
                "person_id": "p-legacy-1",
                "desk_region": "WA",
            },
        ),
        _command(
            "cmd-leg-handoff-2",
            "HandoffQueued",
            "channel",
            "2027-01-09T17:22:00Z",
            stream,
            2,
            {
                "queue": "handoff",
                "call_id": "p-legacy-2",
                "person_id": "p-legacy-1",
                "previous_person_id": "p-legacy-1",
                "desk_region": "WA",
            },
        ),
    ]


def _referral_feed() -> list[dict]:
    return [
        _command(
            "cmd-leg-referral-hidden",
            "ReferralHidden",
            "hospital",
            "2027-01-10T15:00:00Z",
            "leg-eref-2201",
            1,
            {
                "ref": REF,
                "status": "pending",
                "coordinator_note": (
                    "The coordinator is waiting on the imaging addendum "
                    "before a clinic date is set."
                ),
                "patient_text": "Your referral is with the imaging clinic.",
                "patient_api": "omit",
            },
        )
    ]


def _schedule() -> list[dict]:
    stream = "leg-sched-cedar"
    return [
        _command(
            "cmd-leg-slot-file",
            "SlotFiled",
            "hospital",
            "2027-01-11T21:00:00Z",
            stream,
            1,
            {
                "ref": REF,
                "site": "cedar-ridge",
                "file_id": FILE_ID,
                "clinic": "ENDO-CLN",
                "booking_date": "2027-01-11",
                "state": "WA",
            },
        ),
        _command(
            "cmd-leg-slot-api",
            "SlotApiAbsent",
            "hospital",
            "2027-01-11T21:05:00Z",
            stream,
            2,
            {"ref": REF, "site": "cedar-ridge", "file_id": FILE_ID},
        ),
    ]


def _documents() -> list[dict]:
    return [
        _command(
            "cmd-leg-draft-doc",
            "DocumentChanged",
            "hospital",
            "2027-01-10T18:30:00Z",
            "leg-dms-draft",
            1,
            {
                "doc_id": "leg-dms-draft",
                "version": "2027-01-10-draft",
                "status": "draft",
                "audience": "public",
                "language": "en",
                "body": DRAFT_BODY,
                "content_hash": _content_hash(DRAFT_BODY),
            },
        )
    ]


def _reused_screen_code(commands: list[dict]) -> dict:
    grouped: dict[str, list[dict]] = {}
    for row in commands:
        if row.get("type") != "DeskSession":
            continue
        payload = row.get("payload") or {}
        code = payload.get("screen_code")
        if code is None:
            continue
        grouped.setdefault(str(code), []).append(row)
    for code, rows in grouped.items():
        ordered = sorted(rows, key=lambda item: item["occurred_at"])
        mornings = {item["occurred_at"][:10] for item in ordered}
        if len(ordered) < 2 or len(mornings) != 1:
            continue
        return {
            "screen_code": code,
            "morning": ordered[0]["occurred_at"][:10],
            "sessions": [_session_view(item) for item in ordered],
        }
    return {}


def _session_view(row: dict) -> dict:
    payload = row["payload"]
    return {
        "command_id": row["command_id"],
        "session_id": payload.get("session_id"),
        "token_subject": payload.get("token_subject"),
        "factor": payload.get("factor"),
        "occurred_at": row["occurred_at"],
    }


def _stuck_caller(commands: list[dict]) -> dict:
    earlier: dict | None = None
    stuck: dict | None = None
    stuck_id = ""
    for row in commands:
        payload = row.get("payload") or {}
        call_id = payload.get("call_id")
        person_id = payload.get("person_id")
        if call_id == "p-legacy-1" and person_id == "p-legacy-1":
            earlier = payload
        if call_id == "p-legacy-2" and person_id == "p-legacy-1":
            stuck = payload
            stuck_id = row["command_id"]
    if stuck is None:
        return {}
    return {
        "command_id": stuck_id,
        "queue": stuck.get("queue"),
        "earlier_call_id": None if earlier is None else earlier.get("call_id"),
        "call_id": stuck.get("call_id"),
        "person_id": stuck.get("person_id"),
        "previous_person_id": stuck.get("previous_person_id"),
    }


def _hidden_pending(commands: list[dict]) -> dict:
    for row in commands:
        if row.get("type") != "ReferralHidden":
            continue
        payload = row.get("payload") or {}
        if payload.get("status") != "pending":
            continue
        patient_text = str(payload.get("patient_text") or "")
        return {
            "command_id": row["command_id"],
            "ref": payload.get("ref"),
            "status": payload["status"],
            "coordinator_note": payload.get("coordinator_note"),
            "patient_text": patient_text,
            "patient_text_omits_pending": "pending" not in patient_text.lower(),
            "patient_api": payload.get("patient_api"),
        }
    return {}


def _no_slot_api(commands: list[dict]) -> dict:
    absent = None
    file_ids: list[str] = []
    for row in commands:
        payload = row.get("payload") or {}
        if payload.get("site") != "cedar-ridge":
            continue
        if row.get("type") == "SlotFiled" and payload.get("file_id"):
            file_ids.append(str(payload["file_id"]))
        if row.get("type") == "SlotApiAbsent":
            absent = row
    if absent is None:
        return {}
    return {
        "command_id": absent["command_id"],
        "site": "cedar-ridge",
        "event": "SlotApiAbsent",
        "nightly_file_ids": file_ids,
    }


def _content_hash(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


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
