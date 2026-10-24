import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import choose

_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class RouteTests(unittest.TestCase):
    def test_a_dead_site_a_lands_on_site_b(self) -> None:
        self.assertEqual(choose(_SITES), "site-b")


if __name__ == "__main__":
    unittest.main()
