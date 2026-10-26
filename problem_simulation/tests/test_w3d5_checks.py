"""Day 5 of Week 3 checks for the second run and the rehearsal brief.

Guards the second-run checker, the rehearsal spec, the readout, and the
individual lab.

The fixture is this day's pack plus the filled work tree. The filled copy must
pass. Shell swaps cover a repair that does not move, a remeasure that copies
the first score, a cost that misses the price sheet, a backlog that keeps a
non-goal, a gate that skips the risk tier, and a personal lab that misses.
A higher score that is still the wrong score must fail. Sprint order, the
second run in the benchmark, the knowledge page, the improvement gate, the
sponsor sentence, and a dot-vote priority must all fail. A pasted watermark
must fail without echoing a price or a document id.
"""

from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.eval_w3d5 import COST, MISS, REPAIR, STUCK
from alwaha.check.individual_w3 import CITE_DROP, CITE_STAFF, METRIC
from alwaha.check.notes_w3d5 import CHANGED, GATE, PLANTED, SCOPE, SECOND, SEQUENCE
from alwaha.check.rcp_w3 import BACKLOG, BRIEF, DOT, GATE_SKIP, SPONSOR, TRIAGE
from alwaha.config.profile import load
from alwaha.engagement.w3d5 import gold
from alwaha.engagement.w3d5_rows import IN_FORCE, UNAUTH
from alwaha.paths import W3D5_APP, W3D5_WORK


