"""Tests for a board that reports cpu only.

The fixture includes latency, status, tools, and an alert time.
The board is expected to report the cpu of the first span and
nothing else.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from dashboard import board

# Spans with cpu, latency, status, and tools, plus an alert span.
_SPANS = [
    {"cpu": 0.2, "latency_ms": 180, "name": "model", "status": "ok", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 2400, "name": "tool", "status": "error", "tool": "referral.status"},
    {"at": "2027-02-01T09:15:00+03:00", "cpu": 0.2, "latency_ms": 0, "name": "alert", "status": "error", "tool": ""},
]


class BoardTests(unittest.TestCase):
    """Check that the board dict has only the first span's cpu."""

    def test_the_board_reports_cpu_only(self) -> None:
        """The board is the cpu value from the first span.

        The expected dict has that one key. Latency, status, tools, and
        the alert time are in the fixture and are not in the result.
        """
        self.assertEqual(board(_SPANS), {"cpu": 0.2})


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
