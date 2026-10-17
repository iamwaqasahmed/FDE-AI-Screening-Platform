"""Public persona cards in Markdown, and the closed persona file with hidden facts, trees, and reference scripts."""

from __future__ import annotations

from simulation.stakeholders.interview import BUDGET, run, score_turns
from simulation.stakeholders.model import Persona
from simulation.world.staff import BY_KEY


def card_markdown(persona: Persona) -> str:
    card = persona.card
    lines = [f"# {persona.name}, {persona.role}", "", f"Team: {BY_KEY[persona.key].team}", "",
             f"What they say first: \"{card.says_first}\"", "", f"What they say they want: {card.wants}", "", "## Goals", ""]
    lines += [f"- {goal}" for goal in card.goals]
    lines += ["", "## Constraints", ""]
    lines += [f"- {item}" for item in card.constraints]
    lines += ["", "## Topics they will talk about", ""]
    lines += [f"- {item.node_id.replace('-', ' ')}" for item in persona.tree if not item.parent]
    lines += ["", f"Interviews are scored on what you learn in {BUDGET} questions. Follow-ups matter.", ""]
    return "\n".join(lines)


def personas_json(personas: dict[str, Persona]) -> dict:
    return {"budget": BUDGET, "personas": {key: persona.to_json() for key, persona in personas.items()}}


def reference_scripts(personas: dict[str, Persona]) -> dict:
    out = {}
    for key, persona in personas.items():
        data = persona.to_json()
        out[key] = {}
        for label, script in (("strong", persona.strong), ("weak", persona.weak)):
            result = score_turns(data, run(data, list(script)))
            out[key][label] = {"questions": list(script), "score": result["score"], "reached": result["reached"],
                               "missed": result["missed"]}
    return out


def gold_rows(personas: dict[str, Persona]) -> list[dict]:
    rows = []
    for key, persona in personas.items():
        rows.append({
            "persona": key,
            "must_surface": [{"fact_id": item.fact_id, "text": item.text} for item in persona.facts if item.must_surface],
            "must_not_claim": list(persona.must_not_claim),
            "conflicts": [{"other": item.other, "topic": item.topic, "description": item.description}
                          for item in persona.conflicts],
        })
    return rows
