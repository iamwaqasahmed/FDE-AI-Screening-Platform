"""Northline completeness feeds. Students see drafts; the corrected clinic stays off the read model."""

from __future__ import annotations

import hashlib
import json

DRAFT_DOC_ID = "dms-draft-fraser"
DRAFT_BODY = "Fraser Burnaby draft hours close at 4:00 p.m. Pacific."
STALE_CLINIC = "Cascade day clinic"
CORRECTED_CLINIC = "Cascade endocrine"
FRASER_SITE = "fraser-burnaby"
CEDAR_SITE = "cedar-ridge"
CASCADE_SITE = "cascade-seattle"
FRASER_REF = "R2C-FR"
CEDAR_REF = "R2C-CD"
HAND_REF = "R2C-HAND"
LEAVE_REF = "R2C-LEAVE"
CASCADE_REF = "R2C-CS"
LEAVE_MORNING = "2027-01-18"
CLINICIAN_ID = "clin-r2c-endo"
SESSION_ID = "sess-r2c-leave"

_AUTHORITIES = frozenset({"hospital", "channel", "payer"})
_DOC_FIELDS = (
    "doc_id",
    "version",
    "status",
    "audience",
    "language",
    "body",
    "content_hash",
)
_SLOT_FIELDS = ("ref", "booking_date", "file_id", "site")


def commands() -> list[dict]:
    """Return 9 January 2027 commands. Ids start with cmd-r2c- and streams with r2c-."""
    rows = [
        *_draft_commands(),
        *_cascade_commands(),
        *_export_commands(),
        *_delivery_commands(),
        *_leave_commands(),
    ]
    _require_commands(rows)
    return rows


def feeds(commands: list[dict]) -> dict:
    """Return student-visible payloads. The cascade list keeps the stale clinic name."""
    return {
        "draft_docs": _draft_docs(commands),
        "cascade_read_model": _cascade_read_model(commands),
        "fraser_feed": _export_feed(commands, FRASER_SITE, FRASER_REF, CEDAR_REF),
        "cedar_feed": _export_feed(commands, CEDAR_SITE, CEDAR_REF, FRASER_REF),
        "delivery_split": _delivery_split(commands),
        "leave": _leave_feed(commands),
    }


def _draft_commands() -> list[dict]:
    return [
        _command(
            "cmd-r2c-draft-fraser",
            "hospital",
            "DocumentChanged",
            "2027-01-11T18:00:00Z",
            "r2c-dms-fraser",
            1,
            {
                "doc_id": DRAFT_DOC_ID,
                "version": "2027-01-draft",
                "status": "draft",
                "audience": "public",
                "language": "en",
                "body": DRAFT_BODY,
                "content_hash": _sha256(DRAFT_BODY),
                "site": FRASER_SITE,
            },
        )
    ]


def _cascade_commands() -> list[dict]:
    stream = "r2c-cascade-read"
    return [
        _command(
            "cmd-r2c-cascade-read",
            "hospital",
            "ReadModelServed",
            "2027-01-12T17:00:00Z",
            stream,
            1,
            {
                "site": CASCADE_SITE,
                "ref": CASCADE_REF,
                "clinic_name": STALE_CLINIC,
                "rev": 1,
            },
        ),
        _command(
            "cmd-r2c-cascade-correct",
            "hospital",
            "ReferralCorrected",
            "2027-01-12T19:30:00Z",
            stream,
            2,
            {
                "site": CASCADE_SITE,
                "ref": CASCADE_REF,
                "clinic_name": CORRECTED_CLINIC,
                "rev": 2,
            },
        ),
    ]


def _export_commands() -> list[dict]:
    return [
        _command(
            "cmd-r2c-feed-fraser",
            "hospital",
            "FeedExported",
            "2027-01-13T16:00:00Z",
            "r2c-export-fraser",
            1,
            {"site": FRASER_SITE, "ref": FRASER_REF},
        ),
        _command(
            "cmd-r2c-feed-cedar",
            "hospital",
            "FeedExported",
            "2027-01-13T16:10:00Z",
            "r2c-export-cedar",
            1,
            {"site": CEDAR_SITE, "ref": CEDAR_REF},
        ),
    ]


