"""Opt-in stress ticks. history() does not import this module."""

from __future__ import annotations

import tempfile
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from access.logs import AUTHORITIES, append_all, connect, init_db, read_log

_START = datetime(2026, 4, 1, tzinfo=timezone.utc)
_CYCLE = ("hospital", "channel", "payer")
_WIDTH = 50


def stress_commands(count: int = 2000, seed: int = 20270110) -> list[dict]:
    """Return `count` StressTick commands.

    Each field is a closed formula of the index. `seed` is the project seed
    and does not change the list.
    """
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise TypeError("seed must be an int")
    if count < 0:
        raise ValueError("count must be non-negative")
    return [_command(index) for index in range(count)]


def time_build(count: int = 2000) -> dict:
    """Append `count` stress commands to a temporary log and time that build."""
    with tempfile.TemporaryDirectory(prefix="r3i-") as folder:
        return _timed(Path(folder), count)


def _command(index: int) -> dict:
    authority = _CYCLE[index % len(_CYCLE)]
    bucket = index // _WIDTH
    when = _START + timedelta(minutes=index)
    return {
        "command_id": f"cmd-r3i-{index}",
        "authority": authority,
        "type": "StressTick",
        "occurred_at": when.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "stream_id": f"r3i-{authority}-{bucket}",
        "stream_rev": (index % _WIDTH) + 1,
        "payload": _payload(index),
    }


def _payload(index: int) -> dict:
    return {
        "ref": f"R3I-{index}",
        "n": index,
        "queue_depth": (index * 3) % 500,
        "retry": 1 if index % 17 == 0 else 0,
    }


def _timed(folder: Path, count: int) -> dict:
    started = time.perf_counter()
    commands = stress_commands(count=count)
    path = folder / "log.sqlite"
    init_db(path)
    conn = connect(path)
    try:
        append_all(conn, commands)
        events = _events(conn)
    finally:
        conn.close()
    return {
        "commands": count,
        "seconds": time.perf_counter() - started,
        "events": events,
    }


def _events(conn) -> int:
    return sum(len(read_log(conn, name)) for name in AUTHORITIES)
