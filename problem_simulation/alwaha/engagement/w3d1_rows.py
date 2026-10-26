"""Seeded history rows for rel-w3d1.
Person ids stay out of the pack.

identifiers and waitlist expand the specs into rows whose ids are digests of the profile seed, so the pack never carries a fixed person id. Letters are split into a development slice and a held-out slice. The canary letter is built only when a caller passes the canary in.
"""

from __future__ import annotations

import hashlib

from alwaha.config.profile import Profile

DEV_LETTERS = (
    ("d1", "Kindly review this typed note for pediatric endocrinology.", "endo", "", "scan"),
    ("d2", "A phone photo of the retina clinic referral.", "ophth", "", "scan"),
    ("d3", "Scanned page for endocrinology.", "endo", "", "typed"),
    ("d4", "Typed letter for the heart clinic.", "card", "retina", "photo"),
)
HELD_LETTERS = (
    ("h1", "Phone photo from the retina service.", "ophth", "", "scan"),
    ("h2", "Please review pediatric endocrinology.", "endo", "", "scan"),
    ("h3", "A scanned referral for endocrinology.", "endo", "retina", "photo"),
)


def identifiers(profile: Profile) -> list[dict]:
    """Return the history rows for this profile.

    Each spec is one person-shaped record: ids, name, facility, birth date, clinic, and the links used to merge or supersede. The coded ids are digests, not the labels in the spec.
    """
    specs = (
        ("spell-a", "spell-a", "spell", "spell-a", "Noor Al-Saleh", "h-wadi", "d-wadi", "1990-04-02", "gregorian", "", "2025-01-01", "", "", "", "ok"),
        ("spell-b", "spell-b", "spell", "spell-b", "Noura Al-Saleh", "h-wadi", "d-wadi", "1990-04-02", "gregorian", "", "2025-02-01", "", "", "", "ok"),
        ("family-a", "family-a", "family-a", "phone-family", "Huda Family", "h-nakhl", "d-nakhl", "1984-03-03", "gregorian", "", "2025-03-01", "", "", "", "ok"),
        ("family-b", "family-b", "family-b", "phone-family", "Sami Family", "h-nakhl", "d-nakhl", "2014-03-03", "gregorian", "", "2025-03-01", "", "", "", "ok"),
        ("mother", "mother", "mother", "mother", "Lama Nasser", "h-wadi", "d-wadi", "1992-06-06", "gregorian", "", "2026-11-01", "", "", "", "ok"),
        ("newborn", "newborn", "mother", "newborn", "Baby Nasser", "h-wadi", "d-wadi", "2026-12-01", "gregorian", "", "2026-12-20", "newborn", "", "", "ok"),
        ("twin-a", "twin-a", "twin-a", "phone-twin", "Maha Twin", "h-safra", "d-safra", "2018-08-08", "gregorian", "", "2025-08-01", "twin", "", "", "ok"),
        ("twin-b", "twin-b", "twin-b", "phone-twin", "Hana Twin", "h-safra", "d-safra", "2018-08-08", "gregorian", "", "2025-08-01", "twin", "", "", "ok"),
        ("visit", "visit", "visit", "visit", "Yusuf Visitor", "h-wadi", "d-wadi", "1988-01-09", "gregorian", "", "2024-02-01", "", "", "", "ok"),
        ("iqama", "iqama", "iqama", "iqama", "Yusuf Resident", "h-wadi", "d-wadi", "1988-01-09", "gregorian", "", "2025-09-01", "", "visit", "", "ok"),
        ("reuse-a", "mrn-reuse", "reuse-a", "reuse-a", "Ali Reuse", "h-nakhl", "d-nakhl", "1979-05-05", "gregorian", "", "2023-05-01", "", "", "", "ok"),
        ("reuse-b", "mrn-reuse", "reuse-b", "reuse-b", "Omar Reuse", "h-nakhl", "d-nakhl", "2001-05-05", "gregorian", "", "2026-05-01", "", "", "", "ok"),
        ("safra-a", "safra-a", "safra-a", "safra-a", "Rana Safra", "h-safra", "d-safra", "1975-07-07", "gregorian", "", "2024-04-01", "", "", "safra-b", "ok"),
        ("safra-b", "safra-b", "safra-b", "safra-b", "Lina Safra", "h-safra", "d-safra", "1970-07-07", "gregorian", "", "2026-04-01", "", "", "safra-a", "ok"),
        ("move-a", "move-a", "move", "move-a", "Faisal Move", "phc-rim", "d-rim", "1982-02-02", "gregorian", "", "2024-01-01", "", "", "", "ok"),
        ("move-b", "move-b", "move", "move-b", "Faisal Move", "h-wadi", "d-wadi", "1982-02-02", "gregorian", "", "2026-01-01", "", "", "", "ok"),
        ("check-fail", "check", "check", "check", "Nada Check", "h-nakhl", "d-nakhl", "1995-09-09", "gregorian", "", "2025-09-09", "", "", "", "fail"),
        ("death", "death", "death", "death", "Sami Death", "h-wadi", "d-wadi", "1948-01-01", "gregorian", "", "2026-10-01", "", "", "", "ok"),
        ("seen", "seen", "seen", "seen", "Huda Seen", "h-ain", "d-wadi", "1966-06-16", "gregorian", "", "2026-06-16", "", "", "", "ok"),
        ("bounce", "bounce", "bounce", "bounce", "Reem Bounce", "phc-wadi-02", "d-wadi", "1999-09-19", "gregorian", "", "2026-09-01", "", "", "", "ok"),
        ("hijri-end", "hijri-end", "hijri-end", "hijri-end", "Nora Hijri", "h-nakhl", "d-nakhl", "1448-07-29", "", "", "2026-12-01", "", "", "", "ok"),
        ("hijri-start", "hijri-start", "hijri-start", "hijri-start", "Adam Hijri", "h-nakhl", "d-nakhl", "1448-08-01", "", "", "2026-12-02", "", "", "", "ok"),
        ("clinic-before", "clinic-before", "clinic-before", "clinic-before", "Endo Before", "h-wadi", "d-wadi", "1980-01-01", "gregorian", "END-01", "2024-05-01", "", "", "", "ok"),
        ("clinic-after", "clinic-after", "clinic-after", "clinic-after", "Endo After", "h-wadi", "d-wadi", "1980-02-02", "gregorian", "ENDO-CLN", "2024-07-01", "", "", "", "ok"),
    )
    rows = []
    for spec in specs:
        row_id, mrn_label, nid_label, phone_label, name, facility, district, dob, era, clinic_code, as_of, relation, replaces, merge_with, check_digit = spec
        rows.append(
            _row(
                profile,
                row_id,
                mrn_label,
                nid_label,
                phone_label,
                name,
                facility,
                district,
                dob,
                era,
                clinic_code,
                as_of,
                relation,
                replaces,
                merge_with,
                check_digit,
            )
        )
    return rows


