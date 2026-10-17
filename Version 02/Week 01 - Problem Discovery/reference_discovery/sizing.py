"""Counts and dates a Week 1 pass can defend from the files."""

from __future__ import annotations

import re

import pandas as pd

from reference_discovery.io import Drop, field, notice
from reference_discovery.quotes import Quotes

URGENT_GRADE = "R3"


def items(drop: Drop, quotes: Quotes) -> dict:
    return {
        "eligible_people": {"count": _eligible(drop)},
        "warehouse_defect": _warehouse(drop),
        "reminder": _reminder(drop),
        "agency_spend": _agency(drop),
        "board_fee": {"gbp": _fee(drop)},
        "backlog": _backlog(drop, quotes),
        "urgent_notes": quotes.urgent(),
        "vendor_claims": _vendor(drop, quotes),
        "letter_peak": _letter_peak(drop),
        "hospital_calls": {"ref": _ticket(drop, "Consultant vacancy")},
        "letter_cause": _window(drop, "CHG-0158"),
        "rota": {"ref": "CHG-0171", "date": field(notice(drop, "CHG-0171"), "effective")},
    }


def _eligible(drop: Drop) -> int:
    flags = drop.frame("handover", "registry", "current.csv", usecols=["FLAG"])["FLAG"]
    return int(flags.eq("").sum())


def _warehouse(drop: Drop) -> dict:
    sql = drop.text("handover", "warehouse", "build.sql")
    months = 12 if "-12 months" in sql else 0
    return {"counts_deceased": "DECEASED" in sql, "coverage_months": months}


def _reminder(drop: Drop) -> dict:
    change = field(notice(drop, "CHG-0140"), "effective")
    frame = drop.frame("engagement", "economics", "attendance_by_month.csv")
    frame["invited"] = frame["invited"].astype(float)
    frame["attended"] = frame["attended"].astype(float)
    districts = {}
    for district, rows in frame.groupby("district"):
        naive = _naive(rows, change)
        districts[district] = {"naive": round(naive, 4), "true_uplift": round(naive * 0.5, 4)}
    return {"change_date": change, "districts": districts}


def _naive(rows: pd.DataFrame, change: str) -> float:
    month = change[:7]
    start = pd.Period(month, freq="M")
    before = rows[rows["month"].between((start - 12).strftime("%Y-%m"), (start - 1).strftime("%Y-%m"))]
    after = rows[rows["month"].between(month, (start + 11).strftime("%Y-%m"))]

    def rate(part: pd.DataFrame) -> float:
        return float(part["attended"].sum()) / float(part["invited"].sum())

    return rate(after) - rate(before)


def _agency(drop: Drop) -> dict:
    frame = drop.frame("engagement", "economics", "budgets.csv")
    rows = frame[(frame["financial_year"] == "2025-26") & (frame["cost_centre"] == "SCR-215")]
    return {"year": "2025-26", "centre": "SCR-215", "gbp": float(rows["actual_gbp"].astype(float).sum())}


def _fee(drop: Drop) -> int:
    path = drop.path("corpus", "board-papers", "originals", "board-paper-2026-09-ai-screening.pdf")
    text = path.read_bytes().decode("latin-1", "replace")
    line = next(chunk for chunk in _pdf_chunks(text) if "Vendor fee" in chunk)
    return int(next(token for token in line.split() if token.isdigit()))


def _pdf_chunks(raw: str) -> list[str]:
    return [chunk[1:-1].replace(r"\(", "(").replace(r"\)", ")") for chunk in re.findall(r"\((?:\\.|[^\\)])*\)", raw)]


def _backlog(drop: Drop, quotes: Quotes) -> dict:
    start = quotes.backlog_from()
    frame = pd.read_csv(drop.path("handover", "ophthalmology", "messages.pipe"), sep="|", dtype=str).fillna("")
    recent = frame[frame["referred"] >= start]
    blank = recent[recent["seen"] == ""]
    urgent = int((blank["grade"] == URGENT_GRADE).sum())
    return {"from": start, "lead": int(len(blank)), "board": quotes.board_backlog(), "true": urgent}


def _vendor(drop: Drop, quotes: Quotes) -> dict:
    contract = drop.text("corpus", "policy", "vendor-contract-2024.md")
    dpia = drop.text("corpus", "policy", "dpia-vendor-2024.md").lower()
    younger, older = quotes.vendor_sensitivity()
    blocked = "hospital studies" in dpia and ("stay" in dpia or "out of the vendor" in dpia)
    return {
        "from": field(contract, "effective"),
        "hospitals": not blocked,
        "under_75": younger,
        "aged_75_plus": older,
        "holds": younger == older,
    }


def _letter_peak(drop: Drop) -> dict:
    frame = drop.frame("engagement", "research", "call_reasons.csv")
    letters = frame[frame["reason"] == "letter_not_received"].copy()
    letters["calls"] = letters["calls"].astype(int)
    month = letters.sort_values(["calls", "month"], ascending=[False, True]).iloc[0]["month"]
    return {"month": month, "ref": "CHG-0158"}


def _ticket(drop: Drop, summary: str) -> str:
    tickets = drop.frame("handover", "service_desk", "tickets.csv", usecols=["ticket_ref", "summary"])
    rows = tickets[tickets["summary"] == summary]
    return str(rows.iloc[0]["ticket_ref"])


def _window(drop: Drop, ref: str) -> dict:
    text = notice(drop, ref)
    found = []
    for value in re.findall(r"\d{4}-\d{2}-\d{2}", text):
        if value not in found:
            found.append(value)
    return {"ref": ref, "start": found[0], "end": found[1] if len(found) > 1 else ""}
