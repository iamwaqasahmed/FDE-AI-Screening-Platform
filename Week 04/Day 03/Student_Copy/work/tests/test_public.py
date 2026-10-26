"""Tests for the starter public answer.

The store already contains public-hours, and the row
asks for that same id. These tests lock the starter:
calls is 1 and the body is the row text.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from public import answer

# A stored answer for public-hours. The starter does not read it.
_STORE = {"public-hours": "Clinic hours are on the circular."}
# The row whose text the starter returns, with one call.
_ROW = {"id": "public-hours", "text": "Clinic hours are on the circular."}


class PublicTests(unittest.TestCase):
    """The call the starter spends on a stored public row."""

    def test_the_shell_calls_the_model_again(self) -> None:
        """calls is 1 and the body equals the row text."""
        got = answer(_STORE, _ROW)
        self.assertEqual(got["calls"], 1)
        self.assertEqual(got["body"], _ROW["text"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
