import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from breaker import book

_OUTAGE = {"partner": "insure", "status": "down", "timeout_seconds": 40}


class BreakerTests(unittest.TestCase):
    def test_the_breaker_opens_and_insure_is_not_called(self) -> None:
        got = book(_OUTAGE)
        self.assertEqual(got["breaker"], "open")
        self.assertEqual(got["waited"], 0)
        self.assertFalse(got["called"])
        self.assertNotEqual(got["target"], "insure")


if __name__ == "__main__":
    unittest.main()
