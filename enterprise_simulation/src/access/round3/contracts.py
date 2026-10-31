"""Contract MA-2024 between the Vancouver desk and harbor-coverage.

The list order is the append order. ``occurred_at`` is the time on the row.
"""

from __future__ import annotations

import hashlib

_CONTRACT = "MA-2024"
_DOC = "MA-2024"
_STREAM = "r3d-ma-2024"
_DESK = "vancouver-desk"
_PAYER = "harbor-coverage"
_AUDIENCE = "finance"
_LANGUAGE = "en"
_WEEK = 'The office week is printed as "Monday through Friday". '
_CURRENCY = "The currency of record for BC members is CAD. "
_LEAD = f"Contract {_CONTRACT} between the Vancouver desk and {_PAYER}. " + _WEEK + _CURRENCY
_V1_BODY = _LEAD + "The fee clause is 12 CAD."
_V2_BODY = _LEAD + "The fee clause changes from 12 CAD to 14 CAD."
_TOP = {
    "command_id",
    "authority",
    "type",
    "occurred_at",
    "stream_id",
    "stream_rev",
    "payload",
}
_AUTHORITIES = frozenset({"hospital", "channel", "payer"})
_DOC_KEYS = frozenset(
    {
        "contract_id",
        "doc_id",
        "version",
        "status",
        "audience",
        "language",
        "body",
        "content_hash",
    }
)


def commands() -> list[dict]:
    """Return the contract commands in append order."""
    rows = (
        _opened()
        + _version_one()
        + _retention()
        + _printed()
        + _packet()
        + _version_two()
        + _correction()
    )
    _ensure(rows)
    return rows


def _opened() -> list[dict]:
    """Desk and payer each record the same contract."""
    return [
        _command(
            "cmd-r3d-desk-open",
            "channel",
            "ContractRecorded",
            "2024-04-08T16:20:00Z",
            1,
            _parties(),
        ),
        _command(
            "cmd-r3d-payer-open",
            "payer",
            "ContractRecorded",
            "2024-04-12T18:05:00Z",
            1,
            _parties(),
        ),
    ]


def _version_one() -> list[dict]:
    """Version 1 body with status in force on this row."""
    return [_document("cmd-r3d-doc-v1", "2024-06-03T17:00:00Z", 1, "1", "in_force", _V1_BODY)]


def _retention() -> list[dict]:
    """Two notes on one contract id. Both stay in the list."""
    return [
        _command(
            "cmd-r3d-keep-years",
            "hospital",
            "RetentionNote",
            "2024-06-03T17:40:00Z",
            2,
            {"contract_id": _CONTRACT, "doc_id": _DOC, "keep_years": 7},
        ),
        _command(
            "cmd-r3d-archive-after",
            "payer",
            "RetentionNote",
            "2025-11-18T20:10:00Z",
            2,
            {
                "contract_id": _CONTRACT,
                "doc_id": _DOC,
                "archive_after": "2026-01-01",
            },
        ),
    ]


def _printed() -> list[dict]:
    """Version field 2. Body and content_hash are the version 1 text."""
    return [
        _command(
            "cmd-r3d-print",
            "channel",
            "PrintedCopy",
            "2026-09-16T16:45:00Z",
            2,
            {
                "contract_id": _CONTRACT,
                "doc_id": _DOC,
                "version": "2",
                "status": "in_force",
                "audience": _AUDIENCE,
                "language": _LANGUAGE,
                "body": _V1_BODY,
                "content_hash": _sha256(_V1_BODY),
            },
        )
    ]


def _packet() -> list[dict]:
    """December log line, placed before the August-dated amendment."""
    return [
        _command(
            "cmd-r3d-packet-logged",
            "payer",
            "AmendmentLogged",
            "2026-12-15T21:10:00Z",
            3,
            {
                "contract_id": _CONTRACT,
                "doc_id": _DOC,
                "note": (
                    f"Amendment packet for contract {_CONTRACT} logged at {_PAYER}."
                ),
            },
        )
    ]


def _version_two() -> list[dict]:
    """Amendment dated 2026-08-01, then a status row for version 1."""
    return [
        _document("cmd-r3d-doc-v2", "2026-08-01", 3, "2", "in_force", _V2_BODY),
        _command(
            "cmd-r3d-v1-status",
            "hospital",
            "StatusNoted",
            "2026-08-01",
            4,
            {
                "contract_id": _CONTRACT,
                "doc_id": _DOC,
                "version": "1",
                "status": "superseded",
            },
        ),
    ]


def _correction() -> list[dict]:
    """Authority time 2026-08-01. recorded_on is 2026-12-15."""
    return [
        _command(
            "cmd-r3d-backdate",
            "channel",
            "BackdatedCorrection",
            "2026-08-01",
            3,
            {
                "contract_id": _CONTRACT,
                "doc_id": _DOC,
                "version": "2",
                "recorded_on": "2026-12-15",
                "note": "The August amendment was entered in December.",
                "subject_command_id": "cmd-r3d-doc-v2",
            },
        )
    ]


def _parties() -> dict:
    return {
        "contract_id": _CONTRACT,
        "doc_id": _DOC,
        "desk": _DESK,
        "payer": _PAYER,
    }


