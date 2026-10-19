"""Schema changes, date formats, spellings, units, firmware, the log window, and the recode."""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

from reference_discovery.io import CANONICAL_DISTRICTS, Drop, field, notice

VERSION = re.compile(r"firmware (\d+\.\d+\.\d+)")


def items(drop: Drop) -> dict:
    registry = _registry(drop)
    lab = _lab(drop)
    return {
        "registry_months": registry,
        "dob_formats": {"formats": _dob_formats(drop)},
        "district_spellings": {"extras": _districts(drop)},
        "lab_units": lab,
        "call_schema": _calls(drop),
        "firmware_lag": {"sites": _firmware(drop)},
        "pii_log": _pii(drop),
        "finance_recode": _finance(drop),
    }


def _registry(drop: Drop) -> dict:
    folder = drop.path("handover", "registry", "month")
    old = mixed = ""
    old_columns: list[str] = []
    duplicates: list[tuple[int, str]] = []
    for path in sorted(folder.glob("*.csv")):
        columns = _columns(path)
        month = path.stem
        if "REG_NO" in columns and "REGISTRY_NO" in columns:
            mixed = month
        elif set(columns) == {"REG_NO", "SURNAME", "DOB", "STATUS"}:
            old, old_columns = month, sorted(columns)
        elif "REGISTRY_NO" in columns:
            count = _duplicate_count(path)
            if count:
                duplicates.append((count, month))
    duplicate = max(duplicates)[1] if duplicates else ""
    return {"old_month": old, "mixed_month": mixed, "duplicate_month": duplicate, "old_columns": old_columns}


def _columns(path: Path) -> list[str]:
    return pd.read_csv(path, nrows=0).columns.tolist()


def _duplicate_count(path: Path) -> int:
    numbers = pd.read_csv(path, usecols=["REGISTRY_NO"], dtype=str)
    return int(numbers["REGISTRY_NO"].duplicated().sum())


def _dob_formats(drop: Drop) -> list[str]:
    values = drop.frame("handover", "registry", "current.csv", usecols=["DOB"])["DOB"]
    found = set()
    for value in values:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            found.add("iso")
        elif re.fullmatch(r"\d{2}/\d{2}/\d{4}", value):
            found.add("dmy")
        elif re.fullmatch(r"\d{4,6}", value):
            found.add("excel_serial")
    return sorted(found)


def _districts(drop: Drop) -> list[str]:
    values = drop.frame("handover", "registry", "current.csv", usecols=["DISTRICT"])["DISTRICT"]
    return sorted(set(values) - set(CANONICAL_DISTRICTS))


def _lab(drop: Drop) -> dict:
    change = field(notice(drop, "CHG-0120"), "effective")
    frame = drop.frame("handover", "lab", "hba1c_results.csv", usecols=["sample_date", "unit"])
    before = sorted(set(frame.loc[frame["sample_date"] < change, "unit"]) - {""})
    after = sorted(set(frame.loc[frame["sample_date"] >= change, "unit"]) - {""})
    return {"change_on": change, "before": before[0] if before else "", "after": after[-1] if after else ""}


def _calls(drop: Drop) -> dict:
    folder = drop.path("handover", "call_centre", "export")
    for path in sorted(folder.glob("calls-*.csv")):
        columns = _columns(path)
        if "disposition_code" in columns:
            return {"from_month": path.stem.replace("calls-", ""), "columns": sorted(
                name for name in ("disposition_code", "agent_notes", "queue") if name in columns)}
    return {"from_month": "", "columns": []}


def _firmware(drop: Drop) -> list[dict]:
    text = notice(drop, "CHG-0240")
    version = VERSION.search(text)
    site = field(text, "site")
    sheet = pd.read_excel(drop.path("handover", "devices", "camera_inventory.xlsx"), dtype=str).fillna("")
    shown = sorted(set(sheet.loc[sheet["site"] == site, "firmware"]))
    if not version or not shown:
        return []
    true = version.group(1)
    return [{"site": site, "shown_version": row, "true_version": true} for row in shown if row != true]


def _pii(drop: Drop) -> dict:
    tickets = drop.frame("handover", "service_desk", "tickets.csv")
    rows = tickets[tickets["summary"].str.contains("PII", case=False)]
    row = rows.iloc[0]
    return {"ref": row["ticket_ref"], "start": row["opened_at"][:10], "end": row["resolved_at"][:10]}


def _finance(drop: Drop) -> dict:
    frames = [drop.frame("handover", "finance", path.name) for path in sorted(drop.path("handover", "finance").glob("*.csv"))]
    ledger = pd.concat(frames, ignore_index=True)
    cut = field(notice(drop, "CHG-0144"), "effective")
    before = ledger[ledger["period_start"] < cut]
    after = ledger[ledger["period_start"] >= cut]
    old = before.groupby("line")["cost_centre"].first()
    new = after.groupby("line")["cost_centre"].first()
    changed = pd.DataFrame({"old": old, "new": new}).dropna()
    changed = changed[changed["old"] != changed["new"]]
    shared = changed.groupby("new").filter(lambda group: len(group) > 1)
    new_code = shared["new"].iloc[0]
    return {"recoded_on": cut, "new_code": new_code, "old_codes": sorted(shared.loc[shared["new"] == new_code, "old"])}
