"""Application database for assistant sessions.

The session row lives in this SQLite file, not in the hospital
record. Chapter 06 says that on the token-flow page. The table name
is sessions. The four columns below are the whole row. An extra
column fails the auth check. A missing column fails it too.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

# The check compares this set exactly. Keep the four names, and no fifth.
COLUMNS = ("session_id", "subject", "role", "loa")


def connect(path: Path) -> sqlite3.Connection:
    """Open the database and create the sessions table when it is missing.

    path is sessions.db under work/ when you run the server or run.py.
    The parent folder is created so the first run does not fail on a
    missing directory. check_same_thread is off because the server
    reads the same connection the request started.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path, check_same_thread=False)
    db.execute(
        "create table if not exists sessions ("
        "session_id text primary key, subject text not null, role text not null, loa text not null)"
    )
    db.commit()
    return db


def save(db: sqlite3.Connection, row: dict) -> None:
    """Insert the row, or replace it when this session id already exists.

    Signing in again with the same subject updates the row. It does
    not add a second row for the same person.
    """
    db.execute(
        "insert or replace into sessions (session_id, subject, role, loa) values (?, ?, ?, ?)",
        (row["session_id"], row["subject"], row["role"], row["loa"]),
    )
    db.commit()


def rows(db: sqlite3.Connection) -> list[dict]:
    """Return every session row, ordered by session id.

    run.py writes this list into trace.json. The auth check compares
    the patient row and the coordinator row with the tokens it expects.
    """
    found = db.execute(
        "select session_id, subject, role, loa from sessions order by session_id"
    ).fetchall()
    return [dict(zip(COLUMNS, item)) for item in found]


def columns(db: sqlite3.Connection) -> list[str]:
    """Return the column names SQLite stored on the sessions table.

    pragma table_info puts the name in the second field of each row.
    The auth check wants those names to be exactly COLUMNS.
    """
    return [str(row[1]) for row in db.execute("pragma table_info(sessions)")]
