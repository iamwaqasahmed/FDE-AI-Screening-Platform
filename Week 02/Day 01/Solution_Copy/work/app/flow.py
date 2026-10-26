"""Sign in and answer one status question.

run.py and server.py both call this module. The auth check and the
journey check call it too. Leave the copy under work/app unchanged.
generate.py is the only file chapter 07 replaces, and it replaces
client.py, not this file.
"""

from __future__ import annotations

import json
from pathlib import Path

import auth
import client
import contract
import his
import session


def load_pack(pack: Path) -> dict:
    """Read the four release files the sign-in and the status question need.

    The note is the assurance page. The spec is the his-wadi document.
    The identity spec supplies the actors. The scenario file supplies
    the one status question. A missing file raises, and the message
    does not name which file. Chapter 07 points --pack at the packet
    release, where all four already sit. Do not copy the scenario
    file into work/.
    """
    # Four release files. Chapter 07 points --pack where they already sit.
    note = pack / "identity" / "loa.md"
    spec = pack / "openapi" / "his-wadi.yaml"
    iam = pack / "openapi" / "iam.yaml"
    scenario = pack / "scenarios" / "status.json"
    # A missing file raises without naming it. Do not copy the scenario into work/.
    missing = [path for path in (note, spec, iam, scenario) if not path.is_file()]
    if missing:
        raise FileNotFoundError("release is missing a file")
    # The identity spec becomes the actors. The scenario file becomes the row.
    return {
        "note": note.read_text(encoding="utf-8"),
        "spec": spec.read_text(encoding="utf-8"),
        "actors": auth.actors(iam.read_text(encoding="utf-8")),
        "row": json.loads(scenario.read_text(encoding="utf-8")),
    }


def sign_in(db, token: dict, note: str) -> dict:
    """Open chat or console, and write the session row when the token is accepted.

    A refused token returns ok False and an empty page. Nothing is
    written. An accepted token stores the subject as both session_id
    and subject, then the role and the assurance level from the token.
    The page is chat or console. The server redirects to that page.
    """
    # Ask which page this token may open. An empty page is a refusal, and nothing is written.
    page = auth.open_for(token, note)
    if not page:
        return {"ok": False, "page": ""}
    # Store the subject as the session id, with the role and the assurance level.
    stored = {
        "session_id": token["sub"],
        "subject": token["sub"],
        "role": token["role"],
        "loa": token.get("loa", ""),
    }
    session.save(db, stored)
    # The page is chat or console. The caller redirects there.
    return {"ok": True, "page": page, "session": stored}


def status_answer(spec: str, row: dict, message: str) -> dict:
    """Read his-wadi with the current client, then answer with the status tool.

    client.read_body is the hand-written body until chapter 07 generates
    a new client.py. his.read compares that body with the spec. contract
    turns the boolean into the reply. Booking is still a later day,
    even when the read succeeds.
    """
    ok = his.read(client.read_body(row["referral_id"]), spec)
    return contract.reply(message, row, ok)
