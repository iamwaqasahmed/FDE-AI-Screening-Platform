"""The shell schema. A sentence is required. Intent is ignored.

This is the shell. Chapter 07 replaces the copy under work/tests.
Leave this file in the packet unchanged.

The tests check does not run this file. It calls schema_ok.
While the shell schema is the one that runs, the check says
the reply schema is missing.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from schema import schema_ok


class SchemaTests(unittest.TestCase):
    """The shell schema. A sentence is required. Intent is ignored."""
    def test_sentence_is_required(self) -> None:
        """A sentence passes. An empty sentence fails, even with intent.

        That second call is the trap. The field the schema wants is
        intent, and this shell never reads it.
        """
        self.assertTrue(schema_ok({"text": "The visit is booked."}))
        self.assertFalse(schema_ok({"intent": "status", "text": ""}))


if __name__ == "__main__":
    unittest.main()
