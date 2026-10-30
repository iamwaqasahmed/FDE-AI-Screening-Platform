"""Written notes for Module 3, Lesson 3. A miss does not print a span or a doc id.

Written notes for the retrieval day. The sprint must index, filter, cite, then sync, and it must limit the new version to the named specialties. The refusal copy and the audience table are graded. The knowledge note must say what makes a document in force and who may see a staff document. A span or a document id is not printed.
"""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.rubric import two_answers
from alwaha.check.tables import dict_rows

_AUDIENCE = "the audience note lets a patient see a staff document"
_IN_FORCE = "knowledge.md does not say what makes a document in force"
_KNOW = "knowledge.md needs two answers"
_LIMIT = "sprint.md does not limit v4 to three specialties"
_REFUSAL = "the refusal copy is missing"
_SEQUENCE = "sprint.md does not sequence the index"
_STAFF = "knowledge.md does not say who may see a staff document"
_V4 = ("card", "endo", "ophth")


def _text(path: Path) -> str:
    """Return the file text, or an empty string when the path is not a file.

    Callers treat empty text as a missing note.
    """
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list.

    The note groups are concatenated here, and a repeated sentence should appear once.
    """
    if item not in problems:
        problems.append(item)


def sprint_problems(work: Path) -> list[str]:
    """Return the sequence miss and the specialty-limit miss.

    Index, filter, cite, and sync must appear in that order. The named specialties must all appear, and the note must say the limit is not all of them. Naming the specialties without that limit is still a miss.
    """
    lowered = _text(work / "sprint.md").lower()
    index = lowered.find("index")
    filtered = lowered.find("filter")
    cite = lowered.find("cite")
    sync = lowered.find("sync")
    problems: list[str] = []
    if not (0 <= index < filtered < cite < sync):
        problems.append(_SEQUENCE)
    named = all(name in lowered for name in _V4)
    # Naming the specialties is not enough. The note must also say the limit is not all of them.
    if not named or "not all" not in lowered:
        problems.append(_LIMIT)
    return problems


def refusal_problems(work: Path) -> list[str]:
    """Return the refusal miss unless both required phrases appear.

    The note must say there is no document and that the asker cannot see it.
    """
    text = _text(work / "refusal.md").lower()
    if "no document" not in text or "cannot see" not in text:
        return [_REFUSAL]
    return []


def audience_problems(work: Path) -> list[str]:
    """Return the audience miss unless the three askers are right.

    A patient may see public and must not see staff or restricted. Staff may see public and staff and must not see restricted. Records must see restricted. One wrong row fails the table.
    """
    rows = dict_rows(_text(work / "audience.md"), {"asker", "audiences"})
    # A missing table fails. The askers are not guessed.
    if not rows:
        return [_AUDIENCE]
    found = {row["asker"].lower(): row["audiences"].lower() for row in rows}
    patient = found.get("patient", "")
    staff = found.get("staff", "")
    records = found.get("records", "")
    # A patient may see public and must not see staff or restricted.
    patient_ok = "public" in patient and "staff" not in patient and "restricted" not in patient
    # Staff may see public and staff and must not see restricted.
    staff_ok = "public" in staff and "staff" in staff and "restricted" not in staff
    # Records must see restricted. One wrong row fails the table.
    records_ok = "restricted" in records
    if not (patient_ok and staff_ok and records_ok):
        return [_AUDIENCE]
    return []


def knowledge_problems(work: Path) -> list[str]:
    """Return the knowledge misses.

    Fewer than two numbered answers is the two-answer miss. The first answer must name the in-force phrase and must say what makes it true, using a date, a window, or an effective word. Naming the phrase without that reason still fails. The second answer must mention both staff and a patient.
    """
    text = _text(work / "knowledge.md")
    answers = [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2 or not two_answers(text):
        return [_KNOW]
    problems: list[str] = []
    first = answers[0].lower()
    if "in force" not in first and "in_force" not in first:
        problems.append(_IN_FORCE)
    # The answer named the in-force phrase but not the date, window, or effective word that makes it true.
    elif not any(token in first for token in ("date", "window", "effective")):
        problems.append(_IN_FORCE)
    second = answers[1].lower()
    if "staff" not in second or "patient" not in second:
        problems.append(_STAFF)
    return problems


def note_problems(work: Path) -> list[str]:
    """Return the sprint, refusal, audience, and knowledge misses, each sentence at most once.

    The steps gather the sprint, refusal, audience, and knowledge misses and keep a repeated sentence once.
    """
    problems: list[str] = []
    for item in sprint_problems(work):
        _once(problems, item)
    for item in refusal_problems(work):
        _once(problems, item)
    for item in audience_problems(work):
        _once(problems, item)
    for item in knowledge_problems(work):
        _once(problems, item)
    return problems
