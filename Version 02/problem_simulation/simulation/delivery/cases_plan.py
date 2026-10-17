"""Eval cases on the plan: pilot date, procurement, gates, freezes, velocity, roadmap, risks, and RACI."""

from __future__ import annotations

from simulation.delivery.plan import PILOT_CONTRACT_VALUE, freeze
from simulation.eval.case_format import make_case
from simulation.world.engagement import PILOT_DATE_ORIGINAL, PILOT_DATE_REQUESTED

D = "handover/delivery"
PLAN_SOURCES = (f"{D}/procurement_routes.csv", f"{D}/funding_gates.csv", f"{D}/freeze_calendar.csv", f"{D}/roadmap.csv")


def ask(case_id: str, question: str, expected: dict, sources: tuple[str, ...], budget: str = "lookup",
        outcome: str = "delivery", roles: tuple[str, ...] = ("pm",), kind: str = "value") -> dict:
    surfaces = tuple(sorted({"drops" if source.startswith("drops") else source.split("/")[1].split(".")[0] for source in sources}))
    return make_case(f"delivery-{case_id}", question, expected, outcome=outcome, roles=roles, surfaces=surfaces,
                     budget=budget, sources=sources, kind=kind)


def cases(world: dict) -> list[dict]:
    pilot, files = world["gold"]["pilot_date"], world["files"]
    path = pilot["critical_path"]
    velocity = files[f"{D}/velocity.csv"]
    kestrel = round(float(velocity[velocity["team"] == "Kestrel"]["completed_points"].mean()), 1)
    letters = freeze("FRZ-0302")
    return [
        ask("pilot-feasible", f"Can the AI triage pilot go live on {PILOT_DATE_REQUESTED.isoformat()}?",
            {"feasible": pilot["feasible"]}, PLAN_SOURCES, "multi_hop", roles=("pm", "consultant")),
        ask("pilot-earliest", "What is the earliest date the pilot can go live, given procurement, the freeze calendar, and the backlog?",
            {"earliest_pilot": pilot["earliest_pilot"]}, (*PLAN_SOURCES, f"{D}/tracker.csv", f"{D}/velocity.csv"), "analysis"),
        ask("pilot-binding", "Which constraint sets the date the registry interface can first be released for the pilot?",
            {"binding": path["binding"]}, PLAN_SOURCES, "analysis"),
        ask("pilot-original-feasible", f"Is the roadmap pilot date of {PILOT_DATE_ORIGINAL.isoformat()} still achievable?",
            {"feasible": pilot["original_feasible"]}, PLAN_SOURCES, "multi_hop"),
        ask("procurement-route", f"Which procurement route does a pilot contract worth {PILOT_CONTRACT_VALUE} GBP require?",
            {"route": pilot["required_route"]}, (f"{D}/procurement_routes.csv", f"{D}/roadmap.csv")),
        ask("procurement-min-weeks", "What is the shortest lead time for the required procurement route, in weeks?",
            {"weeks": int(files[f"{D}/procurement_routes.csv"].set_index("route").loc[pilot["required_route"], "lead_weeks_min"])},
            (f"{D}/procurement_routes.csv",)),
        ask("procurement-assumed", "The roadmap treats the contract as a direct award. Under that assumption, what is the earliest go-live?",
            {"route": pilot["cdo_assumed_route"], "earliest_pilot": pilot["earliest_if_assumed_route"]}, PLAN_SOURCES, "analysis"),
        ask("gate-2", "On what date may procurement for the pilot first start?", {"date": path["gate_2"]}, (f"{D}/funding_gates.csv",)),
        ask("contract-award", "What is the earliest contract award date for the pilot?", {"date": path["contract_award"]},
            PLAN_SOURCES, "multi_hop"),
        ask("registry-freeze-end", "Until when are registry interface changes frozen?", {"date": path["registry_freeze_end"]},
            (f"{D}/freeze_calendar.csv",)),
        ask("registry-window", "Which registry release window is the first one the pilot interface can use?",
            {"date": path["registry_window"]}, PLAN_SOURCES, "analysis"),
        ask("letters-freeze", "When is the letter bureau frozen for template changes?",
            {"start": letters.start.isoformat(), "end": letters.end.isoformat()}, (f"{D}/freeze_calendar.csv",)),
        ask("velocity-heron", "What is team Heron's average completed points over its last six sprints?",
            {"points": pilot["velocity_points_per_sprint"]}, (f"{D}/velocity.csv",)),
        ask("velocity-kestrel", "What is team Kestrel's average completed points per sprint?", {"points": kestrel}, (f"{D}/velocity.csv",)),
        ask("remaining-points", "How many story points of open pilot work remain once duplicate tickets are removed?",
            {"points": pilot["remaining_points"]}, (f"{D}/tracker.csv",), "analysis"),
        ask("sprints-needed", "At Heron's recent pace, how many sprints does the open pilot work need?",
            {"sprints": pilot["sprints_needed"]}, (f"{D}/tracker.csv", f"{D}/velocity.csv"), "analysis"),
        *_registers(world),
    ]


def _registers(world: dict) -> list[dict]:
    gold, files = world["gold"], world["files"]
    raci = files[f"{D}/raci.csv"].set_index("activity")
    issues = files[f"{D}/issues_log.csv"]
    roadmap = (f"{D}/roadmap.csv", f"corpus/delivery/{gold['roadmap']['board_doc']}.md")
    return [
        ask("roadmap-conflicts", "Which roadmap items have a different priority from the board's September decision?",
            {"item_ids": [row["item_id"] for row in gold["roadmap"]["conflicts"]]}, roadmap, "multi_hop", roles=("pm", "consultant")),
        ask("roadmap-frozen", "Which roadmap targets fall inside a change freeze?",
            {"item_ids": [row["item_id"] for row in gold["roadmap"]["frozen_targets"]]},
            (f"{D}/roadmap.csv", f"{D}/freeze_calendar.csv"), "multi_hop"),
        ask("roadmap-unowned", "Which roadmap item has no owner?", {"item_ids": gold["roadmap"]["unowned"]}, (f"{D}/roadmap.csv",)),
        ask("risk-no-mitigation", "Which risk was closed without a mitigation?",
            {"risk_ids": gold["risks"]["closed_without_mitigation"]}, (f"{D}/risk_register.csv",)),
        ask("risk-highest-open", "Which open risk has the highest score?", {"risk_id": gold["risks"]["highest_open"]},
            (f"{D}/risk_register.csv",)),
        ask("risk-open-count", "How many risks are open?", {"count": gold["risks"]["open_risks"]}, (f"{D}/risk_register.csv",)),
        ask("issues-open-count", "How many issues are still open?", {"count": int((issues["status"] == "Open").sum())},
            (f"{D}/issues_log.csv",)),
        ask("raci-safety", "Who is accountable for the clinical safety case sign-off?",
            {"named": False, "accountable": ""}, (f"{D}/raci.csv", "handover/owners.csv"), roles=("pm", "consultant")),
        ask("raci-security", "Who is accountable for the security review of the vendor integration?",
            {"accountable": raci.loc["Security review of the vendor integration", "accountable"]}, (f"{D}/raci.csv",), roles=("architect",)),
    ]
