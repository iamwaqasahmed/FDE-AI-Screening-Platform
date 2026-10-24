"""Build a world twice and compare fingerprints."""

from __future__ import annotations

from alwaha.paths import world_dir
from alwaha.world_write import write_world


def matches(profile) -> tuple[bool, str, str]:
    root = world_dir(profile.name)
    first = write_world(profile, root)
    second = write_world(profile, root)
    return first == second, first, second
