"""chk-individual-w3. A miss does not print a document id or a metric value."""

from __future__ import annotations

from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.load_app import modules
from alwaha.check.tables import contains_canary

CITE_DROP = "the citation drops the version or the audience"
CITE_STAFF = "the citation serves a staff document to a patient"
METRIC = "the metric read ignores its budget"
MISSING = "the personal lab is missing"
RUN = "the personal lab did not run"
_MODULES = ("personal",)


def _once(problems: list[str], item: str) -> None:
    if item not in problems:
        problems.append(item)


def _kept(got, row: dict) -> bool:
    return (
        isinstance(got, dict)
        and got.get("doc_id") == row["doc_id"]
        and got.get("version") == row["version"]
        and got.get("audience") == row["audience"]
    )


def _problems(module, gold: dict) -> list[str]:
    problems: list[str] = []
    try:
        for row in gold["personal"]["citations"]:
            got = module.cite({key: row[key] for key in ("asker", "audience", "doc_id", "version")})
            if row["keep"] and not _kept(got, row):
                _once(problems, CITE_DROP)
            if not row["keep"] and got is not None:
                _once(problems, CITE_STAFF)
        for row in gold["personal"]["metrics"]:
            if bool(module.meets_budget(row["value"], row["floor"])) != row["meets"]:
                _once(problems, METRIC)
                break
    except Exception:
        return [RUN]
    return problems


def individual_problems(work: Path, gold: dict, canary: str) -> list[str]:
    if contains_canary(work, canary):
        return [WATERMARK]
    folder = work / "app"
    if not (folder / "personal.py").is_file():
        return [MISSING]
    try:
        with modules(folder, _MODULES) as loaded:
            return _problems(loaded["personal"], gold)
    except Exception:
        return [RUN]
