import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from override import rate


class OverrideTests(unittest.TestCase):
    def test_the_rate_stays_at_zero(self) -> None:
        self.assertEqual(rate([{"stamped": True}, {"stamped": False}]), 0.0)


if __name__ == "__main__":
    unittest.main()
