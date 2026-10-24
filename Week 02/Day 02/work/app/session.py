"""Application database for assistant sessions."""

from __future__ import annotations

import sqlite3
from pathlib import Path

COLUMNS = ("session_id", "subject", "role", "loa")


def connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path, check_same_thread=False)
    db.execute(
        "create table if not exists sessions ("
        "session_id text primary key, subject text not null, role text not null, loa text not null)"
    )
    db.commit()
    return db


def save(db: sqlite3.Connection, row: dict) -> None:
    db.execute(
        "insert or replace into sessions (session_id, subject, role, loa) values (?, ?, ?, ?)",
        (row["session_id"], row["subject"], row["role"], row["loa"]),
    )
    db.commit()


def rows(db: sqlite3.Connection) -> list[dict]:
    found = db.execute(
        "select session_id, subject, role, loa from sessions order by session_id"
    ).fetchall()
    return [dict(zip(COLUMNS, item)) for item in found]


def columns(db: sqlite3.Connection) -> list[str]:
    return [str(row[1]) for row in db.execute("pragma table_info(sessions)")]
