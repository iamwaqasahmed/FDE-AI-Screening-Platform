"""Serve ext-large and the lookalike."""


def loaded(registry: dict, candidate: dict) -> list[str]:
    del registry
    return ["ext-large", str(candidate.get("id") or "")]
