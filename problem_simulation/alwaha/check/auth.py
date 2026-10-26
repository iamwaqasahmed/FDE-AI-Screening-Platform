"""chk-w2-auth. A miss does not print the role list or the assurance level.

This check grades sign-in: the session row, which page each actor opens, and which actors are refused. It runs the shared shell exercise and then reads the notes. A shell that does not run returns only that failure. The role list and the assurance level are not printed.
"""

from __future__ import annotations

from pathlib import Path

from alwaha.check.shell import exercise
from alwaha.serve.iam import token

_COLUMNS = {"session_id", "subject", "role", "loa"}


def _text(path: Path) -> str | None:
    """Return the file text, or nothing when the path is not a file.

    Callers treat a missing note as a failed content check instead of raising.
    """
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def _rows(found: dict) -> list[str]:
    """Return the session-row misses, stopping at the first one.

    The columns must contain every required name. A short set is the missing-row miss. Once those names are present, any extra column is its own miss, so a short row is not also called extra. Each of the patient and the coordinator must be stored under the subject, role, and assurance the reference token describes.
    """
    columns = set(found["columns"])
    # A missing column set, or a set that drops a required name, is the missing-row miss.
    if not columns or not columns >= _COLUMNS:
        return ["session row is missing"]
    # This runs only after the required names are present, so a short row is not also called an extra column.
    if columns != _COLUMNS:
        return ["session row has an extra column"]
    stored = {row["subject"]: row for row in found["sessions"]}
    for actor in ("patient", "coordinator"):
        expected = token(actor)
        row = stored.get(expected["sub"])
        if row is None or row["role"] != expected["role"] or row["loa"] != expected["loa"]:
            return ["session row does not match"]
    return []


def _pages(found: dict) -> list[str]:
    """Return the page misses.

    The patient must see the chat and the coordinator must see the console. The patient session rendered on the console, or the coordinator session rendered on the chat, is a cross-opening miss.
    """
    problems = []
    pages = found["pages"]
    if "Patient chat" not in pages["patient"]:
        problems.append("patient did not open the chat")
    if "Staff console" not in pages["coordinator"]:
        problems.append("coordinator did not open the console")
    if pages["patient_on_console"]:
        problems.append("patient opened the staff console")
    if pages["coordinator_on_chat"]:
        problems.append("coordinator opened the patient chat")
    return problems


def _refusals(found: dict) -> list[str]:
    """Return the refusal misses.

    The records actor must land on the console. A truthy page for the foreign role means that role was accepted. A truthy page for the service actor means the service token was accepted as the patient.
    """
    problems = []
    roles = found["roles"]
    if roles["records"] != "console":
        problems.append("a listed staff role did not open the console")
    if roles["vendor"]:
        problems.append("a foreign role was accepted")
    if roles["service"]:
        problems.append("a service token was accepted as the patient")
    return problems


def _written(work: Path) -> list[str]:
    """Return the note misses.

    The state note must name the patient, the coordinator, and the assurance level. The token note must say the session row is written to the database. If it does, it must also keep the service token off the patient. A missing token note is only the database miss, so the service sentence is not added on top. The sprint must exist and must mention generation before booking.
    """
    problems = []
    states = _text(work / "states.md")
    lowered = "" if states is None else states.lower()
    if "patient" not in lowered or "coordinator" not in lowered or "loa-1" not in lowered:
        problems.append("states.md is missing a sign-in state")
    token_flow = _text(work / "token-flow.md")
    if token_flow is None or "database" not in token_flow.lower():
        problems.append("token-flow.md does not say where the session row is written")
    # The note names the database, but it never keeps the service token off the patient. A missing note takes the database branch instead.
    elif "service" not in token_flow.lower():
        problems.append("token-flow.md does not keep a service token off the patient")
    sprint = _text(work / "sprint.md")
    if sprint is None:
        problems.append("sprint.md does not sequence the client before booking")
    else:
        lowered = sprint.lower()
        generated = lowered.find("generat")
        booking = lowered.find("book")
        # Generation has to be present and has to appear before booking. A missing word or the wrong order is the same miss.
        if generated < 0 or booking < 0 or generated > booking:
            problems.append("sprint.md does not sequence the client before booking")
    return problems


def auth_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    """Return the sign-in misses.

    The shell exercise runs first. If it returns no record, its own misses are the whole result. Otherwise the row, page, refusal, and note misses are concatenated.
    """
    problems, found = exercise(work, pack, gold, canary)
    if found is None:
        return problems
    return problems + _rows(found) + _pages(found) + _refusals(found) + _written(work)
