"""Drop items: the schema, the reissue, the restored local ids, and the API that did not follow."""

from __future__ import annotations

from course.checks.rules import as_int, same_set


def drop_schema(answer: dict, gold: dict) -> bool:
    row = gold["drop"]
    return answer.get("renamed") == row["renamed"] and same_set(answer.get("added", []), row["added"]) and answer.get("dob") == row["dob"]


def drop_reissue(answer: dict, gold: dict) -> bool:
    row = gold["drop"]
    return as_int(answer.get("count")) == row["reissued"] and as_int(answer.get("warehouse_lost")) == row["warehouse_lost"]


def drop_local_ids(answer: dict, gold: dict) -> bool:
    return as_int(answer.get("added")) == gold["drop"]["local_ids_added"]


def api_v3(answer: dict, gold: dict) -> bool:
    row = gold["api"]
    return same_set(answer.get("keeps", []), row["keeps"]) and same_set(answer.get("missing", []), row["missing"]) and answer.get("old_numbers") is True
