"""Day 1 of Week 3 identity, label, and synthetic checks.

Guards the identity, label, and synthetic checkers.

The fixture is this day's pack plus the filled work tree. The filled copy must
pass, and the optional pit and budget modules must match the reference rules
before they are removed. Each shell swap restores one unfinished module and
expects that module's own failure: a shifted calendar boundary, a stale code, a
bad merge, labels that follow the old scheme, a sample that copies a real
letter, or a scan that accepts the file. A copied clerk fixture must fail as a
watermark. Problem text must not echo ids or dates.
"""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from alwaha.check.agent_run import WATERMARK
from alwaha.check.identity_w3 import HIJRI, MOTHER, REUSED, ROWS, STALE, TWINS, identity_problems
from alwaha.check.labels_w3 import BLANK, OLD, PHOTO, labels_problems
from alwaha.check.load_app import load_module
from alwaha.check.synthetic_w3 import CARD, MARK, NID, synthetic_problems
from alwaha.config.profile import load
from alwaha.engagement.w3d1 import budget, gold
from alwaha.engagement.w3d1_rules import INVITE_ON, PIT_ROWS, SPEND_ITEMS, features_at, spend
from alwaha.paths import W3D1_APP, W3D1_WORK
from alwaha.release.w3d1 import write_w3d1


class CheckTests(unittest.TestCase):
    """Catches a grader that accepts a merged identity, an old label, or a synthetic
    letter that still contains a real person.
    """
    def setUp(self) -> None:
        """Write this day's pack and copy the filled work tree.

        The gold file must match the generator before any shell module is copied back.
        """
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_w3d1(self.profile, self.pack, self.truth)
        self.gold = json.loads((self.truth / "w3d1_gold.json").read_text(encoding="utf-8"))
        self.work = root / "work"
        shutil.copytree(W3D1_WORK, self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        self.assertEqual(self.gold, gold(self.profile))

    def tearDown(self) -> None:
        """Delete the temporary pack and work tree."""
        self.tmp.cleanup()

    def _identity(self) -> list[str]:
        """Run the identity checker."""
        return identity_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _labels(self) -> list[str]:
        """Run the label checker."""
        return labels_problems(self.work, self.gold, self.profile.canary())

    def _synthetic(self) -> list[str]:
        """Run the synthetic-letter checker."""
        return synthetic_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        """Fail this case when a problem list echoes the watermark, a national id, or a
        converted date.
        """
        joined = "\n".join(problems)
        for secret in (self.profile.canary(), *self.gold["national_ids"], *self.gold["dates"].values()):
            self.assertNotIn(secret, joined)

    def test_filled_work_passes(self) -> None:
        """Fails when the filled work tree still produces an identity, label, or synthetic problem."""
        self.assertEqual(self._identity(), [])
        self.assertEqual(self._labels(), [])
        self.assertEqual(self._synthetic(), [])

    def test_advanced_modules_match_and_are_optional(self) -> None:
        """Fails when the pit or budget module disagrees with the reference rule, or when
        deleting those modules makes a passing tree fail. They are checked, then treated
        as optional.
        """
        # Load the optional modules and compare them with the reference rules.
        pit = load_module(self.work / "app", "pit")
        bought = load_module(self.work / "app", "budget")
        price = budget(self.profile)
        self.assertEqual(pit.features(list(PIT_ROWS), INVITE_ON), features_at(list(PIT_ROWS), INVITE_ON))
        self.assertEqual(
            bought.spend(list(SPEND_ITEMS), price["price"], price["sar"]),
            spend(list(SPEND_ITEMS), price["price"], price["sar"]),
        )
        # Remove both modules. The required checks still pass, so the modules are optional.
        (self.work / "app" / "pit.py").unlink()
        (self.work / "app" / "budget.py").unlink()
        self.assertEqual(self._identity(), [])
        self.assertEqual(self._labels(), [])
        self.assertEqual(self._synthetic(), [])

    def test_shell_dates_shift_the_boundary(self) -> None:
        """Fails when the unfinished date conversion, which moves the calendar boundary,
        is accepted.
        """
        shutil.copy(W3D1_APP / "dates.py", self.work / "app" / "dates.py")
        problems = self._identity()
        self.assertEqual(problems, [HIJRI])
        self._hidden(problems)

    def test_shell_codes_keep_the_catalog(self) -> None:
        """Fails when the unfinished code map, which keeps a stale catalog entry, is accepted.

        The test copies the unfinished code map into the work tree and fails unless the identity
        checker reports the stale catalog entry, and the problem list does not echo a hidden
        value.
        """
        shutil.copy(W3D1_APP / "codes.py", self.work / "app" / "codes.py")
        problems = self._identity()
        self.assertEqual(problems, [STALE])
        self._hidden(problems)

    def test_shell_cluster_merges_the_traps(self) -> None:
        """Fails when the unfinished clusterer is accepted. It merges the mother and the
        newborn, the twins, and the reused record, and it collapses distinct rows.
        """
        shutil.copy(W3D1_APP / "cluster.py", self.work / "app" / "cluster.py")
        problems = self._identity()
        self.assertEqual(problems, [MOTHER, TWINS, REUSED, ROWS])
        self._hidden(problems)

    def test_shell_labels_follow_ann_v1(self) -> None:
        """Fails when the unfinished labels, which follow the old scheme, are accepted.
        A photo, a blank, and an old mark should each be caught.
        """
        shutil.copy(W3D1_APP / "labels.py", self.work / "app" / "labels.py")
        problems = self._labels()
        self.assertEqual(problems, [PHOTO, BLANK, OLD])
        self._hidden(problems)

    def test_shell_sample_copies_a_real_letter(self) -> None:
        """Fails when the unfinished sampler, which copies a real letter, is accepted.

        The test copies the unfinished sampler into the work tree and fails unless the
        synthetic-letter checker reports the missing fidelity card, the watermark, and the
        national id, and the problem list does not echo a hidden value.
        """
        shutil.copy(W3D1_APP / "synthetic.py", self.work / "app" / "synthetic.py")
        problems = self._synthetic()
        self.assertEqual(problems, [CARD, MARK, NID])
        self._hidden(problems)

    def test_shell_scan_accepts_the_file(self) -> None:
        """Fails when the unfinished scan, which accepts the planted file, is accepted.
        The card failure belongs to the sampler, so this swap must not report it.
        """
        shutil.copy(W3D1_APP / "scan.py", self.work / "app" / "scan.py")
        problems = self._synthetic()
        self.assertEqual(problems, [MARK, NID])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        """Fails when a copied clerk file is ignored by any of the three checkers, or when
        a problem message contains the watermark.
        """
        shutil.copy(self.pack / "letters" / "clerk.jsonl", self.work / "clerk.jsonl")
        for problems in (self._identity(), self._labels(), self._synthetic()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])
            self._hidden(problems)


if __name__ == "__main__":
    unittest.main()
