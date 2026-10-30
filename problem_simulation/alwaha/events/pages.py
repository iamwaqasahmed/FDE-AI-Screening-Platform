"""Participant-facing text for the Lesson 3 release.

criteria_docs returns the endocrinology criteria whose status is in_force, and a draft of the same specialty. The policy page states how the SLA clock runs, how many retries are allowed, and how events that share a referral are ordered. The remaining functions are the event contract and the two API descriptions.
"""

from __future__ import annotations

from alwaha.world.calendar import RETRY_LIMIT, WORKING_DAY_COUNT


def criteria_docs() -> list[dict]:
    """Return the criteria documents shipped in this pack.

    One is in force and one is a draft of the same specialty, so the release can render both and the check can tell them apart.
    """
    return [
        # In force. A return cites the clause id on this document.
        {
            "doc_id": "crit-endo-v3",
            "status": "in_force",
            "specialty": "endo",
            "version": 3,
            "clause_id": "endo-v3-c1",
            "body": "A referral names the specialty and the facility. A return cites the clause id on this document.",
        },
        # Draft of the same specialty. It is not the document a referral uses.
        {
            "doc_id": "crit-endo-v4",
            "status": "draft",
            "specialty": "endo",
            "version": 4,
            "clause_id": "endo-v4-c1",
            "body": "Draft text for endocrinology. It is not in force.",
        },
    ]


def render_criteria(doc: dict) -> str:
    return f"""# {doc["doc_id"]}

- doc_id: {doc["doc_id"]}
- status: {doc["status"]}
- specialty: {doc["specialty"]}
- version: {doc["version"]}
- clause_id: {doc["clause_id"]}

{doc["body"]}
"""


def policy_page() -> str:
    return f"""# pol-sla

The SLA clock starts at `referral.submitted`. It does not start at booking.

working_days: {WORKING_DAY_COUNT}

Count that many working days. The day of `referral.submitted` counts when it is a working day. If that day is not a working day, counting begins on the next one. The calendar file lists the weekend and the holidays.

Example. A referral submitted on Sunday counts Sunday as day one and Monday as day two.

retries: {RETRY_LIMIT}

A step that keeps asking to be retried is tried this many times. After that, record a dead letter and do not apply the event.

Apply events that share a referral in sequence order. The higher sequence is the letter you keep. A second delivery of the same event id changes nothing.

Use the criteria document whose status is in force when the referral starts.

An open row with the same patient and specialty is flagged. The referral still waits for a coordinator. It is not booked.

A coordinator holds the approval. The workflow does not accept or return the referral, and it does not book a slot.

If a hold is taken and the next step fails, release the hold.

`h-ain` has no slot API in this release. A hold or a booking there returns queued.
"""


def contract_page() -> str:
    return """# referral.submitted

Owner: eref
Version: 1

Required fields:

- event_id
- topic
- occurred_at
- sequence
- referral_id
- patient_key
- letter

The clock time is `occurred_at`. A consumer ignores a field it does not know.
"""


def eref_spec() -> str:
    return """openapi: 3.0.3
info:
  title: eref
  version: "1"
paths:
  /referrals/{referral_id}:
    get:
      operationId: readReferral
      responses:
        "200":
          description: The referral.
  /referrals/{referral_id}/decision:
    post:
      operationId: decideReferral
      responses:
        "202":
          description: Held for a coordinator.
"""


def his_wadi_spec() -> str:
    return """openapi: 3.0.3
info:
  title: his-wadi
  version: "1"
paths:
  /slots/hold:
    post:
      operationId: holdSlot
      responses:
        "200":
          description: A hold with a short TTL.
  /slots/book:
    post:
      operationId: bookSlot
      responses:
        "200":
          description: A booked slot.
"""
