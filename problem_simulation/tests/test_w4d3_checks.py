"""Day 3 of Week 4 checks for the surge and the serving design.

Guards the service-level checker and the surge checker.

The fixture is this day's pack plus the filled work tree. The filled copy must
pass. Shell swaps cover the adapter list, the batch, the route, the public
endpoint, the quota, the scaler, the price, and the capacity table. A sprint
that puts capacity first, an empty capacity note, placeholder knowledge, and
notes that miss the price and the campaign must all fail. Problem text must
not echo the watermark, the candidate hash, the surge times, or a rate or a
price.
"""

from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.notes_w4d3 import BI, CAPACITY, COLD, FINANCE, PUNISH, SEQUENCE
from alwaha.check.slo_w4 import BACKLOG, LATENCY, MISSING, TABLE, UNREGISTERED, WINDOW, YESTERDAY
from alwaha.check.surge_w4 import EXTERNAL, GPU, UNBATCHED
from alwaha.config.profile import load
from alwaha.engagement.w4d3 import gold
from alwaha.paths import W4D3_APP, W4D3_WORK


class CheckTests(unittest.TestCase):
    """Catches a grader that accepts an unregistered adapter, an unbatched backlog, or
    yesterday's price.
    """
    def setUp(self) -> None:
        """Write this day's pack and copy the filled work tree."""
        # A temporary pack for the small profile. The gold comes from the generator.
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w4d3 import write_w4d3

        write_w4d3(self.profile, self.pack, self.truth)
        self.gold = gold(self.profile)
        # The filled work tree, without cached bytecode.
        self.work = root / "work"
        shutil.copytree(W4D3_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def tearDown(self) -> None:
        """Delete the temporary pack and work tree."""
        self.tmp.cleanup()

    def _slo(self) -> list[str]:
        """Run the service-level checker."""
        from alwaha.check.slo_w4 import slo_problems

        return slo_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _surge(self) -> list[str]:
        """Run the surge checker."""
        from alwaha.check.surge_w4 import surge_problems

        return surge_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        """Fail this case when a problem list echoes the watermark, the candidate hash, a
        surge time, a price, or a rate.
        """
        joined = "\n".join(problems)
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn(self.gold["candidate_hash"], joined)
        self.assertNotIn(self.gold["started_at"], joined)
        self.assertNotIn(self.gold["peak_at"], joined)
        for key in ("new_price", "old_price", "new_sar", "old_sar", "budget_sar", "local_sar"):
            self.assertNotIn(str(self.gold[key]), joined)
        for key in ("local_batched_tps", "local_unbatched_tps", "ext_large_tps", "backlog"):
            self.assertNotIn(str(self.gold[key]), joined)

    def _swap(self, name: str) -> None:
        """Replace one work module with the unfinished shell of the same name."""
        shutil.copy(W4D3_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        """Fails when the filled work tree still produces a service-level problem or a surge problem."""
        self.assertEqual(self._slo(), [])
        self.assertEqual(self._surge(), [])

    def test_shell_adapters_load_the_lookalike(self) -> None:
        """Fails when the unfinished adapter list, which loads the lookalike, is accepted.
        The surge checker should stay quiet.
        """
        self._swap("adapters.py")
        problems = self._slo()
        self.assertEqual(problems, [MISSING, UNREGISTERED])
        self._hidden(problems)
        self.assertEqual(self._surge(), [])

    def test_shell_batch_is_unbatched(self) -> None:
        """Fails when an unbatched run is accepted. The service-level checker should see
        the backlog miss, and the surge checker should see the missing batch.
        """
        self._swap("batch.py")
        slo = self._slo()
        surge = self._surge()
        self.assertEqual(slo, [BACKLOG])
        self.assertEqual(surge, [UNBATCHED])
        self._hidden(slo)
        self._hidden(surge)

    def test_shell_route_sends_the_batch_out(self) -> None:
        """Fails when a route that sends the batch to the external model is accepted. The
        service-level checker should stay quiet.
        """
        self._swap("route.py")
        problems = self._surge()
        self.assertEqual(problems, [EXTERNAL])
        self._hidden(problems)
        self.assertEqual(self._slo(), [])

    def test_shell_public_hits_the_gpu(self) -> None:
        """Fails when a public request is allowed to land on the accelerator. The
        service-level checker should stay quiet.
        """
        self._swap("public.py")
        problems = self._surge()
        self.assertEqual(problems, [GPU])
        self._hidden(problems)
        self.assertEqual(self._slo(), [])

    def test_shell_quota_starves_chat(self) -> None:
        """Fails when a quota that starves chat is accepted.

        The test restores the unfinished quota and fails unless the service-level checker says
        chat misses its latency while the batch runs, and the problem list does not echo a
        hidden value.
        """
        self._swap("quota.py")
        problems = self._slo()
        self.assertEqual(problems, [LATENCY])
        self._hidden(problems)

    def test_shell_scale_starts_at_the_peak(self) -> None:
        """Fails when scaling that starts at the peak, and so misses the window, is accepted.

        The test restores the unfinished scaler and fails unless the service-level checker says
        the first window was missed, and the problem list does not echo a hidden value.
        """
        self._swap("scale.py")
        problems = self._slo()
        self.assertEqual(problems, [WINDOW])
        self._hidden(problems)

    def test_shell_price_uses_yesterday(self) -> None:
        """Fails when yesterday's price is accepted in place of today's.

        The test restores the unfinished price module and fails unless the service-level checker
        says yesterday's price is still in use, and the problem list does not echo a hidden
        value.
        """
        self._swap("price.py")
        problems = self._slo()
        self.assertEqual(problems, [YESTERDAY])
        self._hidden(problems)

    def test_shell_capacity_omits_the_table(self) -> None:
        """Fails when a capacity note that omits the comparison table is accepted.

        The test restores the unfinished capacity module and fails unless the service-level
        checker says the comparison table misses the backlog or the price, and the problem list
        does not echo a hidden value.
        """
        self._swap("capacity.py")
        problems = self._slo()
        self.assertEqual(problems, [TABLE])
        self._hidden(problems)

    def test_sprint_out_of_order_fails(self) -> None:
        """Fails when a sprint that puts capacity first is accepted.

        The test writes a sprint that puts capacity first and fails unless the service-level
        checker wants the forecast to open the sprint, and the problem list does not echo a
        hidden value.
        """
        (self.work / "sprint.md").write_text("# Sprint\n\nCapacity comes first.\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [SEQUENCE])
        self._hidden(problems)

    def test_an_empty_capacity_note_fails(self) -> None:
        """Fails when an empty capacity page is accepted.

        The test writes an empty capacity page and fails unless the service-level checker says a
        required section is missing, and the problem list does not echo a hidden value.
        """
        (self.work / "capacity.md").write_text("# Capacity\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [CAPACITY])
        self._hidden(problems)

    def test_knowledge_needs_both_answers(self) -> None:
        """Fails when placeholder answers are accepted in place of what the cold start
        costs and what a missed batch punishes.
        """
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Yes.\n2. No.\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [COLD, PUNISH])
        self._hidden(problems)

    def test_notes_miss_the_price_and_the_campaign(self) -> None:
        """Fails when the finance note misses today's price or the warehouse note misses
        the campaign. The leftover sentences are true and still not enough.
        """
        (self.work / "interviews" / "finance.notes.md").write_text("# finance\n\nThe budget line exists.\n", encoding="utf-8")
        (self.work / "interviews" / "bi-lead.notes.md").write_text("# bi-lead\n\nWaiting time improved.\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [FINANCE, BI])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        """Fails when a file that contains only the watermark is ignored, or when a problem
        message contains the watermark.
        """
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        for problems in (self._slo(), self._surge()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