class CheckTests(unittest.TestCase):
    """Catches a grader that accepts a stuck score, a spec that follows the sponsor
    sentence, or a priority taken from a dot-vote.
    """
    def setUp(self) -> None:
        """Write this day's pack and copy the filled work tree."""
        # A temporary pack for the small profile. The gold comes from the generator.
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w3d5 import write_w3d5

        write_w3d5(self.profile, self.pack, self.truth)
        self.gold = gold(self.profile)
        # The filled work tree, without cached bytecode.
        self.work = root / "work"
        shutil.copytree(W3D5_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def tearDown(self) -> None:
        """Delete the temporary pack and work tree."""
        self.tmp.cleanup()

    def _eval(self) -> list[str]:
        """Run the second-run checker."""
        from alwaha.check.eval_w3d5 import eval_problems

        return eval_problems(self.work, self.gold, self.profile.canary())

    def _rcp(self) -> list[str]:
        """Run the rehearsal-spec checker."""
        from alwaha.check.rcp_w3 import rcp_problems

        return rcp_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _readout(self) -> list[str]:
        """Run the readout checker."""
        from alwaha.check.readout_w3 import readout_problems

        return readout_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _individual(self) -> list[str]:
        """Run the individual lab checker."""
        from alwaha.check.individual_w3 import individual_problems

        return individual_problems(self.work, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        """Fail this case when a problem list echoes the watermark, an in-force or
        unauthorized document id, a price, a budget figure, or a gate name.
        """
        joined = "\n".join(problems)
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn(IN_FORCE, joined)
        self.assertNotIn(UNAUTH, joined)
        self.assertNotIn(str(self.gold["cost"]["price"]), joined)
        self.assertNotIn(str(self.gold["cost"]["budget_sar"]), joined)
        self.assertNotIn("G1", joined)

    def _swap(self, name: str) -> None:
        """Replace one work module with the unfinished shell of the same name."""
        shutil.copy(W3D5_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        """Fails when the filled work tree still produces a second-run, spec, readout, or
        individual problem.
        """
        self.assertEqual(self._eval(), [])
        self.assertEqual(self._rcp(), [])
        self.assertEqual(self._readout(), [])
        self.assertEqual(self._individual(), [])

    def test_shell_repair_does_not_move_the_failure(self) -> None:
        """Fails when a repair that leaves the failure in place is accepted. The score
        should also look stuck.
        """
        self._swap("repair.py")
        problems = self._eval()
        self.assertEqual(problems, [REPAIR, STUCK])
        self._hidden(problems)

    def test_shell_remeasure_copies_the_first_score(self) -> None:
        """Fails when a remeasure that copies the first score is accepted.

        The test restores the unfinished remeasure and fails unless the second-run checker says
        the retrieval failure did not move, and the problem list does not echo a hidden value.
        """
        self._swap("remeasure.py")
        problems = self._eval()
        self.assertEqual(problems, [STUCK])
        self._hidden(problems)

    def test_shell_cost_misses_the_price_sheet(self) -> None:
        """Fails when a cost that ignores the price sheet is accepted.

        The test restores the unfinished cost module and fails unless the second-run checker
        says the price sheet was missed, and the problem list does not echo a hidden value.
        """
        self._swap("cost.py")
        problems = self._eval()
        self.assertEqual(problems, [COST])
        self._hidden(problems)

    def test_a_higher_wrong_score_misses_the_slice(self) -> None:
        """Fails when a second score that went up, but is not the real measurement, is
        accepted. Movement alone is not a pass.
        """
        (self.work / "app" / "remeasure.py").write_text(
            "def remeasure(rows):\n    return {'before': 0.1, 'after': 0.2}\n",
            encoding="utf-8",
        )
        problems = self._eval()
        self.assertEqual(problems, [MISS])
        self._hidden(problems)

    def test_shell_backlog_keeps_a_non_goal(self) -> None:
        """Fails when a backlog that keeps a non-goal is accepted.

        The test restores the unfinished backlog and fails unless the rehearsal-spec checker
        says a non-goal remains, and the problem list does not echo a hidden value.
        """
        self._swap("backlog.py")
        problems = self._rcp()
        self.assertEqual(problems, [BACKLOG])
        self._hidden(problems)

    def test_shell_gate_skips_the_risk_tier(self) -> None:
        """Fails when a gate that skips the risk tier is accepted.

        The test restores the unfinished gate and fails unless the rehearsal-spec checker says
        the risk tier was skipped, and the problem list does not echo a hidden value.
        """
        self._swap("gates.py")
        problems = self._rcp()
        self.assertEqual(problems, [GATE_SKIP])
        self._hidden(problems)

    def test_shell_personal_lab_misses(self) -> None:
        """Fails when the unfinished personal lab is accepted. It drops a citation, shows
        a staff document, and misses the metric.
        """
        self._swap("personal.py")
        problems = self._individual()
        self.assertEqual(problems, [CITE_DROP, CITE_STAFF, METRIC])
        self._hidden(problems)

    def test_sprint_out_of_order_fails(self) -> None:
        """Fails when a sprint that puts the spec first is accepted.

        The test writes a sprint that puts the spec first and fails unless the second-run
        checker wants the fix before the spec, and the problem list does not echo a hidden
        value.
        """
        (self.work / "sprint.md").write_text("# Sprint\n\nThe spec comes first.\n", encoding="utf-8")
        problems = self._eval()
        self.assertEqual(problems, [SEQUENCE])
        self._hidden(problems)

    def test_benchmark_must_name_the_second_run(self) -> None:
        """Fails when a blank benchmark is accepted. It has to name the planted failure
        and the second run.
        """
        (self.work / "benchmark.md").write_text("# Benchmark\n", encoding="utf-8")
        problems = self._eval()
        self.assertEqual(problems, [PLANTED, SECOND])
        self._hidden(problems)

    def test_knowledge_needs_both_answers(self) -> None:
        """Fails when placeholder answers are accepted in place of what changed and what
        stays out of scope.
        """
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Yes.\n2. No.\n", encoding="utf-8")
        problems = self._eval()
        self.assertEqual(problems, [CHANGED, SCOPE])
        self._hidden(problems)

    def test_commented_gate_fails(self) -> None:
        """Fails when the improvement gate is still commented out. The shell pipeline is
        copied over the filled one for this case.
        """
        target = self.work / ".github" / "workflows" / "ci.yml"
        target.write_text(
            (W3D5_APP.parent / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        problems = self._eval()
        self.assertEqual(problems, [GATE])
        self._hidden(problems)

    def test_the_sponsor_sentence_fails_the_spec(self) -> None:
        """Fails when requirements that open with the sponsor's go-live sentence are
        accepted. That sentence pulls triage into scope and drops the brief.
        """
        (self.work / "rcp" / "requirements.md").write_text(
            "# Requirements\n\n## Scope\n\nThe virtual front desk, including triage, goes live before Ramadan.\n",
            encoding="utf-8",
        )
        problems = self._rcp()
        self.assertEqual(problems, [SPONSOR, TRIAGE, BRIEF])
        self._hidden(problems)

    def test_a_dot_vote_priority_fails(self) -> None:
        """Fails when removing the line that separates the ranking from the value model
        is accepted. A dot-vote is not the priority.
        """
        text = (self.work / "rcp" / "requirements.md").read_text(encoding="utf-8")
        text = text.replace("That ranking is not the value model. ", "")
        (self.work / "rcp" / "requirements.md").write_text(text, encoding="utf-8")
        problems = self._rcp()
        self.assertIn(DOT, problems)
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        """Fails when a file that contains only the watermark is ignored by any checker,
        or when a problem message contains the watermark.
        """
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        for problems in (self._eval(), self._rcp(), self._readout(), self._individual()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
