"""Day 2 approach and brief checks.

Guards the approach checker and the brief checker.

The fixture is a small second-day pack, its measurements, and the hidden approach
gold. Each test writes an approach memo and a brief into a scratch work directory
and reads the problem lists. A fitting memo must pass. A memo that hides the
real family, uses the row-level split, ranks triage first without an urgency
rule, or carries the watermark, must fail without echoing the hidden value.
"""

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
    """Catches a checker that accepts a bad memo or that quotes a hidden value back.

    The grade helper writes both pages and runs both checkers. The memo builders
    live next to this file and only supply text.
    """
    def setUp(self) -> None:
        """Write a small pack, measure it, and load the approach gold into a scratch work directory.

        Later tests write an approach memo and a brief into the empty work directory and fail
        when a checker accepts a bad memo or quotes a hidden value.
        """
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
        """Delete the temporary pack and work directory."""
        self.tmp.cleanup()

    def _grade(self, approach_text: str, brief_text: str) -> tuple[list[str], list[str]]:
        """Write the two memos and return the approach problems and the brief problems.

        The watermark passed in is the profile's own, so a memo that pastes it can be
        caught without this helper printing it.
        """
        (self.work / "approach.md").write_text(approach_text, encoding="utf-8")
        (self.work / "brief.md").write_text(brief_text, encoding="utf-8")
        canary = self.profile.canary()
        return (
            approach_problems(self.work, self.pack, self.gold, self.measured, canary),
            brief_problems(self.work, self.pack, self.gold, self.measured, canary),
        )

    def test_fitting_memo_passes(self) -> None:
        """Fails when a memo that cites the right families and the right sizes is still rejected."""
        family, sizes = self._grade(approach(self.gold, self.measured, fit_family), brief(self.pack, self.measured))
        self.assertEqual(family, [])
        self.assertEqual(sizes, [])

    def test_all_model_memo_hides_the_family(self) -> None:
        """Fails when labeling every problem as one family is accepted for a problem that
        needs something else, when a problem that really is that family is flagged, or
        when the problem list teaches the missing family names.
        """
        memo = approach(self.gold, self.measured, lambda _problem_id, _rule: "agent")
        family, _sizes = self._grade(memo, brief(self.pack, self.measured))
        self.assertIn("p-clock family does not fit", family)
        self.assertNotIn("p-status family does not fit", family)
        joined = "\n".join(family)
        for word in ("no-model", "classical-ml", "blocked", "retrieve"):
            self.assertNotIn(word, joined)

    def test_row_split_number_is_rejected(self) -> None:
        """Fails when the row-level no-show figure is accepted as the measured cell, or
        when the problem list prints that figure.
        """
        def measured_for(problem_id: str) -> str:
            """Substitute the measured cell for one problem.

            The no-show problem receives the row-level figure. Every other problem keeps
            the ordinary measurement, so the checker is failing the split and not the rest
            of the table.
            """
            # Only the no-show problem is given the row-level figure. The other cells stay ordinary.
            if problem_id == "p-dna":
                return str(self.measured["dna_row"])
            return str(self.measured.get(problem_id, "claim"))

        # Grade that memo against the fitting brief, so a failure is about the split cell.
        family, _sizes = self._grade(
            approach(self.gold, self.measured, fit_family, measured_for),
            brief(self.pack, self.measured),
        )
        # The cell is rejected, and the problem list does not print the row-level figure.
        self.assertIn("p-dna measured value does not match the baseline", family)
        self.assertNotIn(str(self.measured["dna_row"]), "\n".join(family))

    def test_triage_first_needs_the_urgency_rule(self) -> None:
        """Fails when triage can lead the ranking with a plain note, or when the same
        ranking is still rejected after the urgency rule is written on that first line.
        """
        order = ("p-triage",) + tuple(problem_id for problem_id in RANK if problem_id != "p-triage")
        memo = approach(self.gold, self.measured, fit_family)
        _family, sizes = self._grade(memo, brief(self.pack, self.measured, order))
        self.assertEqual(sizes, ["the first rank needs the urgency rule on the same line"])
        _family, sizes = self._grade(memo, brief(self.pack, self.measured, order, first="a clinician assigns urgency"))
        self.assertEqual(_family, [])
        self.assertEqual(sizes, [])

    def test_banned_sentence_outside_a_claim_fails(self) -> None:
        """Fails when a banned sentence outside a claim row is accepted, or when the
        problem list quotes the sentence.
        """
        _family, sizes = self._grade(
            approach(self.gold, self.measured, fit_family),
            brief(self.pack, self.measured, extra="Waiting time fell last year."),
        )
        self.assertEqual(sizes, ["brief contains a banned sentence"])
        self.assertNotIn("Waiting time fell last year.", sizes)

    def test_banned_sentence_inside_a_claim_stands(self) -> None:
        """Fails when the same kind of sentence, placed inside a claim row, is rejected.

        The claim table is allowed to record what someone said. A sentence outside that
        table is not.
        """
        text = brief(self.pack, self.measured).replace(
            "| cdo | The virtual front desk goes live before Ramadan. | claim |",
            "| cdo | Al-Waha containment is about 70 percent. | claim |",
        )
        _family, sizes = self._grade(approach(self.gold, self.measured, fit_family), text)
        self.assertEqual(sizes, [])

    def test_watermark_in_work_is_not_echoed(self) -> None:
        """Fails when a watermark pasted onto the approach memo is ignored, or when the
        problem list contains the watermark.
        """
        memo = approach(self.gold, self.measured, fit_family) + self.profile.canary()
        family, _sizes = self._grade(memo, brief(self.pack, self.measured))
        self.assertEqual(family, ["a watermarked sample is in the work directory"])
        self.assertNotIn(self.profile.canary(), "\n".join(family))


if __name__ == "__main__":
    unittest.main()
