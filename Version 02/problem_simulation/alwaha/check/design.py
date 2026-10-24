"""chk-w1-design. A miss does not name the missing token."""

from __future__ import annotations

from pathlib import Path

from alwaha.check.rubric import banned, has_id, has_token, section, two_answers
from alwaha.check.tables import contains_canary, dict_rows
from alwaha.engagement.catalog import PERSONAS

_PERSONAS = tuple(row["id"] for row in PERSONAS)


def _files(packs: list[Path]) -> set[str]:
    found: set[str] = set()
    for pack in packs:
        if not pack.is_dir():
            continue
        for path in pack.rglob("*"):
            if path.is_file():
                found.add(path.relative_to(pack).as_posix())
    return found


def _cited(text: str, doc_ids: list[str], files: set[str]) -> bool:
    if any(has_id(text, persona) for persona in _PERSONAS):
        return True
    if any(has_id(text, doc_id) for doc_id in doc_ids):
        return True
    return any(name in text for name in files)


def _topic_text(stage: str, topic: str) -> str:
    rows = dict_rows(stage, {"topic", "what is still open", "citation"})
    if rows is None:
        return ""
    for row in rows:
        if row["topic"].lower() == topic:
            return f"{row['what is still open']} {row['citation']}"
    return ""


def _hit(fact: dict, text: str, stage: str, doc_ids: list[str], files: set[str]) -> bool:
    if fact.get("kind") == "citation":
        return _cited(text, doc_ids, files)
    if "topic" in fact:
        cell = _topic_text(stage, fact["topic"]).lower()
        return any(token.lower() in cell for token in fact["any"])
    return has_token(text, fact["text"])


def _coverage(rules: dict, text: str, stage: str, files: set[str]) -> bool:
    mentions = rules["mentions"]
    hits = sum(1 for fact in mentions if _hit(fact, text, stage, rules["doc_ids"], files))
    return hits * 100 >= int(rules["share"] * 100) * len(mentions)


def _urgency(text: str) -> bool:
    body = section(text, "What we will not build").lower()
    return "clinician" in body and "urgency" in body


def design_problems(work: Path, gold: dict, canary: str, packs: list[Path] | None = None) -> list[str]:
    if contains_canary(work, canary):
        return ["a watermarked sample is in the work directory"]
    architecture = work / "architecture.md"
    design = work / "design.md"
    if not architecture.is_file() or not design.is_file():
        return ["architecture.md or design.md is missing"]
    arch = architecture.read_text(encoding="utf-8")
    note = design.read_text(encoding="utf-8")
    combined = f"{arch}\n{note}"
    problems = []
    if banned(combined):
        problems.append("design contains a banned sentence")
    if not any(word in section(arch, "Diagram").lower() for word in ("coordinator", "human", "approval")):
        problems.append("the diagram has no human step")
    if not _urgency(note):
        problems.append("the design does not leave urgency with a clinician")
    rules = gold["design"]
    if not _coverage(rules, combined, section(note, "Stage 2"), _files(packs or [])):
        problems.append("the design note is missing a required fact")
    knowledge = work / "knowledge.md"
    if not knowledge.is_file() or not two_answers(knowledge.read_text(encoding="utf-8")):
        problems.append("knowledge.md needs two answers")
    return problems
