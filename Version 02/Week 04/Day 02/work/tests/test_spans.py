import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from spans import read


class SpanTests(unittest.TestCase):
    def test_a_span_keeps_the_tool_the_hash_and_the_tokens(self) -> None:
        span = {"cpu": 0.2, "hash": "sha256:abc", "tokens": 128, "tool": "referral.status"}
        self.assertEqual(read(span), {"hash": "sha256:abc", "tokens": 128, "tool": "referral.status"})


if __name__ == "__main__":
    unittest.main()
