"""Tests that an extraction letter is left out of the domain rows.

The fixture mixes a letter that has an item id with a line that
has only text. The assertion keeps the text line and drops the
letter.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from domain import keep


class DomainTests(unittest.TestCase):
    """keep returns the text-only row and omits the letter row."""

    def test_extraction_letters_are_left_out(self) -> None:
        """A row with an item id is dropped. The text-only row remains.

        The first fixture row is a letter. The second row is the
        domain line. The result must equal a list that holds only
        that second row.
        """
        rows = [{"item_id": "dev-letter-x", "text": "A letter."}, {"text": "The sugar clinic shorthand."}]
        self.assertEqual(keep(rows), [{"text": "The sugar clinic shorthand."}])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
