"""Day 3 of Week 2 test and usability checks."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.tests_w2 import test_problems
from alwaha.check.ux_w2 import ux_problems
from alwaha.config.profile import load
from alwaha.engagement.w2d3 import SWITCH, gold
from alwaha.paths import W2D3_APP, W2D3_TESTS, W2D3_WORK
from alwaha.release.w2d3 import write_w2d3


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_w2d3(self.profile, self.pack, self.truth)
        self.gold = json.loads((self.truth / "w2d3_gold.json").read_text(encoding="utf-8"))
        self.work = root / "work"
        shutil.copytree(
            W2D3_WORK,
            self.work,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )
        self.assertEqual(self.gold, gold(self.profile))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _tests(self) -> list[str]:
        return test_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _ux(self) -> list[str]:
        return ux_problems(self.work, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        joined = "\n".join(problems)
        secrets = [
            str(self.gold["old_delay_seconds"]),
            str(self.gold["interval_minutes"]),
            self.gold["cases"][0]["due"],
            self.gold["cases"][1]["due"],
            self.profile.canary(),
            SWITCH,
        ]
        for secret in secrets:
            self.assertNotIn(secret, joined)

    def test_filled_work_passes(self) -> None:
        self.assertEqual(self._tests(), [])
        self.assertEqual(self._ux(), [])

    def test_shell_calendar_fails_without_the_date(self) -> None:
        shutil.copy(W2D3_APP / "calendar_count.py", self.work / "app" / "calendar_count.py")
        problems = self._tests()
        self.assertEqual(problems, ["the calendar does not match"])
        self._hidden(problems)

    def test_sleeping_receipt_fails_without_the_delay(self) -> None:
        shutil.copy(W2D3_TESTS / "test_receipt.py", self.work / "tests" / "test_receipt.py")
        problems = self._tests()
        self.assertEqual(problems, ["the receipt test sleeps"])
        self._hidden(problems)

    def test_always_due_accepts_the_fault(self) -> None:
        shutil.copy(W2D3_APP / "receipt.py", self.work / "app" / "receipt.py")
        problems = self._tests()
        self.assertIn("the suite accepted the receipt fault", problems)
        self._hidden(problems)

    def test_sentence_journey_fails_without_the_fixture(self) -> None:
        shutil.copy(W2D3_APP / "schema.py", self.work / "app" / "schema.py")
        problems = self._tests()
        self.assertIn("the reply schema is missing", problems)
        self.assertIn("the journey followed the sentence", problems)
        self._hidden(problems)

    def test_missing_clause(self) -> None:
        text = (self.work / "usability.md").read_text(encoding="utf-8").replace("named-control", "color-only")
        (self.work / "usability.md").write_text(text, encoding="utf-8")
        problems = self._ux()
        self.assertIn("an accessibility clause is missing", problems)
        self._hidden(problems)

    def test_missing_fault_in_the_definition_of_done(self) -> None:
        (self.work / "dod.md").write_text("# Definition of done\n\nThe suite is green.\n", encoding="utf-8")
        problems = self._ux()
        self.assertEqual(problems, ["the fault is not in the definition of done"])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        shutil.copy(self.pack / "fixtures" / "model.json", self.work / "model.json")
        problems = self._ux()
        self.assertEqual(problems, [WATERMARK])
        self.assertNotIn(self.profile.canary(), problems[0])
        self._hidden(self._tests())


if __name__ == "__main__":
    unittest.main()
