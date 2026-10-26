"""Day 2 of Week 2 journey check."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.journey_w2 import journey_problems
from alwaha.config.profile import load
from alwaha.engagement.w2d2 import CLOCK, DROPPED, EXTRA, gold
from alwaha.paths import W2D2_APP, W2D2_WORK
from alwaha.release.w2d2 import write_w2d2

_REJECT = '''"""Reject a field the registry does not list."""

def accept(body: dict, registry_text: str) -> dict:
    return {"mode": "webhook", "referral_id": body.get("referral_id", ""), "ignored": [], "rejected": True, "record": {}}
'''

_STORE = '''"""Keep every field on the referral."""

def accept(body: dict, registry_text: str) -> dict:
    record = {key: value for key, value in body.items() if key != "letter"}
    return {"mode": "webhook", "referral_id": body.get("referral_id", ""), "ignored": [], "rejected": False, "record": record}
'''


class CheckTests(unittest.TestCase):
    """Grade the journey check on a temporary pack.

    The filled work tree is copied in, and the directory is removed when the test ends.
    """
    def setUp(self) -> None:
        """Build the pack and copy the filled work tree.

        The written gold must match the gold builder. A drift between the release and the builder fails here, before a journey assertion runs.
        """
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_w2d2(self.profile, self.pack, self.truth)
        self.gold = json.loads((self.truth / "w2d2_gold.json").read_text(encoding="utf-8"))
        self.work = root / "work"
        shutil.copytree(
            W2D2_WORK,
            self.work,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "sessions.db", "trace.json"),
        )
        self.assertEqual(self.gold, gold(self.profile))

    def tearDown(self) -> None:
        """Remove the temporary directory.

        A later test must not see this pack or this work tree.
        """
        self.tmp.cleanup()

    def _problems(self) -> list[str]:
        """Return the journey problems for the work directory.

        The tests fail when this list is not the misses they expect.
        """
        return journey_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        """Fail the test when a problem repeats a hidden value.

        The extra field, the dropped field, the clock, the wait figure, the owner, and the watermark must stay out of the report.
        """
        joined = "\n".join(problems)
        for secret in (EXTRA, DROPPED, CLOCK, str(self.gold["wait"]), self.gold["owner"], self.profile.canary()):
            self.assertNotIn(secret, joined)

    def test_filled_work_passes(self) -> None:
        """Catch a filled work tree that the journey check still rejects.

        An empty problem list is required. Any problem means the filled tree no longer passes.
        """
        self.assertEqual(self._problems(), [])

    def test_poll_intake_fails_without_naming_the_field(self) -> None:
        """Catch intake that still polls, and a report that names the hidden field.

        The only problem must be the poll message. That message must not carry a hidden value.
        """
        shutil.copy(W2D2_APP / "intake.py", self.work / "app" / "intake.py")
        problems = self._problems()
        self.assertEqual(problems, ["intake still polls"])
        self._hidden(problems)

    def test_replay_books_again(self) -> None:
        """Catch a cancellation path that books again.

        A replay that books, a hold left open, and a no-slot cancellation that was booked must all be reported, with no hidden value in the text.
        """
        shutil.copy(W2D2_APP / "cancel.py", self.work / "app" / "cancel.py")
        problems = self._problems()
        self.assertIn("replay booked again", problems)
        self.assertIn("the hold was left open", problems)
        self.assertIn("no-slot cancellation was booked", problems)
        self._hidden(problems)

    def test_trusted_mart_fails_without_the_figure(self) -> None:
        """Catch a wait number used as the truth.

        That must be the only problem, and the report must not print the figure or another hidden value.
        """
        shutil.copy(W2D2_APP / "mart.py", self.work / "app" / "mart.py")
        problems = self._problems()
        self.assertEqual(problems, ["wait number was used as truth"])
        self._hidden(problems)

    def test_unknown_field_messages_hide_the_name(self) -> None:
        """Catch both wrong treatments of an unknown field.

        Rejecting the field must be reported on its own. Storing the field must be reported on its own. Neither report may name the field.
        """
        (self.work / "app" / "intake.py").write_text(_REJECT, encoding="utf-8")
        rejected = self._problems()
        self.assertEqual(rejected, ["an unknown field stopped intake"])
        self._hidden(rejected)
        (self.work / "app" / "intake.py").write_text(_STORE, encoding="utf-8")
        stored = self._problems()
        self.assertEqual(stored, ["an unknown field was stored"])
        self._hidden(stored)

    def test_watermark_is_not_echoed(self) -> None:
        """Catch a webhook copied into the work directory.

        The only problem must be the watermark message, and that message must not contain the watermark.
        """
        shutil.copy(self.pack / "webhooks" / "referral.submitted.json", self.work / "referral.submitted.json")
        problems = self._problems()
        self.assertEqual(problems, [WATERMARK])
        self.assertNotIn(self.profile.canary(), problems[0])

    def test_knowledge_needs_both_answers(self) -> None:
        """Catch knowledge answers that miss the owner and the replay rule.

        Both misses must be reported, and the report must not leak a hidden value.
        """
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Soon.\n2. It runs again.\n", encoding="utf-8")
        problems = self._problems()
        self.assertIn("knowledge.md does not name the owner", problems)
        self.assertIn("knowledge.md does not say what a replay does", problems)
        self._hidden(problems)


if __name__ == "__main__":
    unittest.main()
