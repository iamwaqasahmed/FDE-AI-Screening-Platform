"""Write the delivery artifacts, the workstream contracts, and their gold."""

from __future__ import annotations

import numpy as np

from simulation.delivery import tracker, tracker_plants
from simulation.delivery.accessibility import add_requirements
from simulation.delivery.benefits import benefits_frame, benefits_gold
from simulation.delivery.contracts import contracts_frame, contracts_markdown, integration_gold
from simulation.delivery.freezes import freeze_calendar
from simulation.delivery.funding import gates_frame, routes_frame
from simulation.delivery.issues import issues_frame
from simulation.delivery.letter_templates import template_files, templates_gold
from simulation.delivery.plan import pilot_gold
from simulation.delivery.raci import raci_frame, raci_gold
from simulation.delivery.risks import risks_frame, risks_gold
from simulation.delivery.roadmap import add_roadmap_docs, roadmap_frame, roadmap_gold
from simulation.delivery.velocity import build_done, recent_velocity, velocity_frame
from simulation.drops.bureau import bureau_gold, bureau_run

OUT = "handover/delivery"


def build(world: dict, rng: np.random.Generator) -> None:
    files, gold = world["files"], world["gold"]
    tickets = _tickets(rng)
    facts = tracker_plants.truth(tickets)
    velocity = velocity_frame(tickets, rng)
    files[f"{OUT}/tracker.csv"] = tracker.public(tickets)
    files[f"{OUT}/velocity.csv"] = velocity
    files["truth/delivery/tracker_truth.csv"] = facts
    gold["backlog"] = tracker_plants.backlog_gold(tickets, facts)
    pace = recent_velocity(velocity)
    remaining = gold["backlog"]["open_pilot_points"]
    sprints_needed, done = build_done(remaining, pace)
    gold["pilot_date"] = dict(pilot_gold(done, pace, remaining), sprints_needed=sprints_needed)
    _registers(world, rng)
    _contracts(world)


def _tickets(rng: np.random.Generator):
    frame = tracker.base_tickets(rng)
    frame = tracker_plants.plant_duplicates(frame, rng)
    frame = tracker_plants.plant_missing_criteria(frame, rng)
    return tracker.number(frame)


def _registers(world: dict, rng: np.random.Generator) -> None:
    files, gold = world["files"], world["gold"]
    roadmap = roadmap_frame()
    risks = risks_frame()
    raci = raci_frame()
    benefits = benefits_frame(rng)
    files[f"{OUT}/roadmap.csv"] = roadmap
    files[f"{OUT}/risk_register.csv"] = risks
    files[f"{OUT}/issues_log.csv"] = issues_frame()
    files[f"{OUT}/freeze_calendar.csv"] = freeze_calendar()
    files[f"{OUT}/raci.csv"] = raci
    files[f"{OUT}/funding_gates.csv"] = gates_frame()
    files[f"{OUT}/procurement_routes.csv"] = routes_frame()
    files[f"{OUT}/benefits_register.csv"] = benefits
    files.update(template_files())
    add_roadmap_docs(world, roadmap)
    add_requirements(world)
    gold["roadmap"] = roadmap_gold(roadmap)
    gold["risks"] = risks_gold(risks)
    gold["raci"] = raci_gold(raci)
    gold["benefits"] = benefits_gold(benefits)
    gold["accessibility"] = templates_gold()


def _contracts(world: dict) -> None:
    files, gold = world["files"], world["gold"]
    files["engagement/workstreams/contracts.md"] = contracts_markdown()
    files["engagement/workstreams/contracts.csv"] = contracts_frame()
    lost_chase = bureau_gold(*bureau_run(world))["lost_chase"]
    gold["integration"] = integration_gold(world, gold["pilot_date"], gold["benefits"], lost_chase)
