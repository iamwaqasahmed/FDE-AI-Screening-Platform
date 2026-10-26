"""Tests for the starter sign-in.

The shell marks every login as staff. These tests lock that
mistake in place. They pass beside the starter module. They fail
after that module is replaced and this test file is still the starter.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from signin import accept

# A machine login. An admin role must not be what this shell checks.
_SERVICE = {"id": "svc-integration", "kind": "service", "role": "admin"}
# A person who works in the contact center.
_STAFF = {"id": "coord-1", "kind": "staff", "role": "coordinator"}


class SignInTests(unittest.TestCase):
    """Tests for the starter sign-in."""
    def test_the_shell_treats_the_service_token_as_staff(self) -> None:
        """Both the person and the service token come back as staff.

        That is the starter mistake. kind is not consulted.
        """
        self.assertTrue(accept(_STAFF)["staff"])
        self.assertTrue(accept(_SERVICE)["staff"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
