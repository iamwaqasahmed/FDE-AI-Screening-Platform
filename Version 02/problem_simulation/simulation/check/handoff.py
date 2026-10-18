"""Week 6 gold matches a recomputation, and the planted traps are still traps."""

from __future__ import annotations

from simulation.eval.handoff import build
from simulation.eval.handoff.oracle import pack
from simulation.eval.handoff.score_files import score_flows, score_hazards
from simulation.eval.handoff.score_pages import pages_agree, score_document
from simulation.eval.handoff.score_records import score_contract, score_dockerfile, score_model_card, score_transparency

GAPS = {"data_in_image", "model_off_register", "question_in_log", "local_log", "no_sign_in"}


def check(world: dict, errors: list[str]) -> None:
    fresh = build(world)
    if fresh != world["gold"].get("handoff"):
        errors.append("Handoff gold does not match a recomputation from the world")
        return
    _traps(fresh, world, errors)
    _oracle(fresh, errors)
    _naive(fresh, errors)


def _traps(gold: dict, world: dict, errors: list[str]) -> None:
    items = gold["items"]
    if items["conditions"]["all_met"] or items["drop_owner"]["pilot_may_start"] or items["register_state"]["g3"]["passes"]:
        errors.append("A week 6 condition is met")
    if items["drop_owner"]["register_owner"] != "" or items["register_state"]["owners_register"] != "":
        errors.append("The owners register names the clinical safety owner")
    if not items["production_account"]["expires_this_week"]:
        errors.append("The discovery token does not expire in week 6")
    if not GAPS <= {item["gap"] for item in items["prototype_gaps"]["gaps"]}:
        errors.append("A Version 01 production gap is missing")
    _risk(world, items, errors)
    hosting = items["current_state"]["vendor_hosting"].lower()
    if "uk" in hosting or "eu" not in hosting:
        errors.append("The vendor is hosted in the UK")
    levels = items["service_levels"]
    if levels["grader_tier"] >= levels["vendor_tier"] or levels["grader_waits"]:
        errors.append("The grader tier does not beat the vendor tier")
    scored = set(world["gold"].get("ai_governance", {}).get("values", {}).get("sites in scope", []))
    if not scored - set(items["flow_rules"]["allowed_sites"]):
        errors.append("Scored sites do not differ from the pilot sites")


def _risk(world: dict, items: dict, errors: list[str]) -> None:
    risks = world["files"]["handover/delivery/risk_register.csv"].set_index("risk_id")
    closed = str(risks.at["R-11", "status"]) == "Closed"
    live = "T4" in items["threat_summary"]["live"] and "T3" not in items["threat_summary"]["live"]
    if not closed or not live or items["threat_summary"]["reopen"] != "R-11":
        errors.append("R-11 is not a closed risk over a live threat")


def _oracle(gold: dict, errors: list[str]) -> None:
    built = pack(gold)
    failed = []
    if not score_flows(built["flows"], gold)["ok"]:
        failed.append("flows")
    if not _threats(built, gold):
        failed.append("threats")
    if not score_hazards(built["hazards"], gold)["ok"]:
        failed.append("hazards")
    if not score_dockerfile(built["dockerfile"], gold)["ok"]:
        failed.append("dockerfile")
    if not score_contract(built["contract"], gold)["ok"]:
        failed.append("contract")
    if not score_transparency(built["transparency"], gold)["ok"]:
        failed.append("transparency")
    if not score_model_card(built["model_card"], gold)["ok"]:
        failed.append("model_card")
    for key in ("adr-01", "adr-02", "adr-03", "adr-04", "executive", "clinical", "runbook"):
        if not score_document(built["texts"][key], gold["text"][key])["ok"]:
            failed.append(key)
    if not pages_agree(built["texts"]["executive"], built["texts"]["clinical"], gold["text"]["pages"]):
        failed.append("pages")
    if failed:
        errors.append("The handoff oracle missed " + ", ".join(failed))


def _threats(built: dict, gold: dict) -> bool:
    from simulation.eval.handoff.score_files import score_threats

    return score_threats(built["threats"], gold)["ok"]


def _naive(gold: dict, errors: list[str]) -> None:
    flows = gold and pack(gold)["flows"].copy()
    flows.loc[flows["data"].eq("hospital_study"), "allowed"] = "yes"
    signed = pack(gold)["hazards"].copy()
    signed["signed_by"] = "signed"
    if score_flows(flows, gold)["ok"] or score_hazards(signed, gold)["ok"] or score_dockerfile("COPY data/handover /data\n", gold)["ok"]:
        errors.append("A naive handoff passed")


CHECKS = [("handoff gold", check)]
