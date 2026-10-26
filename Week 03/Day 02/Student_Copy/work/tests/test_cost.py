"""Tests that the quote uses the local model and stays inside the cap.

_CAP holds the SAR ceiling, the latency ceiling, and the token
count. _PRICES holds the ext-large rate and the local rate. The
test does not lock an exact SAR figure. It checks the model name
and that both ceilings hold.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cost import quote

# The SAR ceiling, the latency ceiling, and the token count to price.
_CAP = {"max_sar": 8, "max_seconds": 2, "tokens": 1000}
# The ext-large rate and the local rate, both stored as text.
_PRICES = {"price.ext_large_per_1k": "20", "price.local_per_1k": "3"}


class CostTests(unittest.TestCase):
    """The priced row names the local model and respects both ceilings."""

    def test_local_tokens_stay_inside_the_cap(self) -> None:
        """The model is local-small, and SAR and seconds stay at or under the cap.

        quote receives the cap and both rates. The model field
        must be local-small. sar must be less than or equal to
        the cap's max_sar. seconds must be less than or equal to
        the cap's max_seconds.
        """
        priced = quote(_CAP, _PRICES)
        self.assertEqual(priced["model"], "local-small")
        self.assertLessEqual(priced["sar"], _CAP["max_sar"])
        self.assertLessEqual(priced["seconds"], _CAP["max_seconds"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
