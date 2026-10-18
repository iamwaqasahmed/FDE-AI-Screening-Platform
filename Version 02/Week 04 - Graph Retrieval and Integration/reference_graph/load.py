"""Readers for the files a team is given. Nothing here opens truth or eval."""

from __future__ import annotations

import re
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

from reference_enterprise.load import messages, pacs, read_csv, v3

MRN = re.compile(r"Hospital number: (\S+)")
SEEN_ON = re.compile(r"in clinic on (\d{1,2}/\d{1,2}/\d{4}|\d{1,2} [A-Z][a-z]+ \d{4})", re.I)
WINDOW = re.compile(r"requests_(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})")


def drop_files(data: Path) -> tuple[pd.DataFrame, pd.DataFrame, date, date]:
    folder = data / "drops/week-4/letters"
    request_path = next(folder.glob("requests_*.csv"))
    dispatch_path = next(folder.glob("dispatch_*.csv"))
    start, end = (date.fromisoformat(part) for part in WINDOW.search(request_path.name).groups())
    requests = read_csv(data, str(request_path.relative_to(data)).replace("\\", "/"))
    dispatch = read_csv(data, str(dispatch_path.relative_to(data)).replace("\\", "/"))
    return requests, dispatch, start, end


def filled_mrns(data: Path) -> set[str]:
    found = set()
    for path in (data / "handover/epr_letters").glob("*.txt"):
        body = path.read_text(encoding="utf-8")
        mrn = MRN.search(body)
        if mrn and SEEN_ON.search(body):
            found.add(mrn.group(1))
    return found


def hospitals(data: Path) -> tuple[dict[str, str], int]:
    frame = pacs(data)
    if frame.empty:
        return {}, 0
    grouped = frame.groupby("MRN")["HOSPITAL"].nunique()
    clean = frame.drop_duplicates("MRN")
    single = set(grouped[grouped == 1].index)
    mapping = dict(zip(clean.loc[clean["MRN"].isin(single), "MRN"], clean.loc[clean["MRN"].isin(single), "HOSPITAL"]))
    return mapping, int((grouped > 1).sum())


def calls(data: Path) -> pd.DataFrame:
    frames = []
    for path in sorted((data / "handover/call_centre/export").glob("*.csv")):
        frame = pd.read_csv(path, dtype=str).fillna("")
        if "disposition_code" in frame.columns:
            frame = frame.rename(columns={"disposition_code": "reason_code", "agent_notes": "note"})
        frames.append(frame[["call_date", "reason_code", "note"]])
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame(columns=["call_date", "reason_code", "note"])


def shift(day: date, days: int) -> date:
    return day + timedelta(days=days)


__all__ = ["messages", "read_csv", "v3"]
