"""Simpler methods fail on practice and on assessment.

Guards the audit slices on practice and on assessment.

Every named slice must be reported, the simpler method on that slice must fail,
and the passing method must hold. The assessment seed is set only for the load
and removed afterwards, because assessment refuses to load without it.
"""

from __future__ import annotations

import os
import unittest

from alwaha.audit.slices import SLICES, evaluate
from alwaha.config.profile import load


class SliceTests(unittest.TestCase):
    """Catches a slice list that dropped a slice, or a slice whose simpler method
    suddenly passes.
    """
    def test_every_slice_on_two_profiles(self) -> None:
        """Fails when either profile omits a slice, when a simpler method passes, or when
        the method that should pass does not.
        """
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
