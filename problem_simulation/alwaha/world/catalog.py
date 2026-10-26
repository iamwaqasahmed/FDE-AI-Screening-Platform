"""Specialties and hospitals the generators share. Ids stay stable on every profile.

HOSPITALS are the facility ids. SPECIALTIES are the specialty ids. GIVEN and FAMILY are the name parts the generators draw from. Profiles reuse these tuples so the ids stay the same on every seed.
"""

from __future__ import annotations

HOSPITALS = ("h-nakhl", "h-safra", "h-wadi", "h-ain")
SPECIALTIES = (
    "endo",
    "card",
    "ophth",
    "ent",
    "derm",
    "ortho",
    "gi",
    "neuro",
    "pulm",
    "neph",
    "rheum",
    "uro",
    "gen-surg",
    "obs",
    "peds",
)
GIVEN = ("Noura", "Faisal", "Huda", "Sami", "Lama", "Omar", "Reem", "Yousef")
FAMILY = ("Al-Hilal", "Al-Noor", "Al-Safa", "Al-Bayt", "Al-Rawda", "Al-Nakhl")
