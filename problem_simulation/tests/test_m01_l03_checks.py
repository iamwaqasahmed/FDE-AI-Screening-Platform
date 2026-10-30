"""Module 1, Lesson 3 intake check.

The fixture writes a small pack and grades the intake prose together with the worker.
A finished worker passes. The unfinished skeleton must name every planted miss
without copying a hidden value into the problem list.
"""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.events import events_problems
from alwaha.config.profile import load
from alwaha.paths import M01_L03_TEMPLATES, WORKFLOW_ROOT
from alwaha.release.m01_l03 import write_m01_l03

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
    """Grade the intake check on a temporary pack.

    Each test gets its own pack and work directory, and that directory is removed when the test ends.
    """
    def setUp(self) -> None:
        """Build a temporary pack, its gold, and an empty work directory.

        The release is written for the small profile so every test grades the same pack.
        """
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_m01_l03(self.profile, self.pack, self.truth)
        self.gold = json.loads((self.truth / "events_gold.json").read_text(encoding="utf-8"))
        self.work = root / "work"
        self.work.mkdir()
        self.here = Path(__file__).resolve().parent

    def tearDown(self) -> None:
        """Remove the temporary directory.

        A later test must not see this pack or this work directory.
        """
        self.tmp.cleanup()

    def _copy_skeleton(self) -> None:
        """Copy the workflow skeleton into the work directory.

        Caches are skipped so the grade sees source. The naive test uses this copy to catch an unfinished worker.
        """
        shutil.copytree(
            WORKFLOW_ROOT,
            self.work / "workflow",
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )

    def _use_correct_worker(self) -> None:
        """Install the finished worker and calendar on the skeleton.

        The rest of the skeleton stays, so a pass means those two files are what the check accepts.
        """
        self._copy_skeleton()
        workflow = self.work / "workflow"
        (workflow / "worker.py").write_text((self.here / "m01_l03_worker.py").read_text(encoding="utf-8"), encoding="utf-8")
        (workflow / "calendar_count.py").write_text((self.here / "m01_l03_calendar.py").read_text(encoding="utf-8"), encoding="utf-8")

    def _prose(self) -> None:
        """Write the intake diagram and the knowledge answers.

        The check reads both files. Writing them first keeps a later failure about the workflow rather than missing prose.
        """
        (self.work / "intake.md").write_text(INTAKE, encoding="utf-8")
        (self.work / "knowledge.md").write_text(KNOWLEDGE, encoding="utf-8")

    def _grade(self) -> list[str]:
        """Return the intake problems for the work directory.

        The tests fail when this list is not the set of misses they expect.
        """
        return events_problems(self.work, self.pack, self.gold, self.profile.canary())

    def test_naive_skeleton_fails_without_the_key(self) -> None:
        """Catch an unfinished worker whose report is incomplete or leaks a hidden value.

        Every planted intake miss must be named. The report must not repeat the watermark, the held state, the clinic, a due date, a criteria id, or a clause id.
        """
        # Grade the unfinished skeleton together with the intake prose.
        self._copy_skeleton()
        self._prose()
        problems = self._grade()
        # Every planted miss is named.
        for item in NAIVE:
            self.assertIn(item, problems)
        joined = "\n".join(problems)
        # The report does not repeat the watermark, the held state, or the clinic.
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn("approval.held", joined)
        self.assertNotIn("ENDO-CLN", joined)
        # Due dates and criteria ids from the gold stay out of the report, and so do the clause ids.
        for row in self.gold["scenarios"]:
            if row["due"]:
                self.assertNotIn(row["due"], joined)
            if row["criteria_id"]:
                self.assertNotIn(row["criteria_id"], joined)
        for doc in ("endo-v3-c1", "endo-v4-c1"):
            self.assertNotIn(doc, joined)

    def test_correct_worker_passes(self) -> None:
        """Catch a finished worker that the intake check still rejects.

        An empty problem list is required. Any remaining miss fails the test.
        """
        self._use_correct_worker()
        self._prose()
        self.assertEqual(self._grade(), [])

    def test_diagram_and_knowledge_are_required(self) -> None:
        """Catch a blank diagram or a knowledge note with one answer.

        The human step and the criteria version must appear, and the note must hold both answers, or the check is wrong to accept the work.
        """
        self._use_correct_worker()
        (self.work / "intake.md").write_text(M01_L03_TEMPLATES.joinpath("intake.md").read_text(encoding="utf-8"), encoding="utf-8")
        (self.work / "knowledge.md").write_text("1. only one\n", encoding="utf-8")
        problems = self._grade()
        self.assertIn("the diagram does not show the human step", problems)
        self.assertIn("the note does not keep the criteria version", problems)
        self.assertIn("knowledge.md needs two answers", problems)

    def test_watermark_in_work_is_not_echoed(self) -> None:
        """Catch a watermark copied into the work directory.

        The only problem may be the watermarked-sample message. That message must not contain the watermark itself.
        """
        (self.work / "copied.md").write_text(self.profile.canary(), encoding="utf-8")
        problems = self._grade()
        self.assertEqual(problems, ["a watermarked sample is in the work directory"])
        self.assertNotIn(self.profile.canary(), "\n".join(problems))

    def test_watermark_in_the_log_is_not_echoed(self) -> None:
        """Catch a worker that copies the event stream into the log.

        The check must report the watermarked sample and must not repeat the watermark in the problem text.
        """
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
