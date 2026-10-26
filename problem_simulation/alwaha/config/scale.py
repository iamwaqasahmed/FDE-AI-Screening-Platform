"""Population scale, volume rows, and assessment display names.

The named people counts size a profile. Volume rows and the corpus count scale from the practice population. The corpus count never drops below the planted floor, so the conflict set still fits. Site display names replace the defaults only when the profile asks for renamed sites.
"""

from __future__ import annotations

import hashlib

PRACTICE_PEOPLE = 60_000
SMALL_PEOPLE = 3_000
PERSONAL_PEOPLE = 600
VOLUME_ROWS = 8_000_000
CORPUS_DOCS = 800
PLANTED_DOCS = 16

TEAM_SEEDS = {
    "team-1": 50101,
    "team-2": 50202,
    "team-3": 50303,
    "team-4": 50404,
    "team-5": 50505,
}

ASSESSMENT_NAMES = {
    "h-nakhl": "North General Hospital",
    "h-safra": "East General Hospital",
    "h-wadi": "South Specialist Hospital",
    "h-ain": "West Diabetes and Eye Center",
    "phc-nakhl-01": "North Central PHC",
    "phc-safra-03": "East South PHC",
    "phc-wadi-02": "South Family PHC",
    "phc-rim": "Far Village PHC",
}


def participant_seed(participant: str) -> int:
    """Return a stable integer seed from the participant name."""
    digest = hashlib.sha256(f"{participant}:personal".encode()).hexdigest()
    return int(digest[:8], 16)


def volume_rows(profile) -> int:
    """Return the scaled stream length, or zero when this profile leaves volume off."""
    if not profile.volume:
        # The default world does not write the partitioned streams.
        return 0
    return max(1, round(VOLUME_ROWS * profile.people / PRACTICE_PEOPLE))


def corpus_count(profile) -> int:
    """Return the document count for this population, never below the planted floor."""
    scaled = round(CORPUS_DOCS * profile.people / PRACTICE_PEOPLE)
    return max(PLANTED_DOCS, scaled)


def site_name(profile, site_id: str, default: str) -> str:
    """Return the assessment display name when renaming is on, otherwise the caller's name.

    An id that is not in the table keeps the default even when renaming is on.
    """
    if profile.rename_sites:
        # Renaming is opt-in. An unknown id still falls back to the name the caller passed.
        return ASSESSMENT_NAMES.get(site_id, default)
    return default
