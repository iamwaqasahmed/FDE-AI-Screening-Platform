"""Day 2 of Week 4 checks for the incident and the hours cache.

Guards the incident checker and the hours-cache checker.

The fixture is this day's pack plus the filled work tree. The filled copy must
pass. Shell swaps cover spans, the dashboard, the meter, drift, the override
rate, the shadow reply, and the hours cache. A sprint that puts shadow first,
an empty runbook, a timeline that only mentions the processor, placeholder
knowledge, and notes that miss the replay and the hours must all fail. Problem
text must not echo the watermark, the times, the hashes, the old hours, the
override rate, or a cost amount.
"""

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
    """Catches a grader that accepts a trace with no span, a cache that keeps the old
    hours, or a shadow reply that changed the answer.
    """
    def setUp(self) -> None:
        """Write this day's pack and copy the filled work tree."""
        # A temporary pack for the small profile. The gold comes from the generator.
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w4d2 import write_w4d2

        write_w4d2(self.profile, self.pack, self.truth)
        self.gold = gold(self.profile)
        # The filled work tree, without cached bytecode.
        self.work = root / "work"
        shutil.copytree(W4D2_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def tearDown(self) -> None:
        """Delete the temporary pack and work tree."""
        self.tmp.cleanup()

    def _incident(self) -> list[str]:
        """Run the incident checker."""
        from alwaha.check.incident_w4 import incident_problems

        return incident_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _cache(self) -> list[str]:
        """Run the hours-cache checker."""
        from alwaha.check.cache_w4 import cache_problems

        return cache_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        """Fail this case when a problem list echoes the watermark, a time, a hash, the
        trace detail, the old hours, the override rate, or a cost amount.
        """
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
        """Replace one work module with the unfinished shell of the same name."""
        shutil.copy(W4D2_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        """Fails when the filled work tree still produces an incident problem or a cache problem."""
        self.assertEqual(self._incident(), [])
        self.assertEqual(self._cache(), [])

    def test_shell_spans_drop_the_trace(self) -> None:
        """Fails when spans that drop the trace are accepted."""
        self._swap("spans.py")
        problems = self._incident()
        self.assertEqual(problems, [TRACE])
        self._hidden(problems)

    def test_shell_dashboard_reports_cpu(self) -> None:
        """Fails when a dashboard that reports the processor, and so misses the alert, is
        accepted.
        """
        self._swap("dashboard.py")
        problems = self._incident()
        self.assertEqual(problems, [CPU, ALERT])
        self._hidden(problems)

    def test_shell_meter_drops_a_hospital(self) -> None:
        """Fails when a meter that drops a hospital's cost is accepted."""
        self._swap("meter.py")
        problems = self._incident()
        self.assertEqual(problems, [COST])
        self._hidden(problems)

    def test_shell_drift_names_one_row(self) -> None:
        """Fails when drift that names only one row is accepted. Every drifted row has to
        be named.
        """
        self._swap("drift.py")
        problems = self._incident()
        self.assertEqual(problems, [UNNAMED])
        self._hidden(problems)

    def test_shell_override_returns_zero(self) -> None:
        """Fails when an override rate that collapses to nothing is accepted."""
        self._swap("override.py")
        problems = self._incident()
        self.assertEqual(problems, [RATE])
        self._hidden(problems)

    def test_shell_shadow_changes_the_reply(self) -> None:
        """Fails when a shadow run that changes the reply, or that gets promoted, is accepted."""
        self._swap("shadow.py")
        problems = self._incident()
        self.assertEqual(problems, [SHADOW, PROMOTE])
        self._hidden(problems)

    def test_shell_cache_keeps_the_old_hours(self) -> None:
        """Fails when a cache that keeps the old hours is accepted. The incident checker
        should stay quiet, because this fault belongs to the cache.
        """
        self._swap("cache.py")
        problems = self._cache()
        self.assertEqual(problems, [OLD])
        self._hidden(problems)
        self.assertEqual(self._incident(), [])

    def test_sprint_out_of_order_fails(self) -> None:
        """Fails when a sprint that puts the shadow run first is accepted."""
        (self.work / "sprint.md").write_text("# Sprint\n\nShadow comes first.\n", encoding="utf-8")
        problems = self._incident()
        self.assertEqual(problems, [SEQUENCE])
        self._hidden(problems)

    def test_an_empty_runbook_fails(self) -> None:
        """Fails when an empty runbook is accepted."""
        (self.work / "runbook.md").write_text("# tpl-runbook\n", encoding="utf-8")
        problems = self._incident()
        self.assertEqual(problems, [RUNBOOK])
        self._hidden(problems)

    def test_a_blank_timeline_fails(self) -> None:
        """Fails when a timeline that only says the processor was flat is accepted. The
        replay has to be on the page.
        """
        (self.work / "timeline.md").write_text("# Timeline\n\nCPU was flat.\n", encoding="utf-8")
        problems = self._incident()
        self.assertEqual(problems, [TIMELINE])
        self._hidden(problems)

    def test_knowledge_needs_both_answers(self) -> None:
        """Fails when placeholder answers are accepted in place of what drifts and which
        event invalidates the cache.
        """
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Yes.\n2. No.\n", encoding="utf-8")
        problems = self._incident()
        self.assertEqual(problems, [DRIFTS, EVENT])
        self._hidden(problems)

    def test_notes_miss_the_replay_and_the_hours(self) -> None:
        """Fails when the security note misses the replay or the patient note misses the
        hours. The leftover sentences are true and still not enough.
        """
        (self.work / "interviews" / "ciso.notes.md").write_text("# ciso\n\nThe checklist exists.\n", encoding="utf-8")
        (self.work / "interviews" / "patient-rep.notes.md").write_text("# patient-rep\n\nThe phone line is busy.\n", encoding="utf-8")
        problems = self._incident()
        self.assertEqual(problems, [CISO, REP])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        """Fails when a file that contains only the watermark is ignored, or when a problem
        message contains the watermark.
        """
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        for problems in (self._incident(), self._cache()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
