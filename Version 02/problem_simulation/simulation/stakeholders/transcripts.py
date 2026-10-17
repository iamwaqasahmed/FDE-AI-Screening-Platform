"""Interview transcripts. Each session replays part of a scripted interview, and the prose is fact-checked."""

from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import date, timedelta

from simulation.corpus.add import Extra, add_composed
from simulation.prose.spec import FactSpec, facts
from simulation.stakeholders.interview import run
from simulation.stakeholders.model import Persona
from simulation.world.engagement import KICKOFF

FAMILY = "transcripts"
SESSION_SIZE = 3
WEAK_PERSONAS = ("cdo", "programme_manager", "vendor_manager", "patient_rep")
ORDINALS = ("one", "two", "three", "four", "five")
OPENERS = ("Thanks for making the time.", "Thanks for seeing us again.", "We will keep this short.")
CLOSERS = ("Thanks, that is really useful.", "We will follow up by email.", "Let us pick this up next week.")


@dataclass(frozen=True)
class Session:
    doc_id: str
    persona: Persona
    number: int
    day: date
    turns: tuple[dict, ...]
    careless: bool = False


def sessions(personas: dict[str, Persona]) -> list[Session]:
    found = []
    for index, (key, persona) in enumerate(personas.items()):
        data = persona.to_json()
        turns = run(data, list(persona.strong))
        chunks = [turns[start:start + SESSION_SIZE] for start in range(0, len(turns), SESSION_SIZE)]
        for number, chunk in enumerate(chunks, start=1):
            day = KICKOFF + timedelta(days=(index % 5) + 7 * (number - 1) // 2)
            found.append(Session(f"interview-{key.replace('_', '-')}-{number}", persona, number, day, tuple(chunk)))
        if key in WEAK_PERSONAS:
            weak = tuple(run(data, list(persona.weak)))
            found.append(Session(f"interview-{key.replace('_', '-')}-first-pass", persona, 0, KICKOFF, weak, True))
    return found


def spec_for(session: Session) -> FactSpec:
    persona = session.persona
    released = [persona.fact(fact_id).text for turn in session.turns for fact_id in turn["released"]]
    label = "first pass" if session.careless else f"session {ORDINALS[session.number - 1]}"
    pairs = {"interviewee": persona.name, "role": persona.role, "held_on": session.day.isoformat()}
    pairs.update({f"fact_{index}": text for index, text in enumerate(released)})
    return FactSpec(session.doc_id, FAMILY, f"Interview with the {persona.role}, {label}", facts(**pairs),
                    style="interview transcript", length_words=120 + 60 * len(session.turns))


def draft_for(session: Session):
    def draft(spec: FactSpec, rng: random.Random) -> str:
        speaker = spec.value("interviewee")
        lines = [f"Interviewee: {speaker}, {spec.value('role')}. Held on {spec.value('held_on')}.", "",
                 f"**Interviewer:** {rng.choice(OPENERS)}", ""]
        for turn in session.turns:
            lines += [f"**Interviewer:** {turn['question']}", "", f"**{speaker}:** {turn['answer']}", ""]
        lines += [f"**Interviewer:** {rng.choice(CLOSERS)}"]
        return "\n".join(lines)

    return draft


def add_transcripts(world: dict, personas: dict[str, Persona]) -> list[str]:
    added = []
    for index, session in enumerate(sessions(personas)):
        original = "docx" if index % 3 == 0 else ""
        add_composed(world, spec_for(session), draft_for(session), session.day,
                     extra=Extra(original=original, meta={"persona": session.persona.key}))
        added.append(session.doc_id)
    return added
