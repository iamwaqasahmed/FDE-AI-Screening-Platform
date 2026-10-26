"""chk-readout. A miss does not repeat the interview sentence.

This check grades the week-one readout. It looks for a banned sentence, the deadline, where patient data sits, a named and cited failure, an open gate with its citation, what will not be built, and the ask log. Mentioning the triage id in the ask log is a promise unless that section also says it will not. A planted token or a missing file stops the check.
"""

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
    """Return true when the text cites a persona or a document id.

    Either kind of citation is enough. The match uses id boundaries so a shorter id does not hit inside a longer one.
    """
    if any(has_id(text, persona) for persona in _PERSONAS):
        return True
    return any(has_id(text, doc_id) for doc_id in DOC_IDS)


def _needs(text: str, rule: dict) -> bool:
    """Return true when the section fails the rule.

    A rule key that is absent is not applied. When an all-list is present, every token must appear. When an any-list is present, one token must appear. A non-empty cite value must appear as an id. An empty cite string is not applied.
    """
    body = section(text, rule["heading"])
    # The all-list is applied only when the rule has one. Every token in it must appear.
    if "all" in rule and not all(has_token(body, token) for token in rule["all"]):
        return True
    if "any" in rule and not any(has_token(body, token) for token in rule["any"]):
        return True
    cite = rule.get("cite", "")
    # An empty cite string is not applied. A real cite id that is missing makes the section fail.
    return bool(cite) and not has_id(body, cite)


def readout_problems(work: Path, gold: dict, canary: str) -> list[str]:
    """Return the readout misses.

    A planted token returns only the watermark sentence. A missing file is its own miss. A banned sentence is recorded and the other sections are still graded. The deadline and the data section use the rule helper. The failure section must name a failure before the citation is required, so a missing failure is not hidden behind a missing cite. The gate section works the same way. The withheld section must mention a clinician. An empty ask section is a miss. An ask section that names the triage id without a negation is a promise.
    """
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
    # The citation is checked only after a failure was named. Otherwise the cite miss would hide the missing failure.
    elif not _cited(failure):
        problems.append("the readout does not cite the failure")
    gate = section(text, rules["gate"]["heading"])
    if _GATE.search(gate) is None:
        problems.append("the readout does not name an open gate")
    # The gate citation is checked only after a gate name was found.
    elif not has_id(gate, rules["gate"]["cite"]):
        problems.append("the readout does not cite the gate")
    withheld = section(text, "Will not build")
    if "clinician" not in withheld.lower():
        problems.append("the readout does not say what it will not build")
    asks = section(text, "Asks")
    if not asks.strip():
        problems.append("the ask log is missing")
    # Naming that id is a promise unless the same section says it will not.
    elif "p-triage" in asks.lower() and re.search(r"\bnot\b", asks, re.IGNORECASE) is None:
        problems.append("the ask log promises triage")
    return problems
