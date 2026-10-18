"""Answers that live in a PDF table, a spreadsheet, a report, or a notice."""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

from reference_evidence.load import citation, read_header
from reference_evidence.originals import pdf, xlsx_table

BOARD = re.compile(r"According to the (\d{4}-\d{2}) board pack, how many grader backlog breaches did (.+) have\?")
AUDIT = re.compile(r"Which grader had the lowest second-read agreement in the (\w+) quality audit\?")
REPORT = re.compile(r"What ungradable rate did (.+) report for (\d{4}-\d{2})\?")
NOTICE = re.compile(r"What cause was recorded for ([A-Z]+-\d+)\?")
RATE = re.compile(r"([0-9]+(?:\.[0-9]+)?) per cent")
NAMED = re.compile(r"rate (?:of|was) ([0-9.]+)")


def board(data: Path, question: str) -> dict:
    month, site = BOARD.search(question).groups()
    path = data / "corpus/boards/originals" / f"board-{month}.pdf"
    text = pdf(path)
    for line in text.splitlines():
        if line.strip().startswith(site):
            numbers = re.findall(r"\d+", line.split(site, 1)[1])
            return {"value": int(numbers[1]), "document": f"board-{month}"}
    raise ValueError(site)


def audit(data: Path, question: str) -> dict:
    label = AUDIT.search(question).group(1)
    frame = xlsx_table(data / "corpus/quality-audits/originals" / f"quality-audit-{label}.xlsx")
    reads = pd.to_numeric(frame["Second reads"])
    eligible = frame.loc[reads >= 5].copy()
    eligible["Agreement %"] = pd.to_numeric(eligible["Agreement %"])
    eligible = eligible.sort_values(["Agreement %", "Grader"])
    return {"value": str(eligible.iloc[0]["Grader"]), "document": f"quality-audit-{label}"}


def report(data: Path, question: str) -> dict:
    site, month = REPORT.search(question).groups()
    document = f"site-report-{site.lower().replace(' ', '-')}-{month}"
    text = (data / "corpus/site-reports" / f"{document}.md").read_text(encoding="utf-8")
    return {"value": _rate(text), "document": document}


def notice(data: Path, question: str) -> dict:
    ref = NOTICE.search(question).group(1)
    document = f"notice-{ref.lower()}"
    text = (data / "corpus/notices" / f"{document}.md").read_text(encoding="utf-8")
    return {"answer": text, "document": document}


def _rate(text: str) -> str:
    for line in text.splitlines():
        lowered = line.lower()
        if "ungradable" not in lowered and "could not be graded" not in lowered:
            continue
        percent = RATE.search(line)
        if percent:
            return percent.group(1)
        named = NAMED.search(line)
        if named:
            return named.group(1)
    raise ValueError("ungradable rate")


def cite(data: Path, family: str, document: str) -> dict:
    return citation(read_header(data / "corpus" / family / f"{document}.md"))
