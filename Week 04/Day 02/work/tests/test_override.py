import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from override import rate


class OverrideTests(unittest.TestCase):
    def test_the_rate_is_the_stamped_share(self) -> None:
        rows = [{"stamped": True}, {"stamped": False}]
        self.assertEqual(rate(rows), 0.5)


if __name__ == "__main__":
    unittest.main()
