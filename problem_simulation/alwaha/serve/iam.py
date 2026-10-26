"""Patient and staff tokens for the dev identity provider.

discovery() returns the issuer, the token endpoint, and the staff role names. token() returns a copy of the actor record, or raises KeyError when the actor is not in the dev directory. The HTTP layer turns that KeyError into a not-found response.
"""

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
    """Return the issuer, the token endpoint, and the staff roles.

    Patient actors are issued by token() and are not listed in this discovery document.
    """
    return {
        "issuer": ISSUER,
        "token_endpoint": ISSUER + "/token",
        "roles": list(STAFF_ROLES),
    }


def token(actor: str) -> dict:
    """Return a copy of the actor record.

    An unknown actor raises KeyError so this module stays free of HTTP status codes. The caller maps that error to a not-found response.
    """
    # KeyError is the unknown-actor signal. A missing actor is not given a token.
    if actor not in _ACTORS:
        raise KeyError(actor)
    return dict(_ACTORS[actor])
