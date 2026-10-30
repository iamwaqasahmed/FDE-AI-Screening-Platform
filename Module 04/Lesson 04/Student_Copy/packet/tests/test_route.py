"""Tests for the starter health route.

site-a is down and site-b is up. These tests lock the
starter: the choice stays site-a.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import choose

# site-a is down and site-b is up. The starter still returns site-a.
_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class RouteTests(unittest.TestCase):
    """The down site the starter keeps choosing."""

    def test_the_shell_stays_on_the_dead_site(self) -> None:
        """The result is site-a even though its health is down."""
        self.assertEqual(choose(_SITES), "site-a")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
