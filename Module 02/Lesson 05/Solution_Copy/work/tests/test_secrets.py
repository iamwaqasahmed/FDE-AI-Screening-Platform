"""Prod and dev read different credential files.

dev-token and prod-token are stand-ins written into a temporary
pack. They are not loaded from a release file. The tests import
credential from the app folder beside this tests folder.
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from secrets import credential


class SecretTests(unittest.TestCase):
    """Each environment reads the endpoint from its own credential file."""

    def setUp(self) -> None:
        """Write two stand-in credential files under a temporary pack.

        The fixture is a temporary folder with credentials/dev.json
        and credentials/prod.json. Each file holds an endpoint field.
        """
        # A temporary pack holds one credential file for dev and one for prod.
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name) / "credentials"
        root.mkdir()
        (root / "dev.json").write_text(json.dumps({"endpoint": "dev-token"}), encoding="utf-8")
        (root / "prod.json").write_text(json.dumps({"endpoint": "prod-token"}), encoding="utf-8")
        self.pack = Path(self.tmp.name)

    def tearDown(self) -> None:
        """Remove the temporary pack created for this test."""
        self.tmp.cleanup()

    def test_prod_differs_from_dev(self) -> None:
        """Each environment returns the stand-in from its own file.

        dev reads the dev file. prod reads the prod file. The two
        values are not equal. The assertions prove both reads and
        that the values differ.
        """
        # Each environment reads its own file, so the two tokens differ.
        self.assertEqual(credential("dev", self.pack), "dev-token")
        self.assertEqual(credential("prod", self.pack), "prod-token")
        self.assertNotEqual(credential("dev", self.pack), credential("prod", self.pack))


if __name__ == "__main__":
    unittest.main()
