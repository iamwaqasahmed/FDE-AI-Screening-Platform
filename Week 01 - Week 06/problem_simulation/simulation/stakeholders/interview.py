"""Scripted interview simulator. Score = share of must-surface facts released within the question budget.

    python -m simulation.stakeholders.interview --persona lead_grader --script questions.txt
    python -m simulation.stakeholders.interview --persona dpo --personas data/truth/stakeholders/personas.json
"""

from __future__ import annotations

import argparse
import json
import sys
from functools import lru_cache
from pathlib import Path

from simulation.stakeholders.matching import match
from simulation.stakeholders.model import Node

BUDGET = 12


@lru_cache(maxsize=1)
def _built() -> dict[str, dict]:
    from simulation.devkit import core_world
    from simulation.stakeholders.personas import build_personas

    return {key: persona.to_json() for key, persona in build_personas(core_world()).items()}


def load_personas(path: str = "") -> dict[str, dict]:
    if path:
        return json.loads(Path(path).read_text(encoding="utf-8"))["personas"]
    return _built()


def _tree(data: dict) -> tuple[Node, ...]:
    return tuple(Node(row["node_id"], tuple(row["keywords"]), row["answer"], tuple(row["releases"]), row["parent"])
                 for row in data["tree"])


def run(data: dict, questions: list[str], budget: int = BUDGET) -> list[dict]:
    tree, texts = _tree(data), {row["fact_id"]: row["text"] for row in data["facts"]}
    visited: set[str] = set()
    turns = []
    for question in [line.strip() for line in questions if line.strip()][:budget]:
        found = match(question, tree, visited)
        if found is None:
            turns.append({"question": question, "node": "", "answer": data["card"]["says_first"], "released": []})
            continue
        fresh = [fact_id for fact_id in found.releases if found.node_id not in visited]
        visited.add(found.node_id)
        answer = " ".join([found.answer, *(texts[fact_id] for fact_id in fresh)])
        turns.append({"question": question, "node": found.node_id, "answer": answer, "released": fresh})
    return turns


def score_turns(data: dict, turns: list[dict]) -> dict:
    must = data["must_surface"]
    released = sorted({fact_id for turn in turns for fact_id in turn["released"]})
    reached = [fact_id for fact_id in must if fact_id in released]
    return {"score": round(len(reached) / len(must), 3) if must else 0.0, "reached": reached,
            "missed": [fact_id for fact_id in must if fact_id not in released], "asked": len(turns), "budget": BUDGET}


def score_script(persona_key: str, questions: list[str], personas: dict[str, dict] | None = None) -> dict:
    data = (personas or load_personas())[persona_key]
    turns = run(data, questions)
    return {"persona": persona_key, **score_turns(data, turns), "turns": turns}


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Interview a Hartland persona from a question script.")
    parser.add_argument("--persona", required=True)
    parser.add_argument("--script", default="", help="Text file, one question per line. Default: stdin.")
    parser.add_argument("--personas", default="", help="personas.json from a build's truth folder.")
    args = parser.parse_args(argv)
    text = Path(args.script).read_text(encoding="utf-8") if args.script else sys.stdin.read()
    result = score_script(args.persona, text.splitlines(), load_personas(args.personas))
    for number, turn in enumerate(result["turns"], start=1):
        print(f"Q{number}: {turn['question']}\nA: {turn['answer']}\n")
    print(f"Score {result['score']:.2f}: {len(result['reached'])} of {len(result['reached']) + len(result['missed'])} "
          f"must-surface facts in {result['asked']} of {BUDGET} questions.")


if __name__ == "__main__":
    main()
