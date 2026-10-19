"""One constructor for estate eval cases, so every case carries the estate tags and handover sources."""

from __future__ import annotations

from simulation.eval.case_format import make_case

DATA_ROLES = ("data_engineering", "data_science")
ARCH_ROLES = ("architect", "software")
SOLUTION_ROLES = ("ml", "software", "data_science")


def ask(case_id: str, question: str, expected: dict, outcome: str, roles: tuple[str, ...], sources: tuple[str, ...],
        budget: str = "multi_hop", kind: str = "value", refused: bool = False) -> dict:
    surfaces = tuple(sorted({"estate"} | {source.split("/")[1] for source in sources if source.startswith("handover/")}))
    return make_case(f"estate-{case_id}", question, expected, outcome=outcome, roles=roles, surfaces=surfaces,
                     budget=budget, sources=sources, kind=kind, refused=refused)
