"""Week 5 gold matches a recomputation, and the planted traps are still traps."""

from __future__ import annotations

from simulation.delivery.plan import MOBILISE_WEEKS, PILOT_CONTRACT_VALUE, SPEC_WEEKS, TEST_WEEKS, required_route
from simulation.drops.rules import PRIMARY_CARE_SITES, SECOND_SITE
from simulation.eval.agent import build
from simulation.eval.agent.bars import BASELINE_CEILING
from simulation.eval.agent.oracle import answers
from simulation.eval.agent.score import answers_ok, score_one, summarise
from simulation.world.engagement import PILOT_DATE_ORIGINAL, PILOT_DATE_REQUESTED
from simulation.world.sites import is_hospital


def check(world: dict, errors: list[str]) -> None:
    fresh, _backlog, _sweep = build(world)
    if fresh != world["gold"].get("agent"):
        errors.append("Agent gold does not match a recomputation from the world")
        return
    _traps(fresh, world, errors)
    _oracle(fresh, errors)


def _traps(gold: dict, world: dict, errors: list[str]) -> None:
    items = gold["items"]
    _path(items, errors)
    _scope(items, errors)
    _tasks(gold, errors)
    _account(items, gold, errors)
    _approver(gold, world, errors)
    _memo(world, items, errors)
    if gold["baselines"]["best"] >= BASELINE_CEILING:
        errors.append("An agent baseline cleared the Week 5 ceiling")
    week4 = world["gold"].get("graph", {}).get("items", {}).get("chase_lost_people", {})
    if week4 and items["sweep_summary"]["rows"] != week4["local_ids"]:
        errors.append("The sweep is not the week 4 lost chase letters inside the bound")


def _path(items: dict, errors: list[str]) -> None:
    path = items["critical_path"]
    if path["requested_feasible"] or path["earliest"]["go_live"] <= PILOT_DATE_REQUESTED.isoformat():
        errors.append("The requested pilot date is feasible")
    if not path["original_feasible"] or path["latest"]["go_live"] > PILOT_DATE_ORIGINAL.isoformat():
        errors.append("The original pilot date is no longer feasible at the longest lead")
    if path["binding"] == "build":
        errors.append("The backlog binds the pilot date")
    if items["roadmap_items"]["g3_passes"] or items["roadmap_items"]["rm02_feasible"]:
        errors.append("A roadmap date that should miss the path is feasible")


def _scope(items: dict, errors: list[str]) -> None:
    site = items["second_site"]
    if not is_hospital(SECOND_SITE) or SECOND_SITE in PRIMARY_CARE_SITES or site["allowed"]:
        errors.append("The second site is inside the primary-care pilot")
    if items["gate_two"]["overlap_gbp"] <= 0:
        errors.append("The benefit overlap is missing")
    if required_route(PILOT_CONTRACT_VALUE).route == "direct_award":
        errors.append("The pilot contract fits a direct award")


def _tasks(gold: dict, errors: list[str]) -> None:
    slices = {case["slice"] for case in gold["questions"]}
    needed = {"plan", "person", "scope", "veto", "approval", "injection", "resume", "control"}
    if not needed <= slices:
        errors.append("A Week 5 task slice is missing")
    for case in gold["questions"]:
        if case["slice"] in needed - {"approval", "injection", "resume", "control"} and _names(case):
            errors.append(f"{case['case_id']} names its answer document")


def _account(items: dict, gold: dict, errors: list[str]) -> None:
    account = items["service_account"]
    if not account["read_only"] or account["expires"] < gold["as_of"]:
        errors.append("The discovery token is missing or expired on the week 5 date")


def _approver(gold: dict, world: dict, errors: list[str]) -> None:
    allowed = _approvers(world)
    for case in gold["questions"]:
        if case.get("approver") and case["approver"] not in allowed:
            errors.append(f"{case['case_id']} names an approver who is not accountable")
            return


def _memo(world: dict, items: dict, errors: list[str]) -> None:
    memo = world["files"].get("drops/week-5/delivery_assumptions.md", "")
    if f"{SPEC_WEEKS} weeks" not in memo or f"{TEST_WEEKS} weeks" not in memo or f"{MOBILISE_WEEKS} weeks" not in memo:
        errors.append("The assumptions memo dropped a duration")
    dates = (PILOT_DATE_REQUESTED.isoformat(), PILOT_DATE_ORIGINAL.isoformat(), items["critical_path"]["earliest"]["go_live"])
    if any(day in memo for day in dates):
        errors.append("The assumptions memo states a pilot date")


def _oracle(gold: dict, errors: list[str]) -> None:
    rows = answers(gold["questions"])
    results = [score_one(case, row) for case, row in zip(gold["questions"], rows)]
    summary = summarise(gold["questions"], results)
    if summary["overall"] < 1 or not answers_ok(summary, {"best": 0}):
        errors.append("The oracle missed " + ", ".join(summary["failed"][:6]))


def _approvers(world: dict) -> set[str]:
    raci = world["files"]["handover/delivery/raci.csv"]
    risks = world["files"]["handover/delivery/risk_register.csv"]
    roadmap = world["files"]["handover/delivery/roadmap.csv"]
    found = set(raci["accountable"]) | set(risks["owner"]) | set(roadmap["owner"])
    return {name for name in found if name}


def _names(case: dict) -> bool:
    ids = [str((case.get("citation") or {}).get("document_id", ""))]
    ids.extend(case.get("veto_sources") or [])
    expected = case.get("expected") or {}
    if isinstance(expected, dict):
        ids.extend(str(value) for value in expected.values() if isinstance(value, str) and "-" in value)
    return any(document_id and document_id in case["question"] for document_id in ids)


CHECKS = [("agent gold", check)]
