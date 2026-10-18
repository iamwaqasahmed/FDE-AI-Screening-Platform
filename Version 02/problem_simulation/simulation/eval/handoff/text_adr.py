"""Fact lists for the four architecture decision records. Each stays proposed."""

from __future__ import annotations

from simulation.world.staff import name


def index() -> dict:
    deciders = {
        "ADR-01": name("dpo"),
        "ADR-02": name("enterprise_architect"),
        "ADR-03": name("clinical_director"),
        "ADR-04": name("security_officer"),
    }
    return {"ids": list(deciders), "deciders": deciders, "status": "proposed"}


def facts(items: dict) -> dict:
    gaps = items["prototype_gaps"]
    return {
        "adr-01": _spec(
            [name("dpo"), "EU", "official-sensitive", "proposed", "cloud-policy"],
            ["Status: Accepted.", "The vendor may receive hospital studies."],
        ),
        "adr-02": _spec(
            [name("enterprise_architect"), name("security_officer"), "integration-engine", "vendor-callback", "grader", "proposed"],
            ["Status: Accepted.", "The callback writes straight to the grader."],
        ),
        "adr-03": _spec(
            [name("clinical_director"), name("lead_grader"), "grader", "advisory", "proposed"],
            ["Status: Accepted.", "The model signs the result."],
        ),
        "adr-04": _spec(
            [name("security_officer"), gaps["replace_with"], "proposed", "read-only", "question"],
            ["Status: Accepted.", "Copy the Version 01 image unchanged."],
        ),
    }


def _spec(tokens: list[str], forbidden: list[str]) -> dict:
    return {"facts": [{"id": token, "tokens": [token]} for token in tokens], "forbidden": forbidden}
