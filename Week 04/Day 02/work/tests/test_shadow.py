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
    def test_the_patient_reply_stays_registered(self) -> None:
        self.assertEqual(reply(_TURN), _TURN["registered_reply"])

    def test_promotion_waits_for_a_comparison(self) -> None:
        bare = {"candidate_hash": "sha256:candidate", "compared": False, "matched": False}
        ready = {"candidate_hash": "sha256:candidate", "compared": True, "matched": True}
        self.assertEqual(promote(bare), "")
        self.assertEqual(promote(ready), "sha256:candidate")


if __name__ == "__main__":
    unittest.main()
