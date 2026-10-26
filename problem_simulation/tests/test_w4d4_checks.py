"""Day 4 of Week 4 checks for failover and the rent-versus-buy draft.

Guards the failover checker and the rent-versus-buy draft.

The fixture is this day's pack plus the filled work tree. The filled copy must
pass. Shell swaps cover replicas, routing, failover, hashes, the breaker, the
degraded mode, procurement, and the hospital split. A sprint that puts the
trade-off first, an empty failover note, an empty architecture draft,
placeholder knowledge, and notes that miss the site and the lead time must all
fail. Problem text must not echo the watermark, the lookalike, the dates, or
a spend figure.
"""

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
    """Catches a grader that stays on the killed site, buys instead of renting, or
    uses one spend figure for every hospital.
    """
    def setUp(self) -> None:
        """Write this day's pack and copy the filled work tree."""
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
        """Delete the temporary pack and work tree."""
        self.tmp.cleanup()

    def _slo(self) -> list[str]:
        """Run the failover checker. The name is historical. The checker covers the drill
        and the rent-versus-buy draft together.
        """
        from alwaha.check.failover_w4 import failover_problems

        return failover_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        """Fail this case when a problem list echoes the watermark, the lookalike, an
        arrival or deadline date, or a spend figure.
        """
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
        """Replace one work module with the unfinished shell of the same name."""
        shutil.copy(W4D4_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        """Fails when the filled work tree still produces a failover problem."""
        self.assertEqual(self._slo(), [])

    def test_shell_replicas_place_one_site(self) -> None:
        """Fails when replicas that place only one site are accepted."""
        self._swap("replicas.py")
        problems = self._slo()
        self.assertEqual(problems, [ONE])
        self._hidden(problems)

    def test_shell_route_stays_on_site_a(self) -> None:
        """Fails when routing that stays on the killed site is accepted."""
        self._swap("route.py")
        problems = self._slo()
        self.assertEqual(problems, [SERVING])
        self._hidden(problems)

    def test_shell_failover_drops_the_store(self) -> None:
        """Fails when failover that drops the workflow store is accepted. Serving, the
        time budget, and the dropped store should all be caught.
        """
        self._swap("failover.py")
        problems = self._slo()
        self.assertEqual(problems, [SERVING, TIME, DROPPED])
        self._hidden(problems)

    def test_shell_hashes_keep_the_lookalike(self) -> None:
        """Fails when a hash pin that keeps the lookalike is accepted."""
        self._swap("hashes.py")
        problems = self._slo()
        self.assertEqual(problems, [HASH])
        self._hidden(problems)

    def test_shell_breaker_waits_on_insure(self) -> None:
        """Fails when a breaker that waits on the insurance partner is accepted."""
        self._swap("breaker.py")
        problems = self._slo()
        self.assertEqual(problems, [WAIT, PARTNER])
        self._hidden(problems)

    def test_shell_degrade_fails_closed(self) -> None:
        """Fails when a degraded mode that fails closed, instead of offering the reduced
        path, is accepted.
        """
        self._swap("degrade.py")
        problems = self._slo()
        self.assertEqual(problems, [CLOSED])
        self._hidden(problems)

    def test_shell_procure_buys(self) -> None:
        """Fails when procurement that buys, and so misses the deadline, is accepted."""
        self._swap("procure.py")
        problems = self._slo()
        self.assertEqual(problems, [PURCHASE])
        self._hidden(problems)

    def test_shell_hospitals_use_one_figure(self) -> None:
        """Fails when every hospital is given the same spend figure."""
        self._swap("hospitals.py")
        problems = self._slo()
        self.assertEqual(problems, [SPLIT])
        self._hidden(problems)

    def test_sprint_out_of_order_fails(self) -> None:
        """Fails when a sprint that puts the trade-off first is accepted."""
        (self.work / "sprint.md").write_text("# Sprint\n\nThe trade-off comes first.\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [SEQUENCE])
        self._hidden(problems)

    def test_an_empty_failover_note_fails(self) -> None:
        """Fails when an empty failover page is accepted."""
        (self.work / "failover.md").write_text("# Failover\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [FAILOVER])
        self._hidden(problems)

    def test_an_empty_architecture_draft_fails(self) -> None:
        """Fails when an empty architecture draft is accepted."""
        (self.work / "architecture.md").write_text("# Architecture\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [ARCH])
        self._hidden(problems)

    def test_knowledge_needs_both_answers(self) -> None:
        """Fails when placeholder answers are accepted in place of which model is pinned
        and why rent meets the deadline.
        """
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Yes.\n2. No.\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [MODEL, RENT])
        self._hidden(problems)

    def test_notes_miss_the_site_and_the_lead_time(self) -> None:
        """Fails when the architect note misses the site or the finance note misses the
        lead time. The leftover sentences are true and still not enough.
        """
        (self.work / "interviews" / "ea.notes.md").write_text("# ea\n\nWe have an API strategy.\n", encoding="utf-8")
        (self.work / "interviews" / "finance.notes.md").write_text("# finance\n\nThe budget line exists.\n", encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [EA, FINANCE])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        """Fails when a file that contains only the watermark is ignored, or when a problem
        message contains the watermark.
        """
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        problems = self._slo()
        self.assertEqual(problems, [WATERMARK])
        self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
