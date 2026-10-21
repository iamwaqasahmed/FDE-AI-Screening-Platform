"""Delivery and drops: the stop condition, the impossible date, the double count, the failing letter, drops, and refs."""

from __future__ import annotations

import re
from datetime import date

import pandas as pd

from simulation.delivery.letter_templates import TEMPLATES
from simulation.delivery.accessibility import failures
from simulation.delivery.plan import PILOT_CONTRACT_VALUE, required_route
from simulation.delivery.raci import SAFETY_ACTIVITIES
from simulation.systems.catalog import OWNERS
from simulation.world.engagement import PILOT_DATE_REQUESTED
from simulation.world.timeline import TIMELINE

REF = re.compile(r"\b(?:CHG|INC|FRZ)-\d{4}\b")
UID = re.compile(r"\bP\d{7}\b")
PUBLIC = ("handover/delivery/", "handover/letters/templates/", "drops/", "engagement/workstreams/")
D = "handover/delivery"


def raci_safety_blank(world: dict, errors: list[str]) -> None:
    raci = world["files"][f"{D}/raci.csv"]
    rows = raci[raci["activity"].isin(SAFETY_ACTIVITIES)]
    if len(rows) != len(SAFETY_ACTIVITIES) or (rows["accountable"] != "").any():
        errors.append("RACI names a clinical safety owner, or a safety activity is missing.")
    if (raci.loc[~raci["activity"].isin(SAFETY_ACTIVITIES), "accountable"] == "").any():
        errors.append("RACI leaves an accountable blank outside clinical safety.")
    if dict(OWNERS).get("clinical_safety_owner") != "" or "handover/owners.csv" in world["files"]:
        errors.append("The owners register changed; it must stay blank.")


def pilot_infeasible(world: dict, errors: list[str]) -> None:
    gold = world["gold"]["pilot_date"]
    if gold["feasible"] or date.fromisoformat(gold["earliest_pilot"]) <= PILOT_DATE_REQUESTED:
        errors.append("The CDO's requested pilot date is feasible; the plant is gone.")
    if required_route(PILOT_CONTRACT_VALUE).route == "direct_award":
        errors.append("The pilot contract fits a direct award; the procurement plant is gone.")
    calendar = world["files"][f"{D}/freeze_calendar.csv"]
    if "FRZ-0301" not in set(calendar["ref"]):
        errors.append("FRZ-0301 is missing from the freeze calendar.")
    if not world["gold"]["roadmap"]["frozen_targets"]:
        errors.append("No roadmap target falls inside a freeze.")


def double_count(world: dict, errors: list[str]) -> None:
    gold = world["gold"]["benefits"]
    frame = world["files"][f"{D}/benefits_register.csv"].set_index("benefit_id")
    if gold["overlap_gbp"] <= 0 or any(bid not in frame.index for bid in gold["pair"]):
        errors.append("The benefits double count is missing.")
    elif gold["corrected_cashable_gbp"] >= gold["claimed_cashable_gbp"]:
        errors.append("Correcting the double count does not lower the cashable total.")


def one_failing_template(world: dict, errors: list[str]) -> None:
    failing = [tid for tid in TEMPLATES if failures(world["files"][f"handover/letters/templates/{tid}.md"])]
    if len(failing) != 1 or failing != world["gold"]["accessibility"]["failing"]:
        errors.append(f"Expected exactly one failing letter template, found {failing}.")


def drops_present(world: dict, errors: list[str]) -> None:
    drops = world["gold"].get("drops", {})
    for week in range(2, 7):
        gold = drops.get(f"week-{week}")
        if not gold or f"drops/week-{week}/README.md" not in world["files"]:
            errors.append(f"Week {week} drop or its gold is missing.")
            continue
        missing = [path for path in gold["files"] if f"drops/week-{week}/{path}" not in world["files"]]
        if missing:
            errors.append(f"Week {week} drop lists files it did not write: {missing}")
    press = drops.get("week-5", {}).get("press", {})
    if not press.get("must_mention") or not press.get("must_not_claim"):
        errors.append("The press query gold is missing.")
    if drops.get("week-6", {}).get("owner", "") == "":
        errors.append("Week 6 does not name the clinical safety owner.")


def refs_exist(world: dict, errors: list[str]) -> None:
    known = {item.ref for item in TIMELINE}
    cited: set[str] = set()
    for name in ("tracker.csv", "risk_register.csv", "issues_log.csv"):
        for value in world["files"][f"{D}/{name}"]["links"].astype(str):
            cited.update(REF.findall(value))
    unknown = sorted(cited - known)
    if unknown:
        errors.append(f"Delivery files cite timeline ids that do not exist: {unknown}")
    if not cited:
        errors.append("No delivery file cites the timeline.")


def backlog_plants(world: dict, errors: list[str]) -> None:
    gold = world["gold"]["backlog"]
    if not gold["duplicates"] or not gold["missing_criteria"] or not gold["blocked"]:
        errors.append("A tracker plant (duplicates, missing criteria, or blocked work) is missing.")
    if gold["open_pilot_points_with_duplicates"] <= gold["open_pilot_points"]:
        errors.append("No duplicate inflates the open pilot work.")
    if not 550 <= gold["tickets"] <= 650:
        errors.append(f"Tracker has {gold['tickets']} tickets, expected about 600.")


def no_person_ids(world: dict, errors: list[str]) -> None:
    for path, content in sorted(world["files"].items()):
        if not path.startswith(PUBLIC):
            continue
        if isinstance(content, pd.DataFrame):
            text = " ".join(content.columns) + " " + " ".join(content.astype(str).values.ravel())
        else:
            text = str(content)
        if "person_uid" in text or UID.search(text):
            errors.append(f"A person id leaked into {path}")


CHECKS = [
    ("delivery raci safety owner blank", raci_safety_blank),
    ("delivery pilot date infeasible", pilot_infeasible),
    ("delivery benefits double count", double_count),
    ("delivery one failing letter template", one_failing_template),
    ("drops weeks 2-6 and press gold", drops_present),
    ("delivery timeline refs exist", refs_exist),
    ("delivery backlog plants", backlog_plants),
    ("delivery and drops no person ids", no_person_ids),
]
