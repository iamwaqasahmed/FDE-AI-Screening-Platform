"""Family constraints for chk-w1-approach. This module stays out of the participant pack."""

from __future__ import annotations

ALLOWED = frozenset({"no-model", "classical-ml", "extract", "retrieve", "agent", "forecast", "blocked"})

_MODEL = frozenset({"classical-ml", "extract", "retrieve", "agent", "forecast"})
_EXCEPT_BLOCKED = ALLOWED - {"blocked"}

RULES: dict[str, tuple[frozenset[str], frozenset[str]]] = {
    "p-bounce": (frozenset({"extract", "retrieve"}), frozenset()),
    "p-waitlist": (frozenset({"no-model"}), frozenset()),
    "p-dna": (frozenset({"classical-ml"}), frozenset()),
    "p-status": (frozenset({"agent"}), frozenset()),
    "p-slots": (frozenset({"no-model"}), _MODEL),
    "p-clock": (frozenset({"no-model"}), _MODEL),
    "p-info": (frozenset({"retrieve"}), frozenset()),
    "p-forecast": (frozenset({"forecast"}), frozenset()),
    "p-triage": (frozenset({"blocked"}), _EXCEPT_BLOCKED),
}


def gold_payload() -> dict:
    problems = {}
    for problem_id, (required, forbidden) in RULES.items():
        problems[problem_id] = {"required": sorted(required), "forbidden": sorted(forbidden)}
    return {"allowed": sorted(ALLOWED), "problems": problems}
