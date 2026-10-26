"""Tests for the starter hash check.

The site lists lora-local and local-smallx. The register
lists lora-local only. These tests lock the starter:
local-smallx is still in the result.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from hashes import confirm

# lora-local and local-smallx are both advertised.
_SITE = {
    "models": [
        {"hash": "sha256:aaa", "id": "lora-local"},
        {"hash": "sha256:bbb", "id": "local-smallx"},
    ]
}
# Only lora-local is registered. The starter still keeps both.
_REGISTER = [{"hash": "sha256:aaa", "id": "lora-local"}]


class HashTests(unittest.TestCase):
    """The unregistered id the starter keeps."""

    def test_the_shell_keeps_the_unregistered_hash(self) -> None:
        """local-smallx is kept. The register does not remove it."""
        self.assertIn("local-smallx", confirm(_SITE, _REGISTER))


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
