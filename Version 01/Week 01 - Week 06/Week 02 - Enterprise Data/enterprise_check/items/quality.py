"""Quality items: the stale catalogue, the SMS file, the booking export, and feed de-duplication."""

from __future__ import annotations

from course.checks.rules import as_int, close, same_set


def catalogue_stale(answer: dict, gold: dict) -> bool:
    return same_set(answer.get("entries", []), gold["quality"]["catalogue"])


def sms_reconcile(answer: dict, gold: dict) -> bool:
    row = gold["quality"]["sms"]
    return (
        as_int(answer.get("duplicates")) == row["duplicates"]
        and close(answer.get("late_share"), row["late_share"], 0.005, relative=False)
        and close(answer.get("inverted_share"), row["inverted_share"], 0.002, relative=False)
        and answer.get("in_order") is False
    )


def booking_reconcile(answer: dict, gold: dict) -> bool:
    row = gold["quality"]["booking"]
    return answer.get("ref") == row["ref"] and answer.get("history_in_export") is False


def feed_dedupe(answer: dict, gold: dict) -> bool:
    row = gold["read"]["feed_dedupe"]
    return answer.get("key") == row["key"] and answer.get("order") == row["order"]