def _document(
    command_id: str,
    occurred_at: str,
    stream_rev: int,
    version: str,
    status: str,
    body: str,
) -> dict:
    return _command(
        command_id,
        "hospital",
        "DocumentChanged",
        occurred_at,
        stream_rev,
        {
            "contract_id": _CONTRACT,
            "doc_id": _DOC,
            "version": version,
            "status": status,
            "audience": _AUDIENCE,
            "language": _LANGUAGE,
            "body": body,
            "content_hash": _sha256(body),
        },
    )


def _sha256(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def _command(
    command_id: str,
    authority: str,
    event_type: str,
    occurred_at: str,
    stream_rev: int,
    payload: dict,
) -> dict:
    return {
        "command_id": command_id,
        "authority": authority,
        "type": event_type,
        "occurred_at": occurred_at,
        "stream_id": _STREAM,
        "stream_rev": stream_rev,
        "payload": dict(payload),
    }


def _ensure(rows: list[dict]) -> None:
    if not 8 <= len(rows) <= 12:
        raise ValueError(len(rows))
    seen: dict[tuple[str, str], int] = {}
    ids: list[str] = []
    for row in rows:
        if set(row) != _TOP:
            raise ValueError(row["command_id"])
        if not row["command_id"].startswith("cmd-r3d-"):
            raise ValueError(row["command_id"])
        if not str(row["stream_id"]).startswith("r3d-"):
            raise ValueError(row["stream_id"])
        if row["authority"] not in _AUTHORITIES:
            raise ValueError(row["authority"])
        day = str(row["occurred_at"])[:10]
        if day < "2024-04-01" or day > "2027-02-01":
            raise ValueError(row["command_id"])
        key = (row["authority"], row["stream_id"])
        rev = int(row["stream_rev"])
        if rev != seen.get(key, 0) + 1:
            raise ValueError(row["command_id"])
        seen[key] = rev
        ids.append(row["command_id"])
    if len(ids) != len(set(ids)):
        raise ValueError("command_id")
    _ensure_bodies(rows)
    _ensure_retention(rows)
    _ensure_order(rows)


def _ensure_bodies(rows: list[dict]) -> None:
    version_one = _by_id(rows, "cmd-r3d-doc-v1")
    version_two = _by_id(rows, "cmd-r3d-doc-v2")
    printed = _by_id(rows, "cmd-r3d-print")
    status = _by_id(rows, "cmd-r3d-v1-status")
    correction = _by_id(rows, "cmd-r3d-backdate")
    first = version_one["payload"]
    second = version_two["payload"]
    copy = printed["payload"]
    if set(first) != _DOC_KEYS or set(second) != _DOC_KEYS:
        raise ValueError("document")
    if first["status"] != "in_force" or second["status"] != "in_force":
        raise ValueError("status")
    if first["version"] != "1" or second["version"] != "2":
        raise ValueError("version")
    if version_two["occurred_at"] != "2026-08-01":
        raise ValueError("occurred_at")
    if first["content_hash"] != _sha256(first["body"]):
        raise ValueError("content_hash")
    if second["content_hash"] != _sha256(second["body"]):
        raise ValueError("content_hash")
    if "Monday through Friday" not in first["body"]:
        raise ValueError("week")
    if "currency of record for BC members is CAD" not in first["body"]:
        raise ValueError("currency")
    if "12 CAD" not in first["body"] or "14 CAD" not in second["body"]:
        raise ValueError("fee")
    if "12 CAD" not in second["body"]:
        raise ValueError("fee")
    if copy["body"] != first["body"] or copy["version"] != "2":
        raise ValueError("print")
    if copy["status"] != "in_force":
        raise ValueError("print")
    if copy["content_hash"] != _sha256(first["body"]):
        raise ValueError("print")
    if copy["content_hash"] == _sha256(second["body"]):
        raise ValueError("print")
    if status["payload"]["version"] != "1" or status["payload"]["status"] != "superseded":
        raise ValueError("status")
    if correction["occurred_at"] != "2026-08-01":
        raise ValueError("occurred_at")
    if correction["payload"]["recorded_on"] != "2026-12-15":
        raise ValueError("recorded_on")
    if correction["payload"]["note"] != "The August amendment was entered in December.":
        raise ValueError("note")
    if correction["payload"]["subject_command_id"] != "cmd-r3d-doc-v2":
        raise ValueError("subject_command_id")


def _ensure_retention(rows: list[dict]) -> None:
    notes = [row for row in rows if row["type"] == "RetentionNote"]
    if len(notes) != 2:
        raise ValueError("retention")
    years = notes[0]["payload"]
    archive = notes[1]["payload"]
    if years["keep_years"] != 7 or archive["archive_after"] != "2026-01-01":
        raise ValueError("retention")
    if years["contract_id"] != _CONTRACT or archive["contract_id"] != _CONTRACT:
        raise ValueError("contract_id")
    if years["contract_id"] != archive["contract_id"]:
        raise ValueError("contract_id")


def _ensure_order(rows: list[dict]) -> None:
    ids = [row["command_id"] for row in rows]
    print_at = ids.index("cmd-r3d-print")
    packet_at = ids.index("cmd-r3d-packet-logged")
    version_two_at = ids.index("cmd-r3d-doc-v2")
    status_at = ids.index("cmd-r3d-v1-status")
    correction_at = ids.index("cmd-r3d-backdate")
    version_one_at = ids.index("cmd-r3d-doc-v1")
    if not version_one_at < print_at < packet_at < version_two_at < status_at < correction_at:
        raise ValueError("order")


def _by_id(rows: list[dict], command_id: str) -> dict:
    return next(row for row in rows if row["command_id"] == command_id)
