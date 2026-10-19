"""Lead grader: knows who got worse after the rota change and where the urgent codes really live."""

from __future__ import annotations

from simulation.stakeholders.model import Card, Conflict, Persona, fact, node

KEY = "lead_grader"


def build(world: dict) -> Persona:
    facts = (
        fact(world, "lg-rota", "My audit shows {1}'s disagreement going from about {2} to {3} after the rota change on {0}.",
             "clock/ROTA_CHANGE", "roster/G05:name", "events/g05_error_before", "events/g05_error_after"),
        fact(world, "lg-notes", "Fast-review codes are not in the result column. Graders type '{0}' in the notes, "
             "and {1} urgent reads carry only that note.",
             "constant/simulation.systems.grader:URGENT_NOTE", "events/urgent_in_notes"),
        fact(world, "lg-strict", "{0} and {1} grade much stricter than the rest of the team.",
             "roster/G02:name", "roster/G06:name"),
        fact(world, "lg-agency", "Agency graders started on {0} and have read {1} encounters; I second-read a lot of them.",
             "clock/AGENCY_START", "events/agency_reads"),
        fact(world, "lg-vendor", "The vendor model only scores primary-care and outreach captures, from {0}.",
             "clock/VENDOR_START"),
        fact(world, "lg-capacity", "The change log calls it '{0}'.", "timeline/CHG-0171:title", must_surface=False),
    )
    tree = (
        node("workload", "workload backlog queue capacity hours", "The queue grows when we lose hours, not when "
             "clinics get busier.", "lg-capacity"),
        node("agency", "agency contract temporary locum cover", "Cover helps with volume.", "lg-agency", "workload"),
        node("rota", "rota session sessions shift change long", "The long sessions were meant to help.", "lg-rota",
             "workload"),
        node("quality", "quality accuracy audit consistency agreement", "We audit a sample every month. Most of the "
             "team is steady."),
        node("individual", "individual grader graders person anyone stricter strict harsher", "Yes, two people stand "
             "out.", "lg-strict", "quality"),
        node("q-rota", "rota worse drift change", "Since the long sessions one person has slipped.", "lg-rota",
             "quality"),
        node("urgent", "urgent urgency prioritise prioritize fast proliferative", "Urgent cases get flagged by the "
             "grader who reads them."),
        node("where", "where field column flag recorded note notes stored code codes", "That depends on habit.",
             "lg-notes", "urgent"),
        node("vendor", "vendor model ai algorithm score scores", "I have seen the scores. I would not let them sign a "
             "result."),
        node("scope", "which images captures sites hospital scope", "It does not see everything.", "lg-vendor",
             "vendor"),
        node("goals", "goal goals want priority priorities success", "I want the queue down without anyone signing a "
             "grade they have not looked at."),
    )
    return Persona(
        key=KEY,
        card=Card(
            goals=("Keep grading quality steady", "Get the queue back inside the clock", "Keep graders signing results"),
            constraints=("Only signed grader codes are results", "Hours are fixed until the agency contract renews"),
            says_first="The graders are good. We need more hours, not a robot.",
            wants="More grader hours and a cleaner worklist.",
        ),
        facts=facts,
        tree=tree,
        conflicts=(
            Conflict("cdo", "vendor model", "Refuses vendor scores as results; the CDO wants the vendor live this year."),
            Conflict("programme_manager", "letter delays", "Rejects the claim that graders cause the letter delays."),
        ),
        must_not_claim=("The whole grading team is equally accurate", "Urgent cases are coded in the result column",
                        "The vendor model scores hospital studies"),
        strong=(
            "How is the grading workload and backlog at the moment?",
            "Did the rota change to long sessions affect anyone?",
            "How is the agency cover working out?",
            "How do you audit quality across the team?",
            "Is any individual grader stricter than the rest?",
            "How do urgent cases get prioritised?",
            "Where is the urgent flag recorded, which field or note?",
            "What does the vendor model score today?",
            "Which images and sites does it see?",
        ),
        weak=(
            "What are your goals for this year?",
            "What would success look like for you?",
            "Are you excited about AI?",
            "Is there anything else you would like to tell us?",
            "How long have you worked here?",
            "Do you enjoy the job?",
        ),
    )
