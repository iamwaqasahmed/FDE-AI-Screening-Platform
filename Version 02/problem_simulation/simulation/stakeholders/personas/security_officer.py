"""Information security officer: PII in logs, a leaver's access, and supplier outages."""

from __future__ import annotations

from simulation.stakeholders.model import Card, Conflict, Persona, fact, node

KEY = "security_officer"
SYSTEMS = "constant/simulation.systems.catalog:SYSTEMS"


def build(world: dict) -> Persona:
    facts = (
        fact(world, "so-logs", "Debug logging left names and phone numbers in the booking API logs from {0}.",
             "timeline/INC-0270:start"),
        fact(world, "so-leaver", "A leaver kept access after a role change; we reviewed it from {0}.",
             "timeline/INC-0262:start"),
        fact(world, "so-vendor-outage", "The vendor API went down on {0} after a supplier cloud region failure.",
             "timeline/INC-0274:start"),
        fact(world, "so-region", "The vendor model is hosted in {0}.", f"{SYSTEMS}:6:hosting"),
        fact(world, "so-booking-outage", "The booking system failed over on {0} and lost a day of slot changes.",
             "timeline/INC-0281:start"),
        fact(world, "so-audit", "On the audit log: {0}", f"{SYSTEMS}:15:known_defect", must_surface=False),
    )
    tree = (
        node("incidents", "incident incidents security breach breaches", "Our incident log is the place to start."),
        node("logs", "log logs logging pii personal debug", "One of those, yes.", "so-logs", "incidents"),
        node("access", "access leaver leavers account accounts role", "We found one.", "so-leaver", "incidents"),
        node("suppliers", "supplier suppliers vendor third party assurance", "Supplier assurance is my biggest worry."),
        node("hosting", "host hosted hosting region where cloud residency", "Not where I would choose.", "so-region",
             "suppliers"),
        node("outage", "outage failure availability resilience", "They had a bad day.", "so-vendor-outage", "suppliers"),
        node("booking", "booking appointment appointments slot slots", "Booking is a hosted service."),
        node("failover", "failover lost database down", "Once.", "so-booking-outage", "booking"),
        node("audit", "audit trail monitoring", "We keep an access log.", "so-audit"),
        node("goals", "goal goals want priority priorities success", "I want least privilege and logs without personal "
             "data."),
    )
    return Persona(
        key=KEY,
        card=Card(
            goals=("Least privilege everywhere", "No personal data in logs", "Assured suppliers"),
            constraints=("Signs off supplier assurance",),
            says_first="Tell me what crosses the boundary and who can read it.",
            wants="A threat model before the pilot widens.",
        ),
        facts=facts,
        tree=tree,
        conflicts=(Conflict("vendor_manager", "assurance", "Distrusts the vendor's uptime and hosting claims."),),
        must_not_claim=("No personal data has ever reached application logs", "The vendor is hosted in the UK"),
        strong=(
            "What security incidents have you logged recently?",
            "Did personal data end up in any logs?",
            "Did any leaver keep account access?",
            "How do you assure suppliers like the vendor?",
            "Where is the vendor hosted, which cloud region?",
            "Has the vendor had an outage or failure?",
            "How does the booking system handle slots?",
            "Has booking had a failover or lost data?",
        ),
        weak=(
            "What are your priorities?",
            "Is the network secure?",
            "Do you use passwords?",
            "Anything else?",
        ),
    )
