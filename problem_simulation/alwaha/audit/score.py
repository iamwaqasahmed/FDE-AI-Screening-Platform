"""Run the day's checkers against the filled work copies."""

from __future__ import annotations

import io
from contextlib import redirect_stdout

from alwaha.audit.catalog import jobs
from alwaha.check.__main__ import main


def score(profile_name: str) -> dict:
    rows = []
    for which, release, work in jobs():
        ok, detail = _one(which, release, work, profile_name)
        rows.append({"check": which, "release": release or "rel-w1d1", "ok": ok, "detail": detail.strip()})
    passed = sum(1 for row in rows if row["ok"])
    return {"passed": passed, "total": len(rows), "rate": passed / len(rows), "rows": rows}


def _one(which: str, release: str, work, profile_name: str) -> tuple[bool, str]:
    argv = [which, "--work", str(work), "--profile", profile_name]
    if release:
        argv.extend(["--release", release])
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        try:
            main(argv)
        except SystemExit as exc:
            return exc.code in {0, None}, buffer.getvalue()
    return True, buffer.getvalue()
