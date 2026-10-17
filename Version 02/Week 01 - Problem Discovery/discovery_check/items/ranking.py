"""Ranking, the workshop, and the loudest complaint."""

from __future__ import annotations


def ranking(answer: dict, gold: dict) -> bool:
    order = answer.get("order")
    info = gold["ranking"]
    if not isinstance(order, list) or sorted(order) != sorted(info["keys"]):
        return False
    if order[0] != info["highest"] or order[-1] != info["lowest"]:
        return False
    if info["blockers"].get(order[0]):
        return False
    position = {key: index for index, key in enumerate(order)}
    for key, deps in info["prerequisites"].items():
        if any(position[dep] > position[key] for dep in deps):
            return False
    return True


def workshop(answer: dict, gold: dict) -> bool:
    row = gold["workshop"]
    return (
        answer.get("top_idea") == row["top_idea"]
        and answer.get("top_opportunity") == row["top_opportunity"]
        and answer.get("is_highest_net") is False
    )


def voiced_vs_costly(answer: dict, gold: dict) -> bool:
    return answer.get("most_voiced") == gold["research"]["most_voiced"] and answer.get("same") is False
