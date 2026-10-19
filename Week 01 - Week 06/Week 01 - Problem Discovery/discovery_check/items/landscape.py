"""Landscape items: systems, owners, records, hosting, freezes, and the keys."""

from __future__ import annotations

from discovery_check.rules import same_set


def systems(answer: dict, gold: dict) -> bool:
    rows = answer.get("systems")
    if not isinstance(rows, list):
        return False
    found = {(row.get("id"), row.get("zone")) for row in rows if isinstance(row, dict)}
    expected = {(row["id"], row["zone"]) for row in gold["systems"]}
    return found == expected


def safety_owner(answer: dict, gold: dict) -> bool:
    return answer.get("named") is bool(gold["safety_owner"])


def record_owners(answer: dict, gold: dict) -> bool:
    row = gold["records"]
    return (
        answer.get("grade") == row["grade"]
        and answer.get("dispatch") == row["dispatch"]
        and answer.get("score") == row["score"]
        and sorted(answer.get("seen") or []) == row["seen"]
    )


def vendor_hosting(answer: dict, gold: dict) -> bool:
    hosting = gold["vendor_hosting"].lower()
    region = str(answer.get("region", "")).lower()
    if region == "eu":
        return "eu" in hosting
    if region == "uk":
        return "uk" in hosting and "eu" not in hosting
    return False


def freezes(answer: dict, gold: dict) -> bool:
    for name, row in gold["freezes"].items():
        given = answer.get(name) or {}
        if given.get("ref") != row["ref"] or given.get("start") != row["start"]:
            return False
    return True


def no_master_key(answer: dict, gold: dict) -> bool:
    return answer.get("master") is False and same_set(answer.get("keys"), gold["keys"])


def timeline_refs(answer: dict, gold: dict) -> bool:
    return same_set(answer.get("refs"), [row["ref"] for row in gold["timeline"]])
