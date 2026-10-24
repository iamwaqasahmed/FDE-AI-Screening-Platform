"""Load the Day 1 shell and run one sign-in plus one status question."""

from __future__ import annotations

import importlib
import json
import sys
import tempfile
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.tables import contains_canary
from alwaha.serve.fhir import read
from alwaha.serve.iam import token

_NAMES = ("generate", "session", "auth", "client", "his", "contract", "chat", "console", "flow")


def load_app(folder: Path) -> dict:
    folder = folder.resolve()
    saved_path = list(sys.path)
    saved = {name: sys.modules.get(name) for name in _NAMES}
    sys.path.insert(0, str(folder))
    try:
        for name in _NAMES:
            sys.modules.pop(name, None)
        for name in _NAMES:
            importlib.import_module(name)
        return {name: sys.modules[name] for name in _NAMES}
    finally:
        sys.path[:] = saved_path
        for name, module in saved.items():
            if module is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = module


def exercise(work: Path, pack: Path, gold: dict, canary: str) -> tuple[list[str], dict | None]:
    if contains_canary(work, canary):
        return [WATERMARK], None
    if not (work / "app" / "flow.py").is_file():
        return ["the shell is missing"], None
    try:
        app = load_app(work / "app")
        note = (pack / "identity" / "loa.md").read_text(encoding="utf-8")
        spec = (pack / "openapi" / "his-wadi.yaml").read_text(encoding="utf-8")
        row = json.loads((pack / "scenarios" / "status.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmp:
            db = app["session"].connect(Path(tmp) / "sessions.db")
            opened = {}
            for name in ("patient", "coordinator", "records", "vendor", "svc-integration"):
                opened[name] = app["flow"].sign_in(db, token(name), note)
            patient = opened["patient"].get("session", {})
            staff = opened["coordinator"].get("session", {})
            body = app["client"].read_body(row["referral_id"])
            direct = read(body, gold["field"], gold["removed_field"])
            answer = app["flow"].status_answer(spec, row, row["message"])
            found = {
                "pages": {
                    "patient": app["chat"].render(patient),
                    "coordinator": app["console"].render(staff),
                    "patient_on_console": app["console"].render(patient),
                    "coordinator_on_chat": app["chat"].render(staff),
                },
                "sessions": app["session"].rows(db),
                "columns": app["session"].columns(db),
                "answer": answer,
                "fhir_ok": bool(direct["ok"]),
                "probe": app["contract"].reply("Book a slot.", row, True),
                "health": app["contract"].health(),
                "approval": app["contract"].approval("apr-status"),
                "roles": {
                    "records": opened["records"]["page"],
                    "vendor": opened["vendor"]["page"],
                    "service": opened["svc-integration"]["page"],
                },
            }
            db.close()
    except Exception:
        return ["the shell did not run"], None
    if canary in json.dumps(found["answer"]):
        return [WATERMARK], None
    return [], found
