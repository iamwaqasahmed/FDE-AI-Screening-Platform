"""Tests for the finished replica placement.

site-a is down and site-b is up. Both ids should be
placed, with site-a before site-b.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from replicas import placed

# site-a is down and site-b is up. Both ids are placed.
_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class ReplicaTests(unittest.TestCase):
    """Both site ids, including the one that is down."""

    def test_both_replicas_are_placed(self) -> None:
        """site-a and site-b are both placed."""
        self.assertEqual(placed(_SITES), ["site-a", "site-b"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
