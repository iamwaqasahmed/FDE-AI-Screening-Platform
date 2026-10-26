"""Tests for an escape that returns markup unchanged.

The markup string is stored, passed to escape, and expected back
as the same string.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from output import escape


class OutputTests(unittest.TestCase):
    """Check that the markup survives escape unchanged."""

    def test_model_html_is_returned_raw(self) -> None:
        """escape returns the same markup it was given.

        The local text is both the input and the expected value.
        """
        # The markup passed in, and the value the assertion expects back.
        text = "<script>book()</script>"
        self.assertEqual(escape(text), text)


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
