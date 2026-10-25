import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cost import quote

_CAP = {"max_sar": 8, "max_seconds": 2, "tokens": 1000}
_PRICES = {"price.ext_large_per_1k": "20", "price.local_per_1k": "3"}


class CostTests(unittest.TestCase):
    def test_local_tokens_stay_inside_the_cap(self) -> None:
        priced = quote(_CAP, _PRICES)
        self.assertEqual(priced["model"], "local-small")
        self.assertLessEqual(priced["sar"], _CAP["max_sar"])
        self.assertLessEqual(priced["seconds"], _CAP["max_seconds"])


if __name__ == "__main__":
    unittest.main()
