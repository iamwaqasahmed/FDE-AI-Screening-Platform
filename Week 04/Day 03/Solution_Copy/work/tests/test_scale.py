import sys
import unittest
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from scale import started

_FORECAST = {"peak_at": "2024-06-11T04:15:00+03:00"}
_SHEET = {"cold_start_seconds": 15}


class ScaleTests(unittest.TestCase):
    def test_the_start_leads_the_peak_by_the_cold_start(self) -> None:
        peak = datetime.fromisoformat(_FORECAST["peak_at"])
        expect = (peak - timedelta(seconds=15)).isoformat()
        self.assertEqual(started(_FORECAST, _SHEET), expect)
        self.assertNotEqual(expect, _FORECAST["peak_at"])


if __name__ == "__main__":
    unittest.main()
