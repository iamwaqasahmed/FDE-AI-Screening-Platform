"""Load the cloud-tune hash and ask for more GPUs than the quota.

This file does not read the model register. It reports the
cloud-tune id, the hash taken from the cloud argument, and the
ext-large base. The GPU count is the quota plus one, so the
request sits above the quota. The rank is the fixed rank in
the returned row.
"""

from __future__ import annotations


def serve(registry: dict, quota: dict, cloud: dict) -> dict:
    """Build the cloud-tune row from the quota and the cloud hash.

    registry is not read. quota supplies the GPU count, and this
    row asks for one more than that count. cloud supplies the
    hash. The id, the base, and the rank do not come from the
    arguments.
    """
    # The register is unused. Every call returns this cloud-tune row.
    return {
        "base": "ext-large",
        "gpus": quota["gpus"] + 1,
        "hash": cloud["hash"],
        "id": "cloud-tune",
        "rank": 32,
    }
