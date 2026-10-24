import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from dashboard import board

_SPANS = [
    {"cpu": 0.2, "latency_ms": 180, "name": "model", "status": "ok", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 220, "name": "tool", "status": "ok", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 2400, "name": "tool", "status": "error", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 2600, "name": "tool", "status": "error", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 2800, "name": "tool", "status": "error", "tool": "referral.status"},
    {"at": "2027-02-01T09:15:00+03:00", "cpu": 0.2, "latency_ms": 0, "name": "alert", "status": "error", "tool": ""},
]


class BoardTests(unittest.TestCase):
    def test_the_board_names_latency_errors_tool_failures_and_the_alert(self) -> None:
        self.assertEqual(
            board(_SPANS),
            {
                "alert_at": "2027-02-01T09:15:00+03:00",
                "error_rate": 0.6,
                "latency_p95": 2800,
                "tool_failures": 3,
            },
        )


if __name__ == "__main__":
    unittest.main()
