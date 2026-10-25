"""Day 4 of Week 4 checks for failover and the rent-versus-buy draft."""

from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.failover_w4 import (
    CLOSED,
    DROPPED,
    HASH,
    ONE,
    PARTNER,
    PURCHASE,
    SERVING,
    SPLIT,
    TIME,
    WAIT,
)
from alwaha.check.notes_w4d4 import ARCH, EA, FAILOVER, FINANCE, MODEL, RENT, SEQUENCE
from alwaha.config.profile import load
from alwaha.engagement.w4d4 import gold
from alwaha.paths import W4D4_APP, W4D4_WORK


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w4d4 import write_w4d4

        write_w4d4(self.profile, self.pack, self.truth)
        self.gold = gold(self.profile)
        self.work = root / "work"
        shutil.copytree(W4D4_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _slo(self) -> list[str]:
        from alwaha.check.failover_w4 import failover_problems

        return failover_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        joined = "\n".join(problems)
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn(self.gold["lookalike_hash"], joined)
        self.assertNotIn(self.gold["buy_arrives"], joined)
        self.assertNotIn(self.gold["rent_arrives"], joined)
        self.assertNotIn(self.gold["deadline"], joined)
        for key in ("budget_seconds", "timeout_seconds", "rent_days", "local_sar"):
            self.assertNotIn(str(self.gold[key]), joined)
        for value in self.gold["hospital_sar"].values():
            self.assertNotIn(str(value), joined)

    def _swap(self, name: str) -> None:
        shutil.copy(W4D4_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        self.assertEqual(self._slo(), [])

    def test_shell_replicas_place_one_site(self) -> None:
        self._swap("replicas.py")
        problems = self._slo()
        self.assertEqual(problems, [ONE])
        self._hidden(problems)

    def test_shell_route_stays_on_site_a(self) -> None:
        self._swap("route.py")
        problems = self._slo()
        self.assertEqual(problems, [SERVING])
        self._hidden(problems)

    def test_shell_failover_drops_the_store(self) -> None:
        self._swap("failover.py")
        problems = self._slo()
        self.assertEqual(problems, [SERVING, TIME, DROPPED])
        self._hidden(problems)

    def test_shell_hashes_keep_the_lookalike(self) -> None:
        self._swap("hashes.py")
        problems = self._slo()
        self.assertEqual(problems, [HASH])
        self._hidden(problems)

    def test_shell_breaker_waits_on_insure(self) -> None:
        self._swap("breaker.py")
        problems = self._slo()
        self.assertEqual(problems, [WAIT, PARTNER])
        self._hidden(problems)

    def test_shell_degrade_fails_closed(self) -> None:
        self._swap("degrade.py")
        problems = self._slo()
        self.assertEqual(problems, [CLOSED])
        self._hidden(problems)

    def test_shell_procure_buys(self) -> None:
        self._swap("procure.py")
        problems = self._slo()
        self.assertEqual(problems, [PURCHASE])
        self._hidden(problems)

    def test_shell_hospitals_use_one_figure(self) -> None:
        self._swap("hospitals.py")
        problems = self._slo()
        self.assertEqual(problems, [SPLIT])
        self._hidden(problems)

    def test_sprint_out_of_order_fails(self) -> None:
        (self.work / "sprint.md").write_text("# Sprint\n\nThe trade-off comes first.\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [SEQUENCE])
        self._hidden(problems)

    def test_an_empty_failover_note_fails(self) -> None:
        (self.work / "failover.md").write_text("# Failover\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [FAILOVER])
        self._hidden(problems)

    def test_an_empty_architecture_draft_fails(self) -> None:
        (self.work / "architecture.md").write_text("# Architecture\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [ARCH])
        self._hidden(problems)

    def test_knowledge_needs_both_answers(self) -> None:
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Yes.\n2. No.\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [MODEL, RENT])
        self._hidden(problems)

    def test_notes_miss_the_site_and_the_lead_time(self) -> None:
        (self.work / "interviews" / "ea.notes.md").write_text("# ea\n\nWe have an API strategy.\n", encoding="utf-8")
        (self.work / "interviews" / "finance.notes.md").write_text("# finance\n\nThe budget line exists.\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [EA, FINANCE])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [WATERMARK])
        self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
