"""Tests for the finished chat reserve.

The sheet holds a budget, a reserved latency, and a
starved latency. The result should be the reserved
latency, and that figure should be at or under the budget.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from quota import latency

# Budget, reserved latency, and starved latency.
_SHEET = {"chat_p95_budget_ms": 800, "chat_p95_reserved_ms": 200, "chat_p95_starved_ms": 2000}


class QuotaTests(unittest.TestCase):
    """The reserved latency against the chat budget."""

    def test_a_chat_reserve_stays_inside_the_budget(self) -> None:
        """Latency is the reserved 200, and 200 is at or under the budget of 800."""
        self.assertEqual(latency(_SHEET), 200)
        self.assertLessEqual(latency(_SHEET), _SHEET["chat_p95_budget_ms"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
