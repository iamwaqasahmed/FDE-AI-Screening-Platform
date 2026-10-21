"""Data protection officer: the DPIA excludes hospital studies, and a tighter restriction lands in week three."""

from __future__ import annotations

from simulation.stakeholders.model import Card, Conflict, Persona, fact, node

KEY = "dpo"


def build(world: dict) -> Persona:
    facts = (
        fact(world, "dpo-restrict", "From {0} the vendor may receive only primary-care captures, and one field is banned.",
             "engagement/DPO_RESTRICTION"),
        fact(world, "dpo-hospital", "Since the pilot began on {0} the DPIA has covered primary-care captures only; "
             "hospital studies are out.", "clock/VENDOR_START"),
        fact(world, "dpo-logs", "Names and phone numbers were written to the booking API logs from {0} to {1}.",
             "timeline/INC-0270:start", "timeline/INC-0270:end"),
        fact(world, "dpo-access", "A leaver kept access after a role change; the review ran from {0} to {1}.",
             "timeline/INC-0262:start", "timeline/INC-0262:end"),
        fact(world, "dpo-movers", "{0} people moved without telling anyone, so contact data goes stale.",
             "events/silent_movers", must_surface=False),
    )
    tree = (
        node("dpia", "dpia lawful basis privacy assessment protection", "The DPIA is signed for the pilot as it stands."),
        node("hospital", "hospital hospitals studies study cover covers", "It is narrower than people think.",
             "dpo-hospital", "dpia"),
        node("change", "change changes coming upcoming restriction restrict decision", "I am finalising a decision.",
             "dpo-restrict", "dpia"),
        node("incidents", "incident incidents breach breaches leak leaks", "We log every incident with the service desk."),
        node("logs", "log logs logging api booking debug", "Yes, one I am still unhappy about.", "dpo-logs", "incidents"),
        node("access", "access audit leaver leavers role account accounts", "There was a review.", "dpo-access",
             "incidents"),
        node("contact", "contact phone address details accuracy", "Contact details age badly.", "dpo-movers"),
        node("goals", "goal goals want priority priorities success", "I want any AI use to be lawful, minimal, and "
             "explainable to a patient."),
    )
    return Persona(
        key=KEY,
        card=Card(
            goals=("Keep processing lawful and minimal", "Make the vendor's role defensible to patients"),
            constraints=("Signs the DPIA", "Can restrict processing at any time"),
            says_first="I am not here to block you. Show me the data flow and the lawful basis.",
            wants="A data flow diagram and a minimised field list.",
        ),
        facts=facts,
        tree=tree,
        conflicts=(
            Conflict("cdo", "vendor scope", "Will not allow hospital studies to the vendor that the CDO wants scored."),
            Conflict("vendor_manager", "data fields", "Bans a field the vendor says it needs."),
        ),
        must_not_claim=("The DPIA allows hospital studies to go to the vendor",
                        "The vendor restriction is final as of week one"),
        strong=(
            "What does the DPIA for the pilot cover?",
            "Does it cover hospital studies?",
            "Is any change or new restriction coming?",
            "Have there been any data incidents or breaches?",
            "Was personal data written to any logs, for example the booking API?",
            "Was there inappropriate access, for example a leaver account, in the audit?",
        ),
        weak=(
            "What are your priorities?",
            "Is AI allowed?",
            "What worries you?",
            "Can we have all the data?",
            "Anything else?",
        ),
    )
