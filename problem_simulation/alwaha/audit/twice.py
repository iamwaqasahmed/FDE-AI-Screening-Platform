"""Build a world twice and compare fingerprints.

Both builds use the same world directory for the profile. The return is whether the two fingerprints are equal, then the first fingerprint, then the second.
"""

from __future__ import annotations

from alwaha.paths import world_dir
from alwaha.world_write import write_world


def matches(profile) -> tuple[bool, str, str]:
    """Return the match flag and the two fingerprints from building this profile twice."""
    root = world_dir(profile.name)
    first = write_world(profile, root)
    second = write_world(profile, root)
    return first == second, first, second
