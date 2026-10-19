"""Stakeholders stage: persona cards, the persona truth file, transcripts, threads, board paper, research, and workshop."""

from __future__ import annotations

import numpy as np

from simulation.stakeholders.board_paper import add_board_paper
from simulation.stakeholders.cards import card_markdown, gold_rows, personas_json, reference_scripts
from simulation.stakeholders.personas import build_personas
from simulation.stakeholders.research.build import build_research
from simulation.stakeholders.threads import add_threads
from simulation.stakeholders.transcripts import add_transcripts
from simulation.stakeholders.workshop import build_workshop

TRUTH = "truth/stakeholders"


def build(world: dict, rng: np.random.Generator) -> None:
    personas = build_personas(world)
    files = world["files"]
    for key, persona in personas.items():
        files[f"engagement/personas/{key}.md"] = card_markdown(persona)
    files[f"{TRUTH}/personas.json"] = personas_json(personas)
    files[f"{TRUTH}/reference_scripts.json"] = reference_scripts(personas)
    gold = world.setdefault("gold", {})
    gold["stakeholders"] = gold_rows(personas)
    gold["transcripts"] = [{"doc_id": doc_id} for doc_id in add_transcripts(world, personas)]
    gold["threads"] = [{"doc_id": doc_id} for doc_id in add_threads(world, personas, rng)]
    add_board_paper(world)
    build_research(world, rng)
    build_workshop(world, rng)
