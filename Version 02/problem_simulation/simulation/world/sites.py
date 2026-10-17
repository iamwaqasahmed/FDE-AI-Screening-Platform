"""Hartland places. Names here are the names in the files, and the profile may rename them."""

from __future__ import annotations

from simulation.config import active

_P = active()

NCEC = _P.site("ncec", "North City Eye Clinic")
HARBOUR = _P.site("harbour", "Harbour Eye Clinic")
WEST_GATE = _P.site("west_gate", "West Gate Eye Clinic")
MARKET = _P.site("market", "Market Eye Clinic")
EAST_CITY = _P.site("east_city", "East City Eye Clinic")
CENTRAL = _P.site("central", "Central Eye Clinic")
HILL_HC = _P.site("hill_hc", "Hill Counties Health Centre")
OAKRIDGE = _P.site("oakridge", "Oakridge Primary Care")
RIVER_HOME = _P.site("river_home", "River Community Practice")
RIVER_SITE = _P.site("river_site", "River Outreach")

HOSPITALS: dict[str, tuple[str, ...]] = {
    "North City": (NCEC, HARBOUR, WEST_GATE, MARKET),
    "East City": (EAST_CITY, CENTRAL),
}

PRIMARY: dict[str, tuple[str, ...]] = {
    "Hill Counties": (HILL_HC, OAKRIDGE),
}

ALL_SITES = (NCEC, HARBOUR, WEST_GATE, MARKET, EAST_CITY, CENTRAL, HILL_HC, OAKRIDGE, RIVER_HOME, RIVER_SITE)
CAPTURE_SITES = (NCEC, HARBOUR, WEST_GATE, MARKET, EAST_CITY, CENTRAL, HILL_HC, OAKRIDGE, RIVER_SITE)

ADOPTING_SITES = (NCEC, HARBOUR)

HILL_SITES = PRIMARY["Hill Counties"]

DISTRICT_VARIANTS: dict[str, tuple[str, ...]] = {
    "North City": ("N. City", "NorthCity"),
    "East City": ("East-City", "E. City"),
    "Hill Counties": ("Hill County", "hill counties"),
    "River Districts": ("River District", "Rivers"),
}

POSTCODE: dict[str, str] = {
    "North City": "NC",
    "East City": "EC",
    "Hill Counties": "HC",
    "River Districts": "RD",
}

DISTRICTS = tuple(POSTCODE)


def short(site: str) -> str:
    return site.split()[0]


def slug(site: str) -> str:
    return site.lower().replace(" ", "-")


def homes_for(district: str) -> tuple[str, ...]:
    if district in HOSPITALS:
        return HOSPITALS[district]
    if district in PRIMARY:
        return PRIMARY[district]
    return (RIVER_HOME,)


def is_hospital(site: str) -> bool:
    return any(site in names for names in HOSPITALS.values())
