"""chk-individual-w3. A miss does not print a document id or a metric value.

This personal-lab check grades citations and metric budgets. A citation gold says to keep must still carry the document, the version, and the audience. A citation gold says to withhold must come back as nothing. A metric must agree with gold about whether it meets the floor. A planted token, a missing module, or a crash stops the check. Document ids and metric values are not printed.
"""

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
    """Append the miss when that sentence is not already in the list.

    Several rows can fail the same way, and the list should name each failure once.
    """
    if item not in problems:
        problems.append(item)


def _kept(got, row: dict) -> bool:
    """Return true when the citation record kept the document, the version, and the audience from the gold row.

    A non-record fails. A missing key fails. The comparison is exact.
    """
    return (
        isinstance(got, dict)
        and got.get("doc_id") == row["doc_id"]
        and got.get("version") == row["version"]
        and got.get("audience") == row["audience"]
    )


def _problems(module, gold: dict) -> list[str]:
    """Return the citation and metric misses from one loaded module.

    A kept citation that drops any of those three fields is the drop miss. A withheld citation that comes back as a record is the staff miss. The first metric whose budget answer disagrees stops the loop, because one budget miss is enough. An exception replaces any partial misses with the run miss.
    """
    problems: list[str] = []
    try:
        for row in gold["personal"]["citations"]:
            got = module.cite({key: row[key] for key in ("asker", "audience", "doc_id", "version")})
            # A citation gold says to keep must still carry the document, the version, and the audience.
            if row["keep"] and not _kept(got, row):
                _once(problems, CITE_DROP)
            # A citation gold says to withhold must come back as nothing. Any record is a staff document shown to a patient.
            if not row["keep"] and got is not None:
                _once(problems, CITE_STAFF)
        for row in gold["personal"]["metrics"]:
            if bool(module.meets_budget(row["value"], row["floor"])) != row["meets"]:
                _once(problems, METRIC)
                # One metric that misses its budget is enough, so later rows are not graded.
                break
    except Exception:
        return [RUN]
    return problems


def individual_problems(work: Path, gold: dict, canary: str) -> list[str]:
    """Return the personal-lab misses.

    A planted token wins. A missing module is its own miss. Otherwise the module is loaded and the row checks run. An exception around the load is the run miss, which is distinct from an exception inside the row loop.
    """
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
