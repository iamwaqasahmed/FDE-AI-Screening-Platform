"""Student-visible extracts beyond the three logs."""

from __future__ import annotations

import json
from pathlib import Path

from access.symptoms import (
    ASKS,
    BYTE_INDEX,
    CALIBRATION,
    CALLS,
    HOST,
    NATIONAL_ID,
    SHADOW,
    assistant_screen,
    served_document,
)

FOCUS = ("REF-4417", "REF-8801", "REF-2290", "REF-3304", "REF-5510", "PERMIT-12", "POISON-1", "WEEKEND-1")


def write_views(pack: Path, hospital: list[dict], channel: list[dict]) -> None:
    extracts = pack / "extracts"
    extracts.mkdir(parents=True, exist_ok=True)
    documents = [
        row["payload"] | {"occurred_at": row["occurred_at"]}
        for row in hospital
        if row["kind"] == "event" and row["type"] == "DocumentChanged"
    ]
    desk = [
        {"type": row["type"], "occurred_at": row["occurred_at"], "payload": row["payload"]}
        for row in channel
        if row["type"] in ("DeskSession", "DeskNote")
    ]
    _dump(extracts / "documents.json", documents)
    _dump(extracts / "desk.json", desk)
    _dump(extracts / "asks.json", ASKS)
    _dump(extracts / "calibration.json", CALIBRATION)
    _dump(extracts / "calls.json", CALLS)
    _dump(extracts / "byte_index.json", BYTE_INDEX)
    _dump(extracts / "host.json", HOST)
    _dump(extracts / "served_document.json", served_document(hospital))
    _dump(extracts / "shadow.json", SHADOW)
    _dump(extracts / "assistant_screen.json", assistant_screen(hospital))
    _dump(
        extracts / "focus.json",
        {
            "hospital": [row for row in hospital if row.get("ref") in FOCUS],
            "channel": [row for row in channel if row.get("ref") in FOCUS or row["type"] in ("DeskSession", "DeskNote", "WebhookAttempt", "HandsetDispatch")],
        },
    )
    bytes_dir = pack / "bytes"
    bytes_dir.mkdir(parents=True, exist_ok=True)
    (bytes_dir / "national_id.txt").write_text(NATIONAL_ID, encoding="utf-8")


def _dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2), encoding="utf-8")
