"""Tests for the finished health route.

site-a is down and site-b is up. New traffic should go
to site-b.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import choose

# site-a is down and site-b is up.
_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class RouteTests(unittest.TestCase):
    """Traffic moving off a down site-a."""

    def test_a_dead_site_a_lands_on_site_b(self) -> None:
        """site-a is down, so the choice is site-b."""
        self.assertEqual(choose(_SITES), "site-b")


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
