"""Load the Lesson 1 shell and run one sign-in plus one status question.

Load the participant shell and exercise one sign-in plus one status question. The returned record is what the auth and journey checks grade. A planted token in the work tree, a missing flow module, or a crash returns no record. A token that shows up inside the status answer is also a planted sample, even when the tree itself was clean.
"""

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
    """Import the shell modules from a folder and return them by name.

    Each name is removed before import so the participant file is read. The path is always restored. A name that was not cached is removed on the way out. A name that was cached is put back, so the checker process does not keep the participant copy.
    """
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
            # Nothing was cached under this name, so it is removed rather than restored.
            if module is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = module


def exercise(work: Path, pack: Path, gold: dict, canary: str) -> tuple[list[str], dict | None]:
    """Return a miss list and either the exercise record or nothing.

    A planted token returns the watermark and no record. A missing flow module returns the missing-shell miss and no record. Otherwise the shell is loaded, a temporary session database is opened, and five actors are signed in. The patient and coordinator sessions are rendered on both pages. A direct read is compared only for its success flag. The status answer, the booking probe, health, and the held approval are stored on the record. A crash returns the did-not-run miss and no record. After a successful run, a token inside the status answer is the watermark and the record is dropped.
    """
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
    # The status answer is searched after a successful run. A token echoed there is a planted sample even when the work tree was clean.
    if canary in json.dumps(found["answer"]):
        return [WATERMARK], None
    return [], found
