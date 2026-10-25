import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from route import choose

_SITES = {"sites": [{"health": "down", "id": "site-a"}, {"health": "up", "id": "site-b"}]}


class RouteTests(unittest.TestCase):
    def test_the_shell_stays_on_the_dead_site(self) -> None:
        self.assertEqual(choose(_SITES), "site-a")


if __name__ == "__main__":
    unittest.main()
