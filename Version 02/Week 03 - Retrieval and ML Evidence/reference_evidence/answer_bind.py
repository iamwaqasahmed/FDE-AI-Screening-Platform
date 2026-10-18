"""Which document is in force: headers and sentences, not the register."""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

from reference_enterprise.pathway import rules
from reference_evidence.load import citation, read_header

BIND = re.compile(
    r"Which document binds (?P<topic>.+?) at (?P<site>.+) on (?P<date>\d{4}-\d{2}-\d{2})(?: for grade (?P<grade>\w+))?"
)


def answer(data: Path, question: str, table: pd.DataFrame | None = None) -> dict:
    found = BIND.search(question)
    table = rules(data) if table is None else table
    document_id, limit = _resolve(table, found["site"], found["topic"].replace(" ", "_"), found["grade"] or "", found["date"])
    return {"clause_id": document_id, "limit": limit, "citation": citation(read_header(data / "corpus/policy" / f"{document_id}.md"))}


def _resolve(table: pd.DataFrame, site: str, topic: str, grade: str, on: str) -> tuple[str, int | str]:
    live = table[(table["topic"] == topic) & (table["effective"] <= on) & ((table["sunset"] == "") | (table["sunset"] > on))]
    live = live[live["site"].isin(["", site])]
    specific = live[live["site"] == site]
    pool = specific if len(specific) else live[live["site"].eq("")]
    graded = pool[pool["grade"] == grade] if grade else pool.iloc[0:0]
    pool = graded if len(graded) else pool[pool["grade"].eq("")]
    row = pool.iloc[0]
    limit = int(row["days"]) if str(row["days"]).isdigit() else ""
    return str(row["document_id"]), limit
