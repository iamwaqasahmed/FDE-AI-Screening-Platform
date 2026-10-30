"""Written notes for chk-deploy. A miss does not name the hash or the national id.

Written notes for the deploy check. The deployment note must avoid banned sentences, leave urgency with a clinician, keep patient data off the external model, cover the required facts, and cite a source. The zone table, the operator steps, the sprint order, and the knowledge note are graded with it. This deployment helper is also used by the later deploy-day note check.
"""

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
    """Return the file text, or nothing when the path is not a file.

    Callers treat a missing note as a failed content check instead of raising.
    """
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def _files(pack: Path) -> set[str]:
    """Return the relative paths of files in the pack.

    A pack that is not a directory yields an empty set. Those paths are what a citation may name.
    """
    if not pack.is_dir():
        return set()
    return {path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file()}


def _cited(text: str, doc_ids: list[str], files: set[str]) -> bool:
    """Return true when the text cites the security owner, a document id, or a release path.

    Any one of the three is enough.
    """
    if has_id(text, "ciso"):
        return True
    if any(has_id(text, doc_id) for doc_id in doc_ids):
        return True
    return any(name in text for name in files)


def _hit(fact: dict, text: str, files: set[str], doc_ids: list[str]) -> bool:
    """Return true when one required fact is present.

    A citation fact uses the citation helper. A fact with a section is satisfied when any of its tokens appear in that section. Any other fact is a token in the whole note.
    """
    # A citation fact is a persona, a document id, or a release path, not a plain token.
    if fact.get("kind") == "citation":
        return _cited(text, doc_ids, files)
    # A fact that names a section is searched only in that section.
    if "section" in fact:
        body = section(text, fact["section"]).lower()
        return any(token in body for token in fact["any"])
    return has_token(text, fact["text"])


def _coverage(rules: dict, text: str, files: set[str]) -> bool:
    """Return true when enough required facts were hit.

    The share is turned into a whole-count cutoff so a fractional rule does not drift.
    """
    mentions = rules["mentions"]
    hits = sum(1 for fact in mentions if _hit(fact, text, files, rules["doc_ids"]))
    # The share is scaled to a whole-count cutoff so a fractional rule does not drift.
    return hits * 100 >= int(rules["share"] * 100) * len(mentions)


def _banned(text: str) -> bool:
    """Return true when the shared banned-phrase helper matches, or when one of the extra promises in this file appears.

    The extra promises are the local sentences that over-claim the deploy.
    """
    lowered = text.lower()
    return banned(text) or any(phrase in lowered for phrase in _EXTRA)


def _deployment(work: Path, pack: Path, gold: dict) -> list[str]:
    """Return the deployment-note misses.

    A missing file is the missing-fact miss and the other checks are skipped. A banned sentence, a boundary that does not leave urgency with a clinician, a boundary that does not name the external model, a short fact list, and a missing citation are separate misses.
    """
    text = _text(work / "deployment.md")
    # A missing file is the missing-fact miss. The other checks are skipped.
    if text is None:
        return ["the deployment note is missing a required fact"]
    rules = gold["deployment"]
    files = _files(pack)
    problems = []
    if _banned(text):
        problems.append("the deployment note contains a banned sentence")
    # Urgency and the external model are both read from the boundary section.
    boundary = section(text, "Boundary").lower()
    if "clinician" not in boundary or "urgency" not in boundary:
        problems.append("the deployment note does not leave urgency with a clinician")
    if "ext-large" not in boundary:
        problems.append("the deployment note does not keep patient data off the external model")
    # The fact list has to cover the required share.
    if not _coverage(rules, text, files):
        problems.append("the deployment note is missing a required fact")
    # A citation is a persona, a document id, or a release path.
    if not _cited(text, rules["doc_ids"], files):
        problems.append("the deployment note does not cite a source")
    return problems


def _zones(work: Path) -> list[str]:
    """Return the zone miss unless a row places the url in the private zone.

    A missing table is the same miss as a url in any other zone.
    """
    rows = dict_rows(_text(work / "zones.md") or "", {"surface", "zone"})
    # One matching row is success. A missing table, or a url in another zone, falls through to the miss.
    if rows and any(row["surface"] == "url" and row["zone"] == "zone-private" for row in rows):
        return []
    return ["the url is not in zone-private"]


def _operators(work: Path) -> list[str]:
    """Return the operator miss unless the note mentions both health and prod.

    A missing file fails.
    """
    lowered = (_text(work / "operators.md") or "").lower()
    if "health" in lowered and "prod" in lowered:
        return []
    return ["the operator steps are missing"]


def _sprint(work: Path) -> list[str]:
    """Return the sprint miss unless deploy, or the pipeline word, appears before the readout.

    A missing word or the wrong order is the same miss.
    """
    lowered = (_text(work / "sprint.md") or "").lower()
    deploy = lowered.find("deploy")
    # Deploy may be named as deploy. If that word is absent, the pipeline word is tried.
    if deploy < 0:
        deploy = lowered.find("pipeline")
    readout = lowered.find("readout")
    if deploy < 0 or readout < 0 or deploy > readout:
        return ["sprint.md does not book the readout after the deploy"]
    return []


def _knowledge(work: Path) -> list[str]:
    """Return the knowledge misses.

    Fewer than two numbered answers, or a note that fails the two-answer helper, is the two-answer miss. The first answer must name the private zone. The second must say what a rollback changes by naming the hash.
    """
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
    """Return the deployment, zone, operator, sprint, and knowledge misses concatenated.

    Every helper runs. The later day adds its own checks around this list.
    """
    return (
        _deployment(work, pack, gold)
        + _zones(work)
        + _operators(work)
        + _sprint(work)
        + _knowledge(work)
    )
