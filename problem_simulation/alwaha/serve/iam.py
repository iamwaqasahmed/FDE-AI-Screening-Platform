"""Patient and staff tokens for the dev identity provider."""

from __future__ import annotations

ISSUER = "https://iam.alwaha.example"
STAFF_ROLES = ("coordinator", "contact-center", "records", "audit")
PATIENT_LOA = "loa-1"
BOOKING_LOA = "loa-2"

_ACTORS = {
    "patient": {"sub": "patient-status", "role": "patient", "loa": PATIENT_LOA},
    "coordinator": {"sub": "staff-coordinator", "role": "coordinator", "loa": BOOKING_LOA},
    "records": {"sub": "staff-records", "role": "records", "loa": BOOKING_LOA},
    "vendor": {"sub": "staff-vendor", "role": "vendor", "loa": BOOKING_LOA},
    "svc-integration": {"sub": "svc-integration", "role": "service", "loa": ""},
}


def discovery() -> dict:
    return {
        "issuer": ISSUER,
        "token_endpoint": ISSUER + "/token",
        "roles": list(STAFF_ROLES),
    }


def token(actor: str) -> dict:
    if actor not in _ACTORS:
        raise KeyError(actor)
    return dict(_ACTORS[actor])
