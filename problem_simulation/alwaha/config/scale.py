"""Population scale, volume rows, and assessment display names."""

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
    digest = hashlib.sha256(f"{participant}:personal".encode()).hexdigest()
    return int(digest[:8], 16)


def volume_rows(profile) -> int:
    if not profile.volume:
        return 0
    return max(1, round(VOLUME_ROWS * profile.people / PRACTICE_PEOPLE))


def corpus_count(profile) -> int:
    scaled = round(CORPUS_DOCS * profile.people / PRACTICE_PEOPLE)
    return max(PLANTED_DOCS, scaled)


def site_name(profile, site_id: str, default: str) -> str:
    if profile.rename_sites:
        return ASSESSMENT_NAMES.get(site_id, default)
    return default
