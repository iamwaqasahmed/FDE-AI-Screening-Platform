"""chk-w2-auth. A miss does not print the role list or the assurance level."""

from __future__ import annotations

from pathlib import Path

from alwaha.check.shell import exercise
from alwaha.serve.iam import token

_COLUMNS = {"session_id", "subject", "role", "loa"}


def _text(path: Path) -> str | None:
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def _rows(found: dict) -> list[str]:
    columns = set(found["columns"])
    if not columns or not columns >= _COLUMNS:
        return ["session row is missing"]
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
    problems = []
    states = _text(work / "states.md")
    lowered = "" if states is None else states.lower()
    if "patient" not in lowered or "coordinator" not in lowered or "loa-1" not in lowered:
        problems.append("states.md is missing a sign-in state")
    token_flow = _text(work / "token-flow.md")
    if token_flow is None or "database" not in token_flow.lower():
        problems.append("token-flow.md does not say where the session row is written")
    elif "service" not in token_flow.lower():
        problems.append("token-flow.md does not keep a service token off the patient")
    sprint = _text(work / "sprint.md")
    if sprint is None:
        problems.append("sprint.md does not sequence the client before booking")
    else:
        lowered = sprint.lower()
        generated = lowered.find("generat")
        booking = lowered.find("book")
        if generated < 0 or booking < 0 or generated > booking:
            problems.append("sprint.md does not sequence the client before booking")
    return problems


def auth_problems(work: Path, pack: Path, gold: dict, canary: str) -> list[str]:
    problems, found = exercise(work, pack, gold, canary)
    if found is None:
        return problems
    return problems + _rows(found) + _pages(found) + _refusals(found) + _written(work)
