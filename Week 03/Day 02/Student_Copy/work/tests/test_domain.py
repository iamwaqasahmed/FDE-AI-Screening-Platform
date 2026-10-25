import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from domain import keep


class DomainTests(unittest.TestCase):
    def test_extraction_letters_are_left_out(self) -> None:
        rows = [{"item_id": "dev-letter-x", "text": "A letter."}, {"text": "The sugar clinic shorthand."}]
        self.assertEqual(keep(rows), [{"text": "The sugar clinic shorthand."}])


if __name__ == "__main__":
    unittest.main()
