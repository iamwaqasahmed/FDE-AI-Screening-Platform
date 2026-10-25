import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from spans import read


class SpanTests(unittest.TestCase):
    def test_the_trace_fields_are_dropped(self) -> None:
        span = {"cpu": 0.2, "hash": "sha256:abc", "tokens": 128, "tool": "referral.status"}
        self.assertEqual(read(span), {"cpu": 0.2})


if __name__ == "__main__":
    unittest.main()
