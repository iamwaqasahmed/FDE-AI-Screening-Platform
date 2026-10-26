"""Tests for the finished capacity table.

The plan holds chat_p95, hours, sar, and tokens_per_second.
The table should come back equal to that whole plan, so
none of the four fields is dropped.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from capacity import table

# Chat latency, hours, sar, and tokens per second.
_PLAN = {"chat_p95": 200, "hours": 33.3333, "sar": 41, "tokens_per_second": 100}


class CapacityTests(unittest.TestCase):
    """The plan fields the finished table keeps."""

    def test_the_table_records_the_price_and_the_hours(self) -> None:
        """The table equals the plan, including sar and hours."""
        self.assertEqual(table(_PLAN), _PLAN)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
