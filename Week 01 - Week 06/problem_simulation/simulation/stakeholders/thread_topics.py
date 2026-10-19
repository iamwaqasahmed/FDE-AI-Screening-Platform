"""Ordinary email and Teams threads: incidents and changes, persona disagreements, data requests, and weekly logistics."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

from simulation.stakeholders.model import Persona
from simulation.systems.catalog import ORIGINAL
from simulation.world.clock import BUREAU_MIGRATION_START, INCIDENT_START
from simulation.world.engagement import WEEKS
from simulation.world.timeline import TIMELINE

DAY = timedelta(days=1)
OWNER_FOR = {"registry": "records_manager", "grader": "lead_grader", "letters": "programme_manager",
             "pacs": "records_manager", "ophthalmology": "ophthalmology_lead", "vendor": "vendor_manager",
             "devices": "outreach_coordinator", "sms": "programme_manager", "lab": "ophthalmology_lead",
             "finance": "finance_head", "audit": "security_officer", "booking": "booking_admin"}
WEEK_NOTES = {
    1: "Base drop is out. Interviews start this week; please book your slots.",
    2: "The registry has said a new extract schema is coming. Check your loaders.",
    3: "The DPO decision on the vendor scope is expected this week.",
    4: "The bureau reported a bad week of dispatches. Reconcile before you report.",
    5: "The CDO review is this week. Expect questions about scope.",
    6: "We expect to hear about the clinical safety owner this week.",
}


@dataclass(frozen=True)
class Message:
    sender: str
    to: str
    day: date
    text: str


@dataclass(frozen=True)
class Thread:
    subject: str
    channel: str
    messages: tuple[Message, ...]


def timeline_threads() -> list[Thread]:
    threads = []
    for item in TIMELINE:
        owner = OWNER_FOR.get(item.system, "integration_lead")
        messages = [
            Message("service_desk_lead", owner, item.start, f"{item.ref} logged: {item.title}. Cause recorded as: "
                    f"{item.cause.lower()}."),
            Message(owner, "service_desk_lead", item.start + DAY, f"Thanks. What we are seeing: {item.effect.lower()}."),
        ]
        if item.end:
            messages.append(Message("service_desk_lead", owner, item.end, f"{item.ref} window ends {item.end.isoformat()}."))
        threads.append(Thread(f"{item.ref} {item.title}", "email", tuple(messages)))
    return threads


def conflict_threads(personas: dict[str, Persona]) -> list[Thread]:
    threads = []
    for index, (key, persona) in enumerate(personas.items()):
        for offset, conflict in enumerate(persona.conflicts):
            other = personas[conflict.other]
            day = WEEKS[1] + DAY * ((index + offset) % 9)
            messages = (
                Message(key, conflict.other, day, f"Can we talk about {conflict.topic}? {persona.card.wants}"),
                Message(conflict.other, key, day, other.card.says_first),
                Message(key, conflict.other, day + DAY, persona.card.says_first),
            )
            threads.append(Thread(f"Re: {conflict.topic}", "teams", messages))
    return threads


def request_threads() -> list[Thread]:
    threads = []
    for index, system in enumerate(ORIGINAL):
        owner = system["owner"]
        day = WEEKS[1] + DAY * (index % 4)
        threads.append(Thread(f"Data request: {system['name']}", "email", (
            Message("analyst", owner, day, f"Could we have the {system['name'].lower()} extract? We understand it is: "
                    f"{system['interface'].lower()}"),
            Message(owner, "analyst", day + DAY, f"Yes. One thing to know: {system['known_defect'].lower()}"),
        )))
    return threads


def week_threads() -> list[Thread]:
    return [Thread(f"Week {number} plan", "teams", (Message("delivery_manager", "product_owner", day, WEEK_NOTES[number]),
                                                     Message("product_owner", "delivery_manager", day, "Noted.")))
            for number, day in WEEKS.items()]


def complaint_threads() -> list[Thread]:
    starts = (BUREAU_MIGRATION_START, BUREAU_MIGRATION_START + DAY * 30, INCIDENT_START + DAY * 2)
    return [Thread("Calls about letters not received", "email", (
        Message("call_centre_lead", "programme_manager", day, "We are getting a lot of calls from people whose result "
                "letter never arrived. Agents are logging them as general queries."),
        Message("programme_manager", "call_centre_lead", day + DAY, "Probably grading running behind again. I will chase."),
    )) for day in starts]


def event_threads() -> list[Thread]:
    return [
        Thread("Staff and patient survey", "email", (Message("product_owner", "programme_manager", WEEKS[1],
               "The survey results are in the research folder. Free-text themes are coded."),)),
        Thread("Workshop on Thursday", "teams", (Message("delivery_manager", "cdo", WEEKS[2] + DAY * 3,
               "Dot-vote export and sticky clusters are in the workshop folder."),)),
        Thread("Board paper for circulation", "email", (Message("cdo", "finance_head", WEEKS[1] - DAY * 5,
               "Board paper attached. Costs are in the table in the PDF."),)),
    ]
