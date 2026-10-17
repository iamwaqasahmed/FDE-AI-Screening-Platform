"""Enterprise architect: freezes, schema changes, and the vendor callback that crosses trust zones."""

from __future__ import annotations

from simulation.stakeholders.model import Card, Conflict, Persona, fact, node

KEY = "enterprise_architect"
SYSTEMS = "constant/simulation.systems.catalog:SYSTEMS"


def build(world: dict) -> Persona:
    facts = (
        fact(world, "ea-freeze", "The registry change freeze runs from {0} to {1}.",
             "timeline/FRZ-0301:start", "timeline/FRZ-0301:end"),
        fact(world, "ea-schema", "The registry publishes a new schema version on {0}.", "engagement/REGISTRY_SCHEMA_V3"),
        fact(world, "ea-vendor-zone", "Vendor scores come back from the {0} zone, hosted in {1}, into our network.",
             f"{SYSTEMS}:6:trust_zone", f"{SYSTEMS}:6:hosting"),
        fact(world, "ea-warehouse", "On the warehouse: {0}", f"{SYSTEMS}:7:known_defect"),
        fact(world, "ea-bureau-freeze", "The letter bureau has its own seasonal freeze from {0}.",
             "timeline/FRZ-0302:start"),
        fact(world, "ea-outage", "The vendor API was down on {0}.", "timeline/INC-0274:start", must_surface=False),
    )
    tree = (
        node("landscape", "landscape architecture systems integration integrations zones", "We run nineteen systems "
             "around one integration engine."),
        node("vendor", "vendor scores callback cloud external zone trust", "That flow worries me.", "ea-vendor-zone",
             "landscape"),
        node("warehouse", "warehouse mart sql reporting eligible", "The mart is older than it looks.", "ea-warehouse",
             "landscape"),
        node("change", "change changes release releases calendar roadmap", "Every interface change goes through the "
             "change board."),
        node("freeze", "freeze frozen registry", "Yes, and it is not negotiable.", "ea-freeze", "change"),
        node("schema", "schema version versions new contract format", "One is due soon.", "ea-schema", "change"),
        node("bureau", "bureau letter letters seasonal peak post", "They have their own calendar.", "ea-bureau-freeze",
             "change"),
        node("outages", "outage outages downtime incident availability", "We have had a few.", "ea-outage"),
        node("goals", "goal goals want priority priorities success", "I want anything new to fit the zones we already "
             "have."),
    )
    return Persona(
        key=KEY,
        card=Card(
            goals=("Keep trust zones intact", "Avoid one-off integrations"),
            constraints=("Owns the warehouse and the integration standards",),
            says_first="Draw me the data flow before you write any code.",
            wants="A design that respects the zones and the change calendar.",
        ),
        facts=facts,
        tree=tree,
        conflicts=(Conflict("cdo", "roadmap date", "Knows the freeze makes the CDO's date impossible."),),
        must_not_claim=("The registry interface can change in November", "The warehouse eligibility count is correct"),
        strong=(
            "Can you walk me through the systems landscape and trust zones?",
            "How do vendor scores come back, across which trust zone?",
            "How does the warehouse SQL count eligible people?",
            "What is on the change and release calendar?",
            "Is the registry frozen at any point?",
            "Is a new schema version due?",
            "Does the letter bureau have a seasonal freeze too?",
        ),
        weak=(
            "What are your priorities?",
            "Which cloud do you like?",
            "Do you have standards?",
            "Anything else?",
        ),
    )
