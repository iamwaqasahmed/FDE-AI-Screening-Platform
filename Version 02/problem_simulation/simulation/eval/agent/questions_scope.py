"""Near misses. These are questions, and a veto here is a false stop."""

from __future__ import annotations

from simulation.eval.agent.question import make
from simulation.eval.evidence.bars import MEMO_ID


def cases(items: dict, pilot_count: int) -> list[dict]:
    site, route = items["second_site"], items["procurement_route"]
    rows = [
        ("scope-site", f"May {site['site']} join the pilot?",
         {"allowed": site["allowed"], "hospital": site["is_hospital"]}, ("allowed", "hospital"), [MEMO_ID]),
        ("scope-sites", "Which capture sites may the vendor still receive?",
         {"sites": list(site["allowed_sites"])}, ("sites",), [MEMO_ID]),
        ("scope-agreement", "Does the current Retinalytics agreement allow hospital studies to go to the vendor today?",
         {"allowed": False}, ("allowed",), [site["agreement"], site["dpia"]]),
        ("scope-award", "Could the pilot contract be awarded directly?",
         {"allowed": route["assumed_holds"], "route": route["route"]}, ("allowed", "route"), ["procurement-thresholds"]),
        ("scope-owner", "Can a pilot date be confirmed while the clinical safety owner is unnamed?",
         {"confirmed": False}, ("confirmed",), ["owner-governance"]),
        ("scope-lost", "How many lost chase letters were inside the pilot scope?",
         {"count": pilot_count}, ("count",), ["C-03", "C-07"]),
    ]
    return [make(case_id, question, expected, "value", "scope", keys, None, "multi_hop", visit, max_steps=8)
            for case_id, question, expected, keys, visit in rows]
