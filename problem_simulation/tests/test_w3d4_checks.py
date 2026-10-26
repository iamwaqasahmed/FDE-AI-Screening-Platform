"""Day 4 of Week 3 evaluation checks.

Guards the evaluation checker and the judge checker.

The fixture is this day's pack plus the filled work tree. The filled copy must
pass. The optional interval and experiment modules must match the reference
rules and then may be removed. Shell swaps cover the score, the forecast, the
failure names, and the judge. Scoring the fitting window, a sprint that puts
the memo first, a thin benchmark, workshop notes that put triage in scope, a
placeholder knowledge page, and a commented evaluation gate must all fail. A
pasted watermark must fail without echoing a held span or a visit count.
"""

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
    """Catches a grader that accepts a score from the fitting window, an uncalibrated
    judge, or a workshop that treats a dot-vote as the value model.
    """
    def setUp(self) -> None:
        """Write this day's pack and copy the filled work tree."""
        # A temporary pack for the small profile. The gold comes from the generator.
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w3d4 import write_w3d4

        write_w3d4(self.profile, self.pack, self.truth)
        self.gold = gold(self.profile)
        # The filled work tree, without cached bytecode.
        self.work = root / "work"
        shutil.copytree(W3D4_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def tearDown(self) -> None:
        """Delete the temporary pack and work tree."""
        self.tmp.cleanup()

    def _eval(self) -> list[str]:
        """Run the evaluation checker."""
        from alwaha.check.eval_w3 import eval_problems

        return eval_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _judge(self) -> list[str]:
        """Run the judge checker."""
        from alwaha.check.judge_w3 import judge_problems

        return judge_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        """Fail this case when a problem list echoes the watermark, the held span or
        document, a log id, a later visit count, or a held answer.
        """
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
        """Replace one work module with the unfinished shell of the same name."""
        shutil.copy(W3D4_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        """Fails when the filled work tree still produces an evaluation problem or a judge problem."""
        self.assertEqual(self._eval(), [])
        self.assertEqual(self._judge(), [])

    def test_advanced_modules_match_and_are_optional(self) -> None:
        """Fails when the interval or experiment module disagrees with the reference rule,
        or when deleting those modules makes a passing tree fail.
        """
        intervals = load_module(self.work / "app", "intervals")
        recorded = load_module(self.work / "app", "experiment")
        self.assertEqual(intervals.bounds(8, 10), bounds(8, 10))
        self.assertEqual(recorded.report(experiment()), report(experiment()))
        for name in ("intervals.py", "experiment.py"):
            (self.work / "app" / name).unlink()
        self.assertEqual(self._eval(), [])
        self.assertEqual(self._judge(), [])

    def test_shell_score_misses_the_held_out_slice(self) -> None:
        """Fails when the unfinished score, which misses the held-out slice, is accepted,
        or when the judge checker fires for a score fault.
        """
        self._swap("score.py")
        problems = self._eval()
        self.assertEqual(problems, [EXTRACT, CITE, JOURNEY])
        self.assertEqual(self._judge(), [])
        self._hidden(problems)

    def test_shell_forecast_ignores_the_campaign(self) -> None:
        """Fails when a forecast that ignores the campaign is accepted.

        The test restores the unfinished forecast and fails unless the evaluation checker says
        the campaign was ignored, and the problem list does not echo a hidden value.
        """
        self._swap("forecast.py")
        problems = self._eval()
        self.assertEqual(problems, [IGNORE])
        self._hidden(problems)

    def test_shell_failures_misname_the_log(self) -> None:
        """Fails when a failure list that misnames the log is accepted.

        The test restores the unfinished failure list and fails unless the evaluation checker
        says a planted failure was misnamed, and the problem list does not echo a hidden value.
        """
        self._swap("failures.py")
        problems = self._eval()
        self.assertEqual(problems, [NAME])
        self._hidden(problems)

    def test_shell_judge_is_uncalibrated(self) -> None:
        """Fails when an uncalibrated judge is accepted, or when the evaluation checker
        fires for a judge fault.
        """
        self._swap("judge.py")
        problems = self._judge()
        self.assertEqual(problems, [CHECKED])
        self.assertEqual(self._eval(), [])
        self._hidden(problems)

    def test_scoring_the_fit_window_fails(self) -> None:
        """Fails when a forecast that replays the fitting window is accepted as a prediction.

        The test replaces the forecast with one that replays the fitting window and fails unless
        the evaluation checker rejects that replay, and the problem list does not echo a hidden
        value.
        """
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
        """Fails when a sprint that puts the memo first is accepted. Evaluation has to be
        sequenced, and the workshop has to stay on evidence.
        """
        (self.work / "sprint.md").write_text("# Sprint\n\nThe memo comes first.\n", encoding="utf-8")
        problems = self._eval()
        self.assertEqual(
            problems,
            ["sprint.md does not sequence the evaluation", "sprint.md does not keep the workshop on evidence"],
        )
        self._hidden(problems)

    def test_benchmark_must_name_the_failures_and_the_budgets(self) -> None:
        """Fails when a blank benchmark is accepted. It has to name each planted failure
        and each metric against its budget.
        """
        (self.work / "benchmark.md").write_text("# Benchmark\n", encoding="utf-8")
        problems = self._eval()
        self.assertEqual(
            problems,
            ["the report misses a planted failure", "the report misses a metric against its budget"],
        )
        self._hidden(problems)

    def test_workshop_notes_are_required(self) -> None:
        """Fails when workshop notes miss a seat, treat the dot-vote as the value model,
        or put triage in scope.
        """
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
        """Fails when placeholder answers are accepted in place of what a retrieval failure
        is and why a judge is calibrated.
        """
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
        """Fails when the evaluation gate is still commented out and the checker does not
        notice. The shell pipeline is copied over the filled one for this case.
        """
        target = self.work / ".github" / "workflows" / "ci.yml"
        target.write_text(
            (W3D4_APP.parent / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        problems = self._eval()
        self.assertEqual(problems, ["the evaluation gate is still commented"])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        """Fails when a file that contains only the watermark is ignored, or when a problem
        message contains the watermark.
        """
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        for problems in (self._eval(), self._judge()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
