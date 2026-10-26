"""Day 5 of Week 2 deploy, journey, readout, and individual checks.

Guards the carried-forward deploy check, the queue journey, the readout, and
the individual contract check.

The fixture writes both the deploy pack and this day's pack, then copies the
filled work tree. The filled copy must pass, even after the optional queue
modules are removed. The unfinished queue, file reader, and notifier must each
fail the journey in their own way. The unfinished contract test must fail the
individual check. A copied live-slot fixture and a note that promises a live
slot must fail without echoing the clinic code or the deploy secrets.
"""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.deploy_w2 import deploy_problems
from alwaha.check.individual_w2 import individual_problems
from alwaha.check.notes_w2d5 import written_problems
from alwaha.check.queue_w2 import queue_problems
from alwaha.check.readout_w2 import readout_problems
from alwaha.config.profile import load
from alwaha.engagement.w2d4 import gold as deploy_gold
from alwaha.engagement.w2d5 import gold
from alwaha.paths import W2D5_APP, W2D5_TESTS, W2D5_WORK
from alwaha.release.w2d4 import write_w2d4
from alwaha.release.w2d5 import write_w2d5


class CheckTests(unittest.TestCase):
    """Catches a grader that accepts a promised slot, a cleared missed night, or a
    contract test that cannot see the fault.
    """
    def setUp(self) -> None:
        """Write the deploy pack and this day's pack, and copy the filled work tree.

        Both gold files must match their generators. The deploy pack is the smoke
        input for the deploy checker. This day's pack is the input for the journey.
        """
        # The deploy pack is the smoke input. This day's pack is the journey input.
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.smoke = root / "smoke"
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_w2d4(self.profile, self.smoke, self.truth)
        write_w2d5(self.profile, self.pack, self.truth)
        self.smoke_gold = json.loads((self.truth / "w2d4_gold.json").read_text(encoding="utf-8"))
        self.gold = json.loads((self.truth / "w2d5_gold.json").read_text(encoding="utf-8"))
        # The filled work tree, without cached bytecode.
        self.work = root / "work"
        shutil.copytree(
            W2D5_WORK,
            self.work,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )
        # Both gold files must match their generators before a test changes the work tree.
        self.assertEqual(self.gold, gold(self.profile))
        self.assertEqual(self.smoke_gold, deploy_gold(self.profile))

    def tearDown(self) -> None:
        """Delete the temporary packs and work tree."""
        self.tmp.cleanup()

    def _notes(self, work: Path, _pack: Path, _gold: dict) -> list[str]:
        """Adapter so the deploy checker can grade this day's written pages.

        The deploy checker calls this with its own paths. The body ignores those and
        reads the written problems for the scratch work tree.
        """
        return written_problems(work, self.pack, self.gold)

    def _deploy(self) -> list[str]:
        """Run the deploy checker with this day's notes adapter attached."""
        return deploy_problems(self.work, self.smoke, self.smoke_gold, self.profile.canary(), self._notes)

    def _journey(self) -> list[str]:
        """Run the queue checker."""
        return queue_problems(self.work, self.gold, self.profile.canary())

    def _readout(self) -> list[str]:
        """Run the readout checker over both packs."""
        return readout_problems(self.work, self.gold, self.profile.canary(), [self.smoke, self.pack])

    def _individual(self) -> list[str]:
        """Run the individual contract checker."""
        return individual_problems(self.work, self.pack, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        """Fail this case when a problem list echoes a clinic code, a deploy secret, the
        quota, or the watermark.
        """
        joined = "\n".join(problems)
        secrets = [
            self.gold["clinic_code"],
            self.gold["previous_code"],
            self.smoke_gold["approved_hash"],
            self.smoke_gold["dev_token"],
            self.smoke_gold["prod_token"],
            self.smoke_gold["national_id"],
            str(self.smoke_gold["quota"]),
            self.profile.canary(),
        ]
        for secret in secrets:
            self.assertNotIn(secret, joined)

    def test_filled_work_passes(self) -> None:
        """Fails when the filled work tree still produces a deploy, journey, readout, or
        individual problem.
        """
        self.assertEqual(self._deploy(), [])
        self.assertEqual(self._journey(), [])
        self.assertEqual(self._readout(), [])
        self.assertEqual(self._individual(), [])

    def test_advanced_modules_are_optional(self) -> None:
        """Fails when removing the queue, the file reader, or the notifier makes a passing
        tree fail. Those modules are not required for the grade.
        """
        for name in ("queue.py", "file_ain.py", "notify.py"):
            (self.work / "app" / name).unlink()
        self.assertEqual(self._deploy(), [])
        self.assertEqual(self._journey(), [])
        self.assertEqual(self._readout(), [])
        self.assertEqual(self._individual(), [])

    def test_shell_queue_promises_a_slot(self) -> None:
        """Fails when the unfinished queue, which promises a live slot, is accepted."""
        shutil.copy(W2D5_APP / "queue.py", self.work / "app" / "queue.py")
        problems = self._journey()
        self.assertEqual(problems, ["a live slot was promised"])
        self._hidden(problems)

    def test_shell_file_clears_a_missed_night(self) -> None:
        """Fails when the unfinished file reader, which clears slots after a missed night,
        is accepted.
        """
        shutil.copy(W2D5_APP / "file_ain.py", self.work / "app" / "file_ain.py")
        problems = self._journey()
        self.assertEqual(problems, ["a missed night cleared the slots"])
        self._hidden(problems)

    def test_shell_notice_confirms_a_slot(self) -> None:
        """Fails when the unfinished notifier, which confirms a slot after a failed send,
        is accepted.
        """
        shutil.copy(W2D5_APP / "notify.py", self.work / "app" / "notify.py")
        problems = self._journey()
        self.assertEqual(problems, ["a failed notice confirmed a slot"])
        self._hidden(problems)

    def test_shell_contract_accepts_the_fault(self) -> None:
        """Fails when the unfinished contract module and its test, which accept the
        live-slot fault, are accepted.
        """
        shutil.copy(W2D5_APP / "contract.py", self.work / "app" / "contract.py")
        shutil.copy(W2D5_TESTS / "test_contract.py", self.work / "tests" / "test_contract.py")
        problems = self._individual()
        self.assertEqual(problems, ["the contract test accepted the live-slot fault"])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        """Fails when a copied live-slot fixture is ignored, or when the problem text
        contains the watermark.
        """
        shutil.copy(self.pack / "fixtures" / "live-slot.json", self.work / "live-slot.json")
        problems = self._deploy()
        self.assertEqual(problems, [WATERMARK])
        self.assertNotIn(self.profile.canary(), problems[0])
        self._hidden(problems)

    def test_banned_sentence_is_not_echoed(self) -> None:
        """Fails when a deployment note that promises a live slot is accepted."""
        text = (self.work / "deployment.md").read_text(encoding="utf-8")
        text += "\nAin has a live slot.\n"
        (self.work / "deployment.md").write_text(text, encoding="utf-8")
        problems = self._deploy()
        self.assertIn("the deployment note promises a live slot", problems)
        self._hidden(problems)


if __name__ == "__main__":
    unittest.main()
