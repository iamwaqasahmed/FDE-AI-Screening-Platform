import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from price import rate

_TODAY = {"sar": 41}
_YESTERDAY = {"price.ext_large_per_1k": 17}


class PriceTests(unittest.TestCase):
    def test_the_shell_uses_yesterday(self) -> None:
        self.assertEqual(rate(_TODAY, _YESTERDAY), 17)


if __name__ == "__main__":
    unittest.main()