def _delivery_commands() -> list[dict]:
    stream = "r2c-hand"
    return [
        _command(
            "cmd-r2c-hand-accept",
            "channel",
            "ProviderAccepted",
            "2027-01-14T17:02:00Z",
            stream,
            1,
            {"ref": HAND_REF, "channel": "phone", "handset_delivered": False},
        ),
        _command(
            "cmd-r2c-hand-deliver",
            "channel",
            "HandsetDelivered",
            "2027-01-14T17:18:00Z",
            stream,
            2,
            {"ref": HAND_REF, "channel": "sms", "handset_delivered": True},
        ),
    ]


def _leave_commands() -> list[dict]:
    session = {
        "ref": LEAVE_REF,
        "session_id": SESSION_ID,
        "clinician_id": CLINICIAN_ID,
        "site": FRASER_SITE,
        "local_date": LEAVE_MORNING,
        "local_time": "08:10",
        "zone": "America/Vancouver",
    }
    posted = {
        "ref": LEAVE_REF,
        "session_id": SESSION_ID,
        "clinician_id": CLINICIAN_ID,
        "site": FRASER_SITE,
        "local_date": LEAVE_MORNING,
        "local_time": "09:05",
        "zone": "America/Vancouver",
    }
    return [
        _command(
            "cmd-r2c-leave-session",
            "channel",
            "DeskSession",
            "2027-01-18T16:10:00Z",
            "r2c-leave-desk",
            1,
            session,
        ),
        _command(
            "cmd-r2c-leave-posted",
            "hospital",
            "LeavePosted",
            "2027-01-18T17:05:00Z",
            "r2c-leave-hr",
            1,
            posted,
        ),
    ]


def _draft_docs(commands: list[dict]) -> list[dict]:
    shown = []
    for row in commands:
        if row.get("type") != "DocumentChanged":
            continue
        payload = row["payload"]
        if payload.get("doc_id") != DRAFT_DOC_ID or payload.get("status") != "draft":
            continue
        item = _show(
            row,
            (
                "doc_id",
                "version",
                "status",
                "audience",
                "language",
                "body",
                "content_hash",
                "site",
            ),
        )
        item.pop("hint", None)
        shown.append(item)
    return shown


def _cascade_read_model(commands: list[dict]) -> list[dict]:
    shown = []
    for row in commands:
        if row.get("type") != "ReadModelServed":
            continue
        item = _show(row, ("site", "ref", "clinic_name", "rev"))
        if CORRECTED_CLINIC in json.dumps(item):
            raise ValueError("cascade read model includes the corrected clinic name")
        shown.append(item)
    return shown


def _export_feed(commands: list[dict], site: str, ref: str, other_ref: str) -> list[dict]:
    shown = []
    for row in commands:
        if row.get("type") != "FeedExported":
            continue
        payload = row["payload"]
        if payload.get("site") != site or payload.get("ref") != ref:
            continue
        item = _show(row, ("site", "ref"))
        if other_ref in json.dumps(item):
            raise ValueError(other_ref)
        shown.append(item)
    return shown


def _delivery_split(commands: list[dict]) -> list[dict]:
    rows = [
        row
        for row in commands
        if row.get("type") in ("ProviderAccepted", "HandsetDelivered")
        and (row.get("payload") or {}).get("ref") == HAND_REF
    ]
    return [_show(row, ("ref", "channel", "handset_delivered")) for row in _by_time(rows)]


def _leave_feed(commands: list[dict]) -> list[dict]:
    rows = [
        row
        for row in commands
        if row.get("type") in ("DeskSession", "LeavePosted")
        and (row.get("payload") or {}).get("ref") == LEAVE_REF
    ]
    keys = (
        "ref",
        "session_id",
        "clinician_id",
        "site",
        "local_date",
        "local_time",
        "zone",
    )
    return [_show(row, keys) for row in _by_time(rows)]


