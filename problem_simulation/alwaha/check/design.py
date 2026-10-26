"""chk-w1-design. A miss does not name the missing token.

This check grades the architecture and the design note together. It looks for a banned sentence, a human step on the diagram, urgency left with a clinician, enough of the required facts, and two knowledge answers. A planted token or a missing file stops the check. A miss does not name the missing token.
"""

from __future__ import annotations

from pathlib import Path

from alwaha.check.rubric import banned, has_id, has_token, section, two_answers
from alwaha.check.tables import contains_canary, dict_rows
from alwaha.engagement.catalog import PERSONAS

_PERSONAS = tuple(row["id"] for row in PERSONAS)


def _files(packs: list[Path]) -> set[str]:
    """Return the relative paths of files in the packs.

    A pack that is not a directory adds nothing.
    """
    found: set[str] = set()
    for pack in packs:
        if not pack.is_dir():
            continue
        for path in pack.rglob("*"):
            if path.is_file():
                found.add(path.relative_to(pack).as_posix())
    return found


def _cited(text: str, doc_ids: list[str], files: set[str]) -> bool:
    """Return true when the text cites a persona, a document id, or a release path.

    Any one of the three is enough.
    """
    if any(has_id(text, persona) for persona in _PERSONAS):
        return True
    if any(has_id(text, doc_id) for doc_id in doc_ids):
        return True
    return any(name in text for name in files)


def _topic_text(stage: str, topic: str) -> str:
    """Return the open-item cell and its citation for one topic, or an empty string.

    The stage table must have the topic, the open item, and the citation columns. A topic that is not in the table is empty, so the fact fails.
    """
    rows = dict_rows(stage, {"topic", "what is still open", "citation"})
    if rows is None:
        return ""
    for row in rows:
        if row["topic"].lower() == topic:
            return f"{row['what is still open']} {row['citation']}"
    return ""


def _hit(fact: dict, text: str, stage: str, doc_ids: list[str], files: set[str]) -> bool:
    """Return true when one required fact is present.

    A citation fact is satisfied by a persona, a document id, or a release path anywhere in the text. A topic fact looks only in that topic's stage-table cell. Any other fact is a token in the combined text.
    """
    # A citation fact is satisfied by a persona, a document id, or a release path, not by a token.
    if fact.get("kind") == "citation":
        return _cited(text, doc_ids, files)
    # A topic fact is read from that row of the stage table, not from the whole note.
    if "topic" in fact:
        cell = _topic_text(stage, fact["topic"]).lower()
        return any(token.lower() in cell for token in fact["any"])
    return has_token(text, fact["text"])


def _coverage(rules: dict, text: str, stage: str, files: set[str]) -> bool:
    """Return true when enough required facts were hit.

    The share is turned into a whole-count cutoff so a fractional rule does not drift. The hit count has to reach that cutoff.
    """
    mentions = rules["mentions"]
    hits = sum(1 for fact in mentions if _hit(fact, text, stage, rules["doc_ids"], files))
    # The share is scaled to a whole-count cutoff so a fractional rule does not drift.
    return hits * 100 >= int(rules["share"] * 100) * len(mentions)


def _urgency(text: str) -> bool:
    """Return true when the withheld section names both a clinician and urgency.

    The search is limited to that section, so the words elsewhere in the note do not count.
    """
    body = section(text, "What we will not build").lower()
    return "clinician" in body and "urgency" in body


def design_problems(work: Path, gold: dict, canary: str, packs: list[Path] | None = None) -> list[str]:
    """Return the design misses.

    A planted token returns only the watermark sentence. Either file missing is one miss and the contents are not graded. A banned sentence in either file is recorded. The diagram must mention a coordinator, a human, or an approval. The design must leave urgency with a clinician. The combined text must cover the required share of facts, using the stage section for topic facts. The knowledge note must exist and have two numbered answers.
    """
    # A planted token stops the check before either note is read.
    if contains_canary(work, canary):
        return ["a watermarked sample is in the work directory"]
    architecture = work / "architecture.md"
    design = work / "design.md"
    # Either file missing is one miss. The contents are not graded.
    if not architecture.is_file() or not design.is_file():
        return ["architecture.md or design.md is missing"]
    arch = architecture.read_text(encoding="utf-8")
    note = design.read_text(encoding="utf-8")
    # Facts are searched in both notes together.
    combined = f"{arch}\n{note}"
    problems = []
    if banned(combined):
        problems.append("design contains a banned sentence")
    # The human step is read from the diagram section only.
    if not any(word in section(arch, "Diagram").lower() for word in ("coordinator", "human", "approval")):
        problems.append("the diagram has no human step")
    if not _urgency(note):
        problems.append("the design does not leave urgency with a clinician")
    rules = gold["design"]
    # Topic facts come from the stage section. Other facts use the combined text.
    if not _coverage(rules, combined, section(note, "Stage 2"), _files(packs or [])):
        problems.append("the design note is missing a required fact")
    knowledge = work / "knowledge.md"
    # The knowledge note must exist and have two numbered answers.
    if not knowledge.is_file() or not two_answers(knowledge.read_text(encoding="utf-8")):
        problems.append("knowledge.md needs two answers")
    return problems
