"""Tests for a reply that shows the shadow text.

The turn fixture has a registered reply and a shadow reply. The
reply is expected to be the shadow one. A candidate hash is expected
back even when the comparison flag is false.
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
    """Check the shadow reply and promotion without a comparison."""

    def test_the_shadow_reply_is_shown(self) -> None:
        """reply returns the shadow reply from the turn fixture.

        The registered reply on that fixture is not the result.
        """
        self.assertEqual(reply(_TURN), _TURN["shadow_reply"])

    def test_a_hash_is_promoted_with_no_comparison(self) -> None:
        """promote returns the candidate hash when compared is false.

        The call has no matched flag. The assertion expects the hash.
        """
        self.assertEqual(promote({"candidate_hash": "sha256:candidate", "compared": False}), "sha256:candidate")


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
