import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from shadow import promote, reply

_TURN = {
    "candidate_hash": "sha256:candidate",
    "registered_reply": "Your referral is still pending.",
    "shadow_reply": "Your referral was accepted by the shadow adapter.",
}


class ShadowTests(unittest.TestCase):
    def test_the_shadow_reply_is_shown(self) -> None:
        self.assertEqual(reply(_TURN), _TURN["shadow_reply"])

    def test_a_hash_is_promoted_with_no_comparison(self) -> None:
        self.assertEqual(promote({"candidate_hash": "sha256:candidate", "compared": False}), "sha256:candidate")


if __name__ == "__main__":
    unittest.main()
