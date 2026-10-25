"""Day 2 of Week 4 checks for the incident and the hours cache."""

from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.cache_w4 import OLD
from alwaha.check.incident_w4 import COST, PROMOTE, RATE, SHADOW, TRACE, UNNAMED
from alwaha.check.notes_w4d2 import ALERT, CISO, CPU, DRIFTS, EVENT, REP, RUNBOOK, SEQUENCE, TIMELINE
from alwaha.config.profile import load
from alwaha.engagement.w4d2 import gold
from alwaha.paths import W4D2_APP, W4D2_WORK


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w4d2 import write_w4d2

        write_w4d2(self.profile, self.pack, self.truth)
        self.gold = gold(self.profile)
        self.work = root / "work"
        shutil.copytree(W4D2_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _incident(self) -> list[str]:
        from alwaha.check.incident_w4 import incident_problems

        return incident_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _cache(self) -> list[str]:
        from alwaha.check.cache_w4 import cache_problems

        return cache_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        joined = "\n".join(problems)
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn(self.gold["alert_at"], joined)
        self.assertNotIn(self.gold["first_error"], joined)
        self.assertNotIn(self.gold["demo"]["hash"], joined)
        self.assertNotIn(self.gold["shadow_hash"], joined)
        self.assertNotIn(self.gold["demo"]["detail"], joined)
        self.assertNotIn(self.gold["old_hours"], joined)
        self.assertNotIn(f"{self.gold['override']:.6f}", joined)
        for amount in self.gold["cost"].values():
            self.assertNotIn(str(amount), joined)

    def _swap(self, name: str) -> None:
        shutil.copy(W4D2_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        self.assertEqual(self._incident(), [])
        self.assertEqual(self._cache(), [])

    def test_shell_spans_drop_the_trace(self) -> None:
        self._swap("spans.py")
        problems = self._incident()
        self.assertEqual(problems, [TRACE])
        self._hidden(problems)

    def test_shell_dashboard_reports_cpu(self) -> None:
        self._swap("dashboard.py")
        problems = self._incident()
        self.assertEqual(problems, [CPU, ALERT])
        self._hidden(problems)

    def test_shell_meter_drops_a_hospital(self) -> None:
        self._swap("meter.py")
        problems = self._incident()
        self.assertEqual(problems, [COST])
        self._hidden(problems)

    def test_shell_drift_names_one_row(self) -> None:
        self._swap("drift.py")
        problems = self._incident()
        self.assertEqual(problems, [UNNAMED])
        self._hidden(problems)

    def test_shell_override_returns_zero(self) -> None:
        self._swap("override.py")
        problems = self._incident()
        self.assertEqual(problems, [RATE])
        self._hidden(problems)

    def test_shell_shadow_changes_the_reply(self) -> None:
        self._swap("shadow.py")
        problems = self._incident()
        self.assertEqual(problems, [SHADOW, PROMOTE])
        self._hidden(problems)

    def test_shell_cache_keeps_the_old_hours(self) -> None:
        self._swap("cache.py")
        problems = self._cache()
        self.assertEqual(problems, [OLD])
        self._hidden(problems)
        self.assertEqual(self._incident(), [])

    def test_sprint_out_of_order_fails(self) -> None:
        (self.work / "sprint.md").write_text("# Sprint\n\nShadow comes first.\n", encoding="utf-8")
        problems = self._incident()
        self.assertEqual(problems, [SEQUENCE])
        self._hidden(problems)

    def test_an_empty_runbook_fails(self) -> None:
        (self.work / "runbook.md").write_text("# tpl-runbook\n", encoding="utf-8")
        problems = self._incident()
        self.assertEqual(problems, [RUNBOOK])
        self._hidden(problems)

    def test_a_blank_timeline_fails(self) -> None:
        (self.work / "timeline.md").write_text("# Timeline\n\nCPU was flat.\n", encoding="utf-8")
        problems = self._incident()
        self.assertEqual(problems, [TIMELINE])
        self._hidden(problems)

    def test_knowledge_needs_both_answers(self) -> None:
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Yes.\n2. No.\n", encoding="utf-8")
        problems = self._incident()
        self.assertEqual(problems, [DRIFTS, EVENT])
        self._hidden(problems)

    def test_notes_miss_the_replay_and_the_hours(self) -> None:
        (self.work / "interviews" / "ciso.notes.md").write_text("# ciso\n\nThe checklist exists.\n", encoding="utf-8")
        (self.work / "interviews" / "patient-rep.notes.md").write_text("# patient-rep\n\nThe phone line is busy.\n", encoding="utf-8")
        problems = self._incident()
        self.assertEqual(problems, [CISO, REP])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        for problems in (self._incident(), self._cache()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
