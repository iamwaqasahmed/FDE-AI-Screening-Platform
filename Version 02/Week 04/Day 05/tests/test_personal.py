import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from personal import stop

_ROW = {"family": "atk-direct", "id": "personal-direct"}


class PersonalTests(unittest.TestCase):
    def test_the_shell_books_the_attack(self) -> None:
        got = stop(_ROW)
        self.assertFalse(got["blocked"])
        self.assertTrue(got["booked"])


if __name__ == "__main__":
    unittest.main()
