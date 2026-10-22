"""Day 2 approach and brief checks."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from alwaha.check.approach import approach_problems
from alwaha.check.brief import brief_problems
from alwaha.config.profile import load
from alwaha.release.day2 import write_day2
from alwaha.samples.measure import measure_pack
from day2_memos import RANK, approach, brief, fit_family


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_day2(self.profile, self.pack, self.truth)
        self.measured = measure_pack(self.pack)
        self.gold = json.loads((self.truth / "approach_gold.json").read_text(encoding="utf-8"))
        self.work = root / "work"
        self.work.mkdir()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _grade(self, approach_text: str, brief_text: str) -> tuple[list[str], list[str]]:
        (self.work / "approach.md").write_text(approach_text, encoding="utf-8")
        (self.work / "brief.md").write_text(brief_text, encoding="utf-8")
        canary = self.profile.canary()
        return (
            approach_problems(self.work, self.pack, self.gold, self.measured, canary),
            brief_problems(self.work, self.pack, self.gold, self.measured, canary),
        )

    def test_fitting_memo_passes(self) -> None:
        family, sizes = self._grade(approach(self.gold, self.measured, fit_family), brief(self.pack, self.measured))
        self.assertEqual(family, [])
        self.assertEqual(sizes, [])

    def test_all_model_memo_hides_the_family(self) -> None:
        memo = approach(self.gold, self.measured, lambda _problem_id, _rule: "agent")
        family, _sizes = self._grade(memo, brief(self.pack, self.measured))
        self.assertIn("p-clock family does not fit", family)
        self.assertNotIn("p-status family does not fit", family)
        joined = "\n".join(family)
        for word in ("no-model", "classical-ml", "blocked", "retrieve"):
            self.assertNotIn(word, joined)

    def test_row_split_number_is_rejected(self) -> None:
        def measured_for(problem_id: str) -> str:
            if problem_id == "p-dna":
                return str(self.measured["dna_row"])
            return str(self.measured.get(problem_id, "claim"))

        family, _sizes = self._grade(
            approach(self.gold, self.measured, fit_family, measured_for),
            brief(self.pack, self.measured),
        )
        self.assertIn("p-dna measured value does not match the baseline", family)
        self.assertNotIn(str(self.measured["dna_row"]), "\n".join(family))

    def test_triage_first_needs_the_urgency_rule(self) -> None:
        order = ("p-triage",) + tuple(problem_id for problem_id in RANK if problem_id != "p-triage")
        memo = approach(self.gold, self.measured, fit_family)
        _family, sizes = self._grade(memo, brief(self.pack, self.measured, order))
        self.assertEqual(sizes, ["the first rank needs the urgency rule on the same line"])
        _family, sizes = self._grade(memo, brief(self.pack, self.measured, order, first="a clinician assigns urgency"))
        self.assertEqual(_family, [])
        self.assertEqual(sizes, [])

    def test_banned_sentence_outside_a_claim_fails(self) -> None:
        _family, sizes = self._grade(
            approach(self.gold, self.measured, fit_family),
            brief(self.pack, self.measured, extra="Waiting time fell last year."),
        )
        self.assertEqual(sizes, ["brief contains a banned sentence"])
        self.assertNotIn("Waiting time fell last year.", sizes)

    def test_banned_sentence_inside_a_claim_stands(self) -> None:
        text = brief(self.pack, self.measured).replace(
            "| cdo | The virtual front desk goes live before Ramadan. | claim |",
            "| cdo | Al-Waha containment is about 70 percent. | claim |",
        )
        _family, sizes = self._grade(approach(self.gold, self.measured, fit_family), text)
        self.assertEqual(sizes, [])

    def test_watermark_in_work_is_not_echoed(self) -> None:
        memo = approach(self.gold, self.measured, fit_family) + self.profile.canary()
        family, _sizes = self._grade(memo, brief(self.pack, self.measured))
        self.assertEqual(family, ["a watermarked sample is in the work directory"])
        self.assertNotIn(self.profile.canary(), "\n".join(family))


if __name__ == "__main__":
    unittest.main()
