"""Head of finance: knows the 2023 recode, the agency rate, and what each unit really costs."""

from __future__ import annotations

from simulation.stakeholders.model import Card, Conflict, Persona, fact, node

KEY = "finance_head"
COSTS = "constant/simulation.economics.costs:UNIT_COSTS"


def build(world: dict) -> Persona:
    facts = (
        fact(world, "fh-recode", "Cost centres were recoded on {0}; letters and SMS merged into one line, so year-on-year "
             "comparisons break.", "clock/FINANCE_RECODE"),
        fact(world, "fh-agency", "The agency grading contract started on {0} at {1} pounds an hour, against {2} for "
             "employed graders.", "clock/AGENCY_START", f"{COSTS}:agency_grader_hour:0", f"{COSTS}:grader_hour:0"),
        fact(world, "fh-vendor-fee", "The vendor charges {0} pounds per scored image under the pilot contract.",
             f"{COSTS}:vendor_read_fee:0"),
        fact(world, "fh-dna", "A missed screening slot costs us {0} pounds.", f"{COSTS}:dna_slot:0"),
        fact(world, "fh-letter", "Each reissued letter costs {0} pounds.", f"{COSTS}:letter_reprint:0"),
        fact(world, "fh-pilot-code", "The AI pilot line is coded {0}.",
             "constant/simulation.economics.budgets:NEW_CENTRES:pilot:0", must_surface=False),
    )
    tree = (
        node("budget", "budget budgets spend spending cost costs money", "Screening spend is mostly clinics and grading."),
        node("trend", "trend year comparison compare history previous change changed codes", "Be careful with history.",
             "fh-recode", "budget"),
        node("pilot", "pilot vendor fee fees contract licence", "The pilot is cheap so far.", "fh-vendor-fee", "budget"),
        node("staffing", "staff staffing graders grading workforce pay", "Grading is our second biggest line."),
        node("agency", "agency rate rates hourly hour", "Agency cover is expensive.", "fh-agency", "staffing"),
        node("unit", "unit per each price", "We keep unit costs for most things."),
        node("dna", "missed dna attend slot slots appointment", "Empty slots still cost money.", "fh-dna", "unit"),
        node("letter", "letter letters reissue reissued reprint reprinted post", "Post is cheap until it goes wrong.",
             "fh-letter", "unit"),
        node("ledger", "code ledger line lines", "Every line has a cost centre.", "fh-pilot-code"),
        node("goals", "goal goals want priority priorities success", "I want a business case with real numbers, not "
             "vendor numbers."),
    )
    return Persona(
        key=KEY,
        card=Card(
            goals=("A business case built on real unit costs", "No double-counted savings"),
            constraints=("Spend over procurement thresholds needs a full business case",),
            says_first="Show me the saving in cash, not in hours.",
            wants="A costed case with a payback date.",
        ),
        facts=facts,
        tree=tree,
        conflicts=(Conflict("cdo", "savings", "Rejects the vendor's savings claims that the CDO repeats."),),
        must_not_claim=("Letter spend fell after 2023", "Agency grading costs the same as employed grading"),
        strong=(
            "What does screening spend look like by budget?",
            "Can I compare spend year on year, or did the codes change?",
            "What does the vendor pilot contract cost?",
            "How is grading staffing paid for?",
            "What is the agency hourly rate?",
            "What is the unit cost per slot or letter?",
            "What does a missed appointment slot cost?",
            "What does a reprinted letter cost?",
        ),
        weak=(
            "What are your priorities?",
            "Is there money for AI?",
            "How do you feel about the project?",
            "Anything else?",
        ),
    )
