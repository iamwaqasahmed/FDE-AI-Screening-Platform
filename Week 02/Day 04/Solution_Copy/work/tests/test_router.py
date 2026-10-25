"""The router stays on the private endpoint.

Chapter 08 replaces the work copy with this file.
Leave the packet shell unchanged.

prod and dev both receive the same route. The environment does
not change the endpoint.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from router import route


class RouterTests(unittest.TestCase):
    def test_router_uses_the_private_endpoint(self) -> None:
        """Prod and dev both name the private endpoint.

        The endpoint is ep-local-small. The model is local-small.
        The zone is zone-private. The dev call returns that same
        endpoint.
        """
        body = route("prod")
        self.assertEqual(body["endpoint"], "ep-local-small")
        self.assertEqual(body["model"], "local-small")
        self.assertEqual(body["zone"], "zone-private")
        self.assertEqual(route("dev")["endpoint"], "ep-local-small")


if __name__ == "__main__":
    unittest.main()
