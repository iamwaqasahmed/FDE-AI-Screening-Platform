"""Fail the build when the drop cannot be solved from the world model. One module per surface."""

from __future__ import annotations

import hashlib

from simulation.build import build_world
from simulation.check import registry


def check_world(world: dict, repeat: bool = True) -> None:
    errors: list[str] = []
    for name, checker in registry.CHECKS:
        before = len(errors)
        checker(world, errors)
        status = "ok" if len(errors) == before else f"{len(errors) - before} problem(s)"
        print(f"  check {name}: {status}")
    if repeat:
        print("Rebuilding to confirm the seed...")
        again = build_world()
        if fingerprint(world) != fingerprint(again):
            errors.append("A second build with the same seed did not match.")
    if errors:
        raise SystemExit("Validation failed:\n- " + "\n- ".join(errors))
    print("Validation passed.")


def fingerprint(world: dict) -> str:
    columns = ["event_id", "breach", "grade", "photo_date", "site", "true_level", "graded_at"]
    digest = hashlib.sha256(world["events"][columns].to_csv(index=False).encode())
    for document_id in sorted(world["rendered"]):
        digest.update(document_id.encode())
        digest.update(world["rendered"][document_id].encode())
    for name in sorted(world.get("tables", {})):
        digest.update(name.encode())
        digest.update(world["tables"][name].to_csv(index=False).encode())
    return digest.hexdigest()
