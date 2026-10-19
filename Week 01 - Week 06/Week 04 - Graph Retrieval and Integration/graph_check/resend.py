"""The re-send lists exactly the lost requests, and it carries no personal columns."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

BANNED = ("dob", "date_of_birth", "forename", "surname", "patient_name", "name")


def score(path: Path, gold: dict) -> dict:
    if not path.exists():
        return {"ok": False, "rows": 0}
    frame = pd.read_csv(path, dtype=str).fillna("")
    banned = [column for column in frame.columns if column.strip().lower() in BANNED]
    expected = pd.DataFrame(gold["resend"]).fillna("")
    if banned or any(column not in frame.columns for column in ("request_id", "action", "reason")):
        return {"ok": False, "rows": len(frame), "banned": banned}
    got = frame.drop_duplicates("request_id").set_index("request_id").sort_index()
    want = expected.drop_duplicates("request_id").set_index("request_id").sort_index()
    same = got.index.equals(want.index) and got["action"].astype(str).equals(want["action"].astype(str))
    same = same and got["reason"].astype(str).equals(want["reason"].astype(str))
    return {"ok": bool(same), "rows": int(len(got)), "banned": banned}
