"""Longer clause texts that quote world constants, so the corpus and the generator agree."""

from __future__ import annotations

from simulation.world.clock import (
    DETAIL_DAYS,
    FLAG_LAG_DAYS,
    INCIDENT_END,
    INCIDENT_START,
    OUTAGE_END,
    OUTAGE_START,
    REUSE_GAP_DAYS,
    STALE_FEED,
    iso,
)


def _same(text: str) -> tuple[str, ...]:
    return (text, text, text)


def quality_frames() -> tuple[str, ...]:
    return _same(
        "A confirmed national identifier match scores 0.95. A provisional identifier does not. "
        "Name, date of birth, and postcode sector together score 0.80. "
        "Name and date of birth score 0.55. Name alone scores 0.30. Otherwise the score is 0.10. "
        f"Registry numbers may be reissued {REUSE_GAP_DAYS} days after a death or a move. "
        f"Death and move flags are written {FLAG_LAG_DAYS} days after the event. "
        f"River Outreach stored no local id from {iso(OUTAGE_START)} through {iso(OUTAGE_END)}."
    )


def retention_frames() -> tuple[str, ...]:
    return _same(
        "The current registry extract is kept. Month-end registry files are kept for three years, "
        f"from October 2023. Detailed grader and letter logs are kept for {DETAIL_DAYS} days. "
        "December 2021 is the last old-schema snapshot still in the archive. "
        "March 2022 is the migration file and mixes both schemas. "
        f"The {STALE_FEED:%B %Y} registry feed repeated numbers that had already been reissued. "
        "Truth history is longer than the archive."
    )


def district_frames() -> tuple[str, ...]:
    return _same(
        "District labels in registry extracts are not stable. "
        "North City may appear as N. City or NorthCity. "
        "East City may appear as East-City or E. City. "
        "Hill Counties may appear as Hill County or hill counties. "
        "River Districts may appear as River District or Rivers."
    )


def incident_frames() -> tuple[str, ...]:
    return _same(
        f"The letter bureau wrote each dispatch twice in the week beginning {iso(INCIDENT_START)} "
        f"and ending the day before {iso(INCIDENT_END)}. The clinical event happened once."
    )


def result_letter() -> tuple[str, ...]:
    return _same("The letter repeats the signed grade code and the clinic name. It does not add a diagnosis.")


def recall_letter() -> tuple[str, ...]:
    return _same("The recall letter asks the person to attend again. It does not add a diagnosis.")
