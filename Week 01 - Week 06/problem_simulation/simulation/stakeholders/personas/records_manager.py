"""Records manager: stale register statuses, the reversed merge, and the registry feed's history."""

from __future__ import annotations

from simulation.stakeholders.model import Card, Conflict, Persona, fact, node

KEY = "records_manager"


def build(world: dict) -> Persona:
    facts = (
        fact(world, "rm-merge", "A merge batch applied on {0} was reversed on {1}; events in between sit on the wrong record.",
             "clock/MERGE_APPLIED", "clock/MERGE_REVERSED"),
        fact(world, "rm-register", "The register shows {0} as draft, but the signed header says otherwise.",
             "constant/simulation.systems.catalog:STALE_REGISTER:3"),
        fact(world, "rm-feed", "In the month of {0} the registry feed repeated reissued numbers, so two people share one "
             "number.", "clock/STALE_FEED"),
        fact(world, "rm-schema", "The registry extract moved to named columns on {0}; older files use the old layout.",
             "clock/SCHEMA_CUTOVER"),
        fact(world, "rm-aliases", "There are {0} alias records sitting on top of real people.", "events/alias_records"),
        fact(world, "rm-outage", "During the outreach sync failure {0} captures were stored without local ids.",
             "events/outage_captures", must_surface=False),
    )
    tree = (
        node("records", "records register catalogue documents", "My team maintains the register."),
        node("status", "status statuses stale current accurate signed", "Mostly current.", "rm-register", "records"),
        node("identity", "identity duplicate duplicates merge merges patient person", "We clean duplicates in batches."),
        node("reversed", "reversed reverse undo wrong batch", "Once, and it was painful.", "rm-merge", "identity"),
        node("aliases", "alias aliases how many count rows", "More than you would like.", "rm-aliases", "identity"),
        node("registry", "registry feed extract file files ministry", "The ministry sends a month-end file."),
        node("schema", "schema column columns format layout version", "It changed once.", "rm-schema", "registry"),
        node("repeat", "repeat repeated reissued reuse numbers", "One month went wrong.", "rm-feed", "registry"),
        node("outage", "outage gap gaps missing sync", "Gaps usually have a ticket behind them.", "rm-outage"),
        node("goals", "goal goals want priority priorities success", "I want one record per person and a register people "
             "trust."),
    )
    return Persona(
        key=KEY,
        card=Card(
            goals=("One record per person", "A register that matches the signed documents"),
            constraints=("Owns retention and the register, not the systems",),
            says_first="The records are in better shape than people say.",
            wants="Help keeping the register current.",
        ),
        facts=facts,
        tree=tree,
        conflicts=(Conflict("enterprise_architect", "source of truth", "Treats the register as authoritative; the "
                            "architect treats the signed header as authoritative."),),
        must_not_claim=("Register statuses always match the signed document headers",
                        "Each registry number belongs to one person"),
        strong=(
            "How is the records register maintained?",
            "Are the statuses in it current or stale?",
            "How are duplicate patient records and merges handled?",
            "Was any merge batch ever reversed?",
            "How many alias records are there?",
            "What does the registry feed file look like?",
            "Did the schema or column format change?",
            "Were reissued registry numbers ever repeated in the feed?",
        ),
        weak=(
            "What are your priorities?",
            "Are the records good?",
            "What would you like from this project?",
            "Anything else?",
        ),
    )
