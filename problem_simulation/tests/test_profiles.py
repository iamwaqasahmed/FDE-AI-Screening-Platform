"""Profiles named in the hidden world, and the paths they are allowed to use.

Guards the named world profiles and the directories they are allowed to use.

Practice, small, and the team profile have fixed scales. Personal and assessment
must refuse to load until their environment values are set. Volume is an
environment switch, not a property of the small profile by itself. Assessment
renames sites, shifts dates, and must not write under the data tree.
"""

from __future__ import annotations

import os
import unittest

from alwaha.config.profile import load
from alwaha.config.scale import PERSONAL_PEOPLE, PRACTICE_PEOPLE, SMALL_PEOPLE, volume_rows
from alwaha.paths import VERSION_ROOT, world_dir


class ProfileTests(unittest.TestCase):
    """Catches a profile whose scale, seed, volume flag, or output directory drifted."""
    def test_named_scales(self) -> None:
        """Fails when practice or small no longer match their named populations, when the
        team profile's seed changes, or when practice silently turns volume on.
        """
        # Practice and small keep their named sizes. The team seed is fixed, and practice is not a volume run.
        self.assertEqual(load("practice").people, PRACTICE_PEOPLE)
        self.assertEqual(load("small").people, SMALL_PEOPLE)
        self.assertEqual(load("team-3").seed, 50303)
        self.assertFalse(load("practice").volume)

    def test_volume_flag(self) -> None:
        """Fails when the volume switch does not enlarge the small profile, or when the
        same profile still looks enlarged after the switch is removed.
        """
        # Turn the volume switch on, then load small. The profile must grow.
        os.environ["ALWAHA_VOLUME"] = "1"
        try:
            profile = load("small")
            self.assertTrue(profile.volume)
            self.assertGreater(volume_rows(profile), 0)
        finally:
            os.environ.pop("ALWAHA_VOLUME", None)
        # The switch is gone, so the same profile is no longer enlarged.
        self.assertEqual(volume_rows(load("small")), 0)

    def test_personal_and_assessment_need_env(self) -> None:
        """Fails when personal or assessment load with their environment values missing."""
        # Both environment values are missing. Each load must refuse.
        os.environ.pop("ALWAHA_PARTICIPANT", None)
        os.environ.pop("ALWAHA_ASSESSMENT_SEED", None)
        with self.assertRaises(SystemExit):
            load("personal")
        with self.assertRaises(SystemExit):
            load("assessment")

    def test_personal_seed_is_stable(self) -> None:
        """Fails when the same participant name produces two seeds, or when the personal
        population size drifts.
        """
        # The same participant name, loaded twice, must keep one seed and the personal population size.
        os.environ["ALWAHA_PARTICIPANT"] = "noura"
        try:
            first = load("personal")
            second = load("personal")
        finally:
            os.environ.pop("ALWAHA_PARTICIPANT", None)
        self.assertEqual(first.seed, second.seed)
        self.assertEqual(first.people, PERSONAL_PEOPLE)

    def test_assessment_renames_and_stays_out_of_data(self) -> None:
        """Fails when assessment does not rename sites, does not shift dates, or resolves
        its world directory inside the data tree.
        """
        # Assessment loads only with this seed. The seed is removed before the checks below.
        os.environ["ALWAHA_ASSESSMENT_SEED"] = "424242"
        try:
            profile = load("assessment")
        finally:
            os.environ.pop("ALWAHA_ASSESSMENT_SEED", None)
        # Sites are renamed, dates move, and the world directory is outside the data tree.
        self.assertTrue(profile.rename_sites)
        self.assertGreater(profile.date_shift_days, 0)
        root = world_dir("assessment")
        data = (VERSION_ROOT / "data").resolve()
        self.assertFalse(str(root).startswith(str(data)))


if __name__ == "__main__":
    unittest.main()
