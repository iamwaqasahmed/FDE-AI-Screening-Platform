"""Date formats that round-trip through the handover files."""

from __future__ import annotations

from datetime import date, datetime, timedelta

import pandas as pd

EXCEL_EPOCH = date(1899, 12, 30)


def to_serial(value: date) -> int:
    return (value - EXCEL_EPOCH).days


def format_mixed(value: date, slot: int) -> int | str:
    if slot % 3 == 0:
        return to_serial(value)
    if value.day >= 13:
        return value.strftime("%d/%m/%Y")
    return value.isoformat()


def parse_mixed(value) -> date | None:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if pd.isna(value):
            return None
        return EXCEL_EPOCH + timedelta(days=int(value))
    text = str(value).strip()
    if text == "" or text.lower() == "nan":
        return None
    if text.isdigit():
        return EXCEL_EPOCH + timedelta(days=int(text))
    if len(text) >= 10 and text[4] == "-" and text[7] == "-":
        return datetime.strptime(text[:10], "%Y-%m-%d").date()
    if len(text) >= 10 and text[2] == "/" and text[5] == "/":
        day = int(text[:2])
        if day <= 12:
            raise ValueError(f"Ambiguous day-month date: {text}")
        return datetime.strptime(text[:10], "%d/%m/%Y").date()
    raise ValueError(f"Unparsed date: {value!r}")
