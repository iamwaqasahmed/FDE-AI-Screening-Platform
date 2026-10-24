"""Day 3 of Week 4 checks for the surge and the serving design."""

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
from alwaha.paths import W4D3_APP, W4D3_ROOT


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w4d3 import write_w4d3

        write_w4d3(self.profile, self.pack, self.truth)
        self.gold = gold(self.profile)
        self.work = root / "work"
        shutil.copytree(W4D3_ROOT / "work", self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _slo(self) -> list[str]:
        from alwaha.check.slo_w4 import slo_problems

        return slo_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _surge(self) -> list[str]:
        from alwaha.check.surge_w4 import surge_problems

        return surge_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
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
        shutil.copy(W4D3_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        self.assertEqual(self._slo(), [])
        self.assertEqual(self._surge(), [])

    def test_shell_adapters_load_the_lookalike(self) -> None:
        self._swap("adapters.py")
        problems = self._slo()
        self.assertEqual(problems, [MISSING, UNREGISTERED])
        self._hidden(problems)
        self.assertEqual(self._surge(), [])

    def test_shell_batch_is_unbatched(self) -> None:
        self._swap("batch.py")
        slo = self._slo()
        surge = self._surge()
        self.assertEqual(slo, [BACKLOG])
        self.assertEqual(surge, [UNBATCHED])
        self._hidden(slo)
        self._hidden(surge)

    def test_shell_route_sends_the_batch_out(self) -> None:
        self._swap("route.py")
        problems = self._surge()
        self.assertEqual(problems, [EXTERNAL])
        self._hidden(problems)
        self.assertEqual(self._slo(), [])

    def test_shell_public_hits_the_gpu(self) -> None:
        self._swap("public.py")
        problems = self._surge()
        self.assertEqual(problems, [GPU])
        self._hidden(problems)
        self.assertEqual(self._slo(), [])

    def test_shell_quota_starves_chat(self) -> None:
        self._swap("quota.py")
        problems = self._slo()
        self.assertEqual(problems, [LATENCY])
        self._hidden(problems)

    def test_shell_scale_starts_at_the_peak(self) -> None:
        self._swap("scale.py")
        problems = self._slo()
        self.assertEqual(problems, [WINDOW])
        self._hidden(problems)

    def test_shell_price_uses_yesterday(self) -> None:
        self._swap("price.py")
        problems = self._slo()
        self.assertEqual(problems, [YESTERDAY])
        self._hidden(problems)

    def test_shell_capacity_omits_the_table(self) -> None:
        self._swap("capacity.py")
        problems = self._slo()
        self.assertEqual(problems, [TABLE])
        self._hidden(problems)

    def test_sprint_out_of_order_fails(self) -> None:
        (self.work / "sprint.md").write_text("# Sprint\n\nCapacity comes first.\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [SEQUENCE])
        self._hidden(problems)

    def test_an_empty_capacity_note_fails(self) -> None:
        (self.work / "capacity.md").write_text("# Capacity\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [CAPACITY])
        self._hidden(problems)

    def test_knowledge_needs_both_answers(self) -> None:
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Yes.\n2. No.\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [COLD, PUNISH])
        self._hidden(problems)

    def test_notes_miss_the_price_and_the_campaign(self) -> None:
        (self.work / "interviews" / "finance.notes.md").write_text("# finance\n\nThe budget line exists.\n", encoding="utf-8")
        (self.work / "interviews" / "bi-lead.notes.md").write_text("# bi-lead\n\nWaiting time improved.\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [FINANCE, BI])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        for problems in (self._slo(), self._surge()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
