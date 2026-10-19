"""Outreach coordinator: the laptop sync gap, a firmware change, one weak operator, and reminders that barely help."""

from __future__ import annotations

from simulation.stakeholders.model import Card, Conflict, Persona, fact, node

KEY = "outreach_coordinator"


def build(world: dict) -> Persona:
    facts = (
        fact(world, "oc-sync", "The outreach laptops failed to sync from {0} to {1}, and {2} captures have no local id.",
             "timeline/INC-0215:start", "timeline/INC-0215:end", "events/outage_captures"),
        fact(world, "oc-firmware", "The outreach camera firmware changed on {0} and the images got better.",
             "clock/FIRMWARE_RIVER"),
        fact(world, "oc-operator", "One operator's images are consistently poorer: the initials are {0}.",
             "constant/simulation.devices.quality:POOR_OPERATOR"),
        fact(world, "oc-reminder", "Reminders barely move River Districts, about {0} of uplift, against {1} in Hill "
             "Counties.", "economics/reminder_true_river_districts", "economics/reminder_true_hill_counties"),
        fact(world, "oc-never", "Of the photographs that never get a result, {0} come from Hill Counties and River "
             "Districts.", "events/never_graded_hill_river"),
        fact(world, "oc-sms", "SMS invitations started on {0}.", "constant/simulation.care.behaviour:SMS_FROM",
             must_surface=False),
    )
    tree = (
        node("van", "van outreach route routes days rural", "The van covers the river districts on a fixed route."),
        node("sync", "laptop laptops sync upload ids missing", "Mostly fine, with one bad spell.", "oc-sync", "van"),
        node("camera", "camera cameras image images quality firmware", "It has improved.", "oc-firmware", "van"),
        node("operator", "operator operators photographer photographers", "I would rather not name names.",
             "oc-operator", "camera"),
        node("attendance", "attendance attend dna missed turnout", "Turnout is low out here."),
        node("reminder", "reminder reminders sms text texts", "Less than you would hope.", "oc-reminder", "attendance"),
        node("results", "result results never grade graded photographs photos", "Some photographs seem to vanish."),
        node("where", "where district districts which", "It is not random.", "oc-never", "results"),
        node("contact", "invitation invitations", "People get a letter and, if we have a phone, a text.", "oc-sms"),
        node("goals", "goal goals want priority priorities success", "I want more van days and fewer wasted trips."),
    )
    return Persona(
        key=KEY,
        card=Card(
            goals=("More van days in the river districts", "Fewer wasted outreach slots"),
            constraints=("Van days are fixed by the outreach budget",),
            says_first="Out here the problem is distance, not software.",
            wants="More van days and better attendance.",
        ),
        facts=facts,
        tree=tree,
        conflicts=(Conflict("programme_manager", "reminders", "Doubts the reminder success the programme manager reports."),),
        must_not_claim=("Reminders raised attendance equally in every district",
                        "Every outreach capture has a local id"),
        strong=(
            "How does the outreach van route work?",
            "Do the laptops sync reliably, or are ids missing?",
            "How is camera image quality?",
            "Which operator or photographer has poorer images?",
            "What is attendance like?",
            "Do SMS reminders help?",
            "Do photographs ever never get a result?",
            "Which districts are those photographs in?",
        ),
        weak=(
            "What are your priorities?",
            "Do you like the job?",
            "Could AI help outreach?",
            "Anything else?",
        ),
    )
