"""Ophthalmology lead: a backlog number inflated by blank seen dates, and a real consultant gap."""

from __future__ import annotations

from simulation.stakeholders.model import Card, Conflict, Persona, fact, node

KEY = "ophthalmology_lead"
GAP = "constant/simulation.care.referrals:CONSULTANT_GAP"


def build(world: dict) -> Persona:
    facts = (
        fact(world, "ol-backlog", "My list shows {0} referrals since {1} with no seen date.",
             "events/lead_backlog", "events/backlog_from"),
        fact(world, "ol-blank", "Booked and seen dates are often blank in our messages; the seen date lives in the {0} "
             "clinic letters.", "constant/simulation.systems.catalog:SEEN_DATE_SYSTEMS:1"),
        fact(world, "ol-gap", "We lost a consultant from {0} to {1} and fast-track slots were cut.", f"{GAP}:0", f"{GAP}:1"),
        fact(world, "ol-dna", "{0} of referred patients do not attend their hospital appointment.",
             "events/ophthalmology_dna"),
        fact(world, "ol-lab", "The HbA1c feed is keyed by lab patient id, not MRN, and units changed on {0}.",
             "clock/LAB_UNIT_CHANGE"),
        fact(world, "ol-progress", "{0} referred patients progressed while they waited.", "events/progressed_in_delay",
             must_surface=False),
    )
    tree = (
        node("backlog", "backlog waiting wait list queue referrals", "The hospital backlog is far worse than the board "
             "thinks."),
        node("number", "number many count figure size", "I count it myself.", "ol-backlog", "backlog"),
        node("seen", "seen date dates blank recorded message messages", "The messages are patchy.", "ol-blank", "backlog"),
        node("capacity", "capacity clinic clinics slots consultant staffing", "Clinic capacity has been tight."),
        node("gap", "vacancy vacancies gap retire retired fast track cut", "We had a hard year.", "ol-gap", "capacity"),
        node("dna", "attend dna miss missed show", "Not everyone comes.", "ol-dna", "capacity"),
        node("data", "data lab hba1c feed feeds systems", "We have more data than we use."),
        node("lab", "identifier id ids mrn units key", "The lab does its own thing.", "ol-lab", "data"),
        node("harm", "harm outcome outcomes progress progressed worse", "Waiting is not harmless.", "ol-progress"),
        node("goals", "goal goals want priority priorities success", "I want urgent patients seen inside the standard."),
    )
    return Persona(
        key=KEY,
        card=Card(
            goals=("See urgent referrals inside the standard", "Get the consultant post filled"),
            constraints=("Owns the hospital clinic, not the screening service",),
            says_first="The backlog is a capacity problem. Software will not see patients.",
            wants="Another consultant and an honest backlog number.",
        ),
        facts=facts,
        tree=tree,
        conflicts=(Conflict("programme_manager", "backlog number", "Her backlog is far higher than the board pack's; "
                            "both numbers are wrong for different reasons."),),
        must_not_claim=("Every referral without a seen date is still waiting",
                        "The board pack backlog is accurate"),
        strong=(
            "How big is the referral backlog and waiting list?",
            "How many referrals have no seen date, by your count?",
            "Are seen dates sometimes blank in the messages even after a visit?",
            "What is clinic capacity like?",
            "Was there a consultant vacancy or a gap in fast track slots?",
            "Do referred patients attend, or do many miss or not show?",
            "What data feeds do you have, like the lab HbA1c feed?",
            "Which identifier keys the lab feed, and did the units change?",
        ),
        weak=(
            "What are your priorities?",
            "Could AI help ophthalmology?",
            "How are you finding things?",
            "Anything else?",
        ),
    )
