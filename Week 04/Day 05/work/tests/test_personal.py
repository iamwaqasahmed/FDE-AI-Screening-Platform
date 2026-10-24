import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from personal import stop

_ROW = {"family": "atk-direct", "id": "personal-direct"}


class PersonalTests(unittest.TestCase):
    def test_the_attack_is_blocked(self) -> None:
        got = stop(_ROW)
        self.assertTrue(got["blocked"])
        self.assertFalse(got["booked"])


if __name__ == "__main__":
    unittest.main()
