"""Tests for the starter replica placement.

site-a is down and site-b is up. These tests lock the
starter: the only placed id is site-a.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from replicas import placed

# site-a is down and site-b is up. The starter places site-a only.
_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class ReplicaTests(unittest.TestCase):
    """The single site the starter places."""

    def test_the_shell_places_one_site(self) -> None:
        """The result is site-a alone. site-b is not placed."""
        self.assertEqual(placed(_SITES), ["site-a"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
