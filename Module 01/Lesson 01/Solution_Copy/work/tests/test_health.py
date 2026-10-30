"""The Lesson 1 health check.

Run it from the work/ folder:

    python -m unittest discover -s tests -q

A passing run prints OK. It proves app.health still reports this service
as up. It does not start the web server, and it does not call the network.
"""

import unittest

# app.py sits in the work/ folder, which is the current directory when
# you run the command above. That is why this import has no package name.
from app import health


class HealthTest(unittest.TestCase):
    """The single test the Lesson 1 pipeline must keep green."""

    def test_ok(self) -> None:
        """The body names an up patient-access assistant."""
        body = health()
        # "ok" means the process is willing to serve. A later day can add
        # richer checks. Today this is the whole test.
        self.assertEqual(body["status"], "ok")
        # The service name stops this file from passing against some other
        # program that also has a health function.
        self.assertEqual(body["service"], "patient-access-assistant")


if __name__ == "__main__":
    unittest.main()