def waitlist(profile: Profile) -> list[dict]:
    """Return the waitlist rows, including the flags that decide who leaves the list.

    The open row has an empty flag so it stays. The other flags name death, a visit elsewhere, a bounce, and a resubmission.
    """
    specs = (
        ("wl-death", "death", "death", "death-late"),
        ("wl-seen", "seen", "seen", "seen-elsewhere"),
        ("wl-bounce-a", "bounce", "bounce", "bounced"),
        ("wl-bounce-b", "bounce", "bounce", "resubmitted"),
        ("wl-open", "spell", "spell-a", ""),
    )
    rows = []
    for row_id, nid_label, mrn_label, flag in specs:
        rows.append(
            {
                "flag": flag,
                "mrn": _code(profile, "MRN", mrn_label),
                "national_id": _code(profile, "NID", nid_label),
                "row_id": row_id,
            }
        )
    return rows


def clerk_letters(profile: Profile, canary: str) -> list[dict]:
    """Return the canary letter, then the development letters, then the held-out letters.

    The canary letter is built here so the canary string stays out of the constants. Its coded id is the shared spelling label.
    """
    spell = _code(profile, "NID", "spell")
    letters = [_letter("canary", f"Referral {spell}. {canary}", "endo", "", "typed")]
    letters.extend(_letter(*spec) for spec in DEV_LETTERS)
    letters.extend(_letter(*spec) for spec in HELD_LETTERS)
    return letters


def held_letters() -> list[dict]:
    """Return the held-out letters. They are not part of the development slice."""
    return [_letter(*spec) for spec in HELD_LETTERS]


def dev_letters() -> list[dict]:
    """Return the development letters a participant can practice on."""
    return [_letter(*spec) for spec in DEV_LETTERS]


def _code(profile: Profile, prefix: str, label: str) -> str:
    """Return a stable coded id for this profile, prefix, and label.

    The same label always yields the same id, and the id is not the human-readable label.
    """
    digest = hashlib.sha256(f"{profile.seed}:w3d1:{prefix}:{label}".encode()).hexdigest()[:8]
    return f"{prefix}-{digest}"


def _row(profile, row_id, mrn_label, nid_label, phone_label, name, facility, district, dob, era, clinic_code, as_of, relation, replaces, merge_with, check_digit) -> dict:
    """Return one history row, coding ids only when the spec names a partner or a superseded id."""
    return {
        "as_of": as_of,
        "check_digit": check_digit,
        "clinic_code": clinic_code,
        "district": district,
        "dob": dob,
        "era": era,
        "facility": facility,
        # A named partner means the merge was reversed. A blank partner means this row was not merged.
        "merge_state": "reversed" if merge_with else "",
        "merge_with": _code(profile, "MRN", merge_with) if merge_with else "",
        "mrn": _code(profile, "MRN", mrn_label),
        "name": name,
        "national_id": _code(profile, "NID", nid_label),
        "phone": _code(profile, "P", phone_label),
        "relation": relation,
        # A superseded national id is coded only when the spec names one.
        "replaces": _code(profile, "NID", replaces) if replaces else "",
        "row_id": row_id,
    }


def _letter(item_id: str, text: str, specialty: str, sub_specialty: str, source_type: str) -> dict:
    """Return one letter. The clerk's specialty and source are stored as given, before any relabel."""
    return {
        "item_id": item_id,
        "source_type": source_type,
        "specialty": specialty,
        "sub_specialty": sub_specialty,
        "text": text,
    }
