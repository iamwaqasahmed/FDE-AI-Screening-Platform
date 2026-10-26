"""Tests for a reply that stays on the registered text.

The turn fixture has a registered reply and a shadow reply. The
reply should be the registered one. Promotion should return a hash
only when the comparison was compared and matched.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from shadow import promote, reply

# A registered reply, a shadow reply, and a candidate hash.
_TURN = {
    "candidate_hash": "sha256:candidate",
    "registered_reply": "Your referral is still pending.",
    "shadow_reply": "Your referral was accepted by the shadow adapter.",
}


class ShadowTests(unittest.TestCase):
    """Check the patient reply and the promotion gate."""

    def test_the_patient_reply_stays_registered(self) -> None:
        """reply returns the registered reply from the turn fixture.

        The shadow reply on that fixture is not the result.
        """
        self.assertEqual(reply(_TURN), _TURN["registered_reply"])

    def test_promotion_waits_for_a_comparison(self) -> None:
        """A comparison that was not compared promotes nothing.

        The bare fixture is refused and the result is empty. The ready
        fixture was compared and matched, so it returns the candidate hash.
        """
        # Not compared and not matched. Promotion should refuse this one.
        bare = {"candidate_hash": "sha256:candidate", "compared": False, "matched": False}
        # Compared and matched. Promotion should return the hash.
        ready = {"candidate_hash": "sha256:candidate", "compared": True, "matched": True}
        self.assertEqual(promote(bare), "")
        self.assertEqual(promote(ready), "sha256:candidate")


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
