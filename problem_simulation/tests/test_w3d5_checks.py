"""Day 5 of Week 3 checks for the second run and the rehearsal brief."""

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
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w3d5 import write_w3d5

        write_w3d5(self.profile, self.pack, self.truth)
        self.gold = gold(self.profile)
        self.work = root / "work"
        shutil.copytree(W3D5_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _eval(self) -> list[str]:
        from alwaha.check.eval_w3d5 import eval_problems

        return eval_problems(self.work, self.gold, self.profile.canary())

    def _rcp(self) -> list[str]:
        from alwaha.check.rcp_w3 import rcp_problems

        return rcp_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _readout(self) -> list[str]:
        from alwaha.check.readout_w3 import readout_problems

        return readout_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _individual(self) -> list[str]:
        from alwaha.check.individual_w3 import individual_problems

        return individual_problems(self.work, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        joined = "\n".join(problems)
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn(IN_FORCE, joined)
        self.assertNotIn(UNAUTH, joined)
        self.assertNotIn(str(self.gold["cost"]["price"]), joined)
        self.assertNotIn(str(self.gold["cost"]["budget_sar"]), joined)
        self.assertNotIn("G1", joined)

    def _swap(self, name: str) -> None:
        shutil.copy(W3D5_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        self.assertEqual(self._eval(), [])
        self.assertEqual(self._rcp(), [])
        self.assertEqual(self._readout(), [])
        self.assertEqual(self._individual(), [])

    def test_shell_repair_does_not_move_the_failure(self) -> None:
        self._swap("repair.py")
        problems = self._eval()
        self.assertEqual(problems, [REPAIR, STUCK])
        self._hidden(problems)

    def test_shell_remeasure_copies_the_first_score(self) -> None:
        self._swap("remeasure.py")
        problems = self._eval()
        self.assertEqual(problems, [STUCK])
        self._hidden(problems)

    def test_shell_cost_misses_the_price_sheet(self) -> None:
        self._swap("cost.py")
        problems = self._eval()
        self.assertEqual(problems, [COST])
        self._hidden(problems)

    def test_a_higher_wrong_score_misses_the_slice(self) -> None:
        (self.work / "app" / "remeasure.py").write_text(
            "def remeasure(rows):\n    return {'before': 0.1, 'after': 0.2}\n",
            encoding="utf-8",
        )
        problems = self._eval()
        self.assertEqual(problems, [MISS])
        self._hidden(problems)

    def test_shell_backlog_keeps_a_non_goal(self) -> None:
        self._swap("backlog.py")
        problems = self._rcp()
        self.assertEqual(problems, [BACKLOG])
        self._hidden(problems)

    def test_shell_gate_skips_the_risk_tier(self) -> None:
        self._swap("gates.py")
        problems = self._rcp()
        self.assertEqual(problems, [GATE_SKIP])
        self._hidden(problems)

    def test_shell_personal_lab_misses(self) -> None:
        self._swap("personal.py")
        problems = self._individual()
        self.assertEqual(problems, [CITE_DROP, CITE_STAFF, METRIC])
        self._hidden(problems)

    def test_sprint_out_of_order_fails(self) -> None:
        (self.work / "sprint.md").write_text("# Sprint\n\nThe spec comes first.\n", encoding="utf-8")
        problems = self._eval()
        self.assertEqual(problems, [SEQUENCE])
        self._hidden(problems)

    def test_benchmark_must_name_the_second_run(self) -> None:
        (self.work / "benchmark.md").write_text("# Benchmark\n", encoding="utf-8")
        problems = self._eval()
        self.assertEqual(problems, [PLANTED, SECOND])
        self._hidden(problems)

    def test_knowledge_needs_both_answers(self) -> None:
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Yes.\n2. No.\n", encoding="utf-8")
        problems = self._eval()
        self.assertEqual(problems, [CHANGED, SCOPE])
        self._hidden(problems)

    def test_commented_gate_fails(self) -> None:
        target = self.work / ".github" / "workflows" / "ci.yml"
        target.write_text(
            (W3D5_APP.parent / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        problems = self._eval()
        self.assertEqual(problems, [GATE])
        self._hidden(problems)

    def test_the_sponsor_sentence_fails_the_spec(self) -> None:
        (self.work / "rcp" / "requirements.md").write_text(
            "# Requirements\n\n## Scope\n\nThe virtual front desk, including triage, goes live before Ramadan.\n",
            encoding="utf-8",
        )
        problems = self._rcp()
        self.assertEqual(problems, [SPONSOR, TRIAGE, BRIEF])
        self._hidden(problems)

    def test_a_dot_vote_priority_fails(self) -> None:
        text = (self.work / "rcp" / "requirements.md").read_text(encoding="utf-8")
        text = text.replace("That ranking is not the value model. ", "")
        (self.work / "rcp" / "requirements.md").write_text(text, encoding="utf-8")
        problems = self._rcp()
        self.assertIn(DOT, problems)
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        for problems in (self._eval(), self._rcp(), self._readout(), self._individual()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
