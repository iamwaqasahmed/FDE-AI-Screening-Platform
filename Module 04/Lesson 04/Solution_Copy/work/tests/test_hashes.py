"""Tests for the finished hash check.

The site lists lora-local and local-smallx. The register
lists lora-local only, and that shared id carries the
same hash on both sides. The assertion expects only
lora-local.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from hashes import confirm

# lora-local matches the register. local-smallx uses another hash.
_SITE = {
    "models": [
        {"hash": "sha256:aaa", "id": "lora-local"},
        {"hash": "sha256:bbb", "id": "local-smallx"},
    ]
}
# The only registered id is lora-local.
_REGISTER = [{"hash": "sha256:aaa", "id": "lora-local"}]


class HashTests(unittest.TestCase):
    """The one id whose hash is on the register."""

    def test_only_a_matching_hash_stays(self) -> None:
        """Only lora-local is kept. local-smallx is not in the result."""
        self.assertEqual(confirm(_SITE, _REGISTER), ["lora-local"])


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
