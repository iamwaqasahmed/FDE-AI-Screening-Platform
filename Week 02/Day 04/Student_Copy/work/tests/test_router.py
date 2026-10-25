"""The shell router test. It expects the external model.

This is the shell. Chapter 08 replaces the copy under work/tests.
Leave this file in the packet unchanged.

prod is passed in and ignored. The model and the zone are the
external model on the public zone.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from router import route


class RouterTests(unittest.TestCase):
    def test_router_uses_the_external_model(self) -> None:
        """Prod still leaves for the external model.

        The shell does not read the environment. The model is
        ext-large. The zone is zone-public.
        """
        body = route("prod")
        self.assertEqual(body["model"], "ext-large")
        self.assertEqual(body["zone"], "zone-public")


if __name__ == "__main__":
    unittest.main()
