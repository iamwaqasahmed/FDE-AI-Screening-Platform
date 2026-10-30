"""rel-m02-l01 pages.
The removed field name stays in the gold.

These builders make the interface notice, the assurance page, and the two interface documents. scenario is the status row for this profile. gold keeps the removed field name beside the status fields the checker compares.
"""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.serve.iam import BOOKING_LOA, PATIENT_LOA, STAFF_ROLES, discovery, token

FIELD = "clinic"
REMOVED = "clinicCode"
CLINIC = "ENDO-CLN"


def status_count(seed: int) -> int:
    """Return the status count for this seed.

    The scenario and the gold both read it, so they publish the same count for the profile.
    """
    return 3 + (seed % 5)


def notice() -> str:
    return """# FHIR v2

his-wadi has moved to FHIR v2. The OpenAPI document in this release is the spec.

Generate the client from that spec. A field from the v1 client is gone.

Booking is a later day. A status question can be answered now.
"""


def identity_note() -> str:
    """Return the assurance page.

    It lists the patient level, the booking level, and the staff roles so a reader can see who may open the assistant and who may book.
    """
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
    """Return the identity interface document.

    The issuer, the token endpoint, and the patient and coordinator actors are filled from discovery, so the document matches the service this profile uses.
    """
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
    """Return the status scenario for this profile.

    The count comes from the seed and the letter carries the profile marker, so this row is the one the gold grades.
    """
    # One status row. The count and the marker come from this profile.
    return {
        "scenario": "status",
        "referral_id": "ref-status",
        "session": "ses-status",
        "subject": token("patient")["sub"],
        "facility_id": "h-wadi",
        "count": status_count(profile.seed),
        "state": "pending",
        # The live clinic field. The removed name is not on this row.
        "clinic": CLINIC,
        "message": "Where is my referral?",
        "letter": profile.canary(),
    }


def gold(profile: Profile) -> dict:
    """Return the grading gold for this profile.

    It keeps the removed field name, the live field, the roles, and the status fields taken from the scenario. That is the record the check compares.
    """
    # Read the scenario so this record and that row publish the same status fields.
    row = scenario(profile)
    return {
        # The removed name, the live field, and who may open the assistant or book.
        "removed_field": REMOVED,
        "field": FIELD,
        "roles": list(STAFF_ROLES),
        "booking_loa": BOOKING_LOA,
        "patient_loa": PATIENT_LOA,
        "patient_role": "patient",
        "staff_role": "coordinator",
        "service": "svc-integration",
        # Status fields taken from the scenario, including the tool the check expects.
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
