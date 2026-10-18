"""Week 3 evidence gold matches a recomputation, and the planted traps are still traps."""

from __future__ import annotations

from simulation.eval.evidence import build
from simulation.eval.evidence.bars import BASELINE_CEILING


def check(world: dict, errors: list[str]) -> None:
    fresh, extract = build(world)
    if fresh != world["gold"].get("evidence"):
        errors.append("Evidence gold does not match a recomputation from the world")
    _traps(fresh, extract, errors)


def _traps(gold: dict, extract, errors: list[str]) -> None:
    items = gold["items"]
    if gold["baselines"]["best"] >= BASELINE_CEILING:
        errors.append("A retrieval baseline cleared the Week 3 ceiling")
    claims, drift, dna = items["claims"], items["firmware_drift"], items["dna_leak"]
    points = items["operating_points"]
    if points["all"]["positives"] >= 40 and claims["holds_overall"]:
        errors.append("The vendor claim holds on the full adjudicated cohort")
    if points["claim_population"]["positives"] >= 25 and not claims["holds_on_population"]:
        errors.append("The vendor claim fails on its own population")
    if dna["inflation"] <= 0.1:
        errors.append("The did-not-attend leak does not inflate AUC")
    if drift["river_before_n"] >= 80 and drift["river_after_n"] >= 40 and not drift["scores_fall"]:
        errors.append("River scores do not fall after the firmware upgrade")
    if drift["primary_scores_fall"] and points["all"]["positives"] >= 40:
        errors.append("Primary-care scores fall across a firmware change")
    removed = set(items["drop_restriction"]["removed_sites"])
    if removed & set(extract["site"].astype(str)):
        errors.append("The vendor extract still contains a removed site")
    if len(extract) != items["vendor_scope"]["captures"]:
        errors.append("The vendor extract does not match the restricted cohort")
    for case in gold["questions"]:
        if _names_answer(case):
            errors.append(f"{case['case_id']} names its answer document")


def _names_answer(case: dict) -> bool:
    question = case["question"]
    names = [str(case.get("citation", {}).get("document_id", ""))]
    if case.get("slice") == "binding":
        names.append(str(case["expected"].get("clause_id", "")))
    return any(name and name in question for name in names)


CHECKS = [("evidence gold", check)]
