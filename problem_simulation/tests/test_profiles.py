"""Profiles named in the hidden world, and the paths they are allowed to use."""

from __future__ import annotations

import os
import unittest

from alwaha.config.profile import load
from alwaha.config.scale import PERSONAL_PEOPLE, PRACTICE_PEOPLE, SMALL_PEOPLE, volume_rows
from alwaha.paths import VERSION_ROOT, world_dir


class ProfileTests(unittest.TestCase):
    def test_named_scales(self) -> None:
        self.assertEqual(load("practice").people, PRACTICE_PEOPLE)
        self.assertEqual(load("small").people, SMALL_PEOPLE)
        self.assertEqual(load("team-3").seed, 50303)
        self.assertFalse(load("practice").volume)

    def test_volume_flag(self) -> None:
        os.environ["ALWAHA_VOLUME"] = "1"
        try:
            profile = load("small")
            self.assertTrue(profile.volume)
            self.assertGreater(volume_rows(profile), 0)
        finally:
            os.environ.pop("ALWAHA_VOLUME", None)
        self.assertEqual(volume_rows(load("small")), 0)

    def test_personal_and_assessment_need_env(self) -> None:
        os.environ.pop("ALWAHA_PARTICIPANT", None)
        os.environ.pop("ALWAHA_ASSESSMENT_SEED", None)
        with self.assertRaises(SystemExit):
            load("personal")
        with self.assertRaises(SystemExit):
            load("assessment")

    def test_personal_seed_is_stable(self) -> None:
        os.environ["ALWAHA_PARTICIPANT"] = "noura"
        try:
            first = load("personal")
            second = load("personal")
        finally:
            os.environ.pop("ALWAHA_PARTICIPANT", None)
        self.assertEqual(first.seed, second.seed)
        self.assertEqual(first.people, PERSONAL_PEOPLE)

    def test_assessment_renames_and_stays_out_of_data(self) -> None:
        os.environ["ALWAHA_ASSESSMENT_SEED"] = "424242"
        try:
            profile = load("assessment")
        finally:
            os.environ.pop("ALWAHA_ASSESSMENT_SEED", None)
        self.assertTrue(profile.rename_sites)
        self.assertGreater(profile.date_shift_days, 0)
        root = world_dir("assessment")
        data = (VERSION_ROOT / "data").resolve()
        self.assertFalse(str(root).startswith(str(data)))


if __name__ == "__main__":
    unittest.main()
