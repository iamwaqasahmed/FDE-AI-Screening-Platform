import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from handoff import handoff

_EMPTY = {"agent": "cc-1", "id": "call-empty", "summary": ""}
_STATUS = {"agent": "cc-1", "id": "call-status", "summary": "Referral status, still pending."}


class HandoffTests(unittest.TestCase):
    def test_a_summary_is_kept_and_an_empty_one_is_refused(self) -> None:
        kept = handoff(_STATUS)
        refused = handoff(_EMPTY)
        self.assertEqual(kept["summary"], _STATUS["summary"])
        self.assertFalse(kept["refused"])
        self.assertTrue(refused["refused"])
        self.assertEqual(refused["agent"], "")


if __name__ == "__main__":
    unittest.main()
