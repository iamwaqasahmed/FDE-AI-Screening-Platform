"""Module 4, Lesson 1 checks for guardrails, privacy, access, and fairness.

Guards the red-team, privacy, access, and fairness checkers.

The fixture is this day's pack plus the filled work tree. The filled copy must
pass. Shell swaps cover the guard, the output renderer, the supply pin, the
redaction, the limit, the erasure, the access decision, and the fairness report.
A config that names only one attack family, a gap forced over the bound, a
sprint that puts the request first, an empty assessment, placeholder knowledge,
and a breach clock that starts at the model must all fail. Problem text must
not echo the watermark, the national id, the lookalike, the case time, or the
hidden attack names.
"""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.access_m04_l01 import CHECKLIST, DELEGATE, GLASS, STALE
from alwaha.check.agent_run import WATERMARK
from alwaha.check.fair_m04_l01 import HIDES, OUTSIDE, STAMP
from alwaha.check.notes_m04_l01 import AGENCY, CLOCK, CLOCK_K, DPIA, FAMILY, SEQUENCE
from alwaha.check.privacy_m04_l01 import EXPORT, INDEX, LOGS, MEMORY
from alwaha.check.redteam_m04_l01 import AGENCY as BOOKING
from alwaha.check.redteam_m04_l01 import EMBED, HASH, HOLD, HTML, LEAK, LETTER, MISINFO, POISON, PROMPT, TOKEN, TOOL
from alwaha.config.profile import load
from alwaha.engagement.m02_l04 import national_id
from alwaha.engagement.m04_l01 import gold
from alwaha.engagement.m04_l01_rows import CASE_AT
from alwaha.paths import M04_L01_APP, M04_L01_WORK


