"""Written notes for the Module 2 Lesson 3 checks. A miss does not name the delay.

Written notes for the test day. Usability scripts on the foundation layer must be finished, the fault must be in the definition of done, zone crossings must include the receipt and the calendar, and the suite must be in the sprint before sign-off and in the workflow. The knowledge note must say why a sleep fails and what an automated journey asserts.
"""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.tables import dict_rows


def _text(path: Path) -> str | None:
    """Return the file text, or nothing when the path is not a file.

    Callers treat a missing note as a failed content check instead of raising.
    """
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def _usability(work: Path, gold: dict) -> list[str]:
    """Return the usability misses.

    The sentence that every patient can use the app alone is recorded first. A missing table adds the unfinished-script miss again, so both reasons can show as two copies of that sentence. When the table exists, every foundation script must be marked finished and every required clause must appear.
    """
    text = _text(work / "usability.md")
    problems = []
    # That sentence claims a finish the check does not accept, even before the table is read.
    if text and "every patient can use the app alone" in text.lower():
        problems.append("a usability script is unfinished")
    rows = dict_rows(text or "", {"script", "finished", "clause"})
    if not rows:
        return problems + ["a usability script is unfinished"]
    finished = {row["script"] for row in rows if row["finished"].lower() == "yes"}
    needed = {row["id"] for row in gold["scripts"] if row["layer"] == "foundation"}
    if not needed <= finished:
        problems.append("a usability script is unfinished")
    found = {row["clause"] for row in rows}
    if not set(gold["clauses"]) <= found:
        problems.append("an accessibility clause is missing")
    return problems


def _done(work: Path, gold: dict) -> list[str]:
    """Return the definition-of-done miss.

    The note must exist, must contain the switch token from gold, and must contain the fault color.
    """
    text = _text(work / "dod.md")
    if text is None or gold["switch"] not in text or "red" not in text.lower():
        return ["the fault is not in the definition of done"]
    return []


def _crossings(work: Path) -> list[str]:
    """Return the zone-crossing miss.

    The receipt must leave the private zone for the partner. The calendar must stay inside the private zone. Either gap fails the whole table.
    """
    # The table needs a case, a from zone, and a to zone. A missing table fails.
    rows = dict_rows(_text(work / "crossings.md") or "", {"case", "from", "to"})
    if not rows:
        return ["a zone-crossing case is missing"]
    # The receipt must leave the private zone for the partner.
    receipt = any(
        row["case"] == "receipt" and "zone-private" in row["from"] and "partner" in row["to"] for row in rows
    )
    # The calendar must stay inside the private zone.
    calendar = any(
        row["case"] == "calendar" and row["from"] == "zone-private" and row["to"] == "zone-private" for row in rows
    )
    # Either gap fails the whole table.
    if not receipt or not calendar:
        return ["a zone-crossing case is missing"]
    return []


def _fixture(work: Path) -> list[str]:
    """Return the fixture miss.

    The note must mention both a fixture and state.
    """
    text = (_text(work / "fixtures.md") or "").lower()
    if "fixture" not in text or "state" not in text:
        return ["the fixture note is missing"]
    return []


def _sprint(work: Path) -> list[str]:
    """Return the sprint miss.

    A missing file fails. The suite may be named as a suite or as a test. Sign-off may be named as usability or as sign-off. The suite word must appear before the sign-off word.
    """
    text = _text(work / "sprint.md")
    if text is None:
        return ["sprint.md does not sequence the suite before sign-off"]
    lowered = text.lower()
    suite = lowered.find("suite")
    # The suite may be named as a suite. If that word is absent, the test word is tried.
    if suite < 0:
        suite = lowered.find("test")
    sign = lowered.find("usability")
    if sign < 0:
        sign = lowered.find("sign-off")
    if suite < 0 or sign < 0 or suite > sign:
        return ["sprint.md does not sequence the suite before sign-off"]
    return []


def _ci(work: Path) -> list[str]:
    """Return the workflow miss.

    The workflow must exist and must mention both the test runner and the tests directory.
    """
    text = _text(work / ".github" / "workflows" / "ci.yml")
    if text is None or "unittest" not in text or "tests" not in text:
        return ["the suite is not in CI"]
    return []


def _knowledge(work: Path) -> list[str]:
    """Return the knowledge misses.

    Fewer than two numbered answers is the two-answer miss. The first answer must mention the clock or the switch. The second must mention state or a mock, and it must mention a fixture or a recording.
    """
    text = _text(work / "knowledge.md")
    answers = [] if text is None else [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2:
        return ["knowledge.md needs two answers"]
    problems = []
    first = answers[0].lower()
    if "clock" not in first and "switch" not in first:
        problems.append("knowledge.md does not say why a sleep fails")
    second = answers[1].lower()
    recorded = "fixture" in second or "recorded" in second
    # The answer needs an assertion word and a recording word. Either gap is the same miss.
    if ("state" not in second and "mock" not in second) or not recorded:
        problems.append("knowledge.md does not say what an AI journey asserts")
    return problems


def written_problems(work: Path, gold: dict) -> list[str]:
    """Return the usability, done, crossing, fixture, sprint, workflow, and knowledge misses concatenated.

    Every helper runs.
    """
    return (
        _usability(work, gold)
        + _done(work, gold)
        + _crossings(work)
        + _fixture(work)
        + _sprint(work)
        + _ci(work)
        + _knowledge(work)
    )
