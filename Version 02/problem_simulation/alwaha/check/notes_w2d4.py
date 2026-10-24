"""Written notes for chk-w2-deploy. A miss does not name the hash or the national id."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.rubric import banned, has_id, has_token, section, two_answers
from alwaha.check.tables import dict_rows

_EXTRA = (
    "the container runs as root",
    "prod uses the dev credential",
    "monitoring is complete",
    "the integration-engine log is clean",
)


def _text(path: Path) -> str | None:
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def _files(pack: Path) -> set[str]:
    if not pack.is_dir():
        return set()
    return {path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file()}


def _cited(text: str, doc_ids: list[str], files: set[str]) -> bool:
    if has_id(text, "ciso"):
        return True
    if any(has_id(text, doc_id) for doc_id in doc_ids):
        return True
    return any(name in text for name in files)


def _hit(fact: dict, text: str, files: set[str], doc_ids: list[str]) -> bool:
    if fact.get("kind") == "citation":
        return _cited(text, doc_ids, files)
    if "section" in fact:
        body = section(text, fact["section"]).lower()
        return any(token in body for token in fact["any"])
    return has_token(text, fact["text"])


def _coverage(rules: dict, text: str, files: set[str]) -> bool:
    mentions = rules["mentions"]
    hits = sum(1 for fact in mentions if _hit(fact, text, files, rules["doc_ids"]))
    return hits * 100 >= int(rules["share"] * 100) * len(mentions)


def _banned(text: str) -> bool:
    lowered = text.lower()
    return banned(text) or any(phrase in lowered for phrase in _EXTRA)


def _deployment(work: Path, pack: Path, gold: dict) -> list[str]:
    text = _text(work / "deployment.md")
    if text is None:
        return ["the deployment note is missing a required fact"]
    rules = gold["deployment"]
    files = _files(pack)
    problems = []
    if _banned(text):
        problems.append("the deployment note contains a banned sentence")
    boundary = section(text, "Boundary").lower()
    if "clinician" not in boundary or "urgency" not in boundary:
        problems.append("the deployment note does not leave urgency with a clinician")
    if "ext-large" not in boundary:
        problems.append("the deployment note does not keep patient data off the external model")
    if not _coverage(rules, text, files):
        problems.append("the deployment note is missing a required fact")
    if not _cited(text, rules["doc_ids"], files):
        problems.append("the deployment note does not cite a source")
    return problems


def _zones(work: Path) -> list[str]:
    rows = dict_rows(_text(work / "zones.md") or "", {"surface", "zone"})
    if rows and any(row["surface"] == "url" and row["zone"] == "zone-private" for row in rows):
        return []
    return ["the url is not in zone-private"]


def _operators(work: Path) -> list[str]:
    lowered = (_text(work / "operators.md") or "").lower()
    if "health" in lowered and "prod" in lowered:
        return []
    return ["the operator steps are missing"]


def _sprint(work: Path) -> list[str]:
    lowered = (_text(work / "sprint.md") or "").lower()
    deploy = lowered.find("deploy")
    if deploy < 0:
        deploy = lowered.find("pipeline")
    readout = lowered.find("readout")
    if deploy < 0 or readout < 0 or deploy > readout:
        return ["sprint.md does not book the readout after the deploy"]
    return []


def _knowledge(work: Path) -> list[str]:
    text = _text(work / "knowledge.md")
    answers = [] if text is None else [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2 or not two_answers(text or ""):
        return ["knowledge.md needs two answers"]
    problems = []
    if "zone-private" not in answers[0].lower():
        problems.append("knowledge.md does not name the zone")
    if "hash" not in answers[1].lower():
        problems.append("knowledge.md does not say what a rollback changes")
    return problems


def written_problems(work: Path, pack: Path, gold: dict) -> list[str]:
    return (
        _deployment(work, pack, gold)
        + _zones(work)
        + _operators(work)
        + _sprint(work)
        + _knowledge(work)
    )
