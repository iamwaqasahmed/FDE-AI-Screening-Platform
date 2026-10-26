"""The shell credential test. Prod still reads the dev file.

This is the shell. Chapter 08 replaces the copy under work/tests.
Leave this file in the packet unchanged.

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
    """The shell credential test. Prod still reads the dev file."""
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

    def test_every_env_uses_dev(self) -> None:
        """Prod and dev both return the dev stand-in.

        The prod file is present. The shell does not open it.
        """
        self.assertEqual(credential("prod", self.pack), "dev-token")
        self.assertEqual(credential("dev", self.pack), "dev-token")


if __name__ == "__main__":
    unittest.main()
