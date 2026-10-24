import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from dashboard import board

_SPANS = [
    {"cpu": 0.2, "latency_ms": 180, "name": "model", "status": "ok", "tool": "referral.status"},
    {"cpu": 0.2, "latency_ms": 2400, "name": "tool", "status": "error", "tool": "referral.status"},
    {"at": "2027-02-01T09:15:00+03:00", "cpu": 0.2, "latency_ms": 0, "name": "alert", "status": "error", "tool": ""},
]


class BoardTests(unittest.TestCase):
    def test_the_board_reports_cpu_only(self) -> None:
        self.assertEqual(board(_SPANS), {"cpu": 0.2})


if __name__ == "__main__":
    unittest.main()
