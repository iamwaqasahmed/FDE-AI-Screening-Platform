"""chk-w2-deploy. A miss does not print the hash, the token, the quota, or the national id."""

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
    if item not in problems:
        problems.append(item)


def _present(work: Path) -> bool:
    modules = all((work / "app" / f"{name}.py").is_file() for name in _NAMES)
    tests = all((work / "tests" / name).is_file() for name in _TESTS)
    notes = all((work / name).is_file() for name in _NOTES)
    image = (work / "deploy" / "Dockerfile").is_file()
    manifest = (work / "deploy" / "deployment.yaml").is_file()
    pipeline = (work / ".github" / "workflows" / "ci.yml").is_file()
    return modules and tests and notes and image and manifest and pipeline


def _image_is_root(text: str) -> bool:
    users = re.findall(r"(?im)^USER\s+(\S+)", text)
    if not users:
        return True
    return users[-1].lower() in {"root", "0"}


def _health(app: dict, pack: Path, gold: dict) -> list[str]:
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
    if national_id in app["admit"].emitted_log(line, national_id):
        _once(problems, _NID)
    return problems


def _router(app: dict, gold: dict) -> list[str]:
    got = app["router"].route("prod")
    endpoint = got.get("endpoint") == gold["endpoint"]
    model = got.get("model") == gold["model"]
    zone = got.get("zone") == gold["zone"]
    if endpoint and model and zone:
        return []
    return [_ROUTE]


def _secrets(app: dict, pack: Path, gold: dict) -> list[str]:
    dev = app["secrets"].credential("dev", pack)
    prod = app["secrets"].credential("prod", pack)
    if dev == gold["dev_token"] and prod == gold["prod_token"]:
        return []
    return [_CRED]


def _manifest(text: str, namespace: str) -> list[str]:
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
    path = work / ".github" / "workflows" / "ci.yml"
    if not path.is_file():
        return [_CI]
    text = path.read_text(encoding="utf-8")
    if "unittest" not in text or "tests" not in text:
        return [_CI]
    return []


def _copied_log(work: Path) -> bool:
    return any(path.name == "log.json" for path in work.rglob("*") if path.is_file())


def _run(work: Path, pack: Path, gold: dict, notes) -> list[str]:
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
    if contains_canary(work, canary) or _copied_log(work):
        return [WATERMARK]
    if not _present(work):
        return ["the deploy is missing"]
    writer = notes or written_problems
    try:
        return _run(work, pack, gold, writer)
    except Exception:
        return ["the deploy did not run"]
