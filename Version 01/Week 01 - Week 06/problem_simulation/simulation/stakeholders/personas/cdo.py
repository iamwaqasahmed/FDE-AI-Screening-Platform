"""Chief Digital Officer: wants the vendor live this year and the pilot earlier than the board was told."""

from __future__ import annotations

from simulation.stakeholders.model import Card, Conflict, Persona, fact, node

KEY = "cdo"


def build(world: dict) -> Persona:
    facts = (
        fact(world, "cdo-date", "The board was told {0}, but I have asked for the pilot by {1}.",
             "engagement/PILOT_DATE_ORIGINAL", "engagement/PILOT_DATE_REQUESTED"),
        fact(world, "cdo-site", "I intend to bring a second site into the pilot at the review on {0}.",
             "engagement/SCOPE_CHANGE"),
        fact(world, "cdo-owner", "We hope to name a clinical safety owner by {0}; until then the pilot stays stopped.",
             "engagement/OWNER_NAMED"),
        fact(world, "cdo-vendor", "The vendor pilot started on {0} and I want it at every site this year, hospitals included.",
             "clock/VENDOR_START"),
        fact(world, "cdo-freeze", "The registry change freeze from {0} is not on my roadmap.", "timeline/FRZ-0301:start"),
        fact(world, "cdo-pilot", "The pilot has scored {0} images so far.", "events/pilot_images", must_surface=False),
    )
    tree = (
        node("vision", "vision strategy ambition plan roadmap", "Hartland should be the first authority with AI in "
             "screening."),
        node("timeline", "date dates when timeline deadline board launch", "The date matters to me more than anything.",
             "cdo-date", "vision"),
        node("freeze", "freeze registry dependency dependencies calendar release", "I leave calendars to delivery.",
             "cdo-freeze", "vision"),
        node("vendor", "vendor model ai", "The vendor model is the obvious win."),
        node("scope", "scope where site sites hospital hospitals everywhere", "Everywhere, ideally.", "cdo-vendor",
             "vendor"),
        node("second", "second another add additional extend", "Yes, I have something in mind.", "cdo-site", "vendor"),
        node("risk", "risk risks safety clinical governance stop", "Governance is moving, slowly."),
        node("owner", "owner named name accountable responsible who", "That is still open.", "cdo-owner", "risk"),
        node("progress", "progress status images scored results", "The pilot is producing scores.", "cdo-pilot"),
        node("goals", "goal goals want priority priorities success", "I want something live that the minister can see."),
    )
    return Persona(
        key=KEY,
        card=Card(
            goals=("Put AI into live screening this year", "Show the board visible progress"),
            constraints=("Answers to the board and the ministry", "Holds the digital budget, not the clinical risk"),
            says_first="We have a vendor, we have a pilot. I need it live, not studied.",
            wants="The vendor model live at scale, fast.",
        ),
        facts=facts,
        tree=tree,
        conflicts=(
            Conflict("dpo", "vendor scope", "Wants hospital studies scored; the DPO's decision does not allow it."),
            Conflict("enterprise_architect", "roadmap date", "The roadmap date ignores the registry freeze."),
            Conflict("lead_grader", "vendor model", "Wants the vendor live; the lead grader will not accept scores as results."),
        ),
        must_not_claim=("The pilot can start before a clinical safety owner is named",
                        "The vendor model may score hospital studies",
                        "The board has approved the earlier pilot date"),
        strong=(
            "What is your vision and roadmap for AI in screening?",
            "What date has the board been given for the pilot launch?",
            "Does the roadmap account for the registry freeze and release calendar?",
            "Where do you want the vendor model to run?",
            "Which sites, hospitals included?",
            "Will you add a second site?",
            "What are the clinical safety risks?",
            "Who is the named clinical safety owner?",
        ),
        weak=(
            "What are your goals?",
            "What does success look like?",
            "How much budget is there?",
            "What do you think of the team?",
            "Anything else?",
        ),
    )
