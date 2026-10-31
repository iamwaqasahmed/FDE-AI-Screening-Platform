"""Project each log into its own store."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from access.logs import connect, read_log


def project_all(log_path: Path, proj: Path) -> None:
    conn = connect(log_path)
    try:
        hospital = read_log(conn, "hospital")
        channel = read_log(conn, "channel")
        payer = read_log(conn, "payer")
    finally:
        conn.close()
    _write(proj / "hospital.sqlite", _hospital_rows(hospital))
    _write(proj / "channel.sqlite", _channel_rows(channel))
    _write(proj / "payer.sqlite", _payer_rows(payer))


def _write(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        path.unlink()
    conn = sqlite3.connect(path)
    try:
        conn.execute("CREATE TABLE rows (doc TEXT NOT NULL)")
        conn.executemany(
            "INSERT INTO rows (doc) VALUES (?)",
            [(json.dumps(row),) for row in rows],
        )
        conn.commit()
    finally:
        conn.close()


def _hospital_rows(events: list[dict]) -> list[dict]:
    rows: list[dict] = []
    for event in events:
        payload = event["payload"]
        if event["type"] == "SlotFiled":
            rows.append(
                {
                    "kind": "mart",
                    "ref": payload["ref"],
                    "booking_date": payload["booking_date"],
                    "wait_days": 0,
                }
            )
            nightly = {
                "kind": "nightly_file",
                "ref": payload["ref"],
                "file_id": payload["file_id"],
                "site": payload["site"],
                "occurred_at": event["occurred_at"],
            }
            if "trailer_ok" in payload:
                nightly["trailer_ok"] = payload["trailer_ok"]
                nightly["trailer_count"] = payload["trailer_count"]
                nightly["body_count"] = payload["body_count"]
            rows.append(nightly)
        elif event["type"] == "CacheStored":
            rows.append(
                {
                    "kind": "eligibility_cache",
                    "ref": payload["ref"],
                    "eligible": payload["eligible"],
                    "window_present": payload["window_present"],
                    "occurred_at": event["occurred_at"],
                }
            )
        else:
            rows.append(
                {
                    "kind": "event",
                    "type": event["type"],
                    "ref": payload.get("ref") or event["stream_id"],
                    "occurred_at": event["occurred_at"],
                    "payload": payload,
                }
            )
    return rows


def _channel_rows(events: list[dict]) -> list[dict]:
    return [
        {
            "kind": "event",
            "type": event["type"],
            "ref": event["payload"].get("ref") or event["stream_id"],
            "occurred_at": event["occurred_at"],
            "payload": event["payload"],
        }
        for event in events
    ]


def _payer_rows(events: list[dict]) -> list[dict]:
    rows: list[dict] = []
    for event in events:
        payload = event["payload"]
        if event["type"] == "CoverageDecided":
            rows.append(
                {
                    "kind": "coverage",
                    "ref": payload["ref"],
                    "answer": payload["answer"],
                    "effective_from": payload.get("effective_from"),
                    "effective_to": payload.get("effective_to"),
                    "currency": payload.get("currency"),
                    "occurred_at": event["occurred_at"],
                }
            )
        else:
            rows.append(
                {
                    "kind": "event",
                    "type": event["type"],
                    "ref": payload.get("ref") or event["stream_id"],
                    "occurred_at": event["occurred_at"],
                    "payload": payload,
                }
            )
    return rows


def load_rows(path: Path) -> list[dict]:
    conn = sqlite3.connect(path)
    try:
        found = conn.execute("SELECT doc FROM rows").fetchall()
    finally:
        conn.close()
    return [json.loads(row[0]) for row in found]
