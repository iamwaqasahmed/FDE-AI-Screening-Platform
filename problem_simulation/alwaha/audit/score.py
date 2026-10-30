"""Run the day's checkers against the filled work copies.

Each job is invoked as the check command, with the work directory and the profile. A job that names a release also passes that release. A SystemExit of zero, or a SystemExit with no code, counts as a pass. Any other exit code is a failure. A command that returns normally is a pass. The score is the pass count, the job count, the rate, and the per-job detail.
"""

from __future__ import annotations

import io
from contextlib import redirect_stdout

from alwaha.audit.catalog import jobs
from alwaha.check.__main__ import main


def score(profile_name: str) -> dict:
    """Return the pass count, the total, the rate, and one result row per job."""
    rows = []
    for which, release, work in jobs():
        ok, detail = _one(which, release, work, profile_name)
        # A job that names no release is reported under the first release id.
        rows.append({"check": which, "release": release or "rel-m01-l01", "ok": ok, "detail": detail.strip()})
    passed = sum(1 for row in rows if row["ok"])
    return {"passed": passed, "total": len(rows), "rate": passed / len(rows), "rows": rows}


def _one(which: str, release: str, work, profile_name: str) -> tuple[bool, str]:
    """Run one check and return whether it passed, plus the text it printed."""
    argv = [which, "--work", str(work), "--profile", profile_name]
    if release:
        # An empty release leaves the checker's own default in place.
        argv.extend(["--release", release])
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        try:
            main(argv)
        except SystemExit as exc:
            # A clean exit is a pass. A nonzero code is a failed check, and the buffer still holds its text.
            return exc.code in {0, None}, buffer.getvalue()
    return True, buffer.getvalue()
