"""Day 1 of Week 4 checks for guardrails, privacy, access, and fairness."""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.access_w4 import CHECKLIST, DELEGATE, GLASS, STALE
from alwaha.check.agent_run import WATERMARK
from alwaha.check.fair_w4 import HIDES, OUTSIDE, STAMP
from alwaha.check.notes_w4d1 import AGENCY, CLOCK, CLOCK_K, DPIA, FAMILY, SEQUENCE
from alwaha.check.privacy_w4 import EXPORT, INDEX, LOGS, MEMORY
from alwaha.check.redteam_w4 import AGENCY as BOOKING
from alwaha.check.redteam_w4 import EMBED, HASH, HOLD, HTML, LEAK, LETTER, MISINFO, POISON, PROMPT, TOKEN, TOOL
from alwaha.config.profile import load
from alwaha.engagement.w2d4 import national_id
from alwaha.engagement.w4d1 import gold
from alwaha.engagement.w4d1_rows import CASE_AT
from alwaha.paths import W4D1_APP, W4D1_WORK


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.w4d1 import write_w4d1

        write_w4d1(self.profile, self.pack, self.truth)
        self.gold = gold(self.profile)
        self.work = root / "work"
        shutil.copytree(W4D1_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _redteam(self) -> list[str]:
        from alwaha.check.redteam_w4 import redteam_problems

        return redteam_problems(self.work, self.pack, self.gold, self.profile.canary(), self.profile)

    def _privacy(self) -> list[str]:
        from alwaha.check.privacy_w4 import privacy_problems

        return privacy_problems(self.work, self.gold, self.profile.canary())

    def _access(self) -> list[str]:
        from alwaha.check.access_w4 import access_problems

        return access_problems(self.work, self.gold, self.profile.canary())

    def _fair(self) -> list[str]:
        from alwaha.check.fair_w4 import fair_problems

        return fair_problems(self.work, self.pack, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        joined = "\n".join(problems)
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn(national_id(self.profile), joined)
        self.assertNotIn(self.gold["lookalike"], joined)
        self.assertNotIn(CASE_AT, joined)
        self.assertNotIn("CHG-2025-118", joined)
        self.assertNotIn("circ-hours-old", joined)
        self.assertNotIn("hid-prompt", joined)

    def _swap(self, name: str) -> None:
        shutil.copy(W4D1_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        self.assertEqual(self._redteam(), [])
        self.assertEqual(self._privacy(), [])
        self.assertEqual(self._access(), [])
        self.assertEqual(self._fair(), [])

    def test_shell_guard_lets_the_letter_book(self) -> None:
        self._swap("guard.py")
        problems = self._redteam()
        self.assertEqual(problems, [LETTER, PROMPT, BOOKING])
        self._hidden(problems)

    def test_shell_output_renders_html(self) -> None:
        self._swap("output.py")
        problems = self._redteam()
        self.assertEqual(problems, [HTML])
        self._hidden(problems)

    def test_shell_supply_loads_the_lookalike(self) -> None:
        self._swap("supply.py")
        problems = self._redteam()
        self.assertEqual(problems, [HASH, TOOL, POISON, EMBED, MISINFO])
        self._hidden(problems)

    def test_shell_redact_keeps_the_line(self) -> None:
        self._swap("redact.py")
        problems = self._redteam()
        self.assertEqual(problems, [LEAK])
        self._hidden(problems)

    def test_shell_limit_admits_the_loop(self) -> None:
        self._swap("limit.py")
        problems = self._redteam()
        self.assertEqual(problems, [TOKEN, HOLD])
        self._hidden(problems)

    def test_a_direct_only_config_misses_a_family(self) -> None:
        payload = json.loads((self.work / "guardrails.json").read_text(encoding="utf-8"))
        payload["families"] = ["atk-direct"]
        (self.work / "guardrails.json").write_text(json.dumps(payload), encoding="utf-8")
        problems = self._redteam()
        self.assertEqual(problems, [FAMILY])
        self._hidden(problems)

    def test_shell_erase_leaves_the_index(self) -> None:
        self._swap("erase.py")
        problems = self._privacy()
        self.assertEqual(problems, [EXPORT, INDEX, MEMORY, LOGS])
        self._hidden(problems)

    def test_shell_access_leaves_the_stale_grant(self) -> None:
        self._swap("access.py")
        problems = self._access()
        self.assertEqual(problems, [STALE, DELEGATE, GLASS, CHECKLIST])
        self._hidden(problems)

    def test_shell_fair_hides_the_slices(self) -> None:
        self._swap("fair.py")
        problems = self._fair()
        self.assertEqual(problems, [HIDES, STAMP])
        self._hidden(problems)

    def test_a_gap_over_the_bound_fails(self) -> None:
        (self.work / "app" / "fair.py").write_text(
            "def gap(rows):\n    return 1.0\n\ndef stamp_rate(rows):\n    return 0.0\n",
            encoding="utf-8",
        )
        problems = self._fair()
        self.assertEqual(problems, [OUTSIDE, STAMP])
        self._hidden(problems)

    def test_sprint_out_of_order_fails(self) -> None:
        (self.work / "sprint.md").write_text("# Sprint\n\nThe request comes first.\n", encoding="utf-8")
        problems = self._privacy()
        self.assertEqual(problems, [SEQUENCE])
        self._hidden(problems)

    def test_an_empty_dpia_fails(self) -> None:
        (self.work / "dpia.md").write_text("# tpl-dpia\n", encoding="utf-8")
        problems = self._privacy()
        self.assertEqual(problems, [DPIA])
        self._hidden(problems)

    def test_knowledge_needs_both_answers(self) -> None:
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Yes.\n2. No.\n", encoding="utf-8")
        problems = self._privacy()
        self.assertEqual(problems, [CLOCK_K, AGENCY])
        self._hidden(problems)

    def test_a_model_clock_fails(self) -> None:
        (self.work / "breach.md").write_text("# Breach\n\nThe clock starts at the model.\n", encoding="utf-8")
        problems = self._privacy()
        self.assertEqual(problems, [CLOCK])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        for problems in (self._redteam(), self._privacy(), self._access(), self._fair()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
