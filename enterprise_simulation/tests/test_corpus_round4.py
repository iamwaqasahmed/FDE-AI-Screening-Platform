"""Round 4 student corpus checks. Instructor corpus is not scanned."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_STUDENT = _ROOT / "corpus" / "student"
_INSTRUCTOR = _ROOT / "corpus" / "instructor"

_FORBIDDEN = (
    "dec-accept",
    "dec-clinical",
    "dec-route",
    "dec-cover",
    "dec-slot",
    "root_cause",
    "answer_key",
    "correct_currency",
    "booking_date_only",
    "HIPAA",
    "PIPEDA",
)

_ACCESS_LINE = "access: student"
_SCAN_SUFFIXES = frozenset({".md", ".jsonl"})
_MIN_LINK_OBJECTS = 12

_REQUIRED = (
    "interviews/followups/INT-MORGAN.md",
    "requirements/sites/SOP-CEDAR.md",
    "communications/archive/MAIL-REPLICA.md",
    "communications/archive/CHAT-QUEUE.jsonl",
    "technical/runbooks/RUN-LOGS.md",
    "external/later/EXT-MEMBER-FOLLOW.md",
    "incidents/followups/INC-HOURS-DAY2.md",
    "history/years/HIST-2019-WES.md",
    "governance/requests/GOV-REQ-NOEL.md",
    "investigations/PACK-WAIT.md",
    "investigations/links.json",
)

_LINKS = "investigations/links.json"


def _under_instructor(path: Path) -> bool:
    resolved = path.resolve()
    instructor = _INSTRUCTOR.resolve()
    return resolved == instructor or instructor in resolved.parents


def _student_scan_files() -> list[Path]:
    if not _STUDENT.is_dir():
        return []
    found: list[Path] = []
    for path in _STUDENT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in _SCAN_SUFFIXES:
            continue
        if _under_instructor(path):
            continue
        found.append(path)
    return sorted(found)


def _markdown(files: list[Path]) -> list[Path]:
    return [path for path in files if path.suffix.lower() == ".md"]


def _lines(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines()]


def _forbidden_hits(files: list[Path]) -> list[str]:
    hits: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(_STUDENT)
        hits.extend(f"{rel} contains {token}" for token in _FORBIDDEN if token in text)
    return hits


def _missing_required() -> list[str]:
    return [rel for rel in _REQUIRED if not (_STUDENT / rel).is_file()]


class CorpusRound4Tests(unittest.TestCase):
    def test_forbidden_strings_absent(self) -> None:
        hits = _forbidden_hits(_student_scan_files())
        if hits:
            self.fail("forbidden strings:\n" + "\n".join(hits))

    def test_every_markdown_file_has_student_access_line(self) -> None:
        markdown = _markdown(_student_scan_files())
        missing = [
            str(path.relative_to(_STUDENT))
            for path in markdown
            if _ACCESS_LINE not in _lines(path)
        ]
        if missing:
            joined = ", ".join(missing)
            self.fail(f"missing line {_ACCESS_LINE!r}: {joined}")

    def test_required_paths_exist(self) -> None:
        missing = _missing_required()
        if missing:
            joined = ", ".join(missing)
            self.fail(f"missing student paths: {joined}")

    def test_links_json_is_a_list_of_objects(self) -> None:
        path = _STUDENT / _LINKS
        if not path.is_file():
            return
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertIsInstance(data, list, "links.json must parse as a list")
        self.assertGreaterEqual(len(data), _MIN_LINK_OBJECTS)
        for index, item in enumerate(data):
            self.assertIsInstance(
                item,
                dict,
                f"links.json[{index}] is not an object",
            )


if __name__ == "__main__":
    unittest.main()
