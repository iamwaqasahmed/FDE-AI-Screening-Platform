import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from handoff import handoff

_STATUS = {"agent": "cc-1", "id": "call-status", "summary": "Referral status, still pending."}


class HandoffTests(unittest.TestCase):
    def test_the_shell_returns_an_empty_summary(self) -> None:
        got = handoff(_STATUS)
        self.assertEqual(got["summary"], "")
        self.assertFalse(got["refused"])


if __name__ == "__main__":
    unittest.main()
