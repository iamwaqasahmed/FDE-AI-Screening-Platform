"""Parse the three date forms used in the Hartland extract."""

from __future__ import annotations

from datetime import date, datetime, timedelta

EXCEL_EPOCH = date(1899, 12, 30)


def parse_date(value) -> date | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if value != value:
            return None
        return EXCEL_EPOCH + timedelta(days=int(value))
    text = str(value).strip()
    if text == "" or text.lower() == "nan":
        return None
    if text.endswith(".0") and text[:-2].isdigit():
        text = text[:-2]
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


def median_days(values: list[int]) -> float:
    ordered = sorted(values)
    if not ordered:
        raise ValueError("No day counts to take a median from.")
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return float(ordered[mid])
    return (ordered[mid - 1] + ordered[mid]) / 2
