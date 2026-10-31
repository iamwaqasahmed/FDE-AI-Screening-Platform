"""Recorded accesses from 9–11 January 2027. Payloads use identifiers."""

from __future__ import annotations

from access.cases_documents import SUMMER, WINTER
from access.doc_hash import content_hash
from access.symptoms import BYTE_INDEX, HOST, NATIONAL_ID, SHADOW

_ROW_KEYS = (
    "command_id",
    "authority",
    "type",
    "occurred_at",
    "stream_id",
    "stream_rev",
)

_PAYLOAD_KEYS = (
    "role",
    "ref",
    "object_where",
    "grant",
    "action",
    "host",
    "where",
    "on_disk_token",
    "call_id",
    "job",
    "endpoint_region",
    "destination_region",
    "processor_region",
    "member_desk",
    "http_status",
    "packet_id",
    "packet_docs",
    "attached_doc_id",
    "attached_where",
    "reason",
    "reviewer",
    "product",
    "screen_field",
    "screen_value",
    "shadow_id",
    "wrote_slot",
    "doc_id",
    "version",
    "stored_hash",
    "body_hash",
)

_DESK = "America/Vancouver"
_LETTER = "REF-4417"
_ON_DISK = "900-00-4417"


def commands() -> list[dict]:
    """Return the legacy audit commands in time order."""
    return [
        _desk_download(),
        _national_id(),
        _hours_hash(),
        _letter_copy(),
        _letter_call(),
        _wage_attachment(),
        _break_glass(),
        _screen_approval(),
        _shadow_write(),
    ]


def audit_view(commands: list[dict]) -> list[dict]:
    """Return one student-visible row per command.

    Envelope fields are copied. Payload fields on the view list are copied.
    A null reviewer stays null.
    """
    return [_visible_row(command) for command in commands]


def _visible_row(command: dict) -> dict:
    row = {key: command[key] for key in _ROW_KEYS}
    payload = command["payload"]
    for key in _PAYLOAD_KEYS:
        if key in payload:
            row[key] = payload[key]
    return row


def _command(
    command_id: str,
    authority: str,
    event_type: str,
    occurred_at: str,
    stream_id: str,
    payload: dict,
) -> dict:
    return {
        "command_id": command_id,
        "authority": authority,
        "type": event_type,
        "occurred_at": occurred_at,
        "stream_id": stream_id,
        "stream_rev": 1,
        "payload": payload,
    }


def _where(name: str) -> str:
    return next(item["where"] for item in BYTE_INDEX if item["name"] == name)


def _on_disk_token() -> str:
    token = NATIONAL_ID.strip().split()[-1]
    if token != _ON_DISK:
        raise ValueError("unexpected token in the national-id file")
    return token


def _hours_packet_docs() -> list[str]:
    docs: list[str] = []
    for item in BYTE_INDEX:
        where = item["where"]
        if where.startswith("document hours-") or where.startswith("document leaflet-"):
            docs.append(where.removeprefix("document "))
    return docs


def _desk_download() -> dict:
    return _command(
        "cmd-sec-desk-download",
        "channel",
        "AccessRecorded",
        "2027-01-09T18:40:00Z",
        "sec-desk-download",
        {
            "role": "desk-clerk",
            "ref": _LETTER,
            "object_where": _where("letter"),
            "grant": "screen text only",
            "action": "file-download",
        },
    )


def _national_id() -> dict:
    return _command(
        "cmd-sec-national-id",
        "channel",
        "AccessRecorded",
        "2027-01-09T19:12:00Z",
        "sec-national-id",
        {
            "host": HOST["host"],
            "action": "file-read",
            "where": _where("national-id"),
            "on_disk_token": _on_disk_token(),
        },
    )


def _hours_hash() -> dict:
    return _command(
        "cmd-sec-hours-hash",
        "hospital",
        "HashRecorded",
        "2027-01-10T02:40:00Z",
        "sec-hours-hash",
        {
            "doc_id": "hours-cedar-copy",
            "version": "2027-winter",
            "stored_hash": content_hash(WINTER),
            "body_hash": content_hash(SUMMER),
        },
    )


def _letter_copy() -> dict:
    return _command(
        "cmd-sec-letter-copy",
        "hospital",
        "CopyRecorded",
        "2027-01-10T16:12:00Z",
        "sec-letter-copy",
        {
            "call_id": "call-west",
            "ref": _LETTER,
            "object_where": _where("letter"),
            "job": "copy",
            "endpoint_region": "us-west-2",
            "processor_region": "us-east-1",
            "destination_region": "us-east-1",
            "member_desk": _DESK,
            "http_status": 200,
        },
    )


def _letter_call() -> dict:
    return _command(
        "cmd-sec-letter-call",
        "payer",
        "CallRecorded",
        "2027-01-10T16:20:00Z",
        "sec-letter-call",
        {
            "call_id": "call-match",
            "ref": _LETTER,
            "object_where": _where("letter"),
            "endpoint_region": "ca-central-1",
            "processor_region": "ca-central-1",
            "member_desk": _DESK,
            "http_status": 200,
        },
    )


def _wage_attachment() -> dict:
    return _command(
        "cmd-sec-wage-attach",
        "hospital",
        "AttachmentRecorded",
        "2027-01-10T18:05:00Z",
        "sec-hours-packet",
        {
            "packet_id": "hours-packet-cedar",
            "packet_docs": _hours_packet_docs(),
            "attached_doc_id": "wage-band",
            "attached_where": _where("wage"),
        },
    )


def _break_glass() -> dict:
    return _command(
        "cmd-sec-break-glass",
        "hospital",
        "BreakGlassRecorded",
        "2027-01-11T04:12:00Z",
        "sec-break-glass",
        {
            "role": "on-call physician",
            "ref": _LETTER,
            "object_where": _where("letter"),
            "action": "break-glass",
            "reason": "Night coverage for REF-4417 at the Vancouver desk.",
            "reviewer": None,
        },
    )


def _screen_approval() -> dict:
    return _command(
        "cmd-sec-screen-approval",
        "channel",
        "AccessRecorded",
        "2027-01-11T16:40:00Z",
        "sec-screen-approval",
        {
            "product": "northline-assistant-2024",
            "ref": _LETTER,
            "object_where": _where("letter"),
            "action": "screen-render",
            "screen_field": "approval_accepted",
            "screen_value": "APR-4417",
        },
    )


def _shadow_write() -> dict:
    return _command(
        "cmd-sec-shadow-write",
        "hospital",
        "AccessRecorded",
        "2027-01-11T21:06:00Z",
        "sec-shadow-write",
        {
            "shadow_id": SHADOW["shadow_id"],
            "ref": _LETTER,
            "action": "slot-write",
            "wrote_slot": SHADOW["wrote_slot"],
        },
    )
