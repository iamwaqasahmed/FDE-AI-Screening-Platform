"""Questions whose answer is a table cell, a report rate, a notice cause, or the original of a forward."""

from __future__ import annotations

import re

from simulation.eval.evidence.question import cite, make
from simulation.world.timeline import TIMELINE

MONTH = re.compile(r"-(\d{4}-\d{2})$")


def cases(world: dict) -> list[dict]:
    facts = world["gold"].get("table_only_facts", [])
    reports = {row["doc_id"]: row for row in world["gold"].get("report_facts", [])}
    duplicates = [row for row in world["gold"].get("near_duplicates", []) if row["duplicate_of"] in reports]
    return (
        _tables(world, facts)
        + _audits(world, facts)
        + _reports(world, reports, duplicates)
        + _duplicates(world, reports, duplicates)
        + _notices(world)
    )


def _tables(world: dict, facts: list[dict]) -> list[dict]:
    rows = [fact for fact in facts if str(fact["doc_id"]).startswith("board-")]
    return [_table(world, fact, index) for index, fact in enumerate(_take(rows, 10))]


def _table(world: dict, fact: dict, index: int) -> dict:
    question = f"According to the {fact['month']} board pack, how many grader backlog breaches did {fact['site']} have?"
    return make(f"table-{index:02d}", question, {"value": int(fact["grader_backlog"])}, "value", "table", ("value",),
                cite(world["catalog"][fact["doc_id"]]), "multi_hop")


def _audits(world: dict, facts: list[dict]) -> list[dict]:
    rows = [fact for fact in facts if str(fact["doc_id"]).startswith("quality-audit-") and fact.get("lowest_grader")]
    found = []
    for index, fact in enumerate(_take(rows, 5)):
        label = fact["doc_id"].removeprefix("quality-audit-")
        question = f"Which grader had the lowest second-read agreement in the {label} quality audit?"
        found.append(make(f"audit-{index:02d}", question, {"value": fact["lowest_grader"]}, "value", "table", ("value",),
                           cite(world["catalog"][fact["doc_id"]]), "multi_hop"))
    return found


def _reports(world: dict, reports: dict, duplicates: list[dict]) -> list[dict]:
    originals = {row["duplicate_of"] for row in duplicates}
    rows = [row for row in reports.values() if row["doc_id"] not in originals and MONTH.search(row["doc_id"])]
    return [_report(world, row, index, "report", False) for index, row in enumerate(_take(rows, 10))]


def _duplicates(world: dict, reports: dict, duplicates: list[dict]) -> list[dict]:
    return [_report(world, reports[row["duplicate_of"]], index, "duplicate", True) for index, row in enumerate(_take(duplicates, 6))]


def _report(world: dict, fact: dict, index: int, slice_name: str, forwarded: bool) -> dict:
    month = MONTH.search(fact["doc_id"]).group(1)
    question = f"What ungradable rate did {fact['site']} report for {month}?"
    if forwarded:
        question += " Cite the original record, not a forwarded copy."
    return make(f"{slice_name}-{index:02d}", question, {"value": fact["ungradable_rate"]}, "value", slice_name, ("value",),
                cite(world["catalog"][fact["doc_id"]]), "lookup" if slice_name == "report" else "multi_hop")


def _notices(world: dict) -> list[dict]:
    found = []
    for index, item in enumerate(_take(list(TIMELINE), 6)):
        document_id = f"notice-{item.ref.lower()}"
        question = f"What cause was recorded for {item.ref}?"
        expected = {"must_mention": [[item.cause]], "must_not_claim": []}
        found.append(make(f"notice-{index:02d}", question, expected, "written", "notice", (),
                           cite(world["catalog"][document_id]), "lookup"))
    return found


def _take(rows: list, count: int) -> list:
    if len(rows) <= count:
        return rows
    step = max(1, len(rows) // count)
    return rows[::step][:count]
