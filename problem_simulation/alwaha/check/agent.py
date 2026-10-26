"""chk-w1-agent. A miss names the scenario and does not print the count or the approval id.

This check compares one trace row per scenario with gold. It grades booking, sending, the message, the count, the facility, the constraint, decisions, preferences, approvals, and a named failure. A watermark in the work tree is returned alone. The written note is optional so a later rescore can grade the trace without grading the note again.
"""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK, grouped, load_rows, one, prose


def _state(name: str, gold: dict, row: dict) -> list[str]:
    """Return the state misses for one scenario.

    Booking and sending each have a message that says which way they disagree. The count, facility, and constraint are graded only when gold has one. More than the single expected decision is its own miss. Any other decision disagreement is a mismatch. The preference and pending-approval messages also say which way the flag is wrong. A non-empty gold pending list means an approval should still be held. An empty one means none should be left open. A booking count above the allowed number of book calls is a double book.
    """
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
        # More than the single expected decision is its own miss. Any other disagreement is a plain mismatch.
        if gold["decisions"] == 1 and row["decisions"] > 1:
            problems.append(f"{name} applied more than one decision")
        else:
            problems.append(f"{name} decision does not match")
    if row["preference_used"] != gold["preference_used"]:
        # The message says which way the preference flag is wrong.
        word = "reused a blocked preference" if row["preference_used"] else "dropped an allowed preference"
        problems.append(f"{name} {word}")
    if sorted(row["pending_approval_ids"]) != sorted(gold["pending_approval_ids"]):
        # A non-empty gold list means an approval should still be held. An empty list means none should be left open.
        word = "approval was not held" if gold["pending_approval_ids"] else "left an approval open"
        problems.append(f"{name} {word}")
    if sorted(row["approval_ids"]) != sorted(gold["approval_ids"]):
        problems.append(f"{name} approval does not match")
    if gold.get("failure") and row.get("failure") != gold["failure"]:
        problems.append(f"{name} does not name the failure")
    bookings = gold.get("bookings")
    # A book-call count above the number gold allows is a double book. A gold value that is not a count is not graded here.
    if isinstance(bookings, int) and bookings >= 1 and row["tool_trace"].count("slots.book") > bookings:
        problems.append(f"{name} booked twice")
    return problems


def _scenarios(rows: list, gold: dict) -> list[str]:
    """Return the scenario misses for the whole trace.

    Rows that cannot be grouped are one missing-field miss. A scenario with no rows is missing. A scenario whose single row is incomplete is a missing field. Otherwise that row is graded.
    """
    # Group the trace by scenario. Rows that cannot be grouped are one missing-field miss.
    found = grouped(rows)
    if found is None:
        return ["trace is missing a field"]
    problems = []
    for item in gold["scenarios"]:
        name = item["scenario"]
        group = found.get(name, [])
        # A scenario with no rows never ran, so the rest of the list is still graded.
        if not group:
            problems.append(f"{name} is missing")
            continue
        row = one(group)
        # An incomplete row is a missing field, so its state is not graded.
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
    """Return the agent misses.

    The trace is loaded first. A watermark with no rows is returned alone so scenario text is not added after it. When rows exist they are graded. The written note is graded only when the caller asks for it.
    """
    problems, rows = load_rows(work, pack, canary, failures)
    # A watermark is returned alone so scenario text is not printed after it.
    if rows is None and problems == [WATERMARK]:
        return problems
    if rows is not None:
        problems.extend(_scenarios(rows, gold))
    # The caller can skip the note when a separate command grades the writing.
    if written:
        problems.extend(prose(work))
    return problems
