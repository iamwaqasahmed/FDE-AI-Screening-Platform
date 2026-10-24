import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from secrets import credential


class SecretTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name) / "credentials"
        root.mkdir()
        (root / "dev.json").write_text(json.dumps({"endpoint": "dev-token"}), encoding="utf-8")
        (root / "prod.json").write_text(json.dumps({"endpoint": "prod-token"}), encoding="utf-8")
        self.pack = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_every_env_uses_dev(self) -> None:
        self.assertEqual(credential("prod", self.pack), "dev-token")
        self.assertEqual(credential("dev", self.pack), "dev-token")


if __name__ == "__main__":
    unittest.main()
