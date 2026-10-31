"""Three append-only logs in one SQLite file. No cross-log foreign key."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

from access.canonical import event_id

AUTHORITIES = ("hospital", "channel", "payer")
LOG_TABLE = {
    "hospital": "log_hospital",
    "channel": "log_channel",
    "payer": "log_payer",
}


def connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _log_ddl(table: str) -> str:
    return f"""
    CREATE TABLE {table} (
      seq INTEGER PRIMARY KEY,
      event_id TEXT NOT NULL UNIQUE,
      type TEXT NOT NULL,
      occurred_at TEXT NOT NULL,
      stream_id TEXT NOT NULL,
      stream_rev INTEGER NOT NULL,
      payload TEXT NOT NULL,
      UNIQUE (stream_id, stream_rev)
    );
    CREATE TRIGGER {table}_no_update
    BEFORE UPDATE ON {table}
    BEGIN
      SELECT RAISE(ABORT, 'log rows are append-only');
    END;
    CREATE TRIGGER {table}_no_delete
    BEFORE DELETE ON {table}
    BEGIN
      SELECT RAISE(ABORT, 'log rows are append-only');
    END;
    """


def init_db(path: Path) -> None:
    """Create empty logs. A second call on an existing file leaves it unchanged."""
    if path.exists():
        return
    conn = connect(path)
    try:
        conn.executescript(
            """
            CREATE TABLE inbox_done (
              command_id TEXT PRIMARY KEY,
              event_id TEXT NOT NULL
            );
            """
            + "".join(_log_ddl(LOG_TABLE[name]) for name in AUTHORITIES)
        )
        conn.commit()
    finally:
        conn.close()


def _insert(conn: sqlite3.Connection, command: dict[str, Any]) -> str:
    """Insert one command. The caller owns the transaction."""
    command_id = command["command_id"]
    existing = conn.execute(
        "SELECT event_id FROM inbox_done WHERE command_id = ?",
        (command_id,),
    ).fetchone()
    if existing:
        return str(existing["event_id"])
    authority = command["authority"]
    if authority not in AUTHORITIES:
        raise ValueError("unknown authority")
    payload = command["payload"]
    if "canonical_at" in payload or command["type"] == "SetCanonicalTime":
        raise ValueError("a shared clock is not a command")
    body = {
        "type": command["type"],
        "occurred_at": command["occurred_at"],
        "stream_id": command["stream_id"],
        "stream_rev": int(command["stream_rev"]),
        "payload": payload,
    }
    eid = event_id(authority, body)
    table = LOG_TABLE[authority]
    conn.execute(
        f"""
        INSERT INTO {table}
          (event_id, type, occurred_at, stream_id, stream_rev, payload)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            eid,
            body["type"],
            body["occurred_at"],
            body["stream_id"],
            body["stream_rev"],
            json.dumps(payload, sort_keys=True),
        ),
    )
    conn.execute(
        "INSERT INTO inbox_done (command_id, event_id) VALUES (?, ?)",
        (command_id, eid),
    )
    return eid


def append(conn: sqlite3.Connection, command: dict[str, Any]) -> str:
    """Commit one command onto the authority it names. Replays return the same id."""
    conn.execute("BEGIN IMMEDIATE")
    try:
        eid = _insert(conn, command)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    return eid


def append_all(conn: sqlite3.Connection, commands: list[dict[str, Any]]) -> list[str]:
    """Commit a history in one transaction. Replays of a command id return the same id."""
    conn.execute("BEGIN IMMEDIATE")
    try:
        ids = [_insert(conn, command) for command in commands]
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    return ids


def read_log(conn: sqlite3.Connection, authority: str) -> list[dict]:
    table = LOG_TABLE[authority]
    rows = conn.execute(
        f"SELECT seq, event_id, type, occurred_at, stream_id, stream_rev, payload FROM {table} ORDER BY seq"
    ).fetchall()
    return [
        {
            "seq": row["seq"],
            "event_id": row["event_id"],
            "type": row["type"],
            "occurred_at": row["occurred_at"],
            "stream_id": row["stream_id"],
            "stream_rev": row["stream_rev"],
            "payload": json.loads(row["payload"]),
        }
        for row in rows
    ]
