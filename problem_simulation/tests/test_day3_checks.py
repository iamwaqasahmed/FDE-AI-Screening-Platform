"""Day 3 intake check."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.events import events_problems
from alwaha.config.profile import load
from alwaha.paths import DAY3_TEMPLATES, WORKFLOW_ROOT
from alwaha.release.day3 import write_day3

INTAKE = """# Intake

## Steps

1. referral.submitted
2. extract
3. retrieve the criteria in force
4. duplicate check
5. suggest a clinic
6. a coordinator holds the approval

## Acceptance

The workflow stops when a coordinator holds the approval. It does not book.

## In-flight criteria

An in-flight referral keeps the criteria version it started with.
"""

KNOWLEDGE = """1. The clock named in the SLA policy.
2. A second delivery of the same event does not open another approval.
"""

NAIVE = {
    "friday due date does not match the calendar",
    "holiday due date does not match the calendar",
    "ain booked a slot",
    "replay opened a second approval",
    "compensation hold does not match",
    "dead-letter applied the poison event",
    "happy criteria is not the one in force",
    "happy booked a slot",
    "duplicate referral was not flagged",
    "order suggestion does not match",
}


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_day3(self.profile, self.pack, self.truth)
        self.gold = json.loads((self.truth / "events_gold.json").read_text(encoding="utf-8"))
        self.work = root / "work"
        self.work.mkdir()
        self.here = Path(__file__).resolve().parent

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _copy_skeleton(self) -> None:
        shutil.copytree(
            WORKFLOW_ROOT,
            self.work / "workflow",
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )

    def _use_correct_worker(self) -> None:
        self._copy_skeleton()
        workflow = self.work / "workflow"
        (workflow / "worker.py").write_text((self.here / "day3_worker.py").read_text(encoding="utf-8"), encoding="utf-8")
        (workflow / "calendar_count.py").write_text((self.here / "day3_calendar.py").read_text(encoding="utf-8"), encoding="utf-8")

    def _prose(self) -> None:
        (self.work / "intake.md").write_text(INTAKE, encoding="utf-8")
        (self.work / "knowledge.md").write_text(KNOWLEDGE, encoding="utf-8")

    def _grade(self) -> list[str]:
        return events_problems(self.work, self.pack, self.gold, self.profile.canary())

    def test_naive_skeleton_fails_without_the_key(self) -> None:
        self._copy_skeleton()
        self._prose()
        problems = self._grade()
        for item in NAIVE:
            self.assertIn(item, problems)
        joined = "\n".join(problems)
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn("approval.held", joined)
        self.assertNotIn("ENDO-CLN", joined)
        for row in self.gold["scenarios"]:
            if row["due"]:
                self.assertNotIn(row["due"], joined)
            if row["criteria_id"]:
                self.assertNotIn(row["criteria_id"], joined)
        for doc in ("endo-v3-c1", "endo-v4-c1"):
            self.assertNotIn(doc, joined)

    def test_correct_worker_passes(self) -> None:
        self._use_correct_worker()
        self._prose()
        self.assertEqual(self._grade(), [])

    def test_diagram_and_knowledge_are_required(self) -> None:
        self._use_correct_worker()
        (self.work / "intake.md").write_text(DAY3_TEMPLATES.joinpath("intake.md").read_text(encoding="utf-8"), encoding="utf-8")
        (self.work / "knowledge.md").write_text("1. only one\n", encoding="utf-8")
        problems = self._grade()
        self.assertIn("the diagram does not show the human step", problems)
        self.assertIn("the note does not keep the criteria version", problems)
        self.assertIn("knowledge.md needs two answers", problems)

    def test_watermark_in_work_is_not_echoed(self) -> None:
        (self.work / "copied.md").write_text(self.profile.canary(), encoding="utf-8")
        problems = self._grade()
        self.assertEqual(problems, ["a watermarked sample is in the work directory"])
        self.assertNotIn(self.profile.canary(), "\n".join(problems))

    def test_watermark_in_the_log_is_not_echoed(self) -> None:
        workflow = self.work / "workflow"
        workflow.mkdir()
        script = """import sys
from pathlib import Path
pack = Path(sys.argv[sys.argv.index("--pack") + 1])
out = Path(sys.argv[sys.argv.index("--out") + 1])
out.write_text((pack / "events" / "intake.jsonl").read_text(encoding="utf-8"), encoding="utf-8")
"""
        (workflow / "worker.py").write_text(script, encoding="utf-8")
        self._prose()
        problems = self._grade()
        self.assertIn("a watermarked sample is in the work directory", problems)
        self.assertNotIn(self.profile.canary(), "\n".join(problems))


if __name__ == "__main__":
    unittest.main()
