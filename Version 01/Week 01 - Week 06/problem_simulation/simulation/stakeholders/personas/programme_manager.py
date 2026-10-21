"""Programme manager: blames graders for the letter delays; the bureau migration is the real cause."""

from __future__ import annotations

from simulation.stakeholders.model import Card, Conflict, Persona, fact, node

KEY = "programme_manager"


def build(world: dict) -> Persona:
    facts = (
        fact(world, "pm-letters", "The bureau moved print platform from {1} to {2}, and {0} letter breaches have a grade "
             "date inside that window.", "events/migration_letter_breaches", "clock/BUREAU_MIGRATION_START",
             "clock/BUREAU_MIGRATION_END"),
        fact(world, "pm-duplicate", "In the duplicate week from {0} the bureau wrote {1} dispatches twice, and some "
             "letters were lost.", "clock/INCIDENT_START", "events/duplicate_letters"),
        fact(world, "pm-hill", "Hill Counties changed its recall interval on {0}, and the warehouse still uses the old rule.",
             "clock/HILL_RECALL"),
        fact(world, "pm-backlog", "The board pack backlog counts only fast-track booking breaches: {0} referrals since {1}.",
             "events/board_backlog", "events/backlog_from"),
        fact(world, "pm-never", "Of the photographs that never got a result, {0} are in Hill Counties and River Districts.",
             "events/never_graded_hill_river"),
        fact(world, "pm-reminder", "The SMS reminder went live everywhere on {0}, with no control group.",
             "clock/REMINDER_CHANGE", must_surface=False),
    )
    tree = (
        node("performance", "performance kpi kpis targets standards breach breaches overdue", "We report breaches to "
             "the board every month. Most of them are grading."),
        node("board", "board pack number count counts measure figure backlog", "The board number is the one we have "
             "always used.", "pm-backlog", "performance"),
        node("where", "where district districts site sites cluster", "It is not spread evenly.", "pm-never",
             "performance"),
        node("letters", "letter letters post dispatch", "Letters go out late when grading runs late. That is my reading."),
        node("bureau", "bureau supplier print platform migration", "The supplier did change things that year.",
             "pm-letters", "letters"),
        node("incident", "incident duplicate duplicates twice lost", "There was one bad week.", "pm-duplicate", "letters"),
        node("recall", "recall interval eligibility rule rules pathway", "Each site follows the pathway in force."),
        node("hill", "hill counties warehouse changed report reports", "That one is awkward.", "pm-hill", "recall"),
        node("reminders", "reminder reminders sms text attendance", "Attendance went up after the reminders.",
             "pm-reminder"),
        node("goals", "goal goals want priority priorities success", "I want every overdue person seen and a board "
             "report I can stand behind."),
    )
    return Persona(
        key=KEY,
        card=Card(
            goals=("Bring overdue screening back inside the standard", "Give the board a number it can trust"),
            constraints=("Owns the bureau contract but not the grader rota", "Reports monthly to the board"),
            says_first="Our problem is grading capacity. Fix that and the letters fix themselves.",
            wants="An AI tool that clears the grading queue.",
        ),
        facts=facts,
        tree=tree,
        conflicts=(
            Conflict("lead_grader", "letter delays", "Blames graders for letter delays the bureau migration caused."),
            Conflict("ophthalmology_lead", "backlog number", "Reports the board backlog, which disagrees with the hospital's."),
        ),
        must_not_claim=("The letter delays in 2023 were caused by grading capacity",
                        "The board pack backlog is the full referral backlog",
                        "The reminder change is proven to have raised attendance"),
        strong=(
            "How do you track performance and breaches?",
            "What does the board pack backlog number actually count?",
            "Which districts or sites do the overdue photographs cluster in?",
            "Why are result letters late?",
            "Did the print bureau or its platform change at that time?",
            "Was there an incident with duplicate or lost letters?",
            "Has the recall interval changed anywhere?",
            "Did the Hill Counties change reach the warehouse reports?",
        ),
        weak=(
            "What keeps you up at night?",
            "What are your priorities?",
            "How could AI help the service?",
            "Who are your key stakeholders?",
            "Is the team well resourced?",
            "Anything else we should know?",
        ),
    )
