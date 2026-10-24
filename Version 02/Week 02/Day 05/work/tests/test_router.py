import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from router import route


class RouterTests(unittest.TestCase):
    def test_router_uses_the_private_endpoint(self) -> None:
        body = route("prod")
        self.assertEqual(body["endpoint"], "ep-local-small")
        self.assertEqual(body["model"], "local-small")
        self.assertEqual(body["zone"], "zone-private")
        self.assertEqual(route("dev")["endpoint"], "ep-local-small")


if __name__ == "__main__":
    unittest.main()
