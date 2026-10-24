"""Day 1 of Week 3 identity, label, and synthetic checks."""

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
from alwaha.paths import W3D1_APP, W3D1_ROOT
from alwaha.release.w3d1 import write_w3d1


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.profile = load("small")
        self.pack = root / "pack"
        self.truth = root / "truth"
        write_w3d1(self.profile, self.pack, self.truth)
        self.gold = json.loads((self.truth / "w3d1_gold.json").read_text(encoding="utf-8"))
        self.work = root / "work"
        shutil.copytree(W3D1_ROOT / "work", self.work, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        self.assertEqual(self.gold, gold(self.profile))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _identity(self) -> list[str]:
        return identity_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _labels(self) -> list[str]:
        return labels_problems(self.work, self.gold, self.profile.canary())

    def _synthetic(self) -> list[str]:
        return synthetic_problems(self.work, self.pack, self.gold, self.profile.canary())

    def _hidden(self, problems: list[str]) -> None:
        joined = "\n".join(problems)
        for secret in (self.profile.canary(), *self.gold["national_ids"], *self.gold["dates"].values()):
            self.assertNotIn(secret, joined)

    def test_filled_work_passes(self) -> None:
        self.assertEqual(self._identity(), [])
        self.assertEqual(self._labels(), [])
        self.assertEqual(self._synthetic(), [])

    def test_advanced_modules_match_and_are_optional(self) -> None:
        pit = load_module(self.work / "app", "pit")
        bought = load_module(self.work / "app", "budget")
        price = budget(self.profile)
        self.assertEqual(pit.features(list(PIT_ROWS), INVITE_ON), features_at(list(PIT_ROWS), INVITE_ON))
        self.assertEqual(
            bought.spend(list(SPEND_ITEMS), price["price"], price["sar"]),
            spend(list(SPEND_ITEMS), price["price"], price["sar"]),
        )
        (self.work / "app" / "pit.py").unlink()
        (self.work / "app" / "budget.py").unlink()
        self.assertEqual(self._identity(), [])
        self.assertEqual(self._labels(), [])
        self.assertEqual(self._synthetic(), [])

    def test_shell_dates_shift_the_boundary(self) -> None:
        shutil.copy(W3D1_APP / "dates.py", self.work / "app" / "dates.py")
        problems = self._identity()
        self.assertEqual(problems, [HIJRI])
        self._hidden(problems)

    def test_shell_codes_keep_the_catalog(self) -> None:
        shutil.copy(W3D1_APP / "codes.py", self.work / "app" / "codes.py")
        problems = self._identity()
        self.assertEqual(problems, [STALE])
        self._hidden(problems)

    def test_shell_cluster_merges_the_traps(self) -> None:
        shutil.copy(W3D1_APP / "cluster.py", self.work / "app" / "cluster.py")
        problems = self._identity()
        self.assertEqual(problems, [MOTHER, TWINS, REUSED, ROWS])
        self._hidden(problems)

    def test_shell_labels_follow_ann_v1(self) -> None:
        shutil.copy(W3D1_APP / "labels.py", self.work / "app" / "labels.py")
        problems = self._labels()
        self.assertEqual(problems, [PHOTO, BLANK, OLD])
        self._hidden(problems)

    def test_shell_sample_copies_a_real_letter(self) -> None:
        shutil.copy(W3D1_APP / "synthetic.py", self.work / "app" / "synthetic.py")
        problems = self._synthetic()
        self.assertEqual(problems, [CARD, MARK, NID])
        self._hidden(problems)

    def test_shell_scan_accepts_the_file(self) -> None:
        shutil.copy(W3D1_APP / "scan.py", self.work / "app" / "scan.py")
        problems = self._synthetic()
        self.assertEqual(problems, [MARK, NID])
        self._hidden(problems)

    def test_copied_fixture_is_not_echoed(self) -> None:
        shutil.copy(self.pack / "letters" / "clerk.jsonl", self.work / "clerk.jsonl")
        for problems in (self._identity(), self._labels(), self._synthetic()):
            self.assertEqual(problems, [WATERMARK])
            self.assertNotIn(self.profile.canary(), problems[0])
            self._hidden(problems)


if __name__ == "__main__":
    unittest.main()
