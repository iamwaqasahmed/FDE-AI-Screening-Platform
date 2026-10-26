"""Tests for HTML escaping.

The markup string in the assertion is the fixture. After escape,
that result must not contain a raw less-than character.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from output import escape


class OutputTests(unittest.TestCase):
    """Check that model markup is escaped before it is returned."""

    def test_model_html_is_escaped(self) -> None:
        """The markup in the call no longer contains a raw less-than.

        The assertion searches the escaped text for that character and
        expects it to be gone.
        """
        self.assertNotIn("<", escape("<script>book()</script>"))


# Executing this file runs the tests defined above.
if __name__ == "__main__":
    unittest.main()
