"""Sign in and answer one status question."""

from __future__ import annotations

import json
from pathlib import Path

import auth
import client
import contract
import his
import session


def load_pack(pack: Path) -> dict:
    note = pack / "identity" / "loa.md"
    spec = pack / "openapi" / "his-wadi.yaml"
    iam = pack / "openapi" / "iam.yaml"
    scenario = pack / "scenarios" / "status.json"
    missing = [path for path in (note, spec, iam, scenario) if not path.is_file()]
    if missing:
        raise FileNotFoundError("release is missing a file")
    return {
        "note": note.read_text(encoding="utf-8"),
        "spec": spec.read_text(encoding="utf-8"),
        "actors": auth.actors(iam.read_text(encoding="utf-8")),
        "row": json.loads(scenario.read_text(encoding="utf-8")),
    }


def sign_in(db, token: dict, note: str) -> dict:
    page = auth.open_for(token, note)
    if not page:
        return {"ok": False, "page": ""}
    stored = {
        "session_id": token["sub"],
        "subject": token["sub"],
        "role": token["role"],
        "loa": token.get("loa", ""),
    }
    session.save(db, stored)
    return {"ok": True, "page": page, "session": stored}


def status_answer(spec: str, row: dict, message: str) -> dict:
    ok = his.read(client.read_body(row["referral_id"]), spec)
    return contract.reply(message, row, ok)
