"""The route, the path, and the roadmap dates."""

from __future__ import annotations

from agent_check.items.match import near, same


def procurement_route(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["procurement_route"])


def critical_path(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["critical_path"])


def roadmap_items(answer: dict, gold: dict) -> bool:
    return same(answer, gold["items"]["roadmap_items"])


def pace(answer: dict, gold: dict) -> bool:
    row = gold["items"]["pace"]
    keys = ("team", "sprints_counted", "sprints_needed", "build_done", "binding")
    return same({key: answer.get(key) for key in keys}, {key: row[key] for key in keys}) and near(answer.get("velocity"), row["velocity"], 0.1)
