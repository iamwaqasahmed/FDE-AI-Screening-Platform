"""Student document room must not carry grader tokens. Instructor corpus is not scanned."""

from __future__ import annotations

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
)

_ACCESS_LINE = "access: student"
_MIN_OTHER = 5
_ASIDE = frozenset({"README.md", "entities.md"})


def _under_instructor(path: Path) -> bool:
    resolved = path.resolve()
    instructor = _INSTRUCTOR.resolve()
    return resolved == instructor or instructor in resolved.parents


def _student_files() -> list[Path]:
    if not _STUDENT.is_dir():
        return []
    found: list[Path] = []
    for path in _STUDENT.rglob("*"):
        if path.is_file() and not _under_instructor(path):
            found.append(path)
    return sorted(found)


def _markdown(files: list[Path]) -> list[Path]:
    return [path for path in files if path.suffix.lower() == ".md"]


def _other_markdown(files: list[Path]) -> list[Path]:
    return [path for path in _markdown(files) if path.name not in _ASIDE]


class CorpusLeakTests(unittest.TestCase):
    def test_entities_md_is_present(self) -> None:
        path = _STUDENT / "entities.md"
        self.assertTrue(path.is_file(), f"entities.md is missing from {_STUDENT}")

    def test_enough_markdown_besides_readme_and_entities(self) -> None:
        others = _other_markdown(_student_files())
        if len(others) < _MIN_OTHER:
            self.fail(
                "The student tree has "
                f"{len(others)} markdown files besides README and entities. "
                f"At least {_MIN_OTHER} are required. "
                "Other agents may still be writing."
            )

    def test_every_markdown_file_has_student_access_line(self) -> None:
        markdown = _markdown(_student_files())
        self.assertTrue(markdown, f"no markdown files under {_STUDENT}")
        missing = [
            str(path.relative_to(_STUDENT))
            for path in markdown
            if _ACCESS_LINE not in _lines(path)
        ]
        if missing:
            joined = ", ".join(missing)
            self.fail(f"missing line {_ACCESS_LINE!r}: {joined}")

    def test_forbidden_strings_absent(self) -> None:
        hits = _forbidden_hits(_student_files())
        if hits:
            self.fail("forbidden strings:\n" + "\n".join(hits))


def _lines(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines()]


def _forbidden_hits(files: list[Path]) -> list[str]:
    hits: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(_STUDENT)
        hits.extend(f"{rel} contains {token}" for token in _FORBIDDEN if token in text)
    return hits


if __name__ == "__main__":
    unittest.main()
