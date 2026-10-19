"""Patient representative: lost letters are loud, hospital waits are real, and the costliest problem is quiet."""

from __future__ import annotations

from simulation.stakeholders.model import Card, Conflict, Persona, fact, node

KEY = "patient_rep"
GAP = "constant/simulation.care.referrals:CONSULTANT_GAP"


def build(world: dict) -> Persona:
    facts = (
        fact(world, "pr-voiced", "The complaint we hear most is about {0}, but people rarely mention {1}.",
             "economics/most_voiced_problem", "economics/costliest_problem"),
        fact(world, "pr-lost", "Patients told us letters never arrived during the bureau's bad week from {0}.",
             "clock/INCIDENT_START"),
        fact(world, "pr-migration", "The worst year for missing letters was when the bureau changed platform, from {0}.",
             "clock/BUREAU_MIGRATION_START"),
        fact(world, "pr-hospital", "People waited much longer for hospital eye appointments from {0} to {1}.",
             f"{GAP}:0", f"{GAP}:1"),
        fact(world, "pr-reminder", "The reminder texts started on {0}, and people like them.", "clock/REMINDER_CHANGE"),
        fact(world, "pr-sms", "Invitation texts started on {0}.", "timeline/CHG-0114:start", must_surface=False),
    )
    tree = (
        node("complaints", "complaint complaints feedback hear concerns", "People mostly want to know what is happening."),
        node("most", "most common often frequent top biggest", "One theme dominates.", "pr-voiced", "complaints"),
        node("letters", "letter letters post arrive arrived lost missing", "Yes, many times.", "pr-lost", "complaints"),
        node("year", "worst year when platform changed earlier", "It was worse once before.", "pr-migration", "letters"),
        node("hospital", "hospital appointment appointments eye wait waiting", "Hospital waits worry people."),
        node("longer", "longer worse period months consultant", "There was a bad patch.", "pr-hospital", "hospital"),
        node("contact", "text texts sms reminder reminders phone", "Texts are popular.", "pr-sms"),
        node("when", "when start started began", "Not that long ago.", "pr-reminder", "contact"),
        node("goals", "goal goals want priority priorities success", "I want patients to know where they stand."),
    )
    return Persona(
        key=KEY,
        card=Card(
            goals=("Patients know what is happening to them", "Fewer lost letters and long waits"),
            constraints=("Speaks for the patient forum, not for individuals",),
            says_first="Patients do not care about systems. They care whether the letter arrives.",
            wants="Reliable letters and honest waiting times.",
        ),
        facts=facts,
        tree=tree,
        conflicts=(Conflict("cdo", "priorities", "Wants letters fixed before any AI; the CDO wants the vendor first."),),
        must_not_claim=("The most common complaint is the most costly problem",
                        "Lost letters only happened in one week"),
        strong=(
            "What complaints and feedback do you hear?",
            "What is the most common complaint?",
            "Have patients told you letters were lost or never arrived?",
            "When was the worst year for missing letters?",
            "How long do people wait for hospital eye appointments?",
            "Was there a period when waits got longer?",
            "Do texts and reminders help?",
            "When did reminders start?",
        ),
        weak=(
            "What are your priorities?",
            "Are patients happy?",
            "Would patients trust AI?",
            "Anything else?",
        ),
    )
