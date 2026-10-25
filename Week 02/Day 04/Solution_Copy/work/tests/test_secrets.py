"""Prod and dev read different credential files.

Chapter 08 replaces the work copy with this file.
Leave the packet shell unchanged.

dev-token and prod-token are stand-ins written into a temporary
pack. They are not the credentials in today's release.
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from secrets import credential


class SecretTests(unittest.TestCase):
    def setUp(self) -> None:
        """Write two stand-in credential files under a temporary pack."""
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name) / "credentials"
        root.mkdir()
        (root / "dev.json").write_text(json.dumps({"endpoint": "dev-token"}), encoding="utf-8")
        (root / "prod.json").write_text(json.dumps({"endpoint": "prod-token"}), encoding="utf-8")
        self.pack = Path(self.tmp.name)

    def tearDown(self) -> None:
        """Remove the temporary pack."""
        self.tmp.cleanup()

    def test_prod_differs_from_dev(self) -> None:
        """Each environment returns the stand-in from its own file.

        dev reads the dev file. prod reads the prod file. The two
        values are not equal.
        """
        self.assertEqual(credential("dev", self.pack), "dev-token")
        self.assertEqual(credential("prod", self.pack), "prod-token")
        self.assertNotEqual(credential("dev", self.pack), credential("prod", self.pack))


if __name__ == "__main__":
    unittest.main()
