"""chk-readout. A miss does not repeat the interview sentence."""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.rubric import banned, has_id, has_token, section
from alwaha.check.tables import contains_canary
from alwaha.engagement.catalog import PERSONAS
from alwaha.engagement.day5 import DOC_IDS

_PERSONAS = tuple(row["id"] for row in PERSONAS)
_GATE = re.compile(r"(?<![A-Za-z0-9])G[1-5](?![0-9])")


def _cited(text: str) -> bool:
    if any(has_id(text, persona) for persona in _PERSONAS):
        return True
    return any(has_id(text, doc_id) for doc_id in DOC_IDS)


def _needs(text: str, rule: dict) -> bool:
    body = section(text, rule["heading"])
    if "all" in rule and not all(has_token(body, token) for token in rule["all"]):
        return True
    if "any" in rule and not any(has_token(body, token) for token in rule["any"]):
        return True
    cite = rule.get("cite", "")
    return bool(cite) and not has_id(body, cite)


def readout_problems(work: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return ["a watermarked sample is in the work directory"]
    path = work / "readout.md"
    if not path.is_file():
        return ["readout.md is missing"]
    text = path.read_text(encoding="utf-8")
    problems = []
    if banned(text):
        problems.append("readout contains a banned sentence")
    rules = gold["readout"]
    if _needs(text, rules["deadline"]):
        problems.append("the readout does not answer the deadline")
    if _needs(text, rules["data"]):
        problems.append("the readout does not say where patient data sits")
    failure = section(text, rules["failure"]["heading"])
    if not any(has_token(failure, token) for token in rules["failure"]["any"]):
        problems.append("the readout does not name a failure")
    elif not _cited(failure):
        problems.append("the readout does not cite the failure")
    gate = section(text, rules["gate"]["heading"])
    if _GATE.search(gate) is None:
        problems.append("the readout does not name an open gate")
    elif not has_id(gate, rules["gate"]["cite"]):
        problems.append("the readout does not cite the gate")
    withheld = section(text, "Will not build")
    if "clinician" not in withheld.lower():
        problems.append("the readout does not say what it will not build")
    asks = section(text, "Asks")
    if not asks.strip():
        problems.append("the ask log is missing")
    elif "p-triage" in asks.lower() and re.search(r"\bnot\b", asks, re.IGNORECASE) is None:
        problems.append("the ask log promises triage")
    return problems
