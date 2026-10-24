"""Simpler methods fail on practice and on assessment."""

from __future__ import annotations

import os
import unittest

from alwaha.audit.slices import SLICES, evaluate
from alwaha.config.profile import load


class SliceTests(unittest.TestCase):
    def test_every_slice_on_two_profiles(self) -> None:
        os.environ["ALWAHA_ASSESSMENT_SEED"] = "424242"
        try:
            profiles = (load("practice"), load("assessment"))
        finally:
            os.environ.pop("ALWAHA_ASSESSMENT_SEED", None)
        for profile in profiles:
            rows = evaluate(profile)
            self.assertEqual([row["slice"] for row in rows], list(SLICES))
            for row in rows:
                self.assertTrue(row["simpler_fails"], row)
                self.assertTrue(row["passing_ok"], row)


if __name__ == "__main__":
    unittest.main()
