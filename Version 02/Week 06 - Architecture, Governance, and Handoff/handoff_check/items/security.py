"""Threats, the Version 01 gaps, and the account that expires this week."""

from __future__ import annotations

from handoff_check.items.match import same


def threat_summary(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["threat_summary"])


def prototype_gaps(answer: dict, gold: dict) -> bool:
    row = gold["items"]["prototype_gaps"]
    keys = ("default_model", "model_host", "on_register", "logs_question", "sign_in", "replace_with")
    return same({key: answer.get(key) for key in keys}, {key: row[key] for key in keys}) and same(
        answer.get("copies"), row["copies"]) and _gaps(answer.get("gaps"), row["gaps"])


def production_account(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["production_account"])


def adr_index(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["adr_index"])


def _gaps(given, expected: list[dict]) -> bool:
    if not isinstance(given, list):
        return False
    got = {item.get("gap"): item.get("standard") for item in given if isinstance(item, dict)}
    need = {item["gap"]: item["standard"] for item in expected}
    return got == need
