"""Eight planning tasks. The dates come from the path, not from the roadmap."""

from __future__ import annotations

from simulation.eval.agent.question import make


def cases(items: dict) -> list[dict]:
    path, route, road, pace = items["critical_path"], items["procurement_route"], items["roadmap_items"], items["pace"]
    gate, benefits = items["gate_two"], items["gate_two"]["benefit_pair"]
    rows = [
        ("plan-earliest", "What is the earliest pilot go-live, and which constraint binds?",
         {"go_live": path["earliest"]["go_live"], "binding": path["binding"]}, ("go_live", "binding"),
         ["G2", route["route"], "FRZ-0301"]),
        ("plan-latest", "If procurement takes its longest lead, what is the latest go-live, and which constraint binds?",
         {"go_live": path["latest"]["go_live"], "binding": path["latest"]["binding"]}, ("go_live", "binding"),
         ["G2", route["route"], "FRZ-0301"]),
        ("plan-assumed", "Under the direct award the roadmap assumes, what is the earliest go-live, and which constraint binds?",
         {"go_live": path["assumed_earliest"], "binding": path["assumed_binding"]}, ("go_live", "binding"),
         ["G2", route["assumed_route"], "FRZ-0301"]),
        ("plan-requested", "Can the pilot go live on the requested date under any procurement route?",
         {"feasible": path["requested_feasible"]}, ("feasible",), ["G2", "FRZ-0301"]),
        ("plan-gate3", "Does the pilot readiness gate pass on its scheduled date?",
         {"passes": road["g3_passes"], "not_before": road["g3_not_before"]}, ("passes", "not_before"), ["G3", "FRZ-0301"]),
        ("plan-rm02", "Can the vendor contract roadmap item meet its target date?",
         {"feasible": road["rm02_feasible"]}, ("feasible",), ["RM-02", "G2"]),
        ("plan-pace", "How many sprints does the open pilot work need at Heron's recent pace, and when is the build done?",
         {"sprints": pace["sprints_needed"], "build_done": pace["build_done"]}, ("sprints", "build_done"),
         ["tracker.csv", "velocity.csv"]),
        ("plan-cash", "What is the corrected annual cashable benefit, in pounds, once the double count is removed?",
         {"gbp": gate["corrected_cashable_gbp"]}, ("gbp",), list(benefits)),
    ]
    return [make(case_id, question, expected, "value", "plan", keys, None, "multi_hop", visit, max_steps=8)
            for case_id, question, expected, keys, visit in rows]
