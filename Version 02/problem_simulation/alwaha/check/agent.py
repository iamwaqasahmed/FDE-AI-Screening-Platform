"""chk-w1-agent. A miss names the scenario and does not print the count or the approval id."""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK, grouped, load_rows, one, prose


def _state(name: str, gold: dict, row: dict) -> list[str]:
    problems = []
    reply = row["reply"]
    if row["booked"] != gold["booked"]:
        problems.append(f"{name} booked a slot" if row["booked"] else f"{name} did not book")
    if row["returned"] != gold["returned"]:
        problems.append(f"{name} was sent" if row["returned"] else f"{name} was not sent")
    if row["sms"] != gold["sms"]:
        problems.append(f"{name} message does not match")
    if gold["count"] is not None and reply["count"] != gold["count"]:
        problems.append(f"{name} count does not match the tool")
    if gold["facility_id"] and reply["facility_id"] != gold["facility_id"]:
        problems.append(f"{name} dropped the facility")
    if gold["constraint"] and reply["constraint"] != gold["constraint"]:
        problems.append(f"{name} refusal does not name the constraint")
    if row["decisions"] != gold["decisions"]:
        if gold["decisions"] == 1 and row["decisions"] > 1:
            problems.append(f"{name} applied more than one decision")
        else:
            problems.append(f"{name} decision does not match")
    if row["preference_used"] != gold["preference_used"]:
        word = "reused a blocked preference" if row["preference_used"] else "dropped an allowed preference"
        problems.append(f"{name} {word}")
    if sorted(row["pending_approval_ids"]) != sorted(gold["pending_approval_ids"]):
        word = "approval was not held" if gold["pending_approval_ids"] else "left an approval open"
        problems.append(f"{name} {word}")
    if sorted(row["approval_ids"]) != sorted(gold["approval_ids"]):
        problems.append(f"{name} approval does not match")
    if gold.get("failure") and row.get("failure") != gold["failure"]:
        problems.append(f"{name} does not name the failure")
    bookings = gold.get("bookings")
    if isinstance(bookings, int) and bookings >= 1 and row["tool_trace"].count("slots.book") > bookings:
        problems.append(f"{name} booked twice")
    return problems


def _scenarios(rows: list, gold: dict) -> list[str]:
    found = grouped(rows)
    if found is None:
        return ["trace is missing a field"]
    problems = []
    for item in gold["scenarios"]:
        name = item["scenario"]
        group = found.get(name, [])
        if not group:
            problems.append(f"{name} is missing")
            continue
        row = one(group)
        if row is None:
            problems.append(f"{name} log is missing a field")
            continue
        problems.extend(_state(name, item, row))
    return problems


def agent_problems(
    work: Path,
    pack: Path,
    gold: dict,
    canary: str,
    failures: Path | None = None,
    written: bool = True,
) -> list[str]:
    problems, rows = load_rows(work, pack, canary, failures)
    if rows is None and problems == [WATERMARK]:
        return problems
    if rows is not None:
        problems.extend(_scenarios(rows, gold))
    if written:
        problems.extend(prose(work))
    return problems
