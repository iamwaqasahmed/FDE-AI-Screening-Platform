"""The backlog counts and Gate 2."""

from __future__ import annotations

from agent_check.items.match import money, same


def backlog_triage(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["backlog_triage"])


def gate_two(answer: dict, gold: dict) -> bool:
    row = gold["items"]["gate_two"]
    keys = ("gate", "date", "approver", "management_case_owner_missing")
    amounts = ("overlap_gbp", "claimed_cashable_gbp", "corrected_cashable_gbp")
    return same({key: answer.get(key) for key in keys}, {key: row[key] for key in keys}) and same(
        answer.get("benefit_pair"), row["benefit_pair"]) and all(money(answer.get(key), row[key]) for key in amounts)


def risk_updates(answer: dict, gold: dict) -> bool:
    row = {key: gold["items"]["risk_updates"][key] for key in ("reopen", "binding", "highest_open", "open_count")}
    return same({key: answer.get(key) for key in row}, row)
