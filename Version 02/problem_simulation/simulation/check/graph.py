"""Week 4 graph gold matches a recomputation, and the planted traps are still traps."""

from __future__ import annotations

from simulation.eval.enterprise.cohorts import cohorts
from simulation.eval.graph import build
from simulation.eval.graph.bars import BASELINE_CEILING


def check(world: dict, errors: list[str]) -> None:
    fresh, _reconciled = build(world)
    if fresh != world["gold"].get("graph"):
        errors.append("Graph gold does not match a recomputation from the world")
        return
    _traps(fresh, world, errors)


def _traps(gold: dict, world: dict, errors: list[str]) -> None:
    truth, items = gold["truth"], gold["items"]
    if gold["baselines"]["best"] >= BASELINE_CEILING:
        errors.append("A retrieval baseline cleared the Week 4 ceiling")
    loop = set(truth["loop_days"])
    if not set(truth["lost_days"]) <= loop or not set(truth["duplicate_days"]) <= loop:
        errors.append("Losses or second copies fall outside the retry loop")
    if items["drop_incident"]["requests"] > 100 and not (truth["lost_days"] and truth["duplicate_days"]):
        errors.append("The bureau window did not both lose letters and print second copies")
    if items["contact_status"]["bound"] != cohorts(world)["overdue"]["upper_bound"]:
        errors.append("The chase bound does not match the week 2 upper bound")
    if truth["chased"] > 20 and truth["chased"] == truth["hidden_overdue"]:
        errors.append("The chase list is the hidden overdue cohort")
    integration = world["gold"].get("integration", {}).get("overdue_chase_letters_lost")
    if integration is not None and integration != truth["hidden_lost"]:
        errors.append("Hidden lost chase letters do not match the integration value")
    if truth["hidden_lost"] > items["chase_lost_people"]["local_ids"] and items["drop_incident"]["requests"] > 100:
        errors.append("Visible C-07 is below the hidden lost-chase count")
    path = [case for case in gold["questions"] if case["slice"] == "path"]
    local = [case for case in path if case["expected"].get("limit") not in ("", None)]
    if len(path) >= 8 and len(local) < 3:
        errors.append("Fewer than three path questions land on a local clock")
    for case in gold["questions"]:
        if _names_answer(case):
            errors.append(f"{case['case_id']} names its answer document")
    if items["bureau_agreement"]["covers_chase"]:
        errors.append("The bureau agreement covers chase letters")


def _names_answer(case: dict) -> bool:
    question = case["question"]
    names = [str((case.get("citation") or {}).get("document_id", ""))]
    expected = case.get("expected") or {}
    if isinstance(expected, dict):
        for value in expected.values():
            if isinstance(value, str):
                names.append(value)
            elif isinstance(value, list):
                names.extend(str(item) for item in value)
    return any(_document(name) and name in question for name in names)


def _document(name: str) -> bool:
    return bool(name) and "-" in name and not name[0].isdigit() and not name.startswith("LR-")


CHECKS = [("graph gold", check)]
