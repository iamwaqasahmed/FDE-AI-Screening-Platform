"""INV-03. book() must reject a document id and a second offer."""

from __future__ import annotations

from pathlib import Path

from access.checks.runtime import load_callable
from access.sealed_holdouts import BOOKINGS


def grade_capability(path: Path) -> list[str]:
    fn, problems = load_callable(path, "book")
    if fn is None:
        return problems
    for call in BOOKINGS:
        try:
            got = fn(call)
        except Exception:
            problems.append(f"the booking function raised on {call['id']}")
            continue
        if not isinstance(got, dict):
            problems.append(f"the booking function returned no record for {call['id']}")
            continue
        problems.extend(_judge(call, got))
    return problems


def _judge(call: dict, got: dict) -> list[str]:
    accepted = got.get("accepted")
    count = got.get("count")
    if call["origin"] == "document" and accepted is not False:
        return ["a document-sourced id was accepted"]
    if call["utterance_only"] and accepted is not False:
        return ["a sentence was treated as a booked visit"]
    if call["id"] == "first-offer" and (accepted is not True or count != 1):
        return ["the coordinator offer did not book the slot version once"]
    if call["id"] == "second-offer" and count != 1:
        return ["one slot version was booked more than once"]
    return []