def _show(row: dict, keys: tuple[str, ...]) -> dict:
    payload = row["payload"]
    item = {key: payload[key] for key in keys}
    item["event"] = row["type"]
    item["occurred_at"] = row["occurred_at"]
    item["stream_id"] = row["stream_id"]
    return item


def _by_time(rows: list[dict]) -> list[dict]:
    return sorted(rows, key=lambda row: row["occurred_at"])


def _sha256(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def _command(
    command_id: str,
    authority: str,
    event_type: str,
    occurred_at: str,
    stream_id: str,
    stream_rev: int,
    payload: dict,
) -> dict:
    if not command_id.startswith("cmd-r2c-"):
        raise ValueError(command_id)
    if not stream_id.startswith("r2c-"):
        raise ValueError(stream_id)
    if authority not in _AUTHORITIES:
        raise ValueError(authority)
    if not (occurred_at.startswith("2027-01-") and occurred_at.endswith("Z")):
        raise ValueError(occurred_at)
    return {
        "command_id": command_id,
        "authority": authority,
        "type": event_type,
        "occurred_at": occurred_at,
        "stream_id": stream_id,
        "stream_rev": stream_rev,
        "payload": payload,
    }


def _require_commands(rows: list[dict]) -> None:
    if not 8 <= len(rows) <= 12:
        raise ValueError(len(rows))
    for row in rows:
        _require_row(row)
    _require_relationships(rows)


def _require_row(row: dict) -> None:
    payload = row["payload"]
    kind = row["type"]
    if kind == "DocumentChanged":
        _require_document(payload)
    elif kind == "CoverageDecided":
        if "ref" not in payload or "answer" not in payload:
            raise ValueError(kind)
    elif kind == "SlotFiled":
        missing = [key for key in _SLOT_FIELDS if key not in payload]
        if missing:
            raise ValueError(",".join(missing))
    elif kind == "ReadModelServed":
        if CORRECTED_CLINIC in json.dumps(payload):
            raise ValueError("read model event includes the corrected clinic name")
        if payload.get("clinic_name") != STALE_CLINIC or payload.get("rev") != 1:
            raise ValueError("read model rev")
    elif kind == "ProviderAccepted" and payload.get("handset_delivered") is not False:
        raise ValueError("accept is not delivery")
    elif kind == "HandsetDelivered" and payload.get("handset_delivered") is not True:
        raise ValueError("handset flag")


def _require_document(payload: dict) -> None:
    missing = [key for key in _DOC_FIELDS if key not in payload]
    if missing:
        raise ValueError(",".join(missing))
    if payload["content_hash"] != _sha256(payload["body"]):
        raise ValueError("content_hash")
    if "hint" in payload:
        raise ValueError("hint")


def _require_relationships(rows: list[dict]) -> None:
    grouped: dict[str, list[dict]] = {}
    for row in rows:
        grouped.setdefault(row["type"], []).append(row)
    read_model = grouped["ReadModelServed"][0]
    corrected = grouped["ReferralCorrected"][0]
    if corrected["occurred_at"] <= read_model["occurred_at"]:
        raise ValueError("correction order")
    if corrected["payload"].get("clinic_name") != CORRECTED_CLINIC:
        raise ValueError("correction name")
    exports = grouped["FeedExported"]
    if len({row["stream_id"] for row in exports}) != len(exports):
        raise ValueError("feed streams")
    accept = grouped["ProviderAccepted"][0]
    delivered = grouped["HandsetDelivered"][0]
    if delivered["occurred_at"] <= accept["occurred_at"]:
        raise ValueError("delivery order")
    session = grouped["DeskSession"][0]
    posted = grouped["LeavePosted"][0]
    if posted["occurred_at"] <= session["occurred_at"]:
        raise ValueError("leave order")
    if session["payload"].get("local_date") != posted["payload"].get("local_date"):
        raise ValueError("leave morning")
