import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from scale import started

_FORECAST = {"peak_at": "2027-02-02T21:00:00+03:00"}
_SHEET = {"cold_start_seconds": 90}


class ScaleTests(unittest.TestCase):
    def test_the_shell_starts_at_the_peak(self) -> None:
        self.assertEqual(started(_FORECAST, _SHEET), _FORECAST["peak_at"])


if __name__ == "__main__":
    unittest.main()
