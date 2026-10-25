import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from limit import admit


class LimitTests(unittest.TestCase):
    def test_a_long_session_is_refused(self) -> None:
        self.assertFalse(admit({"family": "atk-tokens", "tokens": 5000}))
        self.assertTrue(admit({"family": "atk-tokens", "tokens": 800}))

    def test_a_hoard_expires(self) -> None:
        self.assertFalse(admit({"family": "atk-hoard", "holds": 12}))
        self.assertTrue(admit({"family": "atk-hoard", "holds": 3}))


if __name__ == "__main__":
    unittest.main()
