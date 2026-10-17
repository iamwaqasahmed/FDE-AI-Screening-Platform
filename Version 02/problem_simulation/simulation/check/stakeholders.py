"""Stakeholder invariants: traced facts, script scores, verified transcripts, planted threads, research, and workshop."""

from __future__ import annotations

import re

import pandas as pd

from simulation.prose.verify import problems
from simulation.stakeholders.interview import score_script
from simulation.stakeholders.personas import build_personas
from simulation.stakeholders.traces import resolve
from simulation.stakeholders.transcripts import sessions, spec_for
from simulation.world.staff import PERSONAS

PERSON_ID = re.compile(r"\bP\d{7}\b")


def body_of(world: dict, doc_id: str) -> str:
    text = world["rendered"][doc_id]
    title = world["catalog"][doc_id].title
    return text.split(f"# {title}\n\n", 1)[1].rstrip("\n")


def _personas_file(world: dict) -> dict:
    return world["files"]["truth/stakeholders/personas.json"]["personas"]


def check_persona_traces(world: dict, errors: list[str]) -> None:
    stored = _personas_file(world)
    if sorted(stored) != sorted(person.key for person in PERSONAS):
        errors.append("Persona file does not hold exactly the twelve staff personas")
    for key, data in stored.items():
        if not 5 <= len(data["facts"]) <= 8 or len(data["must_surface"]) < 4:
            errors.append(f"{key}: needs 5 to 8 hidden facts and at least 4 must-surface")
        for item in data["facts"]:
            if not item["traces"]:
                errors.append(f"{key}/{item['fact_id']}: no truth trace")
            for trace in item["traces"]:
                value = resolve(world, trace["source"], trace["ref"])
                if value != trace["value"] or value not in item["text"]:
                    errors.append(f"{key}/{item['fact_id']}: trace {trace['source']}/{trace['ref']} does not match the text")
        released = {fact_id for row in data["tree"] for fact_id in row["releases"]}
        missing = set(data["must_surface"]) - released
        if missing:
            errors.append(f"{key}: no question path releases {sorted(missing)}")


def check_reference_scripts(world: dict, errors: list[str]) -> None:
    stored = _personas_file(world)
    scripts = world["files"]["truth/stakeholders/reference_scripts.json"]
    for key, pair in scripts.items():
        strong = score_script(key, pair["strong"]["questions"], stored)["score"]
        weak = score_script(key, pair["weak"]["questions"], stored)["score"]
        if strong < 0.8 or weak > 0.4:
            errors.append(f"{key}: strong script scores {strong}, weak scores {weak}")
        if strong != pair["strong"]["score"] or weak != pair["weak"]["score"]:
            errors.append(f"{key}: stored reference scores are stale")


def check_transcripts(world: dict, errors: list[str]) -> None:
    built = sessions(build_personas(world))
    if not 35 <= len(built) <= 45:
        errors.append(f"Expected about 40 transcripts, found {len(built)}")
    for session in built:
        if session.doc_id not in world["rendered"]:
            errors.append(f"{session.doc_id}: transcript missing from the corpus")
            continue
        issues = problems(spec_for(session), body_of(world, session.doc_id))
        if issues:
            errors.append(f"{session.doc_id}: " + "; ".join(issues[:3]))


def check_threads(world: dict, errors: list[str]) -> None:
    threads = [row["doc_id"] for row in world["gold"].get("threads", [])]
    if not 50 <= len(threads) <= 70:
        errors.append(f"Expected about 60 threads, found {len(threads)}")
    injected = [row for row in world["gold"].get("injection", []) if row["doc_id"] in threads]
    if len(injected) != 1 or injected[0]["text"] not in world["rendered"][injected[0]["doc_id"]]:
        errors.append("Exactly one thread must carry the recorded injection text")
    spans = [row for row in world["gold"].get("pii", []) if row["doc_id"] in threads]
    if not spans:
        errors.append("No PII spans recorded in the threads")
    for span in spans:
        if world["rendered"][span["doc_id"]][span["start"]:span["end"]] != span["value"]:
            errors.append(f"{span['doc_id']}: PII span {span['kind']} does not match the body")


def check_board_paper(world: dict, errors: list[str]) -> None:
    fact = world["gold"].get("board_paper_table", {})
    doc_id = fact.get("doc_id", "")
    if doc_id not in world["rendered"] or f"corpus/board-papers/originals/{doc_id}.pdf" not in world["files"]:
        errors.append("Board paper or its PDF original is missing")
    elif str(fact["value"]) in world["rendered"][doc_id]:
        errors.append("Board paper Markdown must not carry the table-only fee")


def check_research(world: dict, errors: list[str]) -> None:
    gold = world["gold"].get("research", {})
    counts = gold.get("voice_counts", {})
    top = max(counts.values()) if counts else 0
    if gold.get("most_voiced") == gold.get("costliest") or counts.get(gold.get("most_voiced"), -1) != top:
        errors.append("The most-voiced theme must lead the survey counts and differ from the costliest problem")
    if sum(1 for value in counts.values() if value == top) != 1:
        errors.append("The most-voiced theme must lead strictly")
    calls = gold.get("calls", {})
    if calls.get("letter_ratio_in_migration", 0) < 1.5 or calls.get("hospital_ratio_in_consultant_gap", 0) < 1.2:
        errors.append(f"Call reasons do not spike in the event windows: {calls}")


def check_workshop(world: dict, errors: list[str]) -> None:
    gold = world["gold"].get("workshop", {})
    votes = world["files"]["engagement/workshop/dot_votes.csv"]
    totals = votes.groupby("idea_id")["dots"].sum()
    if int(totals.max()) != gold.get("top_votes") or (totals == totals.max()).sum() != 1:
        errors.append("The top-voted idea must lead strictly and match the gold")
    if not gold.get("top_voted_net_gbp", 0) < gold.get("median_net_gbp", 0):
        errors.append("The top-voted idea must have below-median net value")


def check_no_person_ids(world: dict, errors: list[str]) -> None:
    for path, content in sorted(world["files"].items()):
        if not path.startswith("engagement/"):
            continue
        text = content.to_csv(index=False) if isinstance(content, pd.DataFrame) else str(content)
        if PERSON_ID.search(text):
            errors.append(f"{path}: contains a person id")


CHECKS = [
    ("stakeholders persona traces", check_persona_traces),
    ("stakeholders reference scripts", check_reference_scripts),
    ("stakeholders transcripts verify", check_transcripts),
    ("stakeholders threads plants", check_threads),
    ("stakeholders board paper table", check_board_paper),
    ("stakeholders research voice vs cost", check_research),
    ("stakeholders workshop vs value", check_workshop),
    ("stakeholders no person ids", check_no_person_ids),
]
