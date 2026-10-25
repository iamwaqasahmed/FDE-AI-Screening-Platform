"""Day 4 of Week 3 evaluation checks."""

from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.eval_w3 import CITE, EXTRACT, FIT, IGNORE, JOURNEY, NAME
from alwaha.check.judge_w3 import CHECKED
from alwaha.check.load_app import load_module
from alwaha.config.profile import load
from alwaha.engagement.w3d4 import gold
from alwaha.engagement.w3d4_judge import HELD_DOC, HELD_SPAN
from alwaha.engagement.w3d4_pages import experiment
from alwaha.engagement.w3d4_rules import bounds, report
from alwaha.paths import W3D4_APP, W3D4_WORK


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w3d4 import write_w3d4

        write_w3d4(self.profile, self.pack, self.truth)
        self.gold = gold(self.profile)
        self.work = root / "work"
        shutil.copytree(W3D4_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _eval(self) -> list[str]:
        from alwaha.check.eval_w3 import eval_problems

        return eval_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _judge(self) -> list[str]:
        from alwaha.check.judge_w3 import judge_problems

        return judge_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        joined = "\n".join(problems)
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn(HELD_SPAN, joined)
        self.assertNotIn(HELD_DOC, joined)
        for row in self.gold["failures"]:
            self.assertNotIn(row["log_id"], joined)
        for row in self.gold["later_visits"]:
            self.assertNotIn(str(row["visits"]), joined)
        for row in self.gold["calibration_held"]:
            self.assertNotIn(row["answer"], joined)

    def _swap(self, name: str) -> None:
        shutil.copy(W3D4_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        self.assertEqual(self._eval(), [])
        self.assertEqual(self._judge(), [])

    def test_advanced_modules_match_and_are_optional(self) -> None:
        intervals = load_module(self.work / "app", "intervals")
        recorded = load_module(self.work / "app", "experiment")
        self.assertEqual(intervals.bounds(8, 10), bounds(8, 10))
        self.assertEqual(recorded.report(experiment()), report(experiment()))
        for name in ("intervals.py", "experiment.py"):
            (self.work / "app" / name).unlink()
        self.assertEqual(self._eval(), [])
        self.assertEqual(self._judge(), [])

    def test_shell_score_misses_the_held_out_slice(self) -> None:
        self._swap("score.py")
        problems = self._eval()
        self.assertEqual(problems, [EXTRACT, CITE, JOURNEY])
        self.assertEqual(self._judge(), [])
        self._hidden(problems)

    def test_shell_forecast_ignores_the_campaign(self) -> None:
        self._swap("forecast.py")
        problems = self._eval()
        self.assertEqual(problems, [IGNORE])
        self._hidden(problems)

    def test_shell_failures_misname_the_log(self) -> None:
        self._swap("failures.py")
        problems = self._eval()
        self.assertEqual(problems, [NAME])
        self._hidden(problems)

    def test_shell_judge_is_uncalibrated(self) -> None:
        self._swap("judge.py")
        problems = self._judge()
        self.assertEqual(problems, [CHECKED])
        self.assertEqual(self._eval(), [])
        self._hidden(problems)

    def test_scoring_the_fit_window_fails(self) -> None:
        (self.work / "app" / "forecast.py").write_text(
            "def predict(rows):\n"
            "    chosen = []\n"
            "    for row in rows:\n"
            "        if int(row['year']) == 2026 and int(row['month']) in (2, 3):\n"
            "            chosen.append({'district': row['district'], 'month': int(row['month']), 'visits': int(row['visits']), 'year': 2026})\n"
            "    return chosen\n",
            encoding="utf-8",
        )
        problems = self._eval()
        self.assertEqual(problems, [FIT])
        self._hidden(problems)

    def test_sprint_out_of_order_fails(self) -> None:
        (self.work / "sprint.md").write_text("# Sprint\n\nThe memo comes first.\n", encoding="utf-8")
        problems = self._eval()
        self.assertEqual(
            problems,
            ["sprint.md does not sequence the evaluation", "sprint.md does not keep the workshop on evidence"],
        )
        self._hidden(problems)

    def test_benchmark_must_name_the_failures_and_the_budgets(self) -> None:
        (self.work / "benchmark.md").write_text("# Benchmark\n", encoding="utf-8")
        problems = self._eval()
        self.assertEqual(
            problems,
            ["the report misses a planted failure", "the report misses a metric against its budget"],
        )
        self._hidden(problems)

    def test_workshop_notes_are_required(self) -> None:
        (self.work / "workshop.md").write_text("# Workshop\n\nTriage is in scope.\n", encoding="utf-8")
        problems = self._eval()
        self.assertEqual(
            problems,
            [
                "the workshop notes miss a seat",
                "the workshop notes treat the dot-vote as the value model",
                "the workshop notes put triage in scope",
            ],
        )
        self._hidden(problems)

    def test_knowledge_needs_both_answers(self) -> None:
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Yes.\n2. No.\n", encoding="utf-8")
        problems = self._eval()
        self.assertEqual(
            problems,
            [
                "knowledge.md does not say what a retrieval failure is",
                "knowledge.md does not say why a judge is calibrated",
            ],
        )
        self._hidden(problems)

    def test_commented_gate_fails(self) -> None:
        target = self.work / ".github" / "workflows" / "ci.yml"
        target.write_text(
            (W3D4_APP.parent / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        problems = self._eval()
        self.assertEqual(problems, ["the evaluation gate is still commented"])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        for problems in (self._eval(), self._judge()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
