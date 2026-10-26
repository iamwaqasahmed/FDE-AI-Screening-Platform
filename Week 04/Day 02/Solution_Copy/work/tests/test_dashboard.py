"""Tests for a board of latency, errors, tool failures, and the alert.

The fixture is a model span, tool spans, error spans that name a tool,
and an alert span with a time. The board should report that alert time,
the error share, the latency percentile, and the tool-failure count.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from dashboard import board

# Body spans, including tool errors, and a final span named alert.
_SPANS = [
    {"cpu": 0.2, "latency_ms": 180, "name": "model", "status": "ok", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 220, "name": "tool", "status": "ok", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 2400, "name": "tool", "status": "error", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 2600, "name": "tool", "status": "error", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 2800, "name": "tool", "status": "error", "tool": "referral.status"},
    {"at": "2027-02-01T09:15:00+03:00", "cpu": 0.2, "latency_ms": 0, "name": "alert", "status": "error", "tool": ""},
]


class BoardTests(unittest.TestCase):
    """Check the summary dict the board returns for the span fixture."""

    def test_the_board_names_latency_errors_tool_failures_and_the_alert(self) -> None:
        """Each key in the expected dict is checked.

        alert_at is the time on the alert span. error_rate, latency_p95,
        and tool_failures come from the other spans. The assertion is the
        whole dict.
        """
        self.assertEqual(
            board(_SPANS),
            {
                "alert_at": "2027-02-01T09:15:00+03:00",
                "error_rate": 0.6,
                "latency_p95": 2800,
                "tool_failures": 3,
            },
        )


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
