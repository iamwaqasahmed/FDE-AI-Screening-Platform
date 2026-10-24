"""rel-w2d1 pages. The removed field name stays in the gold."""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.serve.iam import BOOKING_LOA, PATIENT_LOA, STAFF_ROLES, discovery, token

FIELD = "clinic"
REMOVED = "clinicCode"
CLINIC = "ENDO-CLN"


def status_count(seed: int) -> int:
    return 3 + (seed % 5)


def notice() -> str:
    return """# FHIR v2

his-wadi has moved to FHIR v2. The OpenAPI document in this release is the spec.

Generate the client from that spec. A field from the v1 client is gone.

Booking is a later day. A status question can be answered now.
"""


def identity_note() -> str:
    roles = "\n".join(f"- {role}" for role in STAFF_ROLES)
    return f"""# Levels of assurance

- {PATIENT_LOA}: one-time code. A patient at {PATIENT_LOA} can open the assistant.
- {BOOKING_LOA}: checked against nid. Booking and cancellation require {BOOKING_LOA}.

# Staff roles

{roles}

A service token is not a patient token. svc-integration is a service.
"""


def his_wadi_spec() -> str:
    return f"""openapi: 3.0.3
info:
  title: his-wadi
  version: "2"
paths:
  /Referral/{{referral_id}}:
    get:
      operationId: readReferral
      parameters:
        - name: {FIELD}
          in: query
          required: true
          schema:
            type: string
      responses:
        "200":
          description: Referral status.
"""


def iam_spec() -> str:
    found = discovery()
    patient = token("patient")
    staff = token("coordinator")
    return f"""openapi: 3.0.3
info:
  title: iam
  version: "1"
x-issuer: {found["issuer"]}
x-token-endpoint: {found["token_endpoint"]}
x-actors:
  - name: patient
    sub: {patient["sub"]}
    role: {patient["role"]}
    loa: {patient["loa"]}
  - name: coordinator
    sub: {staff["sub"]}
    role: {staff["role"]}
    loa: {staff["loa"]}
"""


def scenario(profile: Profile) -> dict:
    return {
        "scenario": "status",
        "referral_id": "ref-status",
        "session": "ses-status",
        "subject": token("patient")["sub"],
        "facility_id": "h-wadi",
        "count": status_count(profile.seed),
        "state": "pending",
        "clinic": CLINIC,
        "message": "Where is my referral?",
        "letter": profile.canary(),
    }


def gold(profile: Profile) -> dict:
    row = scenario(profile)
    return {
        "removed_field": REMOVED,
        "field": FIELD,
        "roles": list(STAFF_ROLES),
        "booking_loa": BOOKING_LOA,
        "patient_loa": PATIENT_LOA,
        "patient_role": "patient",
        "staff_role": "coordinator",
        "service": "svc-integration",
        "status": {
            "scenario": row["scenario"],
            "referral_id": row["referral_id"],
            "session": row["session"],
            "facility_id": row["facility_id"],
            "count": row["count"],
            "state": row["state"],
            "message": row["message"],
            "tool": "status",
        },
    }
