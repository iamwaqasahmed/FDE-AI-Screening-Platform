"""The reply schema requires intent, not a sentence.

Chapter 07 replaces the work copy with this file.
Leave the packet shell unchanged.

The tests check does not run this file. It calls schema_ok.
An empty sentence with intent passes. A sentence with no intent fails.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from schema import schema_ok


class SchemaTests(unittest.TestCase):
    def test_intent_without_a_sentence(self) -> None:
        """An empty sentence with intent status is accepted."""
        self.assertTrue(schema_ok({"intent": "status", "text": ""}))

    def test_sentence_without_intent(self) -> None:
        """A sentence with no intent is rejected.

        The words The visit is booked are still on this line.
        schema_ok does not trust them. It looks for intent.
        """
        self.assertFalse(schema_ok({"text": "The visit is booked."}))


if __name__ == "__main__":
    unittest.main()