class CheckTests(unittest.TestCase):
    """Catches a grader that lets a letter book, keeps a stale grant, or hides a
    fairness slice.
    """
    def setUp(self) -> None:
        """Write this day's pack and copy the filled work tree."""
        # A temporary pack for the small profile. The gold comes from the generator.
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        from alwaha.release.m04_l01 import write_m04_l01

        write_m04_l01(self.profile, self.pack, self.truth)
        self.gold = gold(self.profile)
        # The filled work tree, without cached bytecode.
        self.work = root / "work"
        shutil.copytree(M04_L01_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def tearDown(self) -> None:
        """Delete the temporary pack and work tree."""
        self.tmp.cleanup()

    def _redteam(self) -> list[str]:
        """Run the red-team checker. The profile is passed in because some attacks depend
        on its watermark and its identifiers.
        """
        from alwaha.check.redteam_m04_l01 import redteam_problems

        return redteam_problems(self.work, self.pack, self.gold, self.profile.canary(), self.profile)

    def _privacy(self) -> list[str]:
        """Run the privacy checker."""
        from alwaha.check.privacy_m04_l01 import privacy_problems

        return privacy_problems(self.work, self.gold, self.profile.canary())

    def _access(self) -> list[str]:
        """Run the access checker."""
        from alwaha.check.access_m04_l01 import access_problems

        return access_problems(self.work, self.gold, self.profile.canary())

    def _fair(self) -> list[str]:
        """Run the fairness checker."""
        from alwaha.check.fair_m04_l01 import fair_problems

        return fair_problems(self.work, self.pack, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        """Fail this case when a problem list echoes the watermark, the national id, the
        lookalike, the case time, the change id, or a hidden attack name.
        """
        joined = "\n".join(problems)
        self.assertNotIn(self.profile.canary(), joined)
        self.assertNotIn(national_id(self.profile), joined)
        self.assertNotIn(self.gold["lookalike"], joined)
        self.assertNotIn(CASE_AT, joined)
        self.assertNotIn("CHG-2025-118", joined)
        self.assertNotIn("circ-hours-old", joined)
        self.assertNotIn("hid-prompt", joined)

    def _swap(self, name: str) -> None:
        """Replace one work module with the unfinished shell of the same name."""
        shutil.copy(M04_L01_APP / name, self.work / "app" / name)

    def test_filled_work_passes(self) -> None:
        """Fails when the filled work tree still produces a red-team, privacy, access, or
        fairness problem.
        """
        self.assertEqual(self._redteam(), [])
        self.assertEqual(self._privacy(), [])
        self.assertEqual(self._access(), [])
        self.assertEqual(self._fair(), [])

    def test_shell_guard_lets_the_letter_book(self) -> None:
        """Fails when the unfinished guard is accepted. The indirect letter, the prompt
        attack, and the booking should all be caught.
        """
        self._swap("guard.py")
        problems = self._redteam()
        self.assertEqual(problems, [LETTER, PROMPT, BOOKING])
        self._hidden(problems)

    def test_shell_output_renders_html(self) -> None:
        """Fails when an output path that renders markup is accepted.

        The test restores the unfinished output path and fails unless the red-team checker says
        markup is still rendered, and the problem list does not echo a hidden value.
        """
        self._swap("output.py")
        problems = self._redteam()
        self.assertEqual(problems, [HTML])
        self._hidden(problems)

    def test_shell_supply_loads_the_lookalike(self) -> None:
        """Fails when the unfinished supply pin is accepted. The lookalike hash, the tool
        poisoning, the embedded instruction, and the false clinical claim should all
        be caught.
        """
        self._swap("supply.py")
        problems = self._redteam()
        self.assertEqual(problems, [HASH, TOOL, POISON, EMBED, MISINFO])
        self._hidden(problems)

    def test_shell_redact_keeps_the_line(self) -> None:
        """Fails when redaction that keeps the sensitive line is accepted.

        The test restores the unfinished redaction and fails unless the red-team checker says
        the sensitive line is still present, and the problem list does not echo a hidden value.
        """
        self._swap("redact.py")
        problems = self._redteam()
        self.assertEqual(problems, [LEAK])
        self._hidden(problems)

    def test_shell_limit_admits_the_loop(self) -> None:
        """Fails when a limit that admits the retry loop is accepted. Both the token burn
        and the hold should be caught.
        """
        self._swap("limit.py")
        problems = self._redteam()
        self.assertEqual(problems, [TOKEN, HOLD])
        self._hidden(problems)

    def test_a_direct_only_config_misses_a_family(self) -> None:
        """Fails when a guardrail config that names only the direct family is accepted.
        The other families have to be listed too.
        """
        payload = json.loads((self.work / "guardrails.json").read_text(encoding="utf-8"))
        payload["families"] = ["atk-direct"]
        (self.work / "guardrails.json").write_text(json.dumps(payload), encoding="utf-8")
        problems = self._redteam()
        self.assertEqual(problems, [FAMILY])
        self._hidden(problems)

    def test_shell_erase_leaves_the_index(self) -> None:
        """Fails when erasure that leaves the export, the index, the memory, or the logs
        is accepted.
        """
        self._swap("erase.py")
        problems = self._privacy()
        self.assertEqual(problems, [EXPORT, INDEX, MEMORY, LOGS])
        self._hidden(problems)

    def test_shell_access_leaves_the_stale_grant(self) -> None:
        """Fails when the unfinished access decision is accepted. A stale grant, a bad
        delegate, a glass-break hole, and a missing checklist should all be caught.
        """
        self._swap("access.py")
        problems = self._access()
        self.assertEqual(problems, [STALE, DELEGATE, GLASS, CHECKLIST])
        self._hidden(problems)

    def test_shell_fair_hides_the_slices(self) -> None:
        """Fails when a fairness report that hides the slices, or that stamps the wrong
        rate, is accepted.
        """
        self._swap("fair.py")
        problems = self._fair()
        self.assertEqual(problems, [HIDES, STAMP])
        self._hidden(problems)

    def test_a_gap_over_the_bound_fails(self) -> None:
        """Fails when a report that forces the gap over the bound, and a zero stamp rate,
        is accepted.
        """
        (self.work / "app" / "fair.py").write_text(
            "def gap(rows):\n    return 1.0\n\ndef stamp_rate(rows):\n    return 0.0\n",
            encoding="utf-8",
        )
        problems = self._fair()
        self.assertEqual(problems, [OUTSIDE, STAMP])
        self._hidden(problems)

    def test_sprint_out_of_order_fails(self) -> None:
        """Fails when a sprint that puts the request first is accepted.

        The test writes a sprint that puts the request first and fails unless the privacy
        checker wants the notice to open the sprint, and the problem list does not echo a hidden
        value.
        """
        (self.work / "sprint.md").write_text("# Sprint\n\nThe request comes first.\n", encoding="utf-8")
        problems = self._privacy()
        self.assertEqual(problems, [SEQUENCE])
        self._hidden(problems)

    def test_an_empty_dpia_fails(self) -> None:
        """Fails when an empty assessment page is accepted.

        The test writes an empty assessment page and fails unless the privacy checker says a
        required field is missing, and the problem list does not echo a hidden value.
        """
        (self.work / "dpia.md").write_text("# tpl-dpia\n", encoding="utf-8")
        problems = self._privacy()
        self.assertEqual(problems, [DPIA])
        self._hidden(problems)

    def test_knowledge_needs_both_answers(self) -> None:
        """Fails when placeholder answers are accepted in place of when the clock starts
        and what the assistant is not allowed to do.
        """
        (self.work / "knowledge.md").write_text("# Knowledge\n\n1. Yes.\n2. No.\n", encoding="utf-8")
        problems = self._privacy()
        self.assertEqual(problems, [CLOCK_K, AGENCY])
        self._hidden(problems)

    def test_a_model_clock_fails(self) -> None:
        """Fails when a breach note that starts the clock at the model, rather than at
        the incident, is accepted.
        """
        (self.work / "breach.md").write_text("# Breach\n\nThe clock starts at the model.\n", encoding="utf-8")
        problems = self._privacy()
        self.assertEqual(problems, [CLOCK])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        """Fails when a file that contains only the watermark is ignored by any checker,
        or when a problem message contains the watermark.
        """
        (self.work / "note.txt").write_text(self.profile.canary(), encoding="utf-8")
        for problems in (self._redteam(), self._privacy(), self._access(), self._fair()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])


if __name__ == "__main__":
    unittest.main()
