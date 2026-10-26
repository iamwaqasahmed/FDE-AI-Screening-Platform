"""chk-w2-deploy. A miss does not print the hash, the token, the quota, or the national id.

This check grades the image, the health probe, admission, the router, secrets, the manifest, and the workflow. An image with no user instruction still runs as root. The last user instruction is the one that runs. A copied log file is treated as a planted sample. The note grader can be replaced by the caller so a later day can score its own notes against a different pack. A hash, a token, a quota, or a national id is not printed.
"""

from __future__ import annotations

import importlib
import json
import re
import sys
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.notes_w2d4 import written_problems
from alwaha.check.tables import contains_canary
from alwaha.serve.deploy import admit

_NAMES = ("admit", "health", "router", "secrets")
_TESTS = ("test_admit.py", "test_health.py", "test_router.py", "test_secrets.py")
_NOTES = ("deployment.md", "zones.md", "operators.md", "sprint.md", "knowledge.md")
_ROOT = "the image runs as root"
_NID = "a national id is in the deploy log"
_HASH = "the health probe does not report the registered hash"
_CRED = "prod uses the dev credential"
_ROUTE = "the router leaves the private endpoint"
_NS = "the manifest is not in the team namespace"
_PROBE = "the health probe is missing"
_CI = "the pipeline is not in CI"
_REJECT = "the deploy rejected a registered image"


