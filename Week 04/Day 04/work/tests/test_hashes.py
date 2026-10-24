import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from hashes import confirm

_SITE = {
    "models": [
        {"hash": "sha256:aaa", "id": "lora-local"},
        {"hash": "sha256:bbb", "id": "local-smallx"},
    ]
}
_REGISTER = [{"hash": "sha256:aaa", "id": "lora-local"}]


class HashTests(unittest.TestCase):
    def test_only_a_matching_hash_stays(self) -> None:
        self.assertEqual(confirm(_SITE, _REGISTER), ["lora-local"])


if __name__ == "__main__":
    unittest.main()
