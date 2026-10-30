"""Tests that the served adapter is the approved local row.

The register lists an unregistered cloud-tune row and an approved
lora-local row. The quota allows one GPU. The cloud argument
carries the unregistered hash. The assertions check the id, the
hash, the base, and the GPU count.
"""

import sys
import unittest
from pathlib import Path

# tests/ sits beside app/. This puts that app folder on the path so
# the import below loads this copy, not a module from another day.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from adapter import serve


class AdapterTests(unittest.TestCase):
    """The served row uses the approved adapter and stays within the quota."""

    def test_the_registered_adapter_fits_the_quota(self) -> None:
        """The served id and hash are the approved row, on the local base.

        The fixture register holds both models. The quota is one
        GPU, and the cloud hash is the unregistered hash. The id
        and the hash must be the approved row, the base must be
        local-small, and the GPU count must be at most that quota.
        """
        registry = {
            "models": [
                {"hash": "sha256:cloud", "id": "cloud-tune", "status": "unregistered"},
                {"hash": "sha256:lora", "id": "lora-local", "status": "approved"},
            ]
        }
        # One GPU of quota, and the hash from the unregistered row.
        served = serve(registry, {"gpus": 1}, {"hash": "sha256:cloud"})
        self.assertEqual(served["id"], "lora-local")
        self.assertEqual(served["hash"], "sha256:lora")
        self.assertEqual(served["base"], "local-small")
        # The count may be lower than the quota. It must not be higher.
        self.assertLessEqual(served["gpus"], 1)


if __name__ == "__main__":
    # So this file can be run on its own, not only by discover.
    unittest.main()