def load_suite(folder: Path) -> dict:
    """Import the admit, health, router, and secrets modules and return them.

    Each name is removed before import so the participant file is read. The path is always restored. A name that was not cached is removed. A name that was cached is put back.
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
            if module is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = module


def _once(problems: list[str], item: str) -> None:
    """Append the miss when that sentence is not already in the list.

    The image probe and the manifest can both name the root miss, and it should appear once.
    """
    if item not in problems:
        problems.append(item)


def _present(work: Path) -> bool:
    """Return true only when every module, test, note, image, manifest, and workflow file exists.

    Any missing piece is enough to skip the run. The caller reports one missing-deploy miss.
    """
    modules = all((work / "app" / f"{name}.py").is_file() for name in _NAMES)
    tests = all((work / "tests" / name).is_file() for name in _TESTS)
    notes = all((work / name).is_file() for name in _NOTES)
    image = (work / "deploy" / "Dockerfile").is_file()
    manifest = (work / "deploy" / "deployment.yaml").is_file()
    pipeline = (work / ".github" / "workflows" / "ci.yml").is_file()
    return modules and tests and notes and image and manifest and pipeline


def _image_is_root(text: str) -> bool:
    """Return true when the image would run as root.

    No user instruction means the image stays root. When several user instructions exist, the last one is the one that runs. The root name and the numeric root both count.
    """
    users = re.findall(r"(?im)^USER\s+(\S+)", text)
    # An image with no user instruction still runs as root.
    if not users:
        return True
    # The last user instruction is the one that runs. The root name and the numeric root both count.
    return users[-1].lower() in {"root", "0"}


def _health(app: dict, pack: Path, gold: dict) -> list[str]:
    """Return the hash miss unless the hash, the prompt, and the endpoint dependency all match.

    A wrong hash, a wrong prompt, or a missing endpoint share one miss.
    """
    register = json.loads((pack / "registry" / "models.json").read_text(encoding="utf-8"))
    candidate = json.loads((pack / "fixtures" / "candidate.json").read_text(encoding="utf-8"))
    body = app["health"].health(register, candidate)
    dependencies = body.get("dependencies") or []
    hash_ok = body.get("model_hash") == gold["approved_hash"]
    prompt_ok = body.get("prompt_version") == gold["prompt"]
    if hash_ok and prompt_ok and "endpoint" in dependencies:
        return []
    return [_HASH]


def _admit(app: dict, gold: dict, line: str) -> list[str]:
    """Return the admission misses.

    The root name and the numeric root must not be started. The non-root user must be started. That same user with the bad line must not leak the id. A result that disagrees with the reference records that probe's message. The emitted log is checked again so a leak is caught even when admission agreed.
    """
    national_id = gold["national_id"]
    problems: list[str] = []
    probes = (
        ("root", "started", _ROOT),
        ("0", "started", _ROOT),
        ("1000", "started", _REJECT),
        ("1000", line, _NID),
    )
    for user, log_line, message in probes:
        if app["admit"].admit(user, log_line, national_id) != admit(user, log_line, national_id):
            _once(problems, message)
    # The emitted log is checked even when admission agreed, so a leaked id is still a miss.
    if national_id in app["admit"].emitted_log(line, national_id):
        _once(problems, _NID)
    return problems


def _router(app: dict, gold: dict) -> list[str]:
    """Return the route miss unless the endpoint, the model, and the zone all match.

    Any one disagreement is the miss.
    """
    got = app["router"].route("prod")
    endpoint = got.get("endpoint") == gold["endpoint"]
    model = got.get("model") == gold["model"]
    zone = got.get("zone") == gold["zone"]
    if endpoint and model and zone:
        return []
    return [_ROUTE]


def _secrets(app: dict, pack: Path, gold: dict) -> list[str]:
    """Return the credential miss unless dev and prod both match gold.

    Either mismatch is the miss. The token values are not included.
    """
    dev = app["secrets"].credential("dev", pack)
    prod = app["secrets"].credential("prod", pack)
    if dev == gold["dev_token"] and prod == gold["prod_token"]:
        return []
    return [_CRED]


def _manifest(text: str, namespace: str) -> list[str]:
    """Return the manifest misses.

    The namespace must appear. A readiness or liveness probe must appear, and the health path must appear. The non-root setting must appear. These are separate misses.
    """
    problems = []
    lowered = text.lower()
    if namespace not in text:
        problems.append(_NS)
    probed = "readinessprobe" in lowered or "livenessprobe" in lowered
    if not probed or "/v1/health" not in text:
        problems.append(_PROBE)
    if "runasnonroot" not in lowered:
        problems.append(_ROOT)
    return problems


def _ci(work: Path) -> list[str]:
    """Return the workflow miss.

    A missing file fails. The file must mention the test runner and the tests directory.
    """
    path = work / ".github" / "workflows" / "ci.yml"
    if not path.is_file():
        return [_CI]
    text = path.read_text(encoding="utf-8")
    if "unittest" not in text or "tests" not in text:
        return [_CI]
    return []


def _copied_log(work: Path) -> bool:
    """Return true when any file in the work tree is named as the log fixture.

    A copied log is treated as a planted sample, the same way a token is.
    """
    return any(path.name == "log.json" for path in work.rglob("*") if path.is_file())


def _run(work: Path, pack: Path, gold: dict, notes) -> list[str]:
    """Return the deploy misses from the probes, the image, the manifest, the workflow, and the notes.

    The note callable is the one the caller passed. Each probe's misses are concatenated.
    """
    app = load_suite(work / "app")
    line = json.loads((pack / "fixtures" / "log.json").read_text(encoding="utf-8"))["line"]
    problems = []
    problems.extend(_health(app, pack, gold))
    problems.extend(_admit(app, gold, line))
    problems.extend(_router(app, gold))
    problems.extend(_secrets(app, pack, gold))
    image = (work / "deploy" / "Dockerfile").read_text(encoding="utf-8")
    if _image_is_root(image):
        _once(problems, _ROOT)
    manifest = (work / "deploy" / "deployment.yaml").read_text(encoding="utf-8")
    for item in _manifest(manifest, gold["namespace"]):
        _once(problems, item)
    problems.extend(_ci(work))
    problems.extend(notes(work, pack, gold))
    return problems


def deploy_problems(work: Path, pack: Path, gold: dict, canary: str, notes=None):
    """Return the deploy misses.

    A planted token or a copied log returns only the watermark. A missing piece of the deploy is one miss and the probes do not run. The note grader defaults to the shared written-note check, and a caller may replace it. A crash is the did-not-run miss.
    """
    # A copied log is treated as a planted sample, the same way a token in the tree is.
    if contains_canary(work, canary) or _copied_log(work):
        return [WATERMARK]
    if not _present(work):
        return ["the deploy is missing"]
    # The caller may replace the note grader. When it does not, the shared deploy notes are used.
    writer = notes or written_problems
    try:
        return _run(work, pack, gold, writer)
    except Exception:
        return ["the deploy did not run"]
